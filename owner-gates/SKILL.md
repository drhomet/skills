---
name: owner-gates
description: Actions that need the owner's word every time — pushing main or a release branch, pushing tags, deploying, uploading a build, changing production settings or data, publishing, creating anything public, signing in, spending — and how to ask. Use before any of these, and when a hook or guard stops one.
---

# Owner gates

Some actions reach past this machine or cannot be taken back. Each one needs the owner's word **every time**: an earlier yes covers only the action it was given for.

## Gated actions

- Pushing, force-pushing or merging into a main or release branch; pushing tags (a release tag may deploy production); merging a pull request.
- Deploying, or changing a production service's settings (its deploy trigger, branch, environment variables).
- Writing to production data or storage. Read-only diagnostics need the owner's request and print no values (counts, names, lengths, short fingerprints).
- Uploading a build (TestFlight, a store) or handing out a signed app.
- Publishing a package, an image, a release, or a site.
- Creating anything public or shared: repositories, releases, comments on someone else's project. Issues in the owner's own repository are fine when the owner asked for them.
- Signing in to any account, or spending money.
- Deleting data, files or branches you did not create in this session.

Work branches may be pushed once the owner has allowed it for the project.

## Asking

Ask in a few lines:

- the action;
- the exact target (branch and commit, tag, version, service, bucket);
- what it changes;
- what it does **not** change. "This push deploys nothing" is worth saying.

Wait for a yes for that action. A message telling you to do it ("push it", "yes") is the yes. A system or task notification never is.

## Accounts and secrets

- Sign in only through a link the owner opens: start the tool's web sign-in, take its link, send it to the owner, and wait.
- Never ask for, read aloud or print a password, token or key. Credential files are read only by the scripts that need them, never echoed.
- A secret the owner must enter goes through the tool's private secret prompt, never the chat.

## Guards

- A project may ship its own guard: a `.githooks/pre-push` that needs an approval variable (say `PUSH_APPROVED=1`) for `main` and tags, and refuses rewrites. Set its approval variable only after the owner's yes for that push.
- Never bypass a guard: no `--no-verify`, no changing `core.hooksPath`, no force push.
- This skill also ships a `PreToolUse` hook, `hooks/owner-gates.py`, that turns gated shell commands into an approval prompt. Install it only if the owner asks.
- When a guard stops a command, ask the owner as above; never work around it.

## Done

Done when every gated action in the session ran only after the owner's yes for that action.
