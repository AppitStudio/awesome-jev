# Jev-Orchestrated Decision Mesh (CIDM)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Training-free orchestration design where Jev chooses the next unit and reviews each output across a five-unit network, with a Codex CLI broker and skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kentilaok/Jev-Orchestrated-Decision-Mesh) |
| Maintainer | [kentilaok](https://github.com/kentilaok). Independently curated. |
| Format | Agent skill + Python scripts |
| Requirements | Python; TypeSafe key; GPT-6 Luna/Sol or other worker models for units. |
| License | [MIT](https://github.com/kentilaok/Jev-Orchestrated-Decision-Mesh/blob/81e784c96334c537c5e90bad24bc87c8f3d91736/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_decide.py`](https://github.com/kentilaok/Jev-Orchestrated-Decision-Mesh/blob/81e784c96334c537c5e90bad24bc87c8f3d91736/scripts/jev_decide.py) at the pinned commit. |

## When to use

- Route multi-stage, evidence-heavy agent work through checked gates.
- Mismatch: simple one-step tasks are deliberately not routed; heavy research codebase.

## How it works

Code classifies requests with project context; Jev selects next operations and authorizes routes (fused gate protocol optional). Worker models do bounded reasoning; outputs return to Jev. Integration evidence: [`scripts/jev_decide.py`](https://github.com/kentilaok/Jev-Orchestrated-Decision-Mesh/blob/81e784c96334c537c5e90bad24bc87c8f3d91736/scripts/jev_decide.py).

## Get started

From the upstream README (not run on the review host):

```sh
# see SKILL.md and docs/GATE-FUSION.md for broker usage
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Thesis: `docs/COMPLETE-THESIS.md`.
- Fast-exit research: `research/live-gpt6-fast-exit/`.

## Limits and data handling

Token and cost figures are maintainer-reported. Inputs go to TypeSafe and worker model providers.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 81e784c96334](https://github.com/kentilaok/Jev-Orchestrated-Decision-Mesh/tree/81e784c96334c537c5e90bad24bc87c8f3d91736). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
