# paseo-jevgrep-addon by fbettag (Paseo plugin that gives every agent a jevgrep tool to find code by asking what it does)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Plugin for the Paseo agent daemon that attaches a `jevgrep` tool to every agent: ask where a behaviour lives ("where is the HTTP request to the Jev API sent") and get ranked paths with verbatim excerpts. It walks the working directory breadth first, asks Jev to score directories and files against the question and descends into the promising ones, skipping version-control, dependency, build and binary files, with bounded visits, depth and requests. Use Grep or `rg` for exact symbols.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fbettag/paseo-jevgrep-addon) |
| Maintainer | [fbettag](https://github.com/fbettag). Independently curated. |
| Format | Paseo daemon plugin (TypeScript, MIT) |
| Requirements | Paseo 0.16+ with plugins and agent tools enabled, and `TYPESAFE_API_KEY` or `TYPESAFE_API_KEY_FILE` in the daemon's environment (or a loopback OpenJev endpoint). |
| License | [MIT](https://github.com/fbettag/paseo-jevgrep-addon/blob/8e664ff9fb6bfb1bfcb447669c9bf8f90f2d2dab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/client.ts`](https://github.com/fbettag/paseo-jevgrep-addon/blob/8e664ff9fb6bfb1bfcb447669c9bf8f90f2d2dab/server/client.ts) at the pinned commit. |

## When to use

- Help agents find the file behind a behaviour when they don't know the symbol name.
- Mismatch: exact symbol or regex lookups; use rg.

## How it works

`server/client.ts` posts score questions to `https://api.typesafe.ai/v1/systemone` by default, reading the key from `TYPESAFE_API_KEY` or a key file inside the plugin process so it never reaches the agent; `PASEO_JEV_BASE_URL` points it elsewhere. Integration evidence: [`server/client.ts`](https://github.com/fbettag/paseo-jevgrep-addon/blob/8e664ff9fb6bfb1bfcb447669c9bf8f90f2d2dab/server/client.ts).

## Get started

Add the plugin to your Paseo daemon and restart it with the key set.

```sh
export TYPESAFE_API_KEY=...
paseo plugin add git:fbettag/paseo-jevgrep-addon --ref v1.0.0
# restart the Paseo daemon
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/fbettag/paseo-jevgrep-addon/blob/8e664ff9fb6bfb1bfcb447669c9bf8f90f2d2dab/README.md](https://github.com/fbettag/paseo-jevgrep-addon/blob/8e664ff9fb6bfb1bfcb447669c9bf8f90f2d2dab/README.md)

## Limits and data handling

File names and excerpts of the searched folder go to TypeSafe (or your endpoint). Without a key or endpoint the plugin attaches no tool.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 8e664ff9fb6b](https://github.com/fbettag/paseo-jevgrep-addon/tree/8e664ff9fb6bfb1bfcb447669c9bf8f90f2d2dab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
