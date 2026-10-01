# s1-tui

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Terminal UI for System One typed decisions (noul/choice/score) over laya (local MLX) and TypeSafe Jev backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tnaftali/s1-tui) |
| Maintainer | [tnaftali](https://github.com/tnaftali). Independently curated. |
| Format | Rust/TUI (MIT) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/tnaftali/s1-tui/blob/53cfe6e434f74d85cd69b2ae6f2ee1363b5650c4/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/tnaftali/s1-tui.git
cd s1-tui
git checkout 53cfe6e434f74d85cd69b2ae6f2ee1363b5650c4
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 53cfe6e434f7](https://github.com/tnaftali/s1-tui/tree/53cfe6e434f74d85cd69b2ae6f2ee1363b5650c4). AI-assisted README and license inspection; install/live paths not executed.
