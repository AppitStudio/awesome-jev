# Alethe (multi-agent coding desktop workspace with TypeSafe Jev voice-intent routing)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Local-first desktop app that runs Claude Code, Codex, Copilot and shells side by side. Voice intent routing goes through TypeSafe Jev (`src-tauri/src/jev.rs`) so spoken commands map to typed workspace actions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Vnxcarvalho/Alethe-2.0) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Vnxcarvalho/Alethe-2.0#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (AGPL-3.0); TypeSafe key for Jev voice routing. Checked 2026-11-06. |
| Jev evidence | [`src-tauri/src/jev.rs`](https://github.com/Vnxcarvalho/Alethe-2.0/blob/496718314181ed88c39b3e39a529ee95de3fc179/src-tauri/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Vnxcarvalho](https://github.com/Vnxcarvalho). Independently curated. |
| Format | Tauri desktop app (AGPL-3.0) |
| Platform and availability | Desktop (Tauri); local-first multi-agent workspace. |
| Jev's role | Voice intent router: Jev classifies spoken intents into workspace actions via the native TypeSafe decisions client. |
| Requirements | Desktop build toolchain per upstream, and a TypeSafe key for Jev voice-intent routing. |
| License | [AGPL-3.0](https://github.com/Vnxcarvalho/Alethe-2.0/blob/496718314181ed88c39b3e39a529ee95de3fc179/LICENSE) |

## When to use

- Run several coding agents in one local desktop workspace.
- Route voice commands with a typed decision model.
- Mismatch: early/zero-star project; AGPL copyleft applies to distributions.

## How it works

`src-tauri/src/jev.rs` posts to TypeSafe decisions (`https://api.typesafe.ai/v1/decisions`) for voice intent routing. Integration evidence: [`src-tauri/src/jev.rs`](https://github.com/Vnxcarvalho/Alethe-2.0/blob/496718314181ed88c39b3e39a529ee95de3fc179/src-tauri/src/jev.rs).

## Get started

Clone and build per the README; configure a TypeSafe key for voice routing.

```sh
git clone https://github.com/Vnxcarvalho/Alethe-2.0.git && cd Alethe-2.0
export TYPESAFE_API_KEY=...
# build per README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Vnxcarvalho/Alethe-2.0/blob/496718314181ed88c39b3e39a529ee95de3fc179/README.md](https://github.com/Vnxcarvalho/Alethe-2.0/blob/496718314181ed88c39b3e39a529ee95de3fc179/README.md)

## Limits and data handling

Voice transcript/intent text is sent to TypeSafe on your key. AGPL-3.0 obligations apply if you distribute modifications.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 496718314181](https://github.com/Vnxcarvalho/Alethe-2.0/tree/496718314181ed88c39b3e39a529ee95de3fc179). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
