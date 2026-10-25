# ToS Decipher (terms-of-service and privacy-policy reviewer whose claims are checked by Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

English and Spanish web app, Chrome/Edge MV3 extension and Python API that summarise terms of service and privacy policies, highlight important clauses next to their source text and find policy links on a page; Jev classifies links and verifies each finding against the source passages.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/javierBrenesAI/ToS-Defender) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/javierBrenesAI/ToS-Defender#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. You supply OpenRouter and TypeSafe keys. Checked 2026-10-25. |
| Jev evidence | [`apps/api/pipeline.py`](https://github.com/javierBrenesAI/ToS-Defender/blob/13ebb794debf6f79e14024bee131c30ee4c2b5b0/apps/api/pipeline.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [javierBrenesAI](https://github.com/javierBrenesAI). Independently curated. |
| Format | Browser extension, web app and FastAPI service |
| Platform and availability | Chrome/Edge extension loaded unpacked, talking to a local API at `localhost:8000`; not packaged for general distribution. |
| Jev's role | Core: with `TYPESAFE_API_KEY` set, Jev classifies policy links and verifies the generated claims in one bundled request; policy analysis itself uses an OpenRouter model. |
| Requirements | Python with uv, Node.js 22+; OpenRouter and TypeSafe keys for live analysis. |
| License | [MIT](https://github.com/javierBrenesAI/ToS-Defender/blob/13ebb794debf6f79e14024bee131c30ee4c2b5b0/LICENSE) |

## When to use

- Understand a policy's notable terms before you agree to it.
- See a generated finding next to the source excerpt it came from.
- Mismatch: not legal advice; generated explanations can be incomplete or wrong.

## How it works

`pipeline.py` uses `langchain_typesafe`'s `TypeSafeClassifier` with Noul, Choice and Score questions to classify page links as legal documents and to check claims against passages; claim verification refuses to run without a TypeSafe key. Integration evidence: [`apps/api/pipeline.py`](https://github.com/javierBrenesAI/ToS-Defender/blob/13ebb794debf6f79e14024bee131c30ee4c2b5b0/apps/api/pipeline.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # OPENROUTER_API_KEY, TYPESAFE_API_KEY
uv run uvicorn apps.api.server:app --reload --port 8000
npm ci && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/javierBrenesAI/ToS-Defender#readme](https://github.com/javierBrenesAI/ToS-Defender#readme)

## Limits and data handling

Policy text and link labels go to OpenRouter and TypeSafe through your local API. The extension excludes form fields from extraction and reads pages only after you start a review or enable automatic review.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 13ebb794debf](https://github.com/javierBrenesAI/ToS-Defender/tree/13ebb794debf6f79e14024bee131c30ee4c2b5b0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
