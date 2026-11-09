# Sure fork with Jev (self-hosted personal-finance app that can classify transactions with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Independent Portuguese-language fork of Sure (the Maybe Finance community fork) that adds a Jev provider for transaction classification and evals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DougCristiano/sure) |
| Maintainer | [DougCristiano](https://github.com/DougCristiano). Independently curated. |
| Format | Rails app (AGPL-3.0) |
| Requirements | Self-hosted Sure setup (Docker/Rails) and a TypeSafe key, or OpenRouter via `JEV_ENDPOINT`. |
| License | [AGPL-3.0](https://github.com/DougCristiano/sure/blob/9706ecddc83d6c4021a629633a4865515fbca67a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/models/provider/jev.rb`](https://github.com/DougCristiano/sure/blob/9706ecddc83d6c4021a629633a4865515fbca67a/app/models/provider/jev.rb) at the pinned commit. |

## When to use

- Auto-categorize transactions with typed Jev choices.
- Run classification evals in a finance app.
- Mismatch: independent fork; not affiliated with Maybe Finance or Sure.

## How it works

`provider/jev.rb` implements `Provider::Jev` (ClassificationConcept) against `https://api.typesafe.ai/v1/systemone` with `jev-latest`, names the gateway in the data-sharing disclosure, and `lib/tasks/evals.rake` runs evals. Integration evidence: [`app/models/provider/jev.rb`](https://github.com/DougCristiano/sure/blob/9706ecddc83d6c4021a629633a4865515fbca67a/app/models/provider/jev.rb).

## Get started

Self-host the app per the Sure docs and set the Jev settings under hosting settings.

```sh
git clone https://github.com/DougCristiano/sure.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DougCristiano/sure/blob/9706ecddc83d6c4021a629633a4865515fbca67a/README.md](https://github.com/DougCristiano/sure/blob/9706ecddc83d6c4021a629633a4865515fbca67a/README.md)

## Limits and data handling

Transaction descriptions are sent to TypeSafe (or your gateway) when the provider is on.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 9706ecddc83d](https://github.com/DougCristiano/sure/tree/9706ecddc83d6c4021a629633a4865515fbca67a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
