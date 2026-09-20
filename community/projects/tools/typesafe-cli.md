# typesafe-cli

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Shell CLI (`jev`) for TypeSafe Jev: pipe state in, get noul/choice/score answers as numbers—not prose. Distinct from the Python [`typesafeai-cli`](typesafeai-cli.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/y0usaf/typesafe-cli) |
| Maintainer | [y0usaf](https://github.com/y0usaf). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript CLI published as npm `@y0usaf/typesafe-cli` **0.1.0** (`jev` bin); also runnable via Nix flake / `node src/cli.ts`. |
| Requirements | Node.js ≥ 22.18. Live calls need a TypeSafe API key (`--key`, `TYPESAFE_API_KEY`, key file, or shared `~/.pi/agent/pi-jev.json`). |
| License | [MIT](https://github.com/y0usaf/typesafe-cli/blob/d6911318ae10a5ba38a6578193bd240b56cff6ec/LICENSE). |

## When to use

Use it when a human or coding agent should ask typed Jev questions from the shell without embedding an HTTP client. Prefer [`typesafeai-cli`](typesafeai-cli.md) for Python recipe flows (ask/decide/screen/verify), or [Advocaat](advocaat.md) / language SDKs for in-process APIs.

## How it works

[`src/client.ts`](https://github.com/y0usaf/typesafe-cli/blob/d6911318ae10a5ba38a6578193bd240b56cff6ec/src/client.ts) posts to `https://api.typesafe.ai/v1/systemone` (default model `jev-latest`). Commands `noul`, `choice`, `score`, and `ask` map to typed questions; `ask` batches many questions in one request. Output is pipe-friendly text or `--json`. Key resolution prefers CLI flags, then env, then the same config file used by [pi-jev](pi-jev.md).

## Get started

```sh
npm install -g @y0usaf/typesafe-cli
jev --help
# Live (billable): echo "app crashed" | jev noul "Is this a bug report?"
```

From the reviewed commit:

```sh
git clone https://github.com/y0usaf/typesafe-cli.git
cd typesafe-cli
git checkout d6911318ae10a5ba38a6578193bd240b56cff6ec
npm install
npx tsc --noEmit
```

Live commands send state/questions to TypeSafe. This listing did not call the API.

## Examples and demos

- README examples for `noul`, `choice --probs`, and multi-question `ask` JSON.
- Nix: `nix run . -- noul "…" --state "…"`.
- Shares key discovery with [pi-jev](pi-jev.md) for agents already configured there.

## Limits and data handling

State and questions go to TypeSafe on live runs. Keep keys out of shared state files. Package is early (**0.1.0**); CLI surface may change. No automated test suite was found in the reviewed tree.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d691131](https://github.com/y0usaf/typesafe-cli/tree/d6911318ae10a5ba38a6578193bd240b56cff6ec): **0.1.0**, MIT. AI-assisted source review of `client.ts`, CLI entrypoints, README, and license. **`tsc --noEmit`** was the documented check; no live TypeSafe calls were performed.

Related: [typesafeai-cli](typesafeai-cli.md), [pi-jev](pi-jev.md), [Advocaat](advocaat.md).
