# Browser runs for Pi Pocket (goal-driven browser runs decided by Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Pi Pocket extension (0.22.0+) that hands the browser one goal and the values it may type; a run model, Jev through OpenRouter or the session's own model, picks each step's operation, target and value until the goal is visibly done or a clear stop reason applies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/picassio/pi-pocket-browser-runs) |
| Maintainer | [picassio](https://github.com/picassio). Independently curated. |
| Format | Pi Pocket extension (TypeScript) |
| Requirements | Pi Pocket 0.22.0+ with its Browser module; an OpenRouter sign-in for the Jev run model. |
| License | [MIT](https://github.com/picassio/pi-pocket-browser-runs/blob/873fa381a35fb219828df61d12dc9c8ba695671b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`browser-runs.ts`](https://github.com/picassio/pi-pocket-browser-runs/blob/873fa381a35fb219828df61d12dc9c8ba695671b/browser-runs.ts) at the pinned commit. |

## When to use

- Let an agent finish a multi-step browser task without spending its own tokens on each click.
- Get a typed stop reason (done, blocked, needs_value, stuck_loop, budget) instead of a vague failure.
- Mismatch: Jev is one of two run models; the session model works without it.

## How it works

`browser-runs.ts` sends each step's goal, supplied values and the page's controls and text to `typesafe/jev-1.13` on OpenRouter's decisions route as one set of typed questions; it never invents a value that was not supplied. Integration evidence: [`browser-runs.ts`](https://github.com/picassio/pi-pocket-browser-runs/blob/873fa381a35fb219828df61d12dc9c8ba695671b/browser-runs.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# Pi Pocket: Menu → Extensions → Discover → Browser runs → Install
# or copy browser-runs.ts and browser-runs.js into ~/.pi-pocket/extensions/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/picassio/pi-pocket-browser-runs#readme](https://github.com/picassio/pi-pocket-browser-runs#readme)
- Pi Pocket: [github.com/TannerMidd/pi-pocket](https://github.com/TannerMidd/pi-pocket)

## Limits and data handling

With Jev, page controls and text, the goal and supplied values go to OpenRouter and TypeSafe. Runs stop at 25 steps, 180 seconds or the session's spend limit by default.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 873fa381a35f](https://github.com/picassio/pi-pocket-browser-runs/tree/873fa381a35fb219828df61d12dc9c8ba695671b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
