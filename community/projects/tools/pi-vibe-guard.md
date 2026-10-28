# pi-vibe-guard (Pi extension that warns when a prompt reads as vague vibe coding, scored by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that scores every prompt with Jev before it reaches the model and warns when it reads as loose-spec vibe coding, with concrete fixes (add a measurement, an acceptance criterion or a target path); declining returns the text to the editor so you can tighten it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jordilopez/pi-vibe-guard) |
| Maintainer | [jordilopez](https://github.com/jordilopez). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi and a Jev provider configured in Pi. |
| License | [MIT](https://github.com/jordilopez/pi-vibe-guard/blob/75121185a75cdfda01e1e6319e0cbe03dde432e4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`.pi/extensions/vibe-guard.ts`](https://github.com/jordilopez/pi-vibe-guard/blob/75121185a75cdfda01e1e6319e0cbe03dde432e4/.pi/extensions/vibe-guard.ts) at the pinned commit. |

## When to use

- Nudge yourself or a team toward specific prompts for coding agents.
- Mismatch: advisory only; you can always send anyway.

## How it works

`.pi/extensions/vibe-guard.ts` classifies each prompt with `jev-latest` and shows the probability and suggestions before sending. Integration evidence: [`.pi/extensions/vibe-guard.ts`](https://github.com/jordilopez/pi-vibe-guard/blob/75121185a75cdfda01e1e6319e0cbe03dde432e4/.pi/extensions/vibe-guard.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jordilopez/pi-vibe-guard && cd pi-vibe-guard
pi -e ./.pi/extensions/vibe-guard.ts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jordilopez/pi-vibe-guard#readme](https://github.com/jordilopez/pi-vibe-guard#readme)

## Limits and data handling

Each prompt goes to the Jev provider before the main model.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 75121185a75c](https://github.com/jordilopez/pi-vibe-guard/tree/75121185a75cdfda01e1e6319e0cbe03dde432e4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
