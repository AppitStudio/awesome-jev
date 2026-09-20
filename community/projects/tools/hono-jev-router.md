# hono-jev-router

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Experimental Hono router that matches HTTP requests to plain-English route descriptions with TypeSafe Jev Noul judgments (first match above threshold wins).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yusukebe/hono-jev-router) |
| Maintainer | [Yusuke Wada / yusukebe](https://github.com/yusukebe) (Hono). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **hono-jev-router 0.2.0** (TypeScript `JevRouter` for Hono) with a Cloudflare playground. |
| Requirements | A Hono app; live routing needs `TYPESAFE_API_KEY` (or a custom `run`/`choose` adapter such as Workers AI). |
| License | [MIT](https://github.com/yusukebe/hono-jev-router/blob/04f6e103e1397bca659ab85c042011a1f14b679d/LICENSE). |

## When to use

Use it to branch HTTP handling by request meaning (agent vs browser vs suspicious traffic heuristics) while keeping path routes and middleware on Hono's TrieRouter. Prefer [semgate](semgate.md) for Go `net/http` middlewares with the same idea. Do **not** treat semantic routes as authentication or authorization—the request is model input and can be steered.

## How it works

[`src/index.ts`](https://github.com/yusukebe/hono-jev-router/blob/04f6e103e1397bca659ab85c042011a1f14b679d/src/index.ts) registers `app.on('jev', '<description>', handler)`. For unmatched path routes, it posts method/URL/headers/(bounded) body to `https://api.typesafe.ai/v1/systemone` (model `jev-latest` by default) as one Noul question per description in a single call. Sensitive headers are redacted; the first description at or above `threshold` (default 0.5) wins. Results are available as `c.get('jev')`.

## Get started

```sh
npm i hono-jev-router
# or inspect the reviewed tree:
git clone https://github.com/yusukebe/hono-jev-router.git
cd hono-jev-router
git checkout 04f6e103e1397bca659ab85c042011a1f14b679d
# see README for Hono + JevRouter wiring; playground/ for a demo app
```

Every semantically routed request is a billable model call. This listing did not call TypeSafe or deploy the playground.

## Examples and demos

- README examples for agent/browser/suspicious descriptions and `c.get('jev')`.
- [`playground/`](https://github.com/yusukebe/hono-jev-router/tree/04f6e103e1397bca659ab85c042011a1f14b679d/playground) Cloudflare/Vite demo.
- Offline tests under [`test/`](https://github.com/yusukebe/hono-jev-router/tree/04f6e103e1397bca659ab85c042011a1f14b679d/test).

## Limits and data handling

Request metadata and body snippets leave the edge/origin for TypeSafe (or your `run` adapter). Upstream warns against authz use and recommends a rate limit. Probabilities are not guarantees.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 04f6e10](https://github.com/yusukebe/hono-jev-router/tree/04f6e103e1397bca659ab85c042011a1f14b679d): **0.2.0**, MIT. AI-assisted source review of README, `src/index.ts`, `package.json`, and license. Offline tests / live TypeSafe calls were not run on the review host.

Related: [semgate](semgate.md).
