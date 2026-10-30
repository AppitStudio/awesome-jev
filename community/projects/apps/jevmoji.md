# jevmoji (web app that suggests emoji reactions for a chat message by scoring 200 emojis with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Small Go web app: type a line of group-chat banter and the server scores all 200 catalog emojis in one Jev call, one yes/no question per emoji, and shows the best four (50% or higher) plus a fifth above 75% as Slack-style reactions. HTMX front end embedded in a single static binary; Docker and Cloud Run deploy steps included. Built as an example integration of the Jev API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amscotti/jevmoji) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/amscotti/jevmoji#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; bring your own TypeSafe key and any hosting costs. Checked 2026-10-30. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/amscotti/jevmoji/blob/12c2953f6cc195c01f89747fb82a583da08059e6/internal/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [amscotti](https://github.com/amscotti). Independently curated. |
| Format | Self-hosted Go web app |
| Platform and availability | Self-hosted web app (local binary, Docker or Cloud Run); no public instance verified. |
| Jev's role | Scores how well each of 200 emojis fits the message so the app can show the top reactions. |
| Requirements | Go (via mise) or Docker, and a TypeSafe API key. |
| License | [MIT](https://github.com/amscotti/jevmoji/blob/12c2953f6cc195c01f89747fb82a583da08059e6/LICENSE) |

## When to use

- See a compact, readable example of many yes/no questions over one state in a single Jev call.
- Mismatch: a toy demo; no public hosted instance verified.

## How it works

`internal/jev/client.go` sends the message as state with one Noul question per emoji to `/v1/systemone` (`jev-latest`) and returns the probabilities the server ranks. Integration evidence: [`internal/jev/client.go`](https://github.com/amscotti/jevmoji/blob/12c2953f6cc195c01f89747fb82a583da08059e6/internal/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env  # paste your TYPESAFE_API_KEY
mise run build
./jevmoji -addr :8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docker: docker build -t jevmoji:local . && docker run --rm --env-file .env -p 8080:8080 jevmoji:local

## Limits and data handling

Messages you type are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 12c2953f6cc1](https://github.com/amscotti/jevmoji/tree/12c2953f6cc195c01f89747fb82a583da08059e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
