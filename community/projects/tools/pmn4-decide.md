# decide (CLI for typed System One decisions with named profiles)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript CLI for yes/no, choice and score decisions where you call a named profile instead of an engine; each profile maps to an engine and pinned model (TypeSafe Jev or OpenAI Decisions), and every result records which ran.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pmn4/decide) |
| Maintainer | [pmn4](https://github.com/pmn4). Independently curated. |
| Format | Node.js CLI (install from GitHub) |
| Requirements | Node.js 20+; a TypeSafe or OpenAI API key. |
| License | [MIT](https://github.com/pmn4/decide/blob/0087c93b8a0a2dc7113060ae0b7acafeba9b4d7a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engines/typesafe.ts`](https://github.com/pmn4/decide/blob/0087c93b8a0a2dc7113060ae0b7acafeba9b4d7a/src/engines/typesafe.ts) at the pinned commit. |

## When to use

- Call decisions from shell scripts and CI with auditable profile, engine and model fields.
- Switch engines without changing calling scripts.
- Mismatch: not published to npm; install from GitHub.

## How it works

`src/engines/typesafe.ts` posts to `https://api.typesafe.ai/v1/systemone`; the built-in `jev` profile pins `jev-1.13.0`. Keys come from env, the OS keychain or a 0600 credentials file. Integration evidence: [`src/engines/typesafe.ts`](https://github.com/pmn4/decide/blob/0087c93b8a0a2dc7113060ae0b7acafeba9b4d7a/src/engines/typesafe.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g github:pmn4/decide
decide login
decide yesno -q "Does this convey urgency?" -s "Payouts failing for 3 days"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Profiles and examples in the README: [github.com/pmn4/decide#readme](https://github.com/pmn4/decide#readme)

## Limits and data handling

The state you pass is sent to the engine of the active profile.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 0087c93b8a0a](https://github.com/pmn4/decide/tree/0087c93b8a0a2dc7113060ae0b7acafeba9b4d7a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
