# fastbrowse (open-source browser agent where Jev picks each control from the ones the page actually has)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Python browser agent with a Rust core: each page is indexed into the controls it really has and Jev, as a choice model, picks the next one, so the agent cannot click something that is not there. Answers cite verbatim page quotes, and submit, pay, delete and send actions wait for code-level approval with step, time and dollar limits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/agent-labs-dev/fastbrowse) |
| Maintainer | [agent-labs-dev](https://github.com/agent-labs-dev). Independently curated. |
| Format | Python package (`uvx fastbrowse`) with a Rust core |
| Requirements | Python 3.13+; a TypeSafe key (recommended) or an OpenRouter / Vercel AI Gateway key for Jev and the planning LLM. |
| License | [MIT](https://github.com/agent-labs-dev/fastbrowse/blob/98936978ca81e4ea1af351594e0100c5ac09c0b4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/cjberragan/status/2116267217033793920)). |
| Jev evidence | [`crates/fastbrowse-clients/src/system_one.rs`](https://github.com/agent-labs-dev/fastbrowse/blob/98936978ca81e4ea1af351594e0100c5ac09c0b4/crates/fastbrowse-clients/src/system_one.rs) at the pinned commit. |

## When to use

- Run browser tasks at volume where each step is a closed choice over the page's real controls.
- Mismatch: Jev only picks actions; planning, reading and writing still run on a separate LLM.

## How it works

`crates/fastbrowse-clients/src/system_one.rs` calls `POST /v1/systemone` on TypeSafe directly (or OpenRouter, AIMLAPI, Telnyx and other System One hosts) with `jev-1.13`; the planner LLM proposes, Jev picks one indexed control, and code enforces approvals, secrets and limits. Provider failover order is documented in `docs/jev.md`. Integration evidence: [`crates/fastbrowse-clients/src/system_one.rs`](https://github.com/agent-labs-dev/fastbrowse/blob/98936978ca81e4ea1af351594e0100c5ac09c0b4/crates/fastbrowse-clients/src/system_one.rs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
uvx fastbrowse "What is the title of the top story right now?" --start https://news.ycombinator.com/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project announcement on X: [x.com/cjberragan/status/2116267217033793920](https://x.com/cjberragan/status/2116267217033793920)
- PyPI: [pypi.org/project/fastbrowse/](https://pypi.org/project/fastbrowse/)

## Limits and data handling

Page content and indexed controls are sent to the configured Jev host and LLM provider. Beta status per the README; published speed and cost comparisons are the maintainers' own and were not reproduced. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 98936978ca81](https://github.com/agent-labs-dev/fastbrowse/tree/98936978ca81e4ea1af351594e0100c5ac09c0b4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
