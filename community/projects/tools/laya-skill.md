# laya-skill

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill/plugin for System One typed decisions: local Laya (CPU/MPS/CUDA/WebGPU) or hosted TypeSafe Jev via the same wire format, plus fine-tune/calibrate helpers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/StevenLi-phoenix/laya-skill) |
| Maintainer | [StevenLi-phoenix](https://github.com/StevenLi-phoenix). Independently curated. |
| Format | Claude Code skill (`system-one`) + plugin marketplace install; Apache-2.0. No weights in-repo. |
| Requirements | Claude Code; Laya runtime and/or TypeSafe key depending on route; WebGPU demo optional. |
| License | [Apache-2.0](https://github.com/StevenLi-phoenix/laya-skill/blob/0165c83bf16de0704ab1f9bedbcf8b8786b6d145/LICENSE). Hosted Jev usage may incur charges; Laya weights download separately. |
| Disclosure | Laya path is independent open/local System One; Jev path is hosted TypeSafe. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Claude/Laya/TypeSafe paths not run on the review host. |

## When to use

Use when a Claude Code workspace should swap between local Laya and hosted Jev for typed decisions. Prefer official TypeSafe skills when you only need hosted Jev design guidance.

## How it works

Skill documents state + choice/score/noul questions; runners target Laya (local/WebGPU/HTTP) or TypeSafe by base URL. Fine-tune/ONNX/Hub helpers included; weights download at run time.

## Get started

```sh
git clone https://github.com/StevenLi-phoenix/laya-skill.git
cd laya-skill
git checkout 0165c83bf16de0704ab1f9bedbcf8b8786b6d145
# claude plugin marketplace add StevenLi-phoenix/laya-skill --scope project
# claude plugin install system-one@laya-skill --scope project
```

## Examples and demos

- WebGPU demo linked upstream: itch.io Laya typed-decisions.
- Upstream install and fine-tune docs.

## Limits and data handling

Hosted Jev sends state/questions to TypeSafe; local Laya stays on-device. Catalog checks did not install Claude plugins or download weights.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 0165c83](https://github.com/StevenLi-phoenix/laya-skill/tree/0165c83bf16de0704ab1f9bedbcf8b8786b6d145). AI-assisted README and license inspection; install/live paths not executed.
