# SmartDoc Vision (self-hosted archive and drawing review platform with Jev classifiers)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Chinese-language self-hosted review platform for archives, drawings, scans and text: a Go and Gin backend with MySQL and Redis and a Vue 3 admin console run configurable, traceable review pipelines on general LLMs and on Jev Choice and Noul classifiers, with model failover, circuit breaking and token accounting.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ImYoyoData/smart-doc-vision) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ImYoyoData/smart-doc-vision#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. You host MySQL and Redis and supply provider keys. Checked 2026-10-25. |
| Jev evidence | [`backend/internal/ai/jev.go`](https://github.com/ImYoyoData/smart-doc-vision/blob/0c0888275413015f5865bcc792509c77d8d2330d/backend/internal/ai/jev.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ImYoyoData](https://github.com/ImYoyoData). Independently curated. |
| Format | Self-hosted web app (Go, Vue 3) |
| Platform and availability | Self-hosted with Docker Compose or a single Go binary that serves the admin console. |
| Jev's role | Optional: Jev is one of two provider kinds; review configurations can use Jev Choice and Noul questions for classification, beside general LLMs. |
| Requirements | Docker Compose, or Go with MySQL and Redis; your own LLM keys and a TypeSafe key for the Jev provider. |
| License | [MIT](https://github.com/ImYoyoData/smart-doc-vision/blob/0c0888275413015f5865bcc792509c77d8d2330d/LICENSE) |

## When to use

- Run auditable review pipelines on scanned documents and drawings in-house.
- Use Jev for cheap typed classification and fall back across models on failure.
- Mismatch: docs and UI are in Chinese.

## How it works

`backend/internal/ai/jev.go` posts a state plus typed Choice and Noul questions to `{base}/v1/systemone` (default `https://api.typesafe.ai/v1`, `jev-latest`); a failed call moves to the next enabled model in the same category. Integration evidence: [`backend/internal/ai/jev.go`](https://github.com/ImYoyoData/smart-doc-vision/blob/0c0888275413015f5865bcc792509c77d8d2330d/backend/internal/ai/jev.go).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # MySQL, Redis, JWT_SECRET, MASTER_KEY, JEV_BASE_URL, JEV_MODEL
docker compose up -d --build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/ImYoyoData/smart-doc-vision#readme](https://github.com/ImYoyoData/smart-doc-vision#readme)

## Limits and data handling

Documents and extracted text under review go to the providers each review configuration uses. You run and secure the database, Redis and stored files.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 0c0888275413](https://github.com/ImYoyoData/smart-doc-vision/tree/0c0888275413015f5865bcc792509c77d8d2330d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
