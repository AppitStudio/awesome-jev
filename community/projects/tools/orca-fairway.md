# Fairway for Orca (Orca plugin where Jev picks an allowlisted agent, model and effort profile for each task)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An Orca plugin that asks Jev to choose one of your allowlisted Codex, Pi or Cursor Agent profiles (agent + exact model + effort) for a short task description, verifies the pair against each CLI's own model catalog, and only then dispatches through Orca. Paid Jev requests are off and shadow mode is on by default; a Workflow tab can run an approved multi-step plan with bounded launches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/spscream/orca-fairway) |
| Maintainer | [spscream](https://github.com/spscream). Independently curated. |
| Format | Orca plugin (TypeScript) |
| Requirements | Orca 1.4.265+; an OpenRouter key (Jev is called as `typesafe/jev-1.14` through OpenRouter's decisions endpoint) and paid requests enabled in settings; the agent CLIs you route to. |
| License | [MIT](https://github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/jev.ts`](https://github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/src/core/jev.ts) at the pinned commit. |

## When to use

- Route each coding task to the right agent and model automatically while keeping a hard budget and an allowlist.
- Mismatch: users without Orca, or teams that want Jev on TypeSafe's own API; this plugin calls Jev through OpenRouter.

## How it works

`src/core/jev.ts` sends only the typed task description and your profile cards to OpenRouter's decisions endpoint with a price ceiling and no fallbacks, reserving a fixed cost per attempt against a configurable budget; Jev returns a profile ID and launch parameters come only from your configuration. Integration evidence: [`src/core/jev.ts`](https://github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/src/core/jev.ts).

## Get started

Install the pinned release through Orca (it asks for approval of the requested access), then add profiles and your OpenRouter key in the Fairway panel.

```sh
orca plugin install spscream/orca-fairway@v0.6.1 --json
# re-run the exact command Orca prints with its --approve fingerprint
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Workflow guide: [github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/docs/workflows.md](https://github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/docs/workflows.md)
- Architecture: [github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/docs/architecture.md](https://github.com/spscream/orca-fairway/blob/fa16ad3d68d97036075cf97991074875247223d2/docs/architecture.md)

## Limits and data handling

Task descriptions (up to 4,096 bytes) and profile cards are sent to OpenRouter/Jev; project files and history are not collected. Default profiles are unverified examples, and the 0.6 confidence threshold is an initial policy, not a measured one.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit fa16ad3d68d9](https://github.com/spscream/orca-fairway/tree/fa16ad3d68d97036075cf97991074875247223d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
