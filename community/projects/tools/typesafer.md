# typesafer (unofficial R client for the TypeSafe API)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial in-development R package for the TypeSafe AI API: model discovery through `GET /v1/models` and evaluation through `POST /v1/systemone` with Noul, Choice and Score question constructors, timeouts, bounded retries, credential redaction and response structures kept as nested lists.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/reisfe/typesafer) |
| Maintainer | [reisfe](https://github.com/reisfe). Independently curated. |
| Format | R package (GitHub install) |
| Requirements | R with `remotes`; a TypeSafe API key in `TYPESAFE_API_KEY`. |
| License | [GPL-3.0](https://github.com/reisfe/typesafer/blob/72d40c954fee30ae8eacc91ac26c7b838e208f37/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`R/client.R`](https://github.com/reisfe/typesafer/blob/72d40c954fee30ae8eacc91ac26c7b838e208f37/R/client.R) at the pinned commit. |

## When to use

- Call Jev from R scripts or notebooks for classification and scoring.
- Mix Noul, Choice and Score questions in one request from R.
- Mismatch: thin client only; data-frame and vectorised helpers are deferred.

## How it works

`R/client.R` builds the client from `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL` (default `https://api.typesafe.ai`) and `TYPESAFE_DEFAULT_MODEL` (default `jev-latest`) and maps each endpoint to an R function. Integration evidence: [`R/client.R`](https://github.com/reisfe/typesafer/blob/72d40c954fee30ae8eacc91ac26c7b838e208f37/R/client.R).

## Get started

From the upstream README (not run on the review host):

```sh
install.packages("remotes")
remotes::install_github("reisfe/typesafer")
# Sys.setenv(TYPESAFE_API_KEY = "...")
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/reisfe/typesafer#readme](https://github.com/reisfe/typesafer#readme)
- API contract: [github.com/reisfe/typesafer/blob/main/docs/api-contract.md](https://github.com/reisfe/typesafer/blob/main/docs/api-contract.md)

## Limits and data handling

State and questions you pass are sent to TypeSafe. Unofficial and not affiliated with TypeSafe; GPL-3.0 licensed.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 72d40c954fee](https://github.com/reisfe/typesafer/tree/72d40c954fee30ae8eacc91ac26c7b838e208f37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
