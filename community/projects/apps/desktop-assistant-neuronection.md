# Desktop Assistant by Neuronection (system-tray AI launcher whose optional decision layer uses Jev to dispatch short commands straight to tools)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Electron launcher that lives in the system tray: global hotkey, streaming chat with many providers (or local Ollama), voice input, PDF and screen attachments, tool apps and local-only history. Its optional decision layer runs before the chat model: a decision model assigned per capability slot (tool dispatch, yes/no gate, choice, score) sends short commands straight to a tool and also powers voice auto-send, prompt-armed auto-speak, custom rules and live-conversation interruption. The one decision transport that ships is TypeSafe System One, used directly or through OpenRouter's Jev route.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/neuronection/desktop-assistant) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://neuronection.com) |
| Pricing and access | Free download (Apache-2.0, installers on GitHub Releases). You pay your chat provider and TypeSafe or OpenRouter for your own calls. Checked 2026-11-16. |
| Jev evidence | [`src/main/ai/decide/systemone/client.ts`](https://github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/src/main/ai/decide/systemone/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [neuronection](https://github.com/neuronection). Independently curated. |
| Format | Electron desktop app (TypeScript, Apache-2.0); installers for Windows, macOS and Linux |
| Platform and availability | Windows, macOS (Intel and Apple Silicon) and Linux (AppImage, deb); installers on GitHub Releases |
| Jev's role | Optional decision layer: Jev picks the tool and closed-set arguments for short commands and answers yes/no gates for voice features. |
| Requirements | Windows, macOS or Linux; a chat provider key or local Ollama; for the decision layer a TypeSafe key, or an OpenRouter key for its Jev route. |
| License | [Apache-2.0](https://github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/LICENSE) |

## When to use

- Make a desktop assistant act on short commands without a full chat round trip.
- Mismatch: users who want no cloud calls for decisions; the decision layer is cloud-only.

## How it works

`src/main/ai/decide/systemone/client.ts` calls System One through the TypeSafe SDK (`@typesafe-ai/sdk`); `src/shared/ai/providerPresets.generated.ts` defines the TypeSafe preset (`https://api.typesafe.ai`, `jev-latest`) and OpenRouter's pinned `typesafe/jev-1.13`. Tool candidates are projected into a closed choice with a `__none__` option, so the model cannot invent a tool or argument. Integration evidence: [`src/main/ai/decide/systemone/client.ts`](https://github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/src/main/ai/decide/systemone/client.ts).

## Get started

Download an installer from the latest release (or run from source), connect a chat provider, then assign a decision model in Settings → API → Tasks.

```sh
# installers: https://github.com/neuronection/desktop-assistant/releases/latest
git clone https://github.com/neuronection/desktop-assistant.git && cd desktop-assistant
npm install && npm run prisma:generate && npm run dev
# Settings -> API -> Tasks -> assign a TypeSafe or OpenRouter Jev model to the decision slots
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/README.md](https://github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/README.md)
- Decision models guide: [github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/docs/user/decision-models.md](https://github.com/neuronection/desktop-assistant/blob/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a/docs/user/decision-models.md)

## Limits and data handling

The decision layer is off until you assign a decision model; when on, the command and candidate tool list go to TypeSafe or OpenRouter on your key (stored in the OS keyring). Chat goes to the provider you pick. Beta status per the maker.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 01d6d4532f0f](https://github.com/neuronection/desktop-assistant/tree/01d6d4532f0fdb0165f4c90b8afde9ec3b5a368a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
