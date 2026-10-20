# @rbxts/jev (Jev for roblox-ts)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Typed TypeSafe Jev client for roblox-ts games: declare choice, score and noul questions about one state, and the option names become TypeScript types your server code branches on, with a shared rate limiter, retries and request deduplication over Roblox `HttpService`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lypt1x/rbxts-jev) |
| Maintainer | [Lypt1x](https://github.com/Lypt1x). Independently curated. |
| Format | roblox-ts package (install from GitHub) |
| Requirements | A roblox-ts 3 project, Allow HTTP Requests on, and a Roblox secret `TYPESAFE_API_KEY` scoped to `api.typesafe.ai`. |
| License | [MIT](https://github.com/Lypt1x/rbxts-jev/blob/0eb8a53ba481c496de945dff058b56792db455e3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/server/create-jev.ts`](https://github.com/Lypt1x/rbxts-jev/blob/0eb8a53ba481c496de945dff058b56792db455e3/src/server/create-jev.ts) at the pinned commit. |

## When to use

- Let NPCs read player chat intent, mood or a yes/no condition without writing an LLM prompt parser.
- Ask several questions about one state in one request on a Roblox server.
- Mismatch: server-side only; not on npm yet, so pin a tag or commit.

## How it works

`createJev` reads the key from a Roblox secret and `src/server/create-jev.ts` posts to `https://api.typesafe.ai` through `HttpService`. `questions()` builds the request, answers come back typed (choice as a string union, score as a number, noul as a probability), and `decide`, `delegate` and `routeChoice` hand results to your handlers. Integration evidence: [`src/server/create-jev.ts`](https://github.com/Lypt1x/rbxts-jev/blob/0eb8a53ba481c496de945dff058b56792db455e3/src/server/create-jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install github:Lypt1x/rbxts-jev
# Studio: File > Experience Settings > Security > Local Secrets: TYPESAFE_API_KEY
# then put the README example in src/server/decision.server.ts and press Play
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README NPC intent example
- docs/ (Docusaurus guides, build locally)

## Limits and data handling

Game state you send goes to TypeSafe from the Roblox server. Docs site not published yet.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 0eb8a53ba481](https://github.com/Lypt1x/rbxts-jev/tree/0eb8a53ba481c496de945dff058b56792db455e3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
