# jev-model-picker (OpenCode plugin where Jev picks the model for each delegated task)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode V2 plugin that asks a System One backend (TypeSafe Jev or OpenCode Zen free gateway) which model should handle each delegated task, falling back to the original model on errors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/iksinskiyt/jev-model-picker) |
| Maintainer | [iksinskiyt](https://github.com/iksinskiyt). Independently curated. |
| Format | OpenCode V2 plugin (TypeScript, MIT) |
| Requirements | OpenCode host and either a TypeSafe key or the documented free Zen gateway path. |
| License | [MIT](https://github.com/iksinskiyt/jev-model-picker/blob/f802ab1bf557dee330958abe594014915ac12a68/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone.ts`](https://github.com/iksinskiyt/jev-model-picker/blob/f802ab1bf557dee330958abe594014915ac12a68/src/systemone.ts) at the pinned commit. |

## When to use

- Route OpenCode delegations to the right model automatically.
- Use free Zen `jev-1.13-free` or paid TypeSafe interchangeably.
- Mismatch: OpenCode-specific; never blocks the host on picker failure.

## How it works

`src/systemone.ts` POSTs `{model,state,questions}` to `{baseURL}/systemone` (TypeSafe `/v1` or Zen) and returns calibrated answers the picker runtime applies to delegations. Integration evidence: [`src/systemone.ts`](https://github.com/iksinskiyt/jev-model-picker/blob/f802ab1bf557dee330958abe594014915ac12a68/src/systemone.ts).

## Get started

Install the plugin into OpenCode per README examples (`examples/jev-picker.jsonc`), configure a backend, and run a delegated task.

```sh
git clone https://github.com/iksinskiyt/jev-model-picker.git && cd jev-model-picker
# follow README OpenCode plugin install
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/iksinskiyt/jev-model-picker/blob/f802ab1bf557dee330958abe594014915ac12a68/README.md](https://github.com/iksinskiyt/jev-model-picker/blob/f802ab1bf557dee330958abe594014915ac12a68/README.md)

## Limits and data handling

Delegation summaries and available model lists are sent to the configured System One backend. Failures fall back silently to the original model.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit f802ab1bf557](https://github.com/iksinskiyt/jev-model-picker/tree/f802ab1bf557dee330958abe594014915ac12a68). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
