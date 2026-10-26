#!/usr/bin/env python3
"""PreToolUse hook: shell commands that need the owner's word go to the owner for approval."""
import json
import re
import sys

# Each gate: a pattern over the shell command and the line the owner sees.
GATES = [
    (r"\bgit\s+push\b[^;&|]*\s(--force|-f|--force-with-lease)\b", "force push"),
    (r"\bgit\s+push\b[^;&|]*\s(\S+:)?(main|master|release[\w/-]*)\b", "push to a main or release branch"),
    (r"\bgit\s+push\b[^;&|]*\s(--tags|v\d[\w.-]*)", "push tags"),
    (r"\bgh\s+pr\s+merge\b", "merge a pull request"),
    (r"\b(npm|pnpm|yarn|bun)\s+publish\b", "publish a package"),
    (r"\bgh\s+(repo\s+create|release\s+create)\b", "create a public repository or release"),
    (r"\b(npm|pnpm|yarn)\s+(login|adduser)\b|\bgh\s+auth\s+login\b", "sign in to an account"),
]


def gate(command: str):
    for pattern, reason in GATES:
        if re.search(pattern, command):
            return reason
    return None


def main() -> None:
    event = json.load(sys.stdin)
    if event.get("tool_name") != "Bash":
        return
    reason = gate(event.get("tool_input", {}).get("command", ""))
    if reason:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": f"owner-gates: {reason} needs the owner's word.",
        }}))


if __name__ == "__main__":
    main()
