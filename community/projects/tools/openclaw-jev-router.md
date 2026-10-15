# Axeon JEV Router (OpenClaw)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenClaw plugin that asks Jev to pick the model for each interactive turn (Luna, Sol or Astra by default) with owner-controlled `/autoroute` on, off or shadow, keeping host locks, fallbacks and thinking settings untouched.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/axeon-at/openclaw-jev-router) |
| Maintainer | [axeon-at](https://github.com/axeon-at). Independently curated. |
| Format | OpenClaw plugin (Node.js, early release) |
| Requirements | OpenClaw plugin API 2026.9.9+, Node.js 22.13+ with `node:sqlite`, OpenClaw `openai` provider access, `TYPESAFE_API_KEY` on the Gateway. |
| License | [MIT](https://github.com/axeon-at/openclaw-jev-router/blob/c3357a498ece319e3aace03e18c75b65e04b4bc7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.mjs`](https://github.com/axeon-at/openclaw-jev-router/blob/c3357a498ece319e3aace03e18c75b65e04b4bc7/jev.mjs) at the pinned commit. |

## When to use

- Let OpenClaw spend cheaper models on small talk and routine requests without asking the main assistant to classify its own work.
- Shadow-test routing decisions before turning them on.
- Mismatch: routes models only, not thinking effort; no quota or cost saving is guaranteed.

## How it works

On each initial run the plugin sends the host-provided prompt (plus attachment kind labels and the prior case) to `https://api.typesafe.ai/v1/systemone`, sums Jev probability across categories mapped to the same model, and leaves native locks and host fallbacks in charge; OFF makes no call. Integration evidence: [`jev.mjs`](https://github.com/axeon-at/openclaw-jev-router/blob/c3357a498ece319e3aace03e18c75b65e04b4bc7/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/axeon-at/openclaw-jev-router.git && cd openclaw-jev-router
npm test
openclaw plugins install --link .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Privacy notes: `SECURITY.md`.

## Limits and data handling

Active and shadow modes send the current prompt (which may include host-added context) to TypeSafe on your key; route observations stay in local SQLite.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit c3357a498ece](https://github.com/axeon-at/openclaw-jev-router/tree/c3357a498ece319e3aace03e18c75b65e04b4bc7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
