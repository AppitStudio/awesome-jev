# patrol-jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

Photo-to-patrol-log web app: OpenAI reads the photo; TypeSafe Jev classifies the write-up into one of four branches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/patrol-jev/patrol-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/patrol-jev/patrol-jev#readme) |
| Pricing and access | Free source build; live backends BYOK. Checked 2026-10-03. |
| Jev evidence | README: OpenAI for vision, Jev for four-way classification. ([upstream evidence](https://github.com/patrol-jev/patrol-jev/blob/5d822c439f78c7a83b118b01a356e65ae45f7888/README.md)). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/UI paths not run on the Linux review host. |
| Maintainer | [patrol-jev](https://github.com/patrol-jev). Independently curated. |
| Format | TypeScript · Next.js patrol log app (MIT) |
| Platform and availability | See upstream README |
| Jev's role | TypeSafe Jev (or disclosed substitute) supplies typed judgments; application code owns orchestration and side effects. |
| Requirements | See upstream README; provider keys when using live paths. |
| License | [MIT](https://github.com/patrol-jev/patrol-jev/blob/5d822c439f78c7a83b118b01a356e65ae45f7888/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Photo-to-patrol-log web app: OpenAI reads the photo; TypeSafe Jev classifies the write-up into one of four branches.

## Get started

```sh
git clone https://github.com/patrol-jev/patrol-jev.git
cd patrol-jev
git checkout 5d822c439f78c7a83b118b01a356e65ae45f7888
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 5d822c439f78](https://github.com/patrol-jev/patrol-jev/tree/5d822c439f78c7a83b118b01a356e65ae45f7888). AI-assisted README and license inspection; live paths not executed.
