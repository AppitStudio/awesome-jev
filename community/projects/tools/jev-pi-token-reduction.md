# jev-pi-token-reduction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension: TypeSafe Jev trims tool-output chunks before the model sees them (~15% cost on held-out reads).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/auschoi96/jev-pi-token-reduction) |
| Maintainer | [auschoi96](https://github.com/auschoi96). Independently curated. |
| Format | Pi coding-agent extension. |
| Requirements | Pi coding agent; TypeSafe API key; Python per upstream. |
| License | [MIT](https://github.com/auschoi96/jev-pi-token-reduction/blob/fc355383ca2d85386aad878e1c2988e52b031302/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use on **read-heavy Pi sessions** where agents load whole files for narrow questions. Little help when the agent already retrieves narrowly.

## How it works

After read/grep/bash, chunks large outputs and asks Jev hide/outline/condensed/full; markers preserve recoverability via `jev_expand`.

## Get started

```sh
git clone https://github.com/auschoi96/jev-pi-token-reduction.git
cd jev-pi-token-reduction
git checkout fc355383ca2d85386aad878e1c2988e52b031302
# Install as Pi extension per README; needs TYPESAFE_API_KEY
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit fc35538](https://github.com/auschoi96/jev-pi-token-reduction/tree/fc355383ca2d85386aad878e1c2988e52b031302). AI-assisted README and license inspection; install/live paths not executed.
