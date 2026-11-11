---
description: Run the pre-deployment checks and ship the changes 
---

Start deployment procedure using this steps:

1. Pre-deployment checks if any have not been run:
   - clean temporary debug and logging edits
   - tests, code checks, linting and formatting
2. Deployment (if no issues in previous step):
   - if necessary commit using `git-committing` and push to main branch
   - manually close any related issue if no PR was created
3. Report:
   - results of the checks and deployment
   - further instructions if any manual work is required to finalize tasks
