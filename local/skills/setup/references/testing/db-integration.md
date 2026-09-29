# Database integration tests — Vitest

> Scope: integration tests against a SQL database, in a project tested with Vitest. Examples use Postgres, Drizzle, and Testcontainers; the notes after each say what to adapt for another stack.

## Before you start

Find these in the target project:

- **The production database engine and version** — the test container runs the same image.
- **How the schema gets applied** — whether the ORM can push a schema directly, or where the migration files live.
- **How the db client gets its connection string** — the worker setup sets it.
- **Where the schema is defined** — reset derives its table list from it.
- **The workspace layout** — which package owns the database, and which packages run DB tests.

## Approach

- **Real engine, throwaway instance.** Tests run against a container of the production engine and version, started per run — never a shared or hand-provisioned database.
- **Schema built fresh from its source of truth.** Pushed directly when the ORM supports it, instead of replaying the migration history, which is dirty and heavy. Migration replay otherwise.
- **The app runs its own code.** Tests use the app's own db client; the harness only redirects its connection.
- **One database per run.** Test files share it and run one at a time; each file decides when its state resets.
- **The harness lives with the database.** The db package owns it; other packages opt in through config.

## Steps

### 1. Install

```bash
pnpm --filter @repo/db add -D @testcontainers/postgresql drizzle-kit vitest
```

Every package in the workspace resolves the same Vitest install. The `ProvidedContext` augmentation in step 2 only crosses package boundaries when they do.

### 2. Write the harness in the db package

```
packages/db/
  package.json        # exports
  testing/
    container.ts      # starts the database, applies the schema
    global-setup.ts   # one container per run
    setup.ts          # points each worker at it
    helpers.ts        # resetDb
    seed.ts           # fixture builders
    index.ts          # re-exports container, helpers, seed
```

**Container and schema.** Start the container, push the schema, return the URL and a teardown.

```ts
// testing/container.ts
import { PostgreSqlContainer } from "@testcontainers/postgresql"
import { pushSchema } from "drizzle-kit/api"
import { createDb } from "../lib/client"
import * as schema from "../schema"

const IMAGE = "postgres:17-alpine"

export async function startTestDb() {
  const container = await new PostgreSqlContainer(IMAGE).start()
  const url = container.getConnectionUri()

  const db = createDb({ connectionString: url })
  const { apply } = await pushSchema(schema, db)
  await apply()
  await db.$client.end()

  return { url, stop: () => container.stop() }
}
```

- `IMAGE` is the production image and version — take it from `docker-compose.yml` or the hosting config.
- `pushSchema` takes the schema module and a Drizzle instance; `drizzle-kit/api` has a variant per dialect (`pushMySQLSchema`, …).
- `createDb` stands for the project's own client factory, given the container's URL.

Without push, apply the project's migration files instead — no tracking table, and statement by statement in autocommit when the engine rejects some statements inside a transaction. Resolve the folder through package resolution, not `import.meta.url`: bundlers rewrite it away from a `file:` URL.

```ts
import { createRequire } from "node:module"
import path from "node:path"
import { readMigrationFiles } from "drizzle-orm/migrator"

const migrationsFolder = path.join(
  path.dirname(createRequire(import.meta.url).resolve("@repo/db")),
  "migrations",
)

// Drizzle's migrate() wraps the run in a transaction, which Postgres
// rejects for CREATE INDEX CONCURRENTLY.
for (const migration of readMigrationFiles({ migrationsFolder })) {
  for (const statement of migration.sql) await pool.query(statement)
}
```

- The folder is the `out` directory in `drizzle.config.ts`.

**Global setup.** Start one container per run, `provide` its URL to the workers, and return the teardown.

```ts
// testing/global-setup.ts
import type {} from "vitest"
import type { TestProject } from "vitest/node"
import { startTestDb } from "./container"

export default async function setup({ provide }: TestProject) {
  const testDb = await startTestDb()
  provide("databaseUrl", testDb.url)
  return testDb.stop
}

declare module "vitest" {
  export interface ProvidedContext {
    databaseUrl: string
  }
}
```

- `import type {} from "vitest"` brings the root module into scope so the augmentation applies; `vitest/node` alone is not enough.

**Worker setup.** Each worker is its own process, so it sets the client's connection env var from `inject()`. Setup files run before the test file imports the db client.

```ts
// testing/setup.ts
import { inject } from "vitest"
import type {} from "./global-setup"

process.env.DATABASE_URL = inject("databaseUrl")
```

- `DATABASE_URL` is whatever variable the project's client reads its connection string from.

**Reset.** Empty every table in one statement and restart identities. Derive the table list from the schema, so it never drifts as tables are added. Take no parameters, so the function wires straight into a hook — Vitest rejects a hook callback whose first parameter isn't destructured.

```ts
// testing/helpers.ts
import { getTableName, is, sql } from "drizzle-orm"
import { PgTable } from "drizzle-orm/pg-core"
import { db } from "../lib/client"
import * as schema from "../schema"

const tableNames = Object.values(schema)
  .filter((value) => is(value, PgTable))
  .map((table) => getTableName(table))

export async function resetDb() {
  const list = tableNames.map((name) => sql.identifier(name))
  await db.execute(
    sql`TRUNCATE TABLE ${sql.join(list, sql`, `)} RESTART IDENTITY CASCADE`,
  )
}
```

- On another engine, filter by its table class (`MySqlTable`, …) and use its truncation form — MySQL truncates one table per statement and has no `CASCADE`.

**Seeders.** Shared fixture builders live in `testing/seed.ts`; their shape follows the project's data. Seeders only one package needs go in that package's `tests/helpers.ts`.

**Exports.**

```jsonc
// package.json
{
  "name": "@repo/db",
  "exports": {
    ".": "./index.ts",
    "./testing": "./testing/index.ts",
    "./testing/global-setup": "./testing/global-setup.ts",
    "./testing/setup": "./testing/setup.ts"
  }
}
```

### 3. Configure each consumer package

Start integration tests in the package's `tests/` directory; what else counts as an integration test, and where it lives, is up to the project. `fileParallelism: false` keeps files from racing over the one database.

```ts
// api/vitest.config.ts
import { defineConfig } from "vitest/config"

export default defineConfig({
  test: {
    globalSetup: ["@repo/db/testing/global-setup"],
    setupFiles: ["@repo/db/testing/setup"],
    fileParallelism: false,
  },
})
```

- Leave `include` at Vitest's default, so adding the harness doesn't change which tests run.

If the project uses a task runner such as Turborepo, give its `test` task no `dependsOn`:

```jsonc
// turbo.json
{ "tasks": { "test": {} } }
```

### 4. Record the rules

Write into the project's `CLAUDE.md`, for its own paths and packages:

- Where integration tests go.
- Each test file picks its reset: `beforeEach(resetDb)` to isolate every test, or `beforeAll` reset-and-seed for a shared fixture with `afterAll(resetDb)`, so the next file doesn't inherit its rows.

### 5. Verify

- `pnpm test` in a consumer package: the container starts, the schema applies, the suite passes.
- The run's file count includes the unit test files.
