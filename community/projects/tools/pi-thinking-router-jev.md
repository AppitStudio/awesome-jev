# pi-thinking-router-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that only adjusts thinking level (`low` / `medium` / `high` / `xhigh`): consults TypeSafe Jev on task start, reasoning failures, and stable windows, with a local rule engine fallback when unconfigured.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Wh0rigin/pi-thinking-router-jev) |
| Maintainer | [Wh0rigin](https://github.com/Wh0rigin). Independently curated. |
| Format | TypeScript Pi extension (`src/jev-client.ts`, policy + JSONL logs). |
| Requirements | Pi coding agent; optional Jev endpoint/key (`JEV_API_KEY` / config / cc-switch store). |
| License | **Unspecified** at tip (no LICENSE file). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Pi/Jev not run. |

## When to use

Use it to **spend less on easy edits and more on hard debug** without swapping models. Prefer [pi-jev-router](xdeviation-pi-jev-router.md) / other routers for model tier choice rather than thinking level only.

## How it works

Event hooks update agent state; [`src/jev-client.ts`](https://github.com/Wh0rigin/pi-thinking-router-jev/blob/154d80c9913adca029bd80a3894498a2a5a2e553/src/jev-client.ts) asks a Choice question for the next level; policy debounces ±1 steps and writes JSONL. Failures throw into the local rule fallback.

## Get started

```sh
git clone https://github.com/Wh0rigin/pi-thinking-router-jev.git
cd pi-thinking-router-jev
git checkout 154d80c9913adca029bd80a3894498a2a5a2e553
# Install per README as a Pi extension; configure ~/.pi/jev-router.json or env
```

## Examples and demos

- README mermaid architecture and trigger table.
- `test/` offline suite + optional live Jev test (not run here).

## Limits and data handling

Task snapshots leave the host when Jev is configured. Does not modify the agent loop beyond `setThinkingLevel`. Unconfigured installs rely on local rules only.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 154d80c](https://github.com/Wh0rigin/pi-thinking-router-jev/tree/154d80c9913adca029bd80a3894498a2a5a2e553). AI-assisted README + `jev-client.ts` inspection. No live Pi/TypeSafe run.

Related: [pi-jev-sentinel](pi-jev-sentinel.md), [XDeviation pi-jev-router](xdeviation-pi-jev-router.md), [jev-effort](jev-effort.md).
