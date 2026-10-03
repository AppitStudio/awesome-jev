# cleffa

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Native C+Metal Apple Silicon engine for Cloudflare Clef/Clef-Flash with Jev/System One request/response API (MIT; independent of Cloudflare).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zknpr/cleffa) |
| Maintainer | [zknpr](https://github.com/zknpr). Independently curated. |
| Format | C11 + Metal local System One inference for Cloudflare Clef (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/zknpr/cleffa/blob/db38cfcbe924a23ec9ac7e15b4fb914e5c3cab92/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Independent of Cloudflare. Hardware bar is high (tested M5 Max 128 GB; large RAM for weights). Not affiliated with or endorsed by Cloudflare. Live install/inference not run on the review host. |

## When to use

Use for local/private System One–compatible typed decisions with Clef weights on Apple Silicon. Prefer hosted TypeSafe Jev when you need the production Jev model without local GPU memory.

## How it works

Maps BF16 weights, runs one prefill pass per System One request, and returns typed decisions. Optional micro-batched localhost server exposes /v1/systemone.

## Get started

```sh
git clone https://github.com/zknpr/cleffa.git
cd cleffa
git checkout db38cfcbe924a23ec9ac7e15b4fb914e5c3cab92
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit db38cfcbe924](https://github.com/zknpr/cleffa/tree/db38cfcbe924a23ec9ac7e15b4fb914e5c3cab92). AI-assisted README and license inspection; install/live paths not executed.
