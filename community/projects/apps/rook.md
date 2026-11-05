# Rook (open-source desktop app where named AI agents work as a team in channels and ask your approval first, with an optional Jev approval reviewer)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Open-source desktop app that gives AI agents a job, tools and a conversation each, lets them hand work to each other in channels and squads, and stops for your yes before sensitive actions. Its optional Auto Review can let a decision model answer approval requests: a `jev` provider calls TypeSafe System One directly, or `typesafe/jev-1.14` can be used through an OpenRouter connection, and below a confidence floor (default 0.5) it asks you instead.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/corvo-technology/rook) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://rookup.run) |
| Pricing and access | The README describes the local desktop edition as free and open source (Apache-2.0) with no account; model and Jev calls are billed by your own providers. Checked 2026-11-05. |
| Jev evidence | [`packages/adapters/src/jev-auto-review.ts`](https://github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/packages/adapters/src/jev-auto-review.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/rookupbot/status/2118167926498787828)). |
| Maintainer | [corvo-technology](https://github.com/corvo-technology). Independently curated. |
| Format | Desktop app (macOS, Windows, Linux; Apache-2.0 TypeScript monorepo with an install script) |
| Platform and availability | macOS, Windows and Linux desktop app (release installer or source build) |
| Jev's role | Optional Auto Review verifier that can pass or escalate agent approval requests using typed Jev decisions with a confidence floor. |
| Requirements | Run the release install script or build from source; a model connection (your own key, subscription or a local model). Auto Review with Jev needs a `TYPESAFE_API_KEY` or an OpenRouter connection. |
| License | [Apache-2.0](https://github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/LICENSE) |

## When to use

- Let a calibrated decision model screen agent tool-approval requests and fall back to you when it is unsure.
- Run a team of named agents locally with per-tool allow/ask/block rules.
- Mismatch: Jev is an optional approval checker, not the core of the app; the default checker is your own LLM, and the X post's mention of routing with Jev 1.14 was not confirmed in the code (routing in channels is described as done by the Chief agent).

## How it works

`JevAutoReviewProvider` wraps a TypeSafe HTTP decision provider (`providerId: jev`, default model from `DEFAULT_JEV_MODEL`, minimum confidence from `CORVO_AUTO_REVIEW_MIN_CONFIDENCE`) and `DecisionAutoReviewProvider` turns an approval request into a typed pass/ask decision; `.env.example` documents `CORVO_AUTO_REVIEW_PROVIDER=jev` and the OpenRouter route `typesafe/jev-1.14`. Integration evidence: [`packages/adapters/src/jev-auto-review.ts`](https://github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/packages/adapters/src/jev-auto-review.ts).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://github.com/corvo-technology/rook/releases/latest/download/install.sh | sh
# optional Auto Review with Jev: CORVO_AUTO_REVIEW_PROVIDER=jev and TYPESAFE_API_KEY=<your key>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/README.md](https://github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/README.md)
- Auto Review settings: [github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/.env.example](https://github.com/corvo-technology/rook/blob/54241a8a77e1b8b54d8b107bbc7e1d4712af0132/.env.example)
- Product site: [rookup.run](https://rookup.run)

## Limits and data handling

Approval requests (task text, tool name and truncated arguments) are sent to the configured decision provider; a confidence below the floor asks you instead. The Jev path is optional and off unless configured. Costs are on your key.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 54241a8a77e1](https://github.com/corvo-technology/rook/tree/54241a8a77e1b8b54d8b107bbc7e1d4712af0132). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
