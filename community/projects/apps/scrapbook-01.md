# Scrapbook/01 by Franco Roura and Alexis Augoustis (share reels and links to yourself; Jev files them into your categories)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Save reels, TikToks, videos and links from any app's share sheet with one line about what they are; Scrapbook/01 sorts each save into a category, links related saves into a graph and exposes your library to your own AI through an MCP server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/franco-roura/scrapbook-01) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://d2gh6vwoycfx90.cloudfront.net) |
| Pricing and access | Self-hosting is free source (MIT or Apache-2.0) on your own AWS account with your own TypeSafe, embeddings and Claude keys. The hosted app is waitlist-only and uses prepaid credits (new accounts start with some free); credit-pack payments are not connected yet. Checked 2026-11-20. |
| Jev evidence | [`server/internal/ai/jev.go`](https://github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/server/internal/ai/jev.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [franco-roura](https://github.com/franco-roura). Independently curated. |
| Format | Go API + Expo app (MIT OR Apache-2.0) |
| Platform and availability | Expo / React Native app with share extension, web app, Go API on AWS Lambda (hosted waitlist or self-host). |
| Jev's role | Choice question that matches each new save to one of your existing categories; without a TypeSafe key, saves are not matched to existing categories. |
| Requirements | Go, Bun and Docker plus a WorkOS sandbox to run locally (a fake AI server stands in for Jev); for live sorting a `TYPESAFE_API_KEY`, an embeddings key and Claude. |
| License | [MIT OR Apache-2.0](https://github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/LICENSE-MIT) |

## When to use

- Keep a personal, self-sorting scrapbook of things you share to yourself from social apps.
- Mismatch: a mature product; the project is early (v0.1.0), the iOS share extension is untested on devices and the app UI is in Uruguayan Spanish.

## How it works

`server/internal/ai/jev.go` posts a single `choice` question to `/v1/systemone` with your category names as criteria and the save's note and metadata as state; the server uses the chosen label and its probabilities to file the item, while embeddings link related saves. Integration evidence: [`server/internal/ai/jev.go`](https://github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/server/internal/ai/jev.go).

## Get started

Run it locally with the bundled fake AI server, or self-host on AWS.

```sh
git clone https://github.com/franco-roura/scrapbook-01
cd scrapbook-01
# follow docs/getting-started.md (Go, Bun, Docker, WorkOS sandbox)
# live sorting: set TYPESAFE_API_KEY; self-hosting: docs/self-hosting.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/README.md](https://github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/README.md)
- Self-hosting guide: [github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/docs/self-hosting.md](https://github.com/franco-roura/scrapbook-01/blob/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e/docs/self-hosting.md)
- Waitlist page: [d2gh6vwoycfx90.cloudfront.net](https://d2gh6vwoycfx90.cloudfront.net)

## Limits and data handling

Each save's note and link metadata are sent to TypeSafe for sorting, and to embeddings and Claude providers for linking and AI features. The hosted app runs behind a waitlist and was not tried.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit 7ed1cbbc32fd](https://github.com/franco-roura/scrapbook-01/tree/7ed1cbbc32fd17b36dbea8a9e2102a3da110eb8e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
