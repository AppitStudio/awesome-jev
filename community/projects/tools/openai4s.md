# OpenAI4S (open scientific research agent with a default-off TypeSafe Jev judgment layer)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

PKU-YuanGroup's open-source hybrid scientific research agent; an experimental, default-off TypeSafe Jev layer adds skill recommendation and literature-claim checks with a kill switch.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PKU-YuanGroup/OpenAI4S) |
| Maintainer | [PKU-YuanGroup](https://github.com/PKU-YuanGroup). Independently curated. |
| Format | Python agent + web UI (MIT) |
| Requirements | Python 3.10+, a chat provider (e.g. Doubao via Volcengine Ark) and `OPENAI4S_TYPESAFE_API_KEY` to enable judgment. |
| License | [MIT](https://github.com/PKU-YuanGroup/OpenAI4S/blob/6268598ae628e55e2e15e3f615be842639bacb20/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`openai4s/judgment/disclosure.py`](https://github.com/PKU-YuanGroup/OpenAI4S/blob/6268598ae628e55e2e15e3f615be842639bacb20/openai4s/judgment/disclosure.py) at the pinned commit. |

## When to use

- Add calibrated checks to a research agent.
- Run a low-cost research agent with optional Jev judgments.
- Mismatch: judgment layer is experimental and off by default.

## How it works

The judgment layer (`openai4s/judgment/`) is off by default, pins `jev-1.13.0`, and reports what each capability sends; `doctor` shows audit status (see `docs/experimental-judgment.md`). Integration evidence: [`openai4s/judgment/disclosure.py`](https://github.com/PKU-YuanGroup/OpenAI4S/blob/6268598ae628e55e2e15e3f615be842639bacb20/openai4s/judgment/disclosure.py).

## Get started

Install per README, then enable experimental judgment in config or the UI with your TypeSafe key.

```sh
git clone https://github.com/PKU-YuanGroup/OpenAI4S.git && cd OpenAI4S
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Judgment guide: [github.com/PKU-YuanGroup/OpenAI4S/blob/6268598ae628e55e2e15e3f615be842639bacb20/docs/experimental-judgment.md](https://github.com/PKU-YuanGroup/OpenAI4S/blob/6268598ae628e55e2e15e3f615be842639bacb20/docs/experimental-judgment.md)

## Limits and data handling

When enabled, the content of each judged capability is sent to TypeSafe; see the disclosure doc.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 6268598ae628](https://github.com/PKU-YuanGroup/OpenAI4S/tree/6268598ae628e55e2e15e3f615be842639bacb20). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
