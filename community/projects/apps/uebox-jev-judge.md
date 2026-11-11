# UE Box (Unreal Editor agent with a Jev judge role)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Open-source AI agent that operates the Unreal Editor (levels, blueprints, materials, C++), with a structured judge provider for TypeSafe Jev that drives goal-mode autoplay steps and visual checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ueboxai/uebox) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://uebox.ai/en) |
| Pricing and access | Free download (Apache-2.0); bring your own model and TypeSafe keys. Hosted pricing not checked. Checked 2026-11-11. |
| Jev evidence | [`src/main/ai/judge.ts`](https://github.com/ueboxai/uebox/blob/c4825a98c2b0053d04927aa31670c1b2764d8f58/src/main/ai/judge.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ueboxai](https://github.com/ueboxai). Independently curated. |
| Format | Desktop app (Electron, Vue 3 and TypeScript, Apache-2.0) |
| Platform and availability | Windows desktop app; macOS and Linux from source |
| Jev's role | Jev is the judge model for autoplay goal steps and screenshot visual checks. |
| Requirements | Unreal Engine 5.x with the UE Box plugin, a chat-model provider, and a TypeSafe key set as the judge role. |
| License | [Apache-2.0](https://github.com/ueboxai/uebox/blob/c4825a98c2b0053d04927aa31670c1b2764d8f58/LICENSE) |

## When to use

- Let a typed model decide autoplay steps and visual checks for Unreal playtests.
- Drive Unreal Editor changes from an agent.
- Mismatch: docs are mostly Chinese (English README available); autoplay is experimental; macOS/Linux build from source.

## How it works

`src/main/ai/judge.ts` implements noul, choice, score and box judgments on System One; the changelog says the experimental `ue_autoplay` goal mode needs TypeSafe Jev set as the judge role, and visual checks can use Jev 1.14. Integration evidence: [`src/main/ai/judge.ts`](https://github.com/ueboxai/uebox/blob/c4825a98c2b0053d04927aa31670c1b2764d8f58/src/main/ai/judge.ts).

## Get started

Install a release, connect the Unreal plugin, then set TypeSafe Jev as the judge in AI services.

```sh
# download from https://github.com/ueboxai/uebox/releases
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ueboxai/uebox/blob/c4825a98c2b0053d04927aa31670c1b2764d8f58/README.md](https://github.com/ueboxai/uebox/blob/c4825a98c2b0053d04927aa31670c1b2764d8f58/README.md)

## Limits and data handling

Game state and opted-in screenshots go to TypeSafe for judge calls; the editor agent uses your chat provider.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit c4825a98c2b0](https://github.com/ueboxai/uebox/tree/c4825a98c2b0053d04927aa31670c1b2764d8f58). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
