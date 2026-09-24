# kevala

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Browser runtime that runs Laya, Kev, Bruv, SemIf, and related decision models via a zero-dependency Rust engine compiled to WebAssembly plus WebGPU kernels—typed questions without a model server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bvolpato/kevala) |
| Maintainer | [bvolpato](https://github.com/bvolpato). Independently curated. |
| Format | npm/CDN ES modules + WASM (`kevala`). |
| Requirements | Modern browser with WebGPU preferred; first load downloads pinned int8 packs from Hugging Face. |
| License | [Apache-2.0](https://github.com/bvolpato/kevala/blob/6e1754e1a3e73999e2f265fae939d2d06994fa6c/LICENSE). |
| Disclosure | Independent of official TypeSafe Jev weights. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live playground not re-run as measured eval. |

## When to use

Use for **in-browser** typed decisions with open packs and no API key. Prefer hosted TypeSafe Jev for managed cloud System One.

## How it works

`Kevala.load` fetches a model pack; `decide` scores noul/choice/score questions in one forward path inside the tab (per README/architecture).

## Get started

```html
<script type="module">
  import { Kevala } from "https://cdn.jsdelivr.net/npm/kevala@latest/js/src/index.js";
  const kevala = await Kevala.load({ model: "laya", onProgress: console.log });
  // ...
</script>
```

Or `pnpm add kevala`. Pin tip `6e1754e1a3e73999e2f265fae939d2d06994fa6c`. Live site: [bvolpato.github.io/kevala](https://bvolpato.github.io/kevala/).

## Examples and demos

- Playground and Tetris demos on the live site.
- `examples/` in-repo.

## Limits and data handling

First load pulls model packs from Hugging Face into the browser. Independent research—not official Jev.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 6e1754e](https://github.com/bvolpato/kevala/tree/6e1754e1a3e73999e2f265fae939d2d06994fa6c). AI-assisted README inspection; live GPU path not measured on the review host.

Related: [sys1 (alvarobartt)](alvarobartt-sys1.md), [SemIf](semif.md), [open-jev](open-jev.md).
