# Lynkgrids AI for Jev

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Question pack, CLI, agent skill and Claude Code plugin that make typed TypeSafe Jev decisions on a Lynkgrids LinkedIn-leads pipeline — lead fit, reply intent, draft check and meeting readiness — each one Jev request with an `act` / `review` / `human` route set by confidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lynkread/Lynkgrids-AI-for-Jev) |
| Maintainer | [lynkread](https://github.com/lynkread). Independently curated. |
| Format | Node CLI (`lynkgrids-jev`), agent skill and Claude Code plugin with the Lynkgrids MCP wired in |
| Requirements | Node 20+ and a `TYPESAFE_API_KEY`; the agent plugin also needs a Lynkgrids workspace with an active plan or trial (browser sign-in through MCP). |
| License | [MIT](https://github.com/lynkread/Lynkgrids-AI-for-Jev/blob/9a5a30e36adb1a39327d37fd136941a7c15af361/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Lynkgrids is a commercial LinkedIn-leads product; its workspace needs an active paid plan or trial. The repository appears to be published by the Lynkgrids vendor. |

## When to use

- Triage LinkedIn leads and replies with typed decisions instead of free-text LLM judgments.
- Check outreach drafts for generic text, unsupported claims or a bad ask before sending.
- Mismatch: tied to Lynkgrids for data; the CLI works on JSON state you supply.

## How it works

[`lib/questions.js`](https://github.com/lynkread/Lynkgrids-AI-for-Jev/blob/9a5a30e36adb1a39327d37fd136941a7c15af361/lib/questions.js) holds every question and threshold; [`lib/jev.js`](https://github.com/lynkread/Lynkgrids-AI-for-Jev/blob/9a5a30e36adb1a39327d37fd136941a7c15af361/lib/jev.js) is a zero-dependency client for `/v1/systemone` with backoff; [`lib/decisions.js`](https://github.com/lynkread/Lynkgrids-AI-for-Jev/blob/9a5a30e36adb1a39327d37fd136941a7c15af361/lib/decisions.js) turns answers into decisions with an `act` / `review` / `human` route.

## Get started

Link the CLI and dry-run a pack without a key (README *CLI*):

```sh
git clone https://github.com/lynkread/Lynkgrids-AI-for-Jev.git && cd Lynkgrids-AI-for-Jev
npm link
lynkgrids-jev draft-check examples/draft-check.json --dry-run
```

Each pack is one Jev request billed to your TypeSafe key (`--dry-run` makes none); Lynkgrids is billed separately.

## Examples and demos

- Sample states: [`examples/`](https://github.com/lynkread/Lynkgrids-AI-for-Jev/tree/9a5a30e36adb1a39327d37fd136941a7c15af361/examples).
- Agent skill: [`skills/lynkgrids-jev/SKILL.md`](https://github.com/lynkread/Lynkgrids-AI-for-Jev/blob/9a5a30e36adb1a39327d37fd136941a7c15af361/skills/lynkgrids-jev/SKILL.md).

## Limits and data handling

Lead profiles, conversations and drafts go to TypeSafe; lead data comes from Lynkgrids through its MCP. Upstream advises pinning `--model jev-1.13.0` before tuning thresholds. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 9a5a30e36adb](https://github.com/lynkread/Lynkgrids-AI-for-Jev/tree/9a5a30e36adb1a39327d37fd136941a7c15af361). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
