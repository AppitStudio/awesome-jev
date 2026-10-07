# banterarena-engine

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Open Go scoring engine behind Banter Arena: pure-function banter and country scoring, attribution checks, and two-tier reply sentiment where free rules settle obvious replies and an optional TypeSafe Jev adapter judges whether a reply laughs, concedes or calls the joke weak; labelled yardstick in tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muse254/banterarena-engine) |
| Maintainer | [muse254](https://github.com/muse254). Independently curated. |
| Format | Go module (`github.com/muse254/banterarena-engine`) with `jev` adapter package and simulation command |
| Requirements | Go; `TYPESAFE_API_KEY` only for the optional `jev` adapter (rules, attribution and simulation run offline). |
| License | [MIT](https://github.com/muse254/banterarena-engine/blob/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Score engagement-based competitions with documented constants and language-agnostic test vectors.
- Use the tiered pattern — free rules first, Jev for the rest — for reply sentiment.
- Mismatch: gazetteer covers a handful of African countries and English terms; anti-brigading lives in the app, not here.

## How it works

[`score.go`](https://github.com/muse254/banterarena-engine/blob/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/score.go) implements the points formula with every constant explained; [`attribution/`](https://github.com/muse254/banterarena-engine/tree/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/attribution) checks whether a joke targets the claimed country. [`sentiment/tiered.go`](https://github.com/muse254/banterarena-engine/blob/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/sentiment/tiered.go) settles laugh-only or mock-only replies by rule and sends the rest, with the joke they reply to, to [`jev/sentiment.go`](https://github.com/muse254/banterarena-engine/blob/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/jev/sentiment.go) for two yes/no questions. [`jev/testdata/labelled_replies.json`](https://github.com/muse254/banterarena-engine/blob/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/jev/testdata/labelled_replies.json) is the labelled multilingual yardstick.

## Get started

Run the offline simulation and tests:

```sh
git clone https://github.com/muse254/banterarena-engine.git && cd banterarena-engine
go run ./cmd/simulate
go test ./...
```

Rules and simulation are offline; the `jev` adapter is billed to your TypeSafe key.

## Examples and demos

- Formula as data: [`testdata/vectors.json`](https://github.com/muse254/banterarena-engine/blob/ec207d24a044edbe99a9a9f3c6751208fe36e2e9/testdata/vectors.json).
- README *Use it* Go snippet and *Did the joke land?* section.

## Limits and data handling

Constants and scenarios are the maintainer's judgement; the heuristic sentiment is English-centric. Reply text and the joke go to TypeSafe when the Jev adapter is used. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit ec207d24a044](https://github.com/muse254/banterarena-engine/tree/ec207d24a044edbe99a9a9f3c6751208fe36e2e9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
