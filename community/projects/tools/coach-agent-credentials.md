# Coach (desktop app for defining credentials and testing which of your agents can earn them, with an optional Jev Mode)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local desktop app: define a credential as learning targets and checkable assignments, register the agent setups you run (harness, model, effort), and the app writes test prompts and handoff notes, records results as plain Markdown and JSON, and shows which agent to reach for. Optional Jev Mode, off by default, sends text to TypeSafe only when you ask. Early prototype (Tauri, Mac and Linux).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/workshop-maybe/coach) |
| Maintainer | [workshop-maybe](https://github.com/workshop-maybe). Independently curated. |
| Format | Desktop app (Tauri 2, React, Rust) |
| Requirements | Node.js and Rust to build; a TypeSafe API key for Jev Mode. |
| License | [Apache-2.0](https://github.com/workshop-maybe/coach/blob/a80cb10b94fc589db4b91e4bd4ac7ef3ff5c5f03/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src-tauri/src/jev.rs`](https://github.com/workshop-maybe/coach/blob/a80cb10b94fc589db4b91e4bd4ac7ef3ff5c5f03/src-tauri/src/jev.rs) at the pinned commit. |

## When to use

- Keep a checkable record of what each of your agent setups can do.
- Mismatch: planning-stage prototype; build from source.

## How it works

`src-tauri/src/jev.rs` posts to `https://api.typesafe.ai/v1/systemone` with a pinned `jev-1.13.0` and keeps the key in the OS keychain. Integration evidence: [`src-tauri/src/jev.rs`](https://github.com/workshop-maybe/coach/blob/a80cb10b94fc589db4b91e4bd4ac7ef3ff5c5f03/src-tauri/src/jev.rs).

## Get started

Build from source (commands inferred from the Tauri project layout; not run on the review host):

```sh
git clone https://github.com/workshop-maybe/coach && cd coach
npm install
npm run tauri dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/workshop-maybe/coach#readme](https://github.com/workshop-maybe/coach#readme)

## Limits and data handling

Everything stays in your data folder except text you send in Jev Mode.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit a80cb10b94fc](https://github.com/workshop-maybe/coach/tree/a80cb10b94fc589db4b91e4bd4ac7ef3ff5c5f03). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
