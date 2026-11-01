# pi-omarchy-cu (computer use for the Pi coding agent on Omarchy, where Jev picks the accessibility target and action)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Pi extension that drives Linux desktop apps on Omarchy (Hyprland Wayland) through the AT-SPI accessibility tree. The tree stays out of Pi's context: a tool call filters actionable nodes, asks Jev for the target and operation, enforces confidence and risk thresholds, and returns compact evidence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Paul-Yuchao-Dong/pi-omarchy-cu) |
| Maintainer | [Paul-Yuchao-Dong](https://github.com/Paul-Yuchao-Dong). Independently curated. |
| Format | TypeScript Pi extension (npm) |
| Requirements | Pi coding agent, Omarchy/Hyprland with AT-SPI, agent-desktop; a TypeSafe or OpenRouter Jev endpoint. |
| License | [MIT](https://github.com/Paul-Yuchao-Dong/pi-omarchy-cu/blob/255edc2056066e2b622081aeb02c443e1f5282b3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/Paul-Yuchao-Dong/pi-omarchy-cu/blob/255edc2056066e2b622081aeb02c443e1f5282b3/src/jev/client.ts) at the pinned commit. |

## When to use

- Let a coding agent operate desktop apps with typed, thresholded target choices.
- Mismatch: Linux/Omarchy only.

## How it works

`src/jev/client.ts` uses `@typesafe-ai/sdk` in process with `choice`, `noul` and `score` questions over the filtered accessibility nodes; endpoint resolution matches `pi-jev` (`PI_JEV_BASE_URL`, `TYPESAFE_BASE_URL` or OpenRouter). Integration evidence: [`src/jev/client.ts`](https://github.com/Paul-Yuchao-Dong/pi-omarchy-cu/blob/255edc2056066e2b622081aeb02c443e1f5282b3/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:pi-omarchy-cu
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/Paul-Yuchao-Dong/pi-omarchy-cu#readme](https://github.com/Paul-Yuchao-Dong/pi-omarchy-cu#readme)

## Limits and data handling

Window contents are summarized and sent to the Jev endpoint. Desktop actions can have real effects. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 255edc205606](https://github.com/Paul-Yuchao-Dong/pi-omarchy-cu/tree/255edc2056066e2b622081aeb02c443e1f5282b3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
