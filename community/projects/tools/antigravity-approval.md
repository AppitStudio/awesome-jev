# antigravity-approval (fail-closed tool-call guardrail for Antigravity: local rules first, Jev for the ambiguous calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

`PreToolUse` permission hook for Antigravity: a fast local tier (whitelist, blocklist, network gate, path guard) settles clear commands with no network traffic, ambiguous ones go to Jev, and anything uncertain falls back to asking you. Also hosts the shared `jev_eval` policy core reused by the author's ZCode hook. English and Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zjply4000/antigravity-approval) |
| Maintainer | [zjply4000](https://github.com/zjply4000). Independently curated. |
| Format | Python hook package |
| Requirements | Antigravity, Python, `typesafe-sdk` and a TypeSafe API key. |
| License | [MIT](https://github.com/zjply4000/antigravity-approval/blob/d0a8fb90e68e882b9e37ea90cc1a7c314419bcd2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_eval/jev_client.py`](https://github.com/zjply4000/antigravity-approval/blob/d0a8fb90e68e882b9e37ea90cc1a7c314419bcd2/src/jev_eval/jev_client.py) at the pinned commit. |

## When to use

- Auto-handle routine agent commands and stop risky ones.
- Mismatch: on Antigravity 2.0 an allow decision still shows the host's dialog; deny is honored.

## How it works

`src/jev_eval/jev_client.py` uses the official `typesafe_sdk` (`TypeSafeClient`, `Choice`) with `jev-latest` and a retry policy; errors fail closed to manual approval. Integration evidence: [`src/jev_eval/jev_client.py`](https://github.com/zjply4000/antigravity-approval/blob/d0a8fb90e68e882b9e37ea90cc1a7c314419bcd2/src/jev_eval/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/zjply4000/antigravity-approval && cd antigravity-approval
python -m venv .venv
.venv/Scripts/python.exe -m pip install -e ".[dev]" typesafe-sdk
.venv/Scripts/python.exe scripts/install_hook.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zjply4000/antigravity-approval#readme](https://github.com/zjply4000/antigravity-approval#readme)

## Limits and data handling

Ambiguous command text goes to TypeSafe. A heuristic guardrail, not a sandbox.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit d0a8fb90e68e](https://github.com/zjply4000/antigravity-approval/tree/d0a8fb90e68e882b9e37ea90cc1a7c314419bcd2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
