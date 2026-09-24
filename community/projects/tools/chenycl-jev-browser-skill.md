# jev-browser-skill (ChenYCL)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser and computer-use CLI/MCP for coding agents: TypeSafe Jev supplies calibrated action judgments while code owns the control loop (ego lite / Chrome / Safari). Distinct from [zurfyx/jev-browser-skill](jev-browser-skill.md) and [hqman/jev-browser-skill](hqman-jev-browser-skill.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ChenYCL/jev-browser-skill) |
| Maintainer | [ChenYCL](https://github.com/ChenYCL). Independently curated. |
| Format | Node.js ≥ 22 zero-dependency CLI + MCP (`skills/jev-browser`). |
| Requirements | Node.js 22+; TypeSafe (or compatible) API key per README; browser backend as documented. |
| License | [MIT](https://github.com/ChenYCL/jev-browser-skill/blob/905df3c47dccb3db6cd7c5e21838ead2a99b0d5a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live browser/TypeSafe runs not executed. |

## When to use

Use it for **agent-driven browser goals** with recorded step screenshots and a code-owned loop. Prefer zurfyx for the minimal CDP teaching skill; prefer hqman for the `jb` Playwright daemon.

## How it works

`jev-browser run` observes the page, asks Jev for the next calibrated judgment, and executes via the selected backend. Secrets can be typed without exposing raw values in observations (see README form demo).

## Get started

```sh
git clone https://github.com/ChenYCL/jev-browser-skill.git
cd jev-browser-skill
git checkout 905df3c47dccb3db6cd7c5e21838ead2a99b0d5a
# Follow README for skill install + TYPESAFE_API_KEY / provider config
# Example shape: jev-browser run --goal "…"  (see upstream flags)
```

## Examples and demos

- README Wikipedia / form / button-disambiguation demos with GIFs.
- `skills/jev-browser/SKILL.md`; `tests/` (not re-run here).

## Limits and data handling

Page structure and goals leave your machine for the configured Jev provider. Cost/latency figures in the README are upstream-reported, not re-measured here.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 905df3c](https://github.com/ChenYCL/jev-browser-skill/tree/905df3c47dccb3db6cd7c5e21838ead2a99b0d5a). AI-assisted README + skill layout inspection. No live TypeSafe spend.

Related: [Jev Browser Skill](jev-browser-skill.md), [jev-browser-skill (hqman)](hqman-jev-browser-skill.md), [ajevt-browser](ajevt-browser.md).
