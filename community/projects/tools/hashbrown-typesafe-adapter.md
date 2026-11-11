# Hashbrown TypeSafe adapter (Jev decisions for React and Angular agents)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Headless TypeScript framework for AI chat and agents in React or Angular apps whose `@hashbrownai/typesafe` package answers Hashbrown decision requests (including UI-selection decisions) with Jev on your server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/liveloveapp/hashbrown) |
| Maintainer | [liveloveapp](https://github.com/liveloveapp). Independently curated. |
| Format | npm package in a TypeScript framework monorepo (MIT) |
| Requirements | Node.js on the server, `@hashbrownai/core`, and `TYPESAFE_API_KEY` kept server-side. |
| License | [MIT](https://github.com/liveloveapp/hashbrown/blob/3da245d12d65a378095755b65448b5d9e985db47/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/typesafe/src/decide.fn.ts`](https://github.com/liveloveapp/hashbrown/blob/3da245d12d65a378095755b65448b5d9e985db47/packages/typesafe/src/decide.fn.ts) at the pinned commit. |

## When to use

- Add typed decisions (routing, UI selection) to a React or Angular agent.
- Keep the TypeSafe key on the server while the UI runs in the browser.
- Mismatch: Jev is one adapter; Hashbrown chat runs on other providers.

## How it works

`packages/typesafe/src/decide.fn.ts` converts Hashbrown decision requests to TypeSafe's native format (`src/native/`) and back; the package README shows a Next.js route that calls `HashbrownTypeSafe.decide` with `jev-1.14.0`. Integration evidence: [`packages/typesafe/src/decide.fn.ts`](https://github.com/liveloveapp/hashbrown/blob/3da245d12d65a378095755b65448b5d9e985db47/packages/typesafe/src/decide.fn.ts).

## Get started

Install the adapter on the server and expose a decide route for Hashbrown's `useDecision` hooks.

```sh
npm install @hashbrownai/typesafe @hashbrownai/core
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Adapter README: [github.com/liveloveapp/hashbrown/blob/3da245d12d65a378095755b65448b5d9e985db47/packages/typesafe/README.md](https://github.com/liveloveapp/hashbrown/blob/3da245d12d65a378095755b65448b5d9e985db47/packages/typesafe/README.md)
- Docs: [hashbrown.dev/](https://hashbrown.dev/)

## Limits and data handling

Decision state built by your app goes to TypeSafe from your server on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 3da245d12d65](https://github.com/liveloveapp/hashbrown/tree/3da245d12d65a378095755b65448b5d9e985db47). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
