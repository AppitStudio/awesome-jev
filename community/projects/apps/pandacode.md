# PandaCode (native desktop workspace for many coding-agent CLIs with an optional, off-by-default Jev add-on for work review, project rules, context search and worker choice)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Tauri desktop workspace that runs Claude Code, Codex, OpenCode, Pi and many other coding CLIs side by side with projects, Git, a terminal and a browser. The optional Jev add-on (off by default) adds advisory work review, project-rule checks on saved diffs, context excerpts and worker suggestions, plus browser testing; everything works without it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aicodeking/pandacode) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/aicodeking/pandacode#readme) (source-built; no separate product site verified). |
| Pricing and access | Free per the README (no account, license key or telemetry); the license is MIT plus a requirement that public or commercial forks say they are forks of PandaCode, so it is tagged source available. Jev calls are billed on your key. Checked 2026-11-05. |
| Jev evidence | [`src-tauri/src/jev_decisions/api.rs`](https://github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/src-tauri/src/jev_decisions/api.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [aicodeking](https://github.com/aicodeking). Independently curated. |
| Format | Tauri 2 desktop app (Rust, SQLite, TypeScript) |
| Platform and availability | macOS, Windows and Linux desktop app (release installers or source build) |
| Jev's role | Optional advisory checks (work review, project rules, context search, worker choice) from typed Jev decisions over local evidence. |
| Requirements | Release installer or source build; save a TypeSafe key in Settings → Agents → Set up Jev to enable decision assistance. |
| License | [PandaCode License (MIT with an attribution requirement for public or commercial forks)](https://github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/LICENSE) |

## When to use

- Add advisory Jev checks to agent tasks and saved diffs without changing the agent.
- Preview the exact evidence before each Jev run.
- Mismatch: Jev is optional and judgments are advisory, not tests; the license is MIT plus a fork-attribution condition, so this is source available rather than plain MIT.

## How it works

`src-tauri/src/jev_decisions/` builds typed questions from bounded local evidence and calls the TypeSafe API; `docs/jev.md` documents each option, the tools added to harnesses while enabled, and the off-by-default switches. Integration evidence: [`src-tauri/src/jev_decisions/api.rs`](https://github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/src-tauri/src/jev_decisions/api.rs).

## Get started

From the upstream README (not run on the review host):

```sh
# install from https://github.com/aicodeking/pandacode/releases, then Settings → Agents → Set up Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Optional Jev add-on guide: [github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/docs/jev.md](https://github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/docs/jev.md)
- PandaCode License: [github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/LICENSE](https://github.com/aicodeking/pandacode/blob/fc32c3f585db6a72fee967e8d91f2bb50fe67852/LICENSE)

## Limits and data handling

Evidence you choose to run is sent to TypeSafe on your key; probability-based judgments are not proof of correctness. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit fc32c3f585db](https://github.com/aicodeking/pandacode/tree/fc32c3f585db6a72fee967e8d91f2bb50fe67852). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
