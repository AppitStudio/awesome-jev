# Compound Intelligence by kointeligencja (experimental leadership coaching skill for Codex with optional Jev shortlisting and draft checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Codex skill that helps you prepare a leadership move, try it and come back with what happened, built on 21 methods from Caroline Webb's book (the book itself is not included). With your own TypeSafe key, Jev gives advisory method shortlisting and draft checks; each outgoing case or draft needs your explicit approval and the key is entered at a hidden prompt into the child process only. A `--local` mode needs no TypeSafe account. The authors state their small synthetic comparison did not show better single answers than the same model without the skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kointeligencja/compound-intelligence) |
| Maintainer | [kointeligencja](https://github.com/kointeligencja). Independently curated. |
| Format | Codex agent skill with Python helper scripts (MIT) |
| Requirements | Codex; optionally a TypeSafe key, entered at the launcher's hidden prompt. |
| License | [MIT](https://github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/compound-intelligence/scripts/ci_runtime/client.py`](https://github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/skills/compound-intelligence/scripts/ci_runtime/client.py) at the pinned commit. |

## When to use

- Try a structured coaching workflow where Jev only shortlists methods and checks drafts after you approve sending.
- Mismatch: proven coaching outcomes; the authors say effectiveness is not established.

## How it works

`skills/compound-intelligence/scripts/ci_runtime/client.py` sends a minimized, approved case or draft to the TypeSafe System One API for method shortlisting and postflight checks; `references/decision-runtime.md` documents the questions and thresholds. Integration evidence: [`skills/compound-intelligence/scripts/ci_runtime/client.py`](https://github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/skills/compound-intelligence/scripts/ci_runtime/client.py).

## Get started

Install the skill, then launch Codex with `--jev` (or `--local` without TypeSafe) and follow the onboarding guide.

```sh
python3 "$HOME/.agents/skills/compound-intelligence/scripts/launch_codex.py" --jev
# or without TypeSafe:
python3 "$HOME/.agents/skills/compound-intelligence/scripts/launch_codex.py" --local
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/README.md](https://github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/README.md)
- Validation: [github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/docs/PUBLIC-VALIDATION.md](https://github.com/kointeligencja/compound-intelligence/blob/697b22a68a30c86ff00e2136d4e9b23d520347c6/docs/PUBLIC-VALIDATION.md)

## Limits and data handling

Approved, minimized case and draft text goes to TypeSafe; your normal AI host still processes the conversation. Windows and native desktop installation are untested per the README.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 697b22a68a30](https://github.com/kointeligencja/compound-intelligence/tree/697b22a68a30c86ff00e2136d4e9b23d520347c6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
