# fast-jev-opencode (roshan-shaik-ml)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Verbatim OpenCode context prune powered by TypeSafe Jev—history and UI stay untouched.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/roshan-shaik-ml/fast-jev-opencode) |
| Maintainer | [roshan-shaik-ml](https://github.com/roshan-shaik-ml). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Single package exporting v2 `setup()` and v1 `server()` adapters. |
| Requirements | OpenCode v1 (≥1.18.29) or v2; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/roshan-shaik-ml/fast-jev-opencode/blob/7359df24e8868f06b4fb01f51cd4377718925d08/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when OpenCode sessions drown in bulky tool results and you want verbatim prune instead of summarization.

## How it works

Maps messages → Jev noul keep-call/keep-result questions → drop/truncate on the outbound request; fail-open; caches by tool call id. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/roshan-shaik-ml/fast-jev-opencode.git
cd fast-jev-opencode
git checkout 7359df24e8868f06b4fb01f51cd4377718925d08
# install as OpenCode plugin per upstream README; set TYPESAFE_API_KEY
```

Pin revision `7359df24e8868f06b4fb01f51cd4377718925d08` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent of tamaratran/fast-jev-compaction and nrdz-labs/fast-jev-opencode. Live OpenCode/TypeSafe path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 7359df2](https://github.com/roshan-shaik-ml/fast-jev-opencode/tree/7359df24e8868f06b4fb01f51cd4377718925d08). AI-assisted README and LICENSE inspection; install/live paths not executed.
