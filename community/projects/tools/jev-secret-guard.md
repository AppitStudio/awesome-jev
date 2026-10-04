# jev-secret-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hook: block known secret formats locally; send masked unknowns to TypeSafe Jev so checks never leak the secret.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BasmaAbouzied0/jev-secret-guard) |
| Maintainer | [BasmaAbouzied0](https://github.com/BasmaAbouzied0). Independently curated. |
| Format | Claude Code PreToolUse-style hook (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/BasmaAbouzied0/jev-secret-guard/blob/81e8bd0f8d54773fa3045bdc3bcbbbbef1321166/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when claude Code hook: block known secret formats locally; send masked unknowns to TypeSafe Jev so checks never leak the secret. Prefer related catalog tools when another listing better matches your stack.

## How it works

Known key patterns blocked locally; unknown candidates are masked before Jev judges whether they look like secrets.

## Get started

```sh
git clone https://github.com/BasmaAbouzied0/jev-secret-guard.git
cd jev-secret-guard
git checkout 81e8bd0f8d54773fa3045bdc3bcbbbbef1321166
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 81e8bd0f8d54](https://github.com/BasmaAbouzied0/jev-secret-guard/tree/81e8bd0f8d54773fa3045bdc3bcbbbbef1321166). AI-assisted README and license inspection; install/live paths not executed.
