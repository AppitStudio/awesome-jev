# Astra-Ares

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Adaptive reasoning-effort selection for GPT-6 Astra during Codex tasks: TypeSafe Jev chooses how hard Astra should think next (and for how many generations) so token use can track the work ahead.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/miuuyy/Astra-Ares) |
| Maintainer | [miuuyy](https://github.com/miuuyy). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI (`astra-ares` / `ares` **0.2.1**) that installs a separate, patched Codex CLI reference build. |
| Requirements | Node.js ≥ 22, npm, Git, curl, tar, a C/C++ toolchain, and Rust via rustup (~10 GB free for first build). Codex login with Astra access; Jev key via OpenRouter (default), direct TypeSafe, or Vercel AI Gateway (`ares configure`). |
| License | [MIT](https://github.com/miuuyy/Astra-Ares/blob/201f3675cf85187d9dbd79fe110d7174445e4f81/LICENSE). Upstream Codex patch notices in `THIRD_PARTY_NOTICES.md`. Provider usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Experimental patched-Codex preview (macOS Apple Silicon noted as locally tested; Windows unsupported). Source inspected; full `npm run setup` Codex rebuild and live Jev/Astra runs were **not** executed on the review host. |

## When to use

Use it when you want **Jev to adapt Astra reasoning effort mid-Codex-task** while keeping the same model, conversation, and OpenAI connection. Prefer stock Codex or other effort routers ([codex-jev-router](codex-jev-router.md), [Auto Mode for Paseo](auto-mode-for-paseo.md)) when you do not want a patched Codex build.

## How it works

[`src/jev.mjs`](https://github.com/miuuyy/Astra-Ares/blob/201f3675cf85187d9dbd79fe110d7174445e4f81/src/jev.mjs) builds typed Choice questions (`effort`, `lease`) for System One (`typesafe-ai/jev` / OpenRouter `typesafe/jev-1.13` per [`docs/paid-access.md`](https://github.com/miuuyy/Astra-Ares/blob/201f3675cf85187d9dbd79fe110d7174445e4f81/docs/paid-access.md)). Codex applies confirmed effort changes while the task continues; the UI shows `APPLIED` after native application.

## Get started

```sh
git clone https://github.com/miuuyy/Astra-Ares.git
cd Astra-Ares
git checkout 201f3675cf85187d9dbd79fe110d7174445e4f81
npm ci
# Builds a separate patched Codex — several minutes / ~10 GB; not run on this review host
npm run setup
npm link
ares configure   # paste OpenRouter (default) or TypeSafe/Vercel key
astra-ares       # pick Astra-Jev in /model
```

Live Jev and Astra usage incur provider charges. See upstream [installation](https://github.com/miuuyy/Astra-Ares/blob/201f3675cf85187d9dbd79fe110d7174445e4f81/docs/installation.md) and [configuration](https://github.com/miuuyy/Astra-Ares/blob/201f3675cf85187d9dbd79fe110d7174445e4f81/docs/configuration.md).

## Examples and demos

- README walkthrough of effort changes in the Codex transcript.
- Upstream docs: architecture, validation, troubleshooting, paid-access provider notes (checked **2026-09-22** in-repo).

## Limits and data handling

Task/history excerpts used for effort decisions leave the host on live Jev calls. Experimental reference; Windows is unsupported. This listing did not rebuild Codex or run live probes.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 201f367](https://github.com/miuuyy/Astra-Ares/tree/201f3675cf85187d9dbd79fe110d7174445e4f81) (`0.2.1`, MIT). AI-assisted review of README, LICENSE, `src/jev.mjs`, `docs/paid-access.md`, `package.json`. No full setup/live run.

Related: [codex-jev-router](codex-jev-router.md), [Auto Mode for Paseo](auto-mode-for-paseo.md), [Codex Jev Preflight](codex-jev-preflight.md).
