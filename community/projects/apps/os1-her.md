# OS1 by Nicholas Vasilescu (Her-inspired voice-first desktop assistant where Jev decides what to show and routes each turn)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

An experimental voice-first personal assistant: an Electron and Three.js desktop client, a FastAPI orchestrator, a LiveKit voice stack with Fish Audio voices, and a Hermes background agent on a cloud VM. The screen stays quiet while you talk, and Jev decides when a card, inbox or other surface is worth showing (with anti-flicker hysteresis). Risky actions use an undo queue or read-back confirmation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nickvasilescu/os1-her) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/nickvasilescu/os1-her#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you bring keys for Anthropic, LiveKit Cloud and Fish Audio (required) and optionally TypeSafe, Composio and Orgo, and pay those providers. Checked 2026-11-22. |
| Jev evidence | [`services/voice/os1_voice/jev.py`](https://github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/services/voice/os1_voice/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [nickvasilescu](https://github.com/nickvasilescu). Independently curated. |
| Format | Electron app + Python services |
| Platform and availability | Desktop (Electron, developed on macOS) plus local Python services; optional cloud VM on Orgo. |
| Jev's role | Optional ~100 ms System One judgments: the UI Director picks which surface to show, mood and triage, and the turn router decides how each voice turn is handled; every caller still works when Jev is off or times out. |
| Requirements | Node.js 22+, uv (Python 3.12+), keys for Anthropic, LiveKit Cloud and Fish Audio; TypeSafe, Composio and Orgo keys are optional. |
| License | [MIT](https://github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/LICENSE) |

## When to use

- Explore a voice assistant design where a fast decision model controls UI choreography and turn routing.
- Mismatch: a ready-to-use assistant; this is a multi-service stack that needs several paid accounts.

## How it works

`services/voice/os1_voice/jev.py` wraps the TypeSafe Python SDK with a hard latency budget and returns `None` on any failure, so the voice loop never waits on Jev; the orchestrator's Jev UI Director uses the same answers with hysteresis. Integration evidence: [`services/voice/os1_voice/jev.py`](https://github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/services/voice/os1_voice/jev.py).

## Get started

Clone, install and preview any UI surface without keys; the full stack needs the Hermes profile, the orchestrator, the voice worker and the desktop app running together.

```sh
git clone https://github.com/nickvasilescu/os1-her && cd os1-her
cp .env.example .env   # add keys; TYPESAFE_API_KEY enables Jev
npm install
OS1_PREVIEW=home npm run dev   # preview a surface with no keys
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture: [github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/docs/architecture.md](https://github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/docs/architecture.md)
- Jev notes: [github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/docs/jev-reference.md](https://github.com/nickvasilescu/os1-her/blob/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7/docs/jev-reference.md)

## Limits and data handling

Voice, mail and connector data go to the providers you configure; Jev receives the UI and turn state it is asked about. Access to your own Mac runs only through a bounded, opt-in tunnel per the README. Early project.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit a3a7bc4e6cc4](https://github.com/nickvasilescu/os1-her/tree/a3a7bc4e6cc47ef838e9314f0f62b5cc16df4df7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
