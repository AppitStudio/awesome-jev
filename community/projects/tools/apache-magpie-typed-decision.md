# Apache Magpie typed-decision tool by the Apache Magpie project (agent-skill toolkit for open-source maintainers with a Jev-backed typed decision contract)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Apache Magpie is a set of sandboxed agent skills that help maintainers triage issues and PRs, review code and handle security reports, with every outgoing action drafted for a person to post. Its typed-decision tool defines choice, score and noul operations with TypeSafe's Jev as the reference backend and a local OpenAI-compatible provider as the offline option; the PR-triage skill can run it as an opt-in shadow pre-filter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/apache/magpie) |
| Maintainer | [apache](https://github.com/apache). Independently curated. |
| Format | Agent skills marketplace plugin with a Python (uv, stdlib-only) tool |
| Requirements | An agent such as Claude Code or Codex; Python 3.11+ via uv; `TYPESAFE_API_KEY` (or `JEV_API_KEY`) plus a privacy-LLM opt-in entry to enable Jev. |
| License | [Apache-2.0](https://github.com/apache/magpie/blob/46a7f2f31efdcc20a0bde0515c66f225baf66e34/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tools/typed-decision/src/typed_decision/providers/jev.py`](https://github.com/apache/magpie/blob/46a7f2f31efdcc20a0bde0515c66f225baf66e34/tools/typed-decision/src/typed_decision/providers/jev.py) at the pinned commit. |

## When to use

- Add calibrated typed decisions to maintainer workflows with explicit privacy gating.
- Mismatch: users who only want Jev; it is one tool in a larger maintainer toolkit, and the shadow pre-filter is advisory only.

## How it works

`providers/jev.py` sends one question per operation to `https://api.typesafe.ai/v1/systemone` with the model pinned to `jev-1.14.0`, using only `urllib.request`; outbound prompts are gated by Magpie's privacy-llm tool and denied by default. Integration evidence: [`tools/typed-decision/src/typed_decision/providers/jev.py`](https://github.com/apache/magpie/blob/46a7f2f31efdcc20a0bde0515c66f225baf66e34/tools/typed-decision/src/typed_decision/providers/jev.py).

## Get started

Install Magpie from its marketplace per the README, then opt in to the typed-decision provider in your project config.

```sh
# see https://magpie.apache.org/ for marketplace install
uv run --project tools/typed-decision python -c "import typed_decision"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tool docs: [magpie.apache.org/docs/tools/typed-decision/readme/](https://magpie.apache.org/docs/tools/typed-decision/readme/)
- Contract: [github.com/apache/magpie/blob/46a7f2f31efdcc20a0bde0515c66f225baf66e34/tools/typed-decision/tool.md](https://github.com/apache/magpie/blob/46a7f2f31efdcc20a0bde0515c66f225baf66e34/tools/typed-decision/tool.md)

## Limits and data handling

Jev use is opt-in and needs a data-residency entry with maintainer sign-off; PR metadata is sent to TypeSafe when enabled. The README says Magpie is in development for ASF and Python core projects.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 46a7f2f31efd](https://github.com/apache/magpie/tree/46a7f2f31efdcc20a0bde0515c66f225baf66e34). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
