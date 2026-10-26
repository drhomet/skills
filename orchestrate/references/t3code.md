# Orchestrating in T3 Code

T3 Code exposes its orchestration as MCP tools (`mcp__t3-code__*`; the prefix may be normalised by the harness). Some are deferred: load them with the tool search first.

## Builders

- Find the models: `orchestrator_capabilities` lists every provider and model, including ones the native subagent tool cannot reach.
- Start a builder with `delegate_task`:
  - `task`: the agent preamble, then one line pointing at the brief file ("Read and follow exactly the brief in <path>"), plus the hard limits repeated in one line (never push, never contact production, …);
  - `target`: `{"providerInstanceId":"codex","model":"gpt-6.1-sol","options":{"reasoningEffort":"high"}}`;
  - `role: "implementation"`, `mode: "async"`, and a `clientRequestId` naming the round (`<project>-<topic>-build-1`), the same across retries.
- `isolation: "worktree"` gives the builder its own checkout from the parent's commit (uncommitted edits are not copied); otherwise the brief names where it works. Two builders in one checkout only on different files, and the brief tells each which files the other owns.
- A completion arrives as a notification: do not poll. Read it, then check the claim yourself (`git show --stat`, the tests) before reporting it.
- A fix round for the same work: a new `delegate_task` with the original brief, the reviewers' findings and your decisions (a fresh `clientRequestId`, `-fix1`, `-fix2`). To change a running builder's task mid-turn, `t3_thread_send` to its `childThreadId` with `mode: "steer"`.
- A builder that stops "blocked" on something you can answer (a missing skill, a path, a decision already made): answer it in a new task and let it go on.
- A builder's question: `t3_pending_request_read`, then `t3_pending_request_respond` when the brief or the owner's decisions answer it; otherwise ask the owner first.
- Stop a builder: `task_cancel`.

## Reviewers

- One reviewer per model with `delegate_task`, `role: "review"`, a fresh `clientRequestId` for every review round (`<project>-<topic>-review2-opus-1`), and the round's review brief. Each re-review is a new `delegate_task` whose brief carries the previous findings and the responses; never a message to an earlier reviewer's thread.
- Start a round's reviewers in the same turn so they run side by side.
- Opus: `{"providerInstanceId":"claudeAgent","model":"claude-opus-5-5","options":{"effort":"high"}}`. Check the returned options match what you asked for.

## Devices and browsers

- `device_*` tools may be turned off for the environment; then drive the iOS Simulator with `xcrun simctl` (screenshots) and a CGEvent tap script, and Android emulators with `adb shell input` (see the project notes for helpers).
- Emulators and simulators can be shared with other projects' agents: before driving one, check what app is in front (`adb shell dumpsys activity activities | grep topResumedActivity`). If another project's app is in use, start a separate emulator of your own rather than taking it over, and shut down what you started.
- Leave a device as you found it: re-enable networking you disabled, uninstall what you installed on someone else's emulator, delete pushed test files.
- Browser checks: `preview_open`, `preview_evaluate`, `preview_snapshot`; a snapshot can time out, `preview_evaluate` usually still works.

## Timers and long waits

- Recurring work: `schedule_task` with a structured schedule. Report the cadence and the next run time.
- Waiting on a shell condition: a background command whose loop exits when the condition holds.

## Linking for the owner

- A thread: `[title](t3-thread://v1/<threadId>)` with the exact id.
- A pull request you open: `link_pull_request` right after creating it.
- Show a screenshot by its absolute path in markdown; show a page with `html_render`.
