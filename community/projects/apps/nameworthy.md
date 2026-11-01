# nameworthy (World of Warcraft: Forever name auditor that grades a name with one Jev call)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Single-binary Go web app for fun: enter a WoW: Forever first name and surname, optionally pick race and class, and get a grade from S to F, a naming style, a six-stat sheet and probability signals such as 'likely to be reported', all from one System One call with the full distribution shown.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amscotti/nameworthy) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/amscotti/nameworthy#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you supply a TypeSafe key. Checked 2026-11-01. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/amscotti/nameworthy/blob/502c6bc221bba4993a3b778c9dfae0e53fffa410/internal/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [amscotti](https://github.com/amscotti). Independently curated. |
| Format | Web app (single Go binary or Docker) |
| Platform and availability | Self-hosted web app in the browser; no hosted instance verified. |
| Jev's role | Grades a name, picks a style and rates six stats in one call. |
| Requirements | Go or Docker; a TypeSafe key. |
| License | [MIT](https://github.com/amscotti/nameworthy/blob/502c6bc221bba4993a3b778c9dfae0e53fffa410/LICENSE) |

## When to use

- Show off Jev's choice, score and noul answers in a playful single-page app.
- Mismatch: entertainment only; not Blizzard's actual naming policy.

## How it works

`internal/jev/client.go` sends one request to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with choice, score and noul questions; `internal/server/server.go` renders the grade, style, stats and signals with their probabilities. Integration evidence: [`internal/jev/client.go`](https://github.com/amscotti/nameworthy/blob/502c6bc221bba4993a3b778c9dfae0e53fffa410/internal/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
TYPESAFE_API_KEY=sk-... ./nameworthy -addr :8080
# or: docker build -t nameworthy . && docker run --rm -p 127.0.0.1:8080:8080 --env-file .env nameworthy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/amscotti/nameworthy#readme](https://github.com/amscotti/nameworthy#readme)

## Limits and data handling

Names you enter are sent to TypeSafe. Not affiliated with Blizzard. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit 502c6bc221bb](https://github.com/amscotti/nameworthy/tree/502c6bc221bba4993a3b778c9dfae0e53fffa410). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
