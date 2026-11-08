# Writ (contract-first AI development workflow with an optional TypeSafe Jev judgment provider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Spec-first multi-agent SDLC framework for Claude Code; `jev-judge.py` lets TypeSafe Jev pre-judge acceptance criteria, decide when to ask questions, and log shadow verdicts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sellke/writ) |
| Maintainer | [sellke](https://github.com/sellke). Independently curated. |
| Format | Claude Code plugin + Python scripts (MIT) |
| Requirements | Claude Code, Python 3, and a TypeSafe key (direct or Vercel AI Gateway). |
| License | [MIT](https://github.com/sellke/writ/blob/a5f5dc0c7c19c779aa49f16767f7d9d9c25bf058/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev-judge.py`](https://github.com/sellke/writ/blob/a5f5dc0c7c19c779aa49f16767f7d9d9c25bf058/scripts/jev-judge.py) at the pinned commit. |

## When to use

- Flag contradictory or ambiguous acceptance criteria.
- Decide when an agent should ask instead of act.
- Mismatch: advisory only; humans own the gates.

## How it works

`jev-judge.py` posts to `/v1/systemone` (stdlib urllib, retries) for spec-findings, doubt decisions and setup; it is enabled only when `.writ/config.md` names a provider and the key exists. Integration evidence: [`scripts/jev-judge.py`](https://github.com/sellke/writ/blob/a5f5dc0c7c19c779aa49f16767f7d9d9c25bf058/scripts/jev-judge.py).

## Get started

Install the Writ plugin, then run `scripts/jev-judge.py setup --provider typesafe`.

```sh
git clone https://github.com/sellke/writ.git && cd writ
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sellke/writ/blob/a5f5dc0c7c19c779aa49f16767f7d9d9c25bf058/README.md](https://github.com/sellke/writ/blob/a5f5dc0c7c19c779aa49f16767f7d9d9c25bf058/README.md)

## Limits and data handling

Spec text and criteria are sent to TypeSafe when the provider is enabled.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit a5f5dc0c7c19](https://github.com/sellke/writ/tree/a5f5dc0c7c19c779aa49f16767f7d9d9c25bf058). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
