# Logging — Node on Google Cloud

> This guide commits to one default with firm rules. When in doubt, follow the rules.
>
> Scope: any Node process deployed on GCP where the platform collects stdout — Cloud Run,
> Cloud Run functions, GKE, App Engine.

## The decision

**Use [Pino](https://getpino.io), configured with [`@google-cloud/pino-logging-gcp-config`](https://googlecloudplatform.github.io/cloud-solutions/pino-logging-gcp-config/), writing JSON to stdout.** Don't write to the Cloud Logging API from the app.

The platform already ingests stdout into Cloud Logging. The config emits the JSON field names Cloud Logging reserves, so entries arrive fully structured — severity, trace correlation, Error Reporting — with no client, credentials, or network path in the app.

## Install

```bash
npm install pino @google-cloud/pino-logging-gcp-config
npm install --save-dev pino-pretty
```

One logger module for the whole service, exporting a single instance. Detect the GCP environment and switch format on it — structured JSON there, `pino-pretty` everywhere else:

```ts
// logger.ts
import { pino, type LoggerOptions } from 'pino';
import { createGcpLoggingPinoConfig } from '@google-cloud/pino-logging-gcp-config';

// K_SERVICE is set by the platform on Cloud Run / Cloud Run functions
const onGcp = process.env.K_SERVICE !== undefined;

const options: LoggerOptions = {
  level: process.env.LOG_LEVEL ?? 'info',
  // strip secrets before they can reach a log sink
  redact: {
    paths: ['token', 'password', 'secret', '*.token', '*.password', '*.secret'],
    remove: true,
  },
  // drops pid and hostname, which say nothing useful about a container
  base: undefined,
};

export const logger = pino(
  onGcp
    ? createGcpLoggingPinoConfig(
        {
          serviceContext: {
            service: process.env.K_SERVICE!,
            version: process.env.K_REVISION ?? 'unknown',
          },
        },
        options,
      )
    : { ...options, transport: { target: 'pino-pretty' } },
);
```

`serviceContext` is what attributes errors to a service in Error Reporting; `K_SERVICE` and `K_REVISION` are set by the platform.

`redact` is a backstop, not a licence — rule 8 still applies. It catches the field that slips through in an object you didn't inspect, and only for the paths you list.

## Usage rules

1. **One logger instance for the service**, created in a single module and imported. Never construct a logger per request or per module.
2. **Structured fields, not interpolated strings.** `logger.info({ orderId }, 'order placed')` — not `` logger.info(`order ${orderId} placed`) ``. The first is queryable; the second is a string to grep.
3. **The message is a constant.** Same event → same message text every time, with the varying parts in fields. That's what makes entries groupable.
4. **Use child loggers for scoped context.** `const requestLogger = logger.child({ requestId })` at the entry point, then pass it down — rather than threading the same fields into every call site. For a long-lived component, bind it once at module level and add `msgPrefix` so its lines are identifiable: `const authLogger = logger.child({}, { msgPrefix: '[AuthService] ' })`.
5. **Pass the `Error` object, not its message** — `logger.error({ err }, 'charge failed')`. The config turns it into the `stack_trace` field that routes the entry to Error Reporting; `err.message` in a string gets you a log line and nothing else. For an error condition with no `Error` to attach, add the type marker instead:

   ```ts
   logger.error(
     { '@type': 'type.googleapis.com/google.devtools.clouderrorreporting.v1beta1.ReportedErrorEvent' },
     'payment provider returned an unmapped status',
   );
   ```
6. **Never `console.log` in application code.** It still reaches Cloud Logging, but as an unstructured line with no severity, so it can't be filtered or alerted on.
7. **Levels mean something.** `error` = something needs a human; `warn` = degraded but handled; `info` = a business event worth keeping; `debug` = off in production. If everything is `info`, severity filtering is dead.
8. **Never log secrets or personal data.** Credentials, tokens, full request bodies, and raw PII stay out. Logs are retained, broadly readable, and exportable.

## Record the rules for future agents

Installing the logger is a one-time act; using it correctly is every future change. Once the logger module exists, write the usage rules into the project's agent instructions (`CLAUDE.md`, or the nearest one covering the service) so later work follows them without this guide being loaded.

Write the rules as they apply to *this* project — the logger's import path, the levels it uses, the fields the service always attaches — not a copy of the list above. Keep it to what changes how code gets written; leave out the reasoning that only mattered while picking the tool.
