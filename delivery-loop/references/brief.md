# Brief

Fill every heading. Delete a heading only when it truly does not apply, and say so in one line.

## Skills
First load the skills ponytail, caveman and tdd and follow them. (If a skill is missing, say so and use the test commands below.)

## Task
One sentence: what this round delivers, and the ticket, report or decision it comes from.

## Evidence
What you proved before briefing: the reproduction, the cause, `file:line`, the data or log line. "Suspected" where not proved.

## Workspace
Repository, branch or worktree, base commit. Test databases or other throwaway resources by exact name, and that they
are cleaned up after. Which files another agent is editing at the same time, if any.

## Limits
What not to touch: ports, databases, other projects, credential files, branches and tags that need the owner's word,
generated files (regenerate them instead), devices other agents use. Never print a secret. Never push, deploy, upload
or contact production unless the round is for that and the owner said yes.

## Rules
Every rule the result must keep: the project's own (`AGENTS.md`, `CLAUDE.local.md` by path), the owner's decisions this
round depends on, and the mobile UX rule for any screen. Write the rule you would otherwise catch in review.

## Build
What to change, item by item, each with a failing test first where the project tests that layer.

## Acceptance
What a user would observe when it is right: the screens, sizes, languages and themes; the data cases (old or imported
data too); the permission and privacy cases; what must stay unchanged. These are the checks the reviewers will run.

## Before handing over
Run the project's checks (name the commands) and the acceptance checks you can run. Leave the full shared suite to the
orchestrator if this says so. Remove temporary code and test data.

## Reply
At most N lines: commits (hash and sentence), test counts, where the evidence is, anything not verified, any P1/P2
risk, and a status: done, done with concerns, needs context, or blocked.
