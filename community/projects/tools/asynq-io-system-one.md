# system-one (asynq-io)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Vendor-neutral Python SDK for typed System One decisions (yes/no, choice, score) over hosted TypeSafe/OpenRouter or local ONNX.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asynq-io/system-one) |
| Maintainer | [asynq-io](https://github.com/asynq-io). Independently curated. |
| Format | Python · PyPI SDK (`system-one`, Apache-2.0) |
| Requirements | Python; `SYSTEM_ONE_API_KEY` / provider settings for hosted backends; ONNX assets for local. |
| License | [`Apache-2.0`](https://github.com/asynq-io/system-one/blob/c32b654e6a4c66dddadfdbc855427fc0263b39da/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/asynq-io/system-one.git
cd system-one
git checkout c32b654e6a4c66dddadfdbc855427fc0263b39da
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit c32b654e6a4c](https://github.com/asynq-io/system-one/tree/c32b654e6a4c66dddadfdbc855427fc0263b39da). AI-assisted README and license inspection; install/live paths not executed.
