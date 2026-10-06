# trirouter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One prompt router for Claude Code, Codex and Antigravity (formerly jev-router): JEV — via a TypeSafe token or an OpenRouter key — classifies each prompt's task and difficulty to pick the model tier and adds a destructive-command verdict on top of a regex safety net; a built-in local classifier with the same answer format is the fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hajdu-patrik/trirouter) |
| Maintainer | [hajdu-patrik](https://github.com/hajdu-patrik). Independently curated. |
| Format | CLI (`trirouter`) installed by `python install.py`, with hooks and MCP entries |
| Requirements | Python 3.10+ and at least one of Claude Code, Codex CLI or Antigravity CLI; a TypeSafe token or OpenRouter key for JEV (optional). |
| License | [MIT](https://github.com/hajdu-patrik/trirouter/blob/272aa9890488a0406fc999c6134899568f25bff8/LICENSE.md). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Stop hand-picking models: let a typed classifier map task × difficulty to a tier from `routes.json`.
- Add a second, calibrated opinion on destructive commands beside a regex net.
- Mismatch: without a key the local classifier decides — useful, but not Jev.

## How it works

Each prompt goes through language detection, `is_destructive()` (regex + JEV verdict), a skill-catalog prefilter (≤ 8 candidates), then `classify()` with JEV (TypeSafe or OpenRouter) or the built-in classifier, and `decide()` maps task × difficulty to a tier in `routes.json`. Pasted blocks are context only and never decide language or task type. Model and effort are enforced, not suggested.

## Get started

Clone and run the installer; paste a TypeSafe token or OpenRouter key at the JEV step (live calls per prompt):

```sh
git clone https://github.com/hajdu-patrik/trirouter.git trirouter
cd trirouter
python install.py          # detects agents, asks for JEV access, installs hooks + MCP
trirouter help
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *How It Works* pipeline and routing table.
- `docs/cli.md` full command reference.

## Limits and data handling

Prompts (and pasted context) are sent to TypeSafe or OpenRouter when a key is set. The installer edits agent hooks/MCP config and PATH (migration from jev-router is automatic). GitHub reports the license as NOASSERTION; `LICENSE.md` is the MIT text. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 272aa9890488](https://github.com/hajdu-patrik/trirouter/tree/272aa9890488a0406fc999c6134899568f25bff8). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
