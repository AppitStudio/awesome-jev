# Claude Code Trace (desktop, web and terminal viewer for Claude Code session logs with an optional Jev efficiency analysis)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Viewer for the session logs Claude Code keeps in `~/.claude/projects`: readable conversations with expandable tool calls and diffs, live tailing, session picker, and desktop (Tauri), web and terminal front ends. The optional efficiency analysis sends a redacted session summary to Jev after you confirm the exact payload and shows trace-linked findings such as repeated work, thrashing and recovery.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/delexw/claude-code-trace) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/delexw/claude-code-trace#readme) (source-built; no separate product site verified). |
| Pricing and access | Free and open source (MIT) with no account; only the optional efficiency analysis needs your own Jev API key, billed by TypeSafe. Checked 2026-11-05. |
| Jev evidence | [`src-tauri/src/efficiency/jev.rs`](https://github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/src-tauri/src/efficiency/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [delexw](https://github.com/delexw). Independently curated. |
| Format | Tauri 2 desktop app plus web app and terminal UI (Rust backend, MIT) |
| Platform and availability | macOS (Apple Silicon), Linux and Windows desktop app, plus web app and terminal UI |
| Jev's role | Optional efficiency analysis of a Claude Code session: typed Jev decisions over redacted windows of actions that become trace-linked findings. |
| Requirements | The release installer (macOS Apple Silicon dmg, Linux deb/rpm/AppImage, Windows msi/exe), the macOS one-line install script, Docker, or a source build; a Jev API key (Settings, Analytics, or `JEV_API_KEY` for web and terminal modes) only for efficiency analysis. |
| License | [MIT](https://github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/LICENSE) |

## When to use

- Read and live-tail Claude Code sessions as a conversation with tool calls, sub-agents and token counts.
- Get an optional second opinion on whether an agent session wasted effort, with findings linked to trace entries.
- Mismatch: Jev is an optional feature; the viewer works without a key and sends nothing unless you start an analysis.

## How it works

`src-tauri/src/efficiency/jev.rs` sends redacted windows of a session (up to 12 windows of 6 actions, state capped near 80,000 characters) to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`; the key is stored in the OS credential store and a confirmation dialog shows the exact payload first. Integration evidence: [`src-tauri/src/efficiency/jev.rs`](https://github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/src-tauri/src/efficiency/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
# macOS (Apple Silicon)
curl -fsSL https://raw.githubusercontent.com/delexw/claude-code-trace/main/script/install-macos.sh | bash
cctrace        # desktop app; cctrace --web or --tui for the others
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (features, install, efficiency analysis): [github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/README.md](https://github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/README.md)
- Jev integration spec: [github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/specs/14-jev-integration.md](https://github.com/delexw/claude-code-trace/blob/a889d88a72ca64dabb452a1a8a0b56786892b337/specs/14-jev-integration.md)
- Latest release: [github.com/delexw/claude-code-trace/releases/tag/v0.19.0](https://github.com/delexw/claude-code-trace/releases/tag/v0.19.0)

## Limits and data handling

Efficiency analysis sends a redacted session summary to TypeSafe on your key after you confirm it; session logs may still contain sensitive project text, so read the payload before confirming. The macOS app is ad-hoc signed but not notarized. Findings are model judgments, not proof.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit a889d88a72ca](https://github.com/delexw/claude-code-trace/tree/a889d88a72ca64dabb452a1a8a0b56786892b337). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
