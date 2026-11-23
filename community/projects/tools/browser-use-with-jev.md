# Browser Use with Jev by garry-schuette (Jev picks browser actions in the Codex sidebar or with Browser Use)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Lets Jev choose the next concrete browser action from validated candidates while a host model handles generation, recovery and final verification. In Codex desktop it drives the visible in-app browser through a bundled skill; the Python SDK and standalone mode keep the installed Browser Use engine unpatched. Early alpha with a public verification ledger, including failed holdout runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/garry-schuette/browser-use-with-jev) |
| Maintainer | [garry-schuette](https://github.com/garry-schuette). Independently curated. |
| Format | Python package + Codex skill |
| Requirements | Python 3.11+ and uv; a TypeSafe API key and a Browser Use-compatible host model (for example an OpenAI key); `browser-use==0.13.10`. |
| License | [MIT](https://github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/browser_use_with_jev/jev.py`](https://github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/src/browser_use_with_jev/jev.py) at the pinned commit. |

## When to use

- Experiment with Jev as a fast action picker under a larger browsing agent, with the host keeping control of text and completion.
- Mismatch: reliable unattended browsing; the author's holdout runs passed 0/5 to 1/5 new tasks before later fixes.

## How it works

`src/browser_use_with_jev/jev.py` posts Choice questions to `https://api.typesafe.ai/v1/systemone`, reading `TYPESAFE_API_KEY` only from the environment or an explicitly given file. Jev selects clicks, scrolls, tab switches and fields; the host supplies text, uploads, extraction and the final assessment, and the page and target are rechecked before each action. Integration evidence: [`src/browser_use_with_jev/jev.py`](https://github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/src/browser_use_with_jev/jev.py).

## Get started

Install, add keys and run the standalone example (it opens a browser and makes real model calls).

```sh
git clone https://github.com/garry-schuette/browser-use-with-jev && cd browser-use-with-jev
uv sync --locked
cp .env.example .env   # TYPESAFE_API_KEY, OPENAI_API_KEY
uv run --env-file .env python examples/basic.py --model YOUR_HOST_MODEL_ID "Open https://example.com and report its title."
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Verification record: [github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/docs/five-round-real-site-verification.md](https://github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/docs/five-round-real-site-verification.md)
- Holdout results: [github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/docs/holdout-verification.md](https://github.com/garry-schuette/browser-use-with-jev/blob/8b367416861cae49c1a9f29320c3b9eec3c8abe5/docs/holdout-verification.md)

## Limits and data handling

Page observations and candidate actions go to TypeSafe and the host provider. Early alpha. The README's clone and CI links point to ZiyaoLi/browser-use-with-jev, which returned 404 on the review date; the LICENSE copyright is ZiyaoLi.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 8b367416861c](https://github.com/garry-schuette/browser-use-with-jev/tree/8b367416861cae49c1a9f29320c3b9eec3c8abe5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
