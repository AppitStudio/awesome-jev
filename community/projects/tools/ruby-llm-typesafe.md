# ruby_llm-typesafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

RubyLLM 2 provider for TypeSafe System One / Jev structured judgments (Choice/Noul/Score).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kieranklaassen/ruby_llm-typesafe) |
| Maintainer | [kieranklaassen](https://github.com/kieranklaassen). Independently curated. |
| Format | Ruby · gem (`ruby_llm-typesafe`, MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/kieranklaassen/ruby_llm-typesafe/blob/3ca481b4bc5e0b4a2396a346db1f2ff2c65b5573/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream notes RubyLLM may absorb judgments natively; do not load both providers named `:typesafe`. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/kieranklaassen/ruby_llm-typesafe.git
cd ruby_llm-typesafe
git checkout 3ca481b4bc5e0b4a2396a346db1f2ff2c65b5573
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 3ca481b4bc5e](https://github.com/kieranklaassen/ruby_llm-typesafe/tree/3ca481b4bc5e0b4a2396a346db1f2ff2c65b5573). AI-assisted README and license inspection; install/live paths not executed.
