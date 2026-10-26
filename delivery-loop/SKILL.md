---
name: delivery-loop
description: Run one round of work from brief to landed change, with a builder, two reviewers and your own check. Use when the orchestrator delivers a ticket, fixes a reported bug, or the owner asks for a round.
---

# Delivery loop

One **round** turns one piece of work into a landed change. Keep each round's records in `.rounds/<round>/` at the repository root, unless the owner names another place: `brief.md`, `reviews/`, and `status.md` (one dated line per event). Add `.rounds/` to `.git/info/exclude` so the records stay on this machine and never reach a commit. Never keep them in `/tmp`: it gets wiped. A new session picks a round up from `status.md`.

## 1. Evidence, then brief

For a bug, reproduce it first and find the cause (logs, data, a direct call to the API, the device), and put what you proved in the brief. Then write the whole brief from [`references/brief.md`](references/brief.md), covering:

- the goal;
- where the work happens;
- the limits;
- every rule the result must keep;
- the acceptance checks, as what a user would observe;
- "run these yourself before handing over";
- the reply.

Done when a builder with no other context could finish it. A rule left implicit costs a whole extra round.

## 2. Build

Start the builder (see `orchestrate`). Builders work test-first: a failing test for each change, then the code. Run builders in parallel only on independent work in different files, and tell each which files the other owns. Heavy shared checks (the full suite) run once, by you.

Each builder ends with a status:

- **done**: check its claim (`git show --stat`, a quick read of the diff), then review.
- **done with concerns**: read the concerns first.
- **needs context** or **blocked**: answer from the brief, the code or the owner, or change the brief, then start it again.

## 3. Review and fix

Review with `cross-review`. Merge the findings into one fix list.

- **Fix now:** every P1 and P2.
- **Fold into the same fix round:** cheap P3s that a user would notice.
- **Deferred:** the rest, noted in the report or filed as an issue.

Send the fix list as a new task to a builder, then re-review with fresh reviewers given the history. After three fix rounds without a clean review, stop and tell the owner: the brief is usually the problem. A fix that changes only a comment, a label or an ignore rule gets your own check instead of a review round.

## 4. Own check

Run what the reviewers could not:

- the full test suite;
- generated files up to date;
- for anything a user sees, the real thing: the simulator or emulator, in each language and theme the change touches (`design-ui`).

Look at the screenshots yourself; reviewers pass things a person would not. Clean up what the check created: test rows, uploaded files, accounts you no longer need, devices' settings.

## 5. Land and report

Commit (the builder already did, usually), then land through `owner-gates`: ask before every push, deploy, upload or tag. Tell the owner in plain words:

- what changed;
- what you verified, and how;
- what you did not verify;
- what waits on them.

Add the last line to `status.md`.

Done when the change is committed, every reviewer said ready on it, your own check passed, and the owner has the report.
