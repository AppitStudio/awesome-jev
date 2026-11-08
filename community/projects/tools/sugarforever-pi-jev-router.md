# pi-jev-router by sugarforever (pi extension that asks TypeSafe Jev to continue, fork or start a new session)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Extension for the pi coding agent (in the yummy-pi-extensions collection) that asks TypeSafe Jev, before a prompt enters the session, whether to continue, fork or start fresh. Distinct from philippdubach's pi-jev-router.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sugarforever/yummy-pi-extensions) |
| Maintainer | [sugarforever](https://github.com/sugarforever). Independently curated. |
| Format | pi extension (TypeScript, MIT) |
| Requirements | pi and a TypeSafe or OpenRouter key. |
| License | [MIT](https://github.com/sugarforever/yummy-pi-extensions/blob/187f7553fcbbb8d66f378d08430297312ceeeb6a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pi-jev-router/src/jev.ts`](https://github.com/sugarforever/yummy-pi-extensions/blob/187f7553fcbbb8d66f378d08430297312ceeeb6a/pi-jev-router/src/jev.ts) at the pinned commit. |

## When to use

- Keep pi sessions focused by forking off unrelated prompts.
- Automate session hygiene with a cheap decision.
- Mismatch: pi only.

## How it works

`pi-jev-router/src/jev.ts` targets `https://api.typesafe.ai/v1/systemone` with `jev-latest`, or OpenRouter with `typesafe/jev-1.13`. Integration evidence: [`pi-jev-router/src/jev.ts`](https://github.com/sugarforever/yummy-pi-extensions/blob/187f7553fcbbb8d66f378d08430297312ceeeb6a/pi-jev-router/src/jev.ts).

## Get started

Install `@sugarforever/pi-jev-router` into pi and set TYPESAFE_API_KEY or OPENROUTER_API_KEY.

```sh
git clone https://github.com/sugarforever/yummy-pi-extensions.git && cd yummy-pi-extensions
export TYPESAFE_API_KEY=...
cd pi-jev-router && npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sugarforever/yummy-pi-extensions/blob/187f7553fcbbb8d66f378d08430297312ceeeb6a/README.md](https://github.com/sugarforever/yummy-pi-extensions/blob/187f7553fcbbb8d66f378d08430297312ceeeb6a/README.md)

## Limits and data handling

Your prompt and a session summary are sent to TypeSafe/OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 187f7553fcbb](https://github.com/sugarforever/yummy-pi-extensions/tree/187f7553fcbbb8d66f378d08430297312ceeeb6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
