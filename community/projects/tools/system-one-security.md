# system-one-security

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rerunnable security experiments on System One models (TypeSafe Jev, Cloudflare Clef): truncation, injection, poisoning, tripwires.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ankushchadha/system-one-security) |
| Maintainer | [ankushchadha](https://github.com/ankushchadha). Independently curated. |
| Format | Security experiment harness (MIT; draft; some results withheld) |
| Requirements | See upstream README; TypeSafe/OpenRouter/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/ankushchadha/system-one-security/blob/ecdda3654cb86a029c3dfb319ec3512245e184de/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when rerunnable security experiments on System One models (TypeSafe Jev, Cloudflare Clef): truncation, injection, poisoning, tripwires. Prefer related catalog tools when another listing better matches your stack.

## How it works

Scripts send synthetic citation-check states to Jev/Clef backends and record verdict shifts under adversarial edits.

## Get started

```sh
git clone https://github.com/ankushchadha/system-one-security.git
cd system-one-security
git checkout ecdda3654cb86a029c3dfb319ec3512245e184de
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit ecdda3654cb8](https://github.com/ankushchadha/system-one-security/tree/ecdda3654cb86a029c3dfb319ec3512245e184de). AI-assisted README and license inspection; install/live paths not executed.
