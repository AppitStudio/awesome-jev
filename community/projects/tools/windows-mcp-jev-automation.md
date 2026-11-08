# Windows-MCP × Jev (desktop automation with TypeSafe Jev bounded-action decisions)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Worked example (in Chinese) that posts approved daily reports into DingTalk on Windows by combining Windows-MCP, TypeSafe Jev bounded-action judgments, a local executor and update watching, to cut LLM observe/act round trips.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xvlihao11/windows-mcp-jev-automation) |
| Maintainer | [xvlihao11](https://github.com/xvlihao11). Independently curated. |
| Format | Python workflow source + docs (no SPDX license file on the reviewed commit) |
| Requirements | Windows, Windows-MCP, DingTalk desktop, Python 3, and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`asphalt-daily/wincli-trial/jev_desktop_trial.py`](https://github.com/xvlihao11/windows-mcp-jev-automation/blob/32950de0fc867efd2ba95c35e89032499899abf9/asphalt-daily/wincli-trial/jev_desktop_trial.py) at the pinned commit. |

## When to use

- Study a concrete pattern for Jev-gated Windows desktop automation.
- Reduce repeated screenshot/observe calls to a large model.
- Mismatch: not a download-and-run package; tailored to DingTalk; no OSI license on the reviewed commit.

## How it works

`asphalt-daily/wincli-trial/jev_desktop_trial.py` posts screen state and a bounded action list to `https://api.typesafe.ai/v1/systemone`; `docs/reproduction.md` and synthetic decision summaries document the trials. Integration evidence: [`asphalt-daily/wincli-trial/jev_desktop_trial.py`](https://github.com/xvlihao11/windows-mcp-jev-automation/blob/32950de0fc867efd2ba95c35e89032499899abf9/asphalt-daily/wincli-trial/jev_desktop_trial.py).

## Get started

Read `docs/reproduction.md`, adapt the config samples to your own report store and desktop tools.

```sh
git clone https://github.com/xvlihao11/windows-mcp-jev-automation.git && cd windows-mcp-jev-automation
export TYPESAFE_API_KEY=...
cat docs/reproduction.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/xvlihao11/windows-mcp-jev-automation/blob/32950de0fc867efd2ba95c35e89032499899abf9/README.md](https://github.com/xvlihao11/windows-mcp-jev-automation/blob/32950de0fc867efd2ba95c35e89032499899abf9/README.md)

## Limits and data handling

Desktop state sent for decisions goes to TypeSafe on your key; personal reports and raw screenshots are not in the repository.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 32950de0fc86](https://github.com/xvlihao11/windows-mcp-jev-automation/tree/32950de0fc867efd2ba95c35e89032499899abf9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
