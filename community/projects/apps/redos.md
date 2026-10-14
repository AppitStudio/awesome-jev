# RedOS

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS menu-bar assistant for voice and text commands where a System One model using the Jev protocol routes request kinds and decides whether to speak or stay quiet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Carassale/redos) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Carassale/redos#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-14. |
| Jev evidence | [`Sources/RedOSCore/SystemOne/JevHTTPSystemOne.swift`](https://github.com/Carassale/redos/blob/a9a94b8516f0d17ce9883d2648305d04af82e6f7/Sources/RedOSCore/SystemOne/JevHTTPSystemOne.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Carassale](https://github.com/Carassale). Independently curated. |
| Format | macOS menu-bar app (Swift) |
| Platform and availability | macOS (source build) |
| Jev's role | Jev-protocol System One decisions route request kinds and speak/notify/silent choices; optional. |
| Requirements | macOS; Swift toolchain to build; an assistant provider key or Copilot CLI; a local or custom Jev-protocol server (for example Codiv OpenJev) for fast decisions. |
| License | [MIT](https://github.com/Carassale/redos/blob/a9a94b8516f0d17ce9883d2648305d04af82e6f7/LICENSE) |

## When to use

- Control a Mac by voice/text with a fast decision layer that classifies the kind of each request.
- Proactive notices where a typed decision chooses speak / quiet notification / silence.
- Mismatch: Jev-protocol decisions are optional; without a configured Jev server the app uses fixed rules.

## How it works

A small System One model chooses among available actions via the Jev protocol and recognizes the kind of each request (action, steps, screen task). The assistant LLM provider does the generative work; code executes Mac actions. The Jev endpoint is configurable (local, Codiv OpenJev, or a custom Jev server). Integration evidence: [`Sources/RedOSCore/SystemOne/JevHTTPSystemOne.swift`](https://github.com/Carassale/redos/blob/a9a94b8516f0d17ce9883d2648305d04af82e6f7/Sources/RedOSCore/SystemOne/JevHTTPSystemOne.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Carassale/redos.git
cd redos
make
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evaluation harness in `Sources/RedOSEval/`.
- Settings → Models → Fast decisions selects the Jev server (per upstream README).

## Limits and data handling

Grants broad Mac control permissions; commands go to your configured assistant provider and Jev server. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit a9a94b8516f0](https://github.com/Carassale/redos/tree/a9a94b8516f0d17ce9883d2648305d04af82e6f7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
