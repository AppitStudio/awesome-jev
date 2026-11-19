# pi-jev-router by Jakub Čermák (opt-in jev/auto model for Pi that routes each request to a model and thinking level, with optional Jev classification)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi 1.5 package that registers one selectable virtual model, `jev/auto`, and routes each request to a physical model and thinking level by task class and risk. Nothing happens until you select it; Pi keeps requests, tools, retries and sessions. Local policy works without a network call; optional Jev classification (default off, needs terms acknowledged) sends only metadata through Pi's classifier API. Includes status and preview commands showing exactly what would go to Jev, and a default-off assignment-scoring service.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jakucermak/pi-jev-router) |
| Maintainer | [jakucermak](https://github.com/jakucermak). Independently curated. |
| Format | Pi package (TypeScript) |
| Requirements | Pi 1.5 with the models you want to route to; for the optional Jev classification, a Jev model (`typesafe/jev-latest` by default) configured in Pi's classifier API. |
| License | [MIT](https://github.com/jakucermak/pi-jev-router/blob/e82211bc3378ae437ab2f7ac8e980db21fd80901/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classifier.ts`](https://github.com/jakucermak/pi-jev-router/blob/e82211bc3378ae437ab2f7ac8e980db21fd80901/src/classifier.ts) at the pinned commit. |

## When to use

- Let Pi choose a cheaper or stronger model per request without giving up control of the session.
- Mismatch: an always-on Jev router; Jev classification is off by default and routing is mostly local policy.

## How it works

`src/classifier.ts` sends metadata-only Jev classifications through the host's native classifier API when `jev.enabled` and `termsAcknowledged` are set in `jev-router.json`; `src/policy.ts` turns the class and risk into a model and level. Integration evidence: [`src/classifier.ts`](https://github.com/jakucermak/pi-jev-router/blob/e82211bc3378ae437ab2f7ac8e980db21fd80901/src/classifier.ts).

## Get started

Try it for one run, or add the package to Pi's settings and pick `jev/auto` with `/model`.

```sh
git clone https://github.com/jakucermak/pi-jev-router
pi -e ./pi-jev-router --model jev/auto
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jakucermak/pi-jev-router/blob/e82211bc3378ae437ab2f7ac8e980db21fd80901/README.md](https://github.com/jakucermak/pi-jev-router/blob/e82211bc3378ae437ab2f7ac8e980db21fd80901/README.md)

## Limits and data handling

With Jev classification on, request metadata (not full content, per the README) goes to the configured Jev provider. Recommends models only; it enforces and approves nothing.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit e82211bc3378](https://github.com/jakucermak/pi-jev-router/tree/e82211bc3378ae437ab2f7ac8e980db21fd80901). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
