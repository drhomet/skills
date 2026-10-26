---
name: cross-review
description: Review a round with two (or more) independent reviewers on different models, merge their findings into one fix list, and repeat with fresh reviewers until every reviewer says ready. Use when a round is built and before it lands.
---

# Cross-review

**Independent** reviewers check the same round; their findings become one fix list; the round repeats until every reviewer says ready on the same final commit.

## Reviewers

- Two by default, on different models so they miss different things: the owner's pair is Sol and Opus (see `orchestrate`). Use more for risky work (data, security, releases, anything hard to undo), or when the owner asks.
- Reviewers read only: no edits, no commits, no pushes, no production, no devices other agents use. They may run the tests and builds.
- A reviewer whose model refuses the work is replaced by another model; word security reviews as a defensive review of your own code, stating what must hold.

## The review brief

Write it to a file and give each reviewer the same one. It holds:

- the round's brief;
- the commits to review (`git show <hash>`, or `base..head` for several);
- what you verified yourself and how;
- the limits;
- what to check hardest: the rules and acceptance checks first, then the scenarios most likely to break (races, failures, old data, privacy, the release path).

The reply asks for:

- findings by severity, as `path:line — problem — scenario — fix`, each marked confirmed or suspected;
- what was checked and clean;
- whether it is ready.

Keep it short: "under 20 lines".

Severity:

- **P1:** data loss, a security or privacy hole, or production broken.
- **P2:** a real bug a user or the owner will hit, or a rule broken.
- **P3:** small, cosmetic, a test gap, or a rare edge.

Only P1 and P2 block.

The first review of a round is blind: reviewers do not see each other's findings. A re-review is a **new reviewer task** (never a message to the previous reviewer). Its brief carries:

- the history: each finding, the response, and the commit;
- the instruction to verify that each fix holds and that nothing new broke.

## Merging

1. Collect every reviewer's findings.
2. Check the ones that matter yourself: reproduce a bug before you send it on. A finding can be wrong, and so can your brief: when a finding traces back to the brief, fix the brief too.
3. When reviewers disagree, decide with a reason, unless it is a critical decision for the owner.
4. Write one fix list: each item once, in its strongest form, plus the owner's decisions it depends on. Cheap P3s go in; the rest are noted and dropped, or filed as issues.

## Done

Done when every reviewer has said ready on the same final commit, with no P1 or P2 open, and every P3 either fixed or recorded as dropped.
