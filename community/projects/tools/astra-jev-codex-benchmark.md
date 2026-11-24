# Astra + Jev benchmark (DeepSWE) by hvvze (paired test of plain Codex CLI against the jev-codex-harness `jev/auto` router)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Ran plain Codex CLI and the listed teo-nex/jev-codex-harness `jev/auto` routing on the same DeepSWE tasks in isolated containers. On 4 complete pairs, plain Codex passed 4/4 and `jev/auto` 2/4, sent 22.1× more uncached input tokens and routed 0 of 215 calls to the cheaper model. A negative result, published with full evidence; English and Russian READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hqvdvn-cmd/astra-jev-benchmark) |
| Maintainer | [hvvze](https://github.com/hqvdvn-cmd). Independently curated. |
| Format | Python benchmark harness with run evidence |
| Requirements | Python, Docker, Codex CLI with a ChatGPT subscription, and the jev-codex-harness for the Jev arm. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`evidence/2026-11-24-deepswe-pilot-10-v1/summary.md`](https://github.com/hqvdvn-cmd/astra-jev-benchmark/blob/738dca0911a6026476dddea4706d73efa175f741/evidence/2026-11-24-deepswe-pilot-10-v1/summary.md) at the pinned commit. |

## When to use

- Check how a Jev model router behaves on hard multi-file coding tasks before adopting one.
- Mismatch: a general verdict on Jev routing; it is 4 tasks with one policy commit.

## How it works

`evidence/2026-11-24-deepswe-pilot-10-v1/summary.md` records per-task pass, token and routing counts for both arms; the Jev routing itself happens inside jev-codex-harness. Integration evidence: [`evidence/2026-11-24-deepswe-pilot-10-v1/summary.md`](https://github.com/hqvdvn-cmd/astra-jev-benchmark/blob/738dca0911a6026476dddea4706d73efa175f741/evidence/2026-11-24-deepswe-pilot-10-v1/summary.md).

## Get started

Read the summary and manifest; re-running needs the same harness commit and corpus.

```sh
git clone https://github.com/hqvdvn-cmd/astra-jev-benchmark.git && cd astra-jev-benchmark
cat evidence/2026-11-24-deepswe-pilot-10-v1/summary.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evidence: [github.com/hqvdvn-cmd/astra-jev-benchmark/tree/738dca0911a6026476dddea4706d73efa175f741/evidence/2026-11-24-deepswe-pilot-10-v1](https://github.com/hqvdvn-cmd/astra-jev-benchmark/tree/738dca0911a6026476dddea4706d73efa175f741/evidence/2026-11-24-deepswe-pilot-10-v1)
- Harness under test: [github.com/teo-nex/jev-codex-harness](https://github.com/teo-nex/jev-codex-harness)

## Limits and data handling

Pilot ended early at task 5 on a subscription rate limit; only 4 valid pairs. Results apply to one harness commit (`cea6502`) and policy. No license file, so no reuse terms are granted.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 738dca0911a6](https://github.com/hqvdvn-cmd/astra-jev-benchmark/tree/738dca0911a6026476dddea4706d73efa175f741). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
