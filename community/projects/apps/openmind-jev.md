# Openmind (self-hosted commonplace book with Jev-assisted organisation)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted place to save links, quotes, images and notes and find them again by a fragment; optional AI-assisted organisation uses Jev for capture tags, Lens re-ranking and daily Drift scoring.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rohithgilla12/open-mind) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Rohithgilla12/open-mind#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (AGPL-3.0); you host it and pay any TypeSafe usage. Checked 2026-11-11. |
| Jev evidence | [`apps/api/internal/jev/client.go`](https://github.com/Rohithgilla12/open-mind/blob/04ee1bc32390d3cb4872190da4c77ba2123da62e/apps/api/internal/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Rohithgilla12](https://github.com/Rohithgilla12). Independently curated. |
| Format | Self-hosted web app (Go API, AGPL-3.0) |
| Platform and availability | Web (self-hosted) |
| Jev's role | Jev suggests capture tags, re-ranks Lens results and scores daily Drift items. |
| Requirements | A self-hosted deployment, `OPENMIND_TYPESAFE_API_KEY`, and the per-user AI-assisted organisation setting. |
| License | [AGPL-3.0](https://github.com/Rohithgilla12/open-mind/blob/04ee1bc32390d3cb4872190da4c77ba2123da62e/LICENSE) |

## When to use

- Tag and re-rank a personal knowledge store with typed decisions.
- Mismatch: AGPL-3.0; Jev needs both a server key and a per-user opt-in (default off).

## How it works

`apps/api/internal/jev/client.go` is a hand-rolled `POST /v1/systemone` client that is disabled with an empty key; `docs/self-hosting.md` lists the Jev surfaces and what is sent. Integration evidence: [`apps/api/internal/jev/client.go`](https://github.com/Rohithgilla12/open-mind/blob/04ee1bc32390d3cb4872190da4c77ba2123da62e/apps/api/internal/jev/client.go).

## Get started

Self-host per `docs/self-hosting.md`, set the key, then enable AI-assisted organisation per user.

```sh
git clone https://github.com/Rohithgilla12/open-mind.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Self-hosting doc: [github.com/Rohithgilla12/open-mind/blob/04ee1bc32390d3cb4872190da4c77ba2123da62e/docs/self-hosting.md](https://github.com/Rohithgilla12/open-mind/blob/04ee1bc32390d3cb4872190da4c77ba2123da62e/docs/self-hosting.md)

## Limits and data handling

With both switches on, URL, title, site, short excerpts and a filtered 14-day activity summary go to TypeSafe; never full documents per the docs.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 04ee1bc32390](https://github.com/Rohithgilla12/open-mind/tree/04ee1bc32390d3cb4872190da4c77ba2123da62e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
