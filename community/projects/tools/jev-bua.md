# Jev-BUA (browser agent where Jev picks the next click or field and element from a numbered page, with plain-English web-app tests)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser agent and test runner that connects to Chrome through Browser Use's Browser Harness: give it one goal and Jev picks an operation and a numbered element from the page in one request, while a small helper model writes text only for typing steps. It also runs plain-English test files with page-read checks as the verdict, replays verified runs with no model calls, and exposes an MCP server and a skill for coding agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AkshayReddyGujjula/Jev-BUA) |
| Maintainer | [AkshayReddyGujjula](https://github.com/AkshayReddyGujjula). Independently curated. |
| Format | Python CLI, library and MCP server (uv) |
| Requirements | Python and uv, Chrome with remote debugging; `TYPESAFE_API_KEY` for Jev and a `TEXT_MODEL_API_KEY` for the text helper. |
| License | [MIT](https://github.com/AkshayReddyGujjula/Jev-BUA/blob/5731b4679be012fcee44e09dfd2041cfbec47a59/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`AgentJevUltraFast/model.py`](https://github.com/AkshayReddyGujjula/Jev-BUA/blob/5731b4679be012fcee44e09dfd2041cfbec47a59/AgentJevUltraFast/model.py) at the pinned commit. |

## When to use

- Drive a real Chrome tab toward a goal, or write web-app tests as short plain-English steps that replay cheaply.
- Mismatch: the headline Google Flights timing is a historical baseline recorded before later changes, and a fresh benchmark is still pending.

## How it works

`AgentJevUltraFast/model.py` posts the indexed page elements to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) with an operation head and a target head in one round trip; checks read off the page decide pass or fail, and a helper model is called only for `TYPE_TEXT`. Integration evidence: [`AgentJevUltraFast/model.py`](https://github.com/AkshayReddyGujjula/Jev-BUA/blob/5731b4679be012fcee44e09dfd2041cfbec47a59/AgentJevUltraFast/model.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AkshayReddyGujjula/Jev-BUA.git
cd Jev-BUA
uv tool install --editable .
cp .env.example .env   # add TYPESAFE_API_KEY and TEXT_MODEL_API_KEY
jev "open youtube and search for MKBHD"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the test-spec format, demo clips and measurements: [github.com/AkshayReddyGujjula/Jev-BUA#readme](https://github.com/AkshayReddyGujjula/Jev-BUA#readme)
- Measurements: [github.com/AkshayReddyGujjula/Jev-BUA/blob/main/docs/performance.md](https://github.com/AkshayReddyGujjula/Jev-BUA/blob/main/docs/performance.md)

## Limits and data handling

Page element text and your goal go to TypeSafe on your key and a separate text-helper provider, and the agent acts in your Chrome session, so use a test profile. The README's timings are the author's own; the LICENSE file carries a Browser Use copyright line and the README calls this an independent personal project. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 5731b4679be0](https://github.com/AkshayReddyGujjula/Jev-BUA/tree/5731b4679be012fcee44e09dfd2041cfbec47a59). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
