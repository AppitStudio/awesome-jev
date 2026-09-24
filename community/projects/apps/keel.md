# Keel

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local-first macOS (Apple Silicon) coding workspace (Rust/GPUI) with sessions, composer, terminal, and ACP agent connections. Default decision mode uses local Laya; hosted TypeSafe Jev is an opt-in selector for fresh unpinned tasks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/codejunkie99/keel) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [GitHub README](https://github.com/codejunkie99/keel) |
| Pricing and access | No app purchase fee for the MIT source build; no downloadable release package at review. Local Laya is on-device; optional Jev uses a TypeSafe credential (BYOK). Coding providers keep their own auth/costs. Checked 2026-09-24. |
| Jev evidence | README decision-mode table and [docs/decision-architecture.md](https://github.com/codejunkie99/keel/blob/9f7fcf1f5008a0c804f9715676790c7b1ea409b6/docs/decision-architecture.md): Laya (default) vs optional hosted TypeSafe Jev vs Normal harness. |
| Disclosure | Open source MIT. Independently curated; no affiliation. Listing is not an endorsement. Live macOS build/UI not exercised on the Linux review host. Jev is optional. |
| Maintainer | [codejunkie99](https://github.com/codejunkie99). Independently curated. |
| Format | Application |
| Platform and availability | macOS 15+ Apple Silicon recommended for packaged Laya; build from source (`docs/build.md`). Release stage: source-build workspace (0.2.0). |
| Jev's role | Optional selector chooses an eligible route for a fresh unpinned task; host code checks the choice before applying. Pinned/live sessions keep existing routes. External ACP agents keep their own tool loops. |
| Requirements | Apple Silicon macOS; Rust toolchain to build; optional TypeSafe credential for Jev mode; coding CLI/provider accounts as configured. |
| License | [MIT](https://github.com/codejunkie99/keel/blob/9f7fcf1f5008a0c804f9715676790c7b1ea409b6/LICENSE). |

## When to use

Use for a **local-first** coding workspace with optional Jev route selection. Prefer cloud IDEs when you need hosted collaboration.

## How it works

Keel prepares allowed route candidates; Laya or Jev selects or abstains; Keel validates before apply. Exact ACP adapter set is documented upstream.

## Get started

```sh
git clone https://github.com/codejunkie99/keel.git
cd keel
git checkout 9f7fcf1f5008a0c804f9715676790c7b1ea409b6
# follow docs/build.md on macOS Apple Silicon; choose Laya, Jev, or Normal in Settings
```

## Examples and demos

- `docs/guide.md`, `docs/decision-architecture.md`.
- Workspace UI surfaces described in README.

## Limits and data handling

Jev mode sends bounded decision payloads to TypeSafe. Coding providers may send full task context separately. Linux review host could not build the macOS app.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 9f7fcf1](https://github.com/codejunkie99/keel/tree/9f7fcf1f5008a0c804f9715676790c7b1ea409b6). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [Jaste](jaste.md), [macbrow](macbrow.md).
