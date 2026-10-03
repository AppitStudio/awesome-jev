# jevmem (illescasDaniel)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent long-term memory via TypeSafe Jev typed decisions (MCP, Claude Code hooks, CLI, SQLite)—no generative LLM in the memory loop (MIT; distinct from libingzheren/Jev-Mem).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/illescasDaniel/jev-mem) |
| Maintainer | [illescasDaniel](https://github.com/illescasDaniel). Independently curated. |
| Format | Python MCP/hooks/CLI agent memory driven by Jev (MIT, beta) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/illescasDaniel/jev-mem/blob/cdd4e81db6e354b62d89d0edd11a94d820ba4170/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from already-listed [libingzheren/Jev-Mem](https://github.com/libingzheren/Jev-Mem) (multi-view graph package)—this is the MCP/hooks/CLI product referencing the same research line. Beta. Live install/inference not run on the review host. |

## When to use

Use when you want Claude Code/MCP memory with Jev gating and cheap recall. Prefer libingzheren/Jev-Mem for the graph-controller research package.

## How it works

Writes are screened and typed with Jev; recall judges relevance and sufficiency; System Two (your agent) writes note text. Fails open if Jev is down.

## Get started

```sh
git clone https://github.com/illescasDaniel/jev-mem.git
cd jev-mem
git checkout cdd4e81db6e354b62d89d0edd11a94d820ba4170
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit cdd4e81db6e3](https://github.com/illescasDaniel/jev-mem/tree/cdd4e81db6e354b62d89d0edd11a94d820ba4170). AI-assisted README and license inspection; install/live paths not executed.
