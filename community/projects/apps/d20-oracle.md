# d20-oracle (one-page Go demo where Jev scores your name, profession and a d20 roll against the twelve D&D classes)

[All projects](../README.md) · [Web apps](README.md#web-apps)

One-page Go web demo: type a name and profession, roll a d20 for destiny and a d6 for a little weirdness, and Jev scores your identity and roll against the twelve core 5e classes in one choice question. The highest probability wins, up to two runners-up show as close calls, and a local d6 picks a quirk.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amscotti/d20-oracle) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/amscotti/d20-oracle#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you pay TypeSafe through your own key and cover any hosting. Checked 2026-11-03. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/amscotti/d20-oracle/blob/ea2e9c5aff01220472cc9dfad78caa98f56a4dcc/internal/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [amscotti](https://github.com/amscotti). Independently curated. |
| Format | Go web server with embedded HTMX frontend (single binary or scratch Docker image) |
| Platform and availability | Self-hosted Go server (browser UI); Docker image supported. |
| Jev's role | Scores the user's name, profession and roll against the twelve D&D classes. |
| Requirements | mise (Go toolchain) or Docker; a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/amscotti/d20-oracle/blob/ea2e9c5aff01220472cc9dfad78caa98f56a4dcc/LICENSE) |

## When to use

- Look at a small, complete example of one Jev choice question driving a web page.
- Mismatch: a toy demo; without a key the page loads but `/api/class` returns 503.

## How it works

`internal/jev/client.go` posts the identity and roll to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) as one choice question over twelve classes, with a 15 s deadline, two attempts and backoff on 429/529, and the server picks the top class and the runners-up from the probabilities. Integration evidence: [`internal/jev/client.go`](https://github.com/amscotti/d20-oracle/blob/ea2e9c5aff01220472cc9dfad78caa98f56a4dcc/internal/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
mise install
cp .env.example .env      # paste your key
mise run build
./d20-oracle -addr :8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the run steps, Docker usage and screenshot: [github.com/amscotti/d20-oracle#readme](https://github.com/amscotti/d20-oracle#readme)

## Limits and data handling

The typed name, profession and roll go to TypeSafe on your key; the page loads HTMX, Alpine.js and Open Props from pinned unpkg URLs with SRI hashes. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit ea2e9c5aff01](https://github.com/amscotti/d20-oracle/tree/ea2e9c5aff01220472cc9dfad78caa98f56a4dcc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
