# BUTLR.ai (Windows desktop assistant that operates the focused app, choosing each UI action with Jev)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Focus any Windows app, press Ctrl+Win and type what you want done. BUTLR.ai reads the app's accessible controls through Windows UI Automation, asks Jev (through Vercel AI Gateway) to pick the next action, then types, clicks and checks the result. Steps such as Submit, Send, Pay, Delete or Install always wait for your approval, password fields and card numbers are never captured, and password managers are blocked.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/notyourgiantcoder/BUTLR.ai) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/notyourgiantcoder/BUTLR.ai#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; bring your own Vercel AI Gateway key. Checked 2026-10-30. |
| Jev evidence | [`windows/src/Butlr.Core/Jev/JevOptions.cs`](https://github.com/notyourgiantcoder/BUTLR.ai/blob/1de637b14bc8e9fd245dcd88fb3589f8f4050e8c/windows/src/Butlr.Core/Jev/JevOptions.cs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [notyourgiantcoder](https://github.com/notyourgiantcoder). Independently curated. |
| Format | Windows desktop app (.NET) |
| Platform and availability | Windows x64; source build (no GitHub release published when reviewed). |
| Jev's role | Picks the next UI action for each step of your instruction. |
| Requirements | Windows x64 and a Vercel AI Gateway key with access to `typesafe-ai/jev`. |
| License | [MIT](https://github.com/notyourgiantcoder/BUTLR.ai/blob/1de637b14bc8e9fd245dcd88fb3589f8f4050e8c/LICENSE) |

## When to use

- Automate small chores in desktop apps by typing what you want instead of clicking.
- Mismatch: version 0.1; the README's release zip was not published when reviewed, so build from source.

## How it works

`windows/src/Butlr.Core/Jev/JevOptions.cs` points at `https://ai-gateway.vercel.sh` with model `typesafe-ai/jev`; the Jev client scores candidate UI actions for each step. Integration evidence: [`windows/src/Butlr.Core/Jev/JevOptions.cs`](https://github.com/notyourgiantcoder/BUTLR.ai/blob/1de637b14bc8e9fd245dcd88fb3589f8f4050e8c/windows/src/Butlr.Core/Jev/JevOptions.cs).

## Get started

Adapted from the upstream README and repo layout (not run on the review host):

```sh
git clone https://github.com/notyourgiantcoder/BUTLR.ai && cd BUTLR.ai
dotnet build windows/Butlr.sln -c Release
cp .env.example .env   # set AI_GATEWAY_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with safety rules: [github.com/notyourgiantcoder/BUTLR.ai#readme](https://github.com/notyourgiantcoder/BUTLR.ai#readme)

## Limits and data handling

Your instruction and the visible control tree of the focused window go to Vercel AI Gateway; sensitive fields are redacted.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 1de637b14bc8](https://github.com/notyourgiantcoder/BUTLR.ai/tree/1de637b14bc8e9fd245dcd88fb3589f8f4050e8c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
