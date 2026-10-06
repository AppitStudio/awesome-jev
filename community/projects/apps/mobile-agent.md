# Mobile Agent (KYRIE66nb)

[All projects](../README.md) · [Android apps](README.md#android-apps)

Open-source on-device Android AI agent (Chinese/English) that sees and taps the screen, with an optional dedicated decision backend — TypeSafe Jev or self-hosted Laya over `/v1/systemone` — for safety-gate verdicts and low-risk navigation choices; off by default, SHADOW/ENFORCE modes, explicit consent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KYRIE66nb/mobile-agent) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/KYRIE66nb/mobile-agent#readme) ([English](https://github.com/KYRIE66nb/mobile-agent/blob/46a75df562194ba8cf49280112bbde1ba9f8f8b0/README.en.md)); APKs on [GitHub Releases](https://github.com/KYRIE66nb/mobile-agent/releases/latest). |
| Pricing and access | Free APK (v0.1.17 on GitHub Releases) and Apache-2.0 source. Requires your own chat-model provider key; the Jev backend needs your own TypeSafe key (or a self-hosted Laya server). Usage billed by those providers. Checked 2026-10-06. |
| Jev evidence | README *可选专用决策后端（Laya/Jev）* and [`DecisionGate.kt`](https://github.com/KYRIE66nb/mobile-agent/blob/46a75df562194ba8cf49280112bbde1ba9f8f8b0/agent-core/src/main/kotlin/xyz/chouxuewei/mobile_agent/core/DecisionGate.kt) / `DecisionContract.kt` implement the `/v1/systemone` decision backend; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [KYRIE66nb](https://github.com/KYRIE66nb). Independently curated. |
| Format | Android app (APK) |
| Platform and availability | Android 7.0+. |
| Jev's role | Optional decision backend: adjudicates the safety gate for risky actions (timeouts/failures fall back to asking the user) and can pick among locally built candidates for low-risk UI navigation. |
| Requirements | Android 7.0+, accessibility permission, a chat-model provider key; optional TypeSafe key or self-hosted Laya for decisions. |
| License | [Apache-2.0](https://github.com/KYRIE66nb/mobile-agent/blob/46a75df562194ba8cf49280112bbde1ba9f8f8b0/LICENSE). |

## When to use

- Let an on-device agent operate your phone while a separate typed decision model judges whether risky steps should proceed.
- Compare hosted Jev with self-hosted Laya behind the same `/v1/systemone` contract (the two backends are mutually exclusive).
- Mismatch: early-stage software — the README warns to use a test device and never let it perform payments or account-security actions.

## How it works

Settings → 专用决策后端 connects one independent decision service (TypeSafe Jev hosted API or self-hosted Laya, deployment notes in `deploy/laya/`). It is off by default and only used for interactive tasks; outbound calls need explicit consent and send only the minimal decision context. In SHADOW mode verdicts are recorded; in ENFORCE they gate risky actions. Read-only operations never enter the gate, and gate timeouts or failures degrade to "needs human confirmation".

## Get started

Install the APK (or build), configure your chat model, then enable the decision backend in Settings (live TypeSafe calls once consented):

```sh
# APK: https://github.com/KYRIE66nb/mobile-agent/releases/latest
git clone https://github.com/KYRIE66nb/mobile-agent.git
cd mobile-agent
./gradlew :app:assembleDebug   # app/build/outputs/apk/debug/
# Settings → 专用决策后端 → TypeSafe Jev (or Laya), SHADOW first
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README screenshots of the Settings safety gate, failover and capability overview pages.
- `deploy/laya/` notes for self-hosting a Laya decision server.

## Limits and data handling

Early development; use a test device. The agent itself sends screen context to your chat provider; the decision backend sends minimal decision context to TypeSafe (or your Laya host) only after consent. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 46a75df56219](https://github.com/KYRIE66nb/mobile-agent/tree/46a75df562194ba8cf49280112bbde1ba9f8f8b0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
