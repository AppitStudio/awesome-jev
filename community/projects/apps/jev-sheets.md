# Jev Sheets (OpenHarness)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Spreadsheet pane inside the OpenHarness desktop app: type a question as a column header and TypeSafe Jev answers it for every row, with Confidence, review gates, and Question Lab wording trials.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/autonomous-ai/openharness) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Harness desktop download](https://harness.autonomous.ai/desktop) — macOS and Linux installers for OpenHarness, which ships the Jev Sheets harness. |
| Pricing and access | MIT source and the public desktop download show **no app purchase fee** (checked **2026-09-24**). Live answers need a TypeSafe, OpenRouter, or Cloudflare Workers AI key (BYOK); provider usage is separate. An offline practice mode runs without a key (word-matching stand-in only). Optional Harness hardware device is separate and not required for this listing. |
| Jev evidence | Inspected [`store/agents/jev-sheets/README.md`](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/store/agents/jev-sheets/README.md), [`toolchain/jev.mjs`](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/store/agents/jev-sheets/toolchain/jev.mjs) (TypeSafe / OpenRouter / Cloudflare / offline mock), and [`viewer/grammar.mjs`](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/store/agents/jev-sheets/viewer/grammar.mjs) (header → `noul` / `choice` / `score`). Featured in the root README [Beyond code: Data / Jev Sheets](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/README.md). |
| Disclosure | AI-assisted catalog review; independently curated; no affiliation with Autonomous or TypeSafe. Listing is not an endorsement. Source and public README inspected; OpenHarness desktop install and live Jev calls were **not** run on the review host. Upstream cost/accuracy tables are vendor-reported for dated made-up fixtures—not independently re-measured here. |
| Maintainer | [Autonomous](https://github.com/autonomous-ai) (`autonomous-ai/openharness`). Independently curated by AppitStudio catalog admin. |
| Format | Domain-specific harness (DSH) for OpenHarness: sheet pane + analyst agent (`harness.json` id `autonomous/jev-sheets`). |
| Platform and availability | OpenHarness desktop on **macOS or Linux** ([download](https://harness.autonomous.ai/desktop) or build from source). Jev Sheets is installed from the in-app Store / `store/agents/jev-sheets/`. |
| Jev's role | Answers typed column questions (`noul`, `choice`, `score`) for every row via the harness Jev client; Question Lab compares wordings with paired Jev requests. Application code owns import, caching, review UI, `answers.csv`, and findings tooling. Offline practice uses a deterministic word-matching stand-in. Claude (or other coding engines) may assist as the side-pane analyst—that is not the sheet judgment path. |
| Requirements | OpenHarness desktop (or source build); Node toolchain bundled with the harness; live mode needs a provider key saved locally (for example under `~/.config/typesafe/credentials`). |
| License | [MIT](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/LICENSE) (repo); harness wrapper also [MIT](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/store/agents/jev-sheets/LICENSE). |

## When to use

Use it when you want a **desktop sheet workflow** that asks the same TypeSafe Jev questions across thousands of reviews, tickets, survey answers, or leads, with confidence fading, a review line, and Question Lab before rolling a wording to the whole file. Prefer [jev-table](../tools/jev-table.md) for a headless CSV/JSONL CLI, or [Jev Column Race](jev-column-race.md) for a side-by-side labeling race demo. This listing covers **Jev Sheets only**—not the rest of OpenHarness’s domain harnesses.

## How it works

OpenHarness hosts coding agents beside a live viewer. The Jev Sheets harness serves a loopback sheet pane: you load `.xlsx` / CSV / TSV / JSON(L) (or paste rows), type headers that [`grammar.mjs`](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/store/agents/jev-sheets/viewer/grammar.mjs) maps to typed questions, and [`jev.mjs`](https://github.com/autonomous-ai/openharness/blob/a53351bd1a2c33c2976b7df6869e3666578fdd7d/store/agents/jev-sheets/toolchain/jev.mjs) `evaluate()` fills cells (TypeSafe System One, OpenRouter Decisions, Cloudflare Workers AI, or the offline mock). Question Lab freezes a sample of rows and compares original vs candidate wording through the same client. The side agent helps craft questions and write `findings.md`; row judgments remain Jev’s job.

## Get started

```sh
# Option A — download OpenHarness for macOS or Linux
# https://harness.autonomous.ai/desktop
# Then open Jev Sheets from the Store (Productivity / Data).

# Option B — build OpenHarness from the reviewed tip
git clone https://github.com/autonomous-ai/openharness.git
cd openharness
git checkout a53351bd1a2c33c2976b7df6869e3666578fdd7d
# Follow upstream docs/development.md (Node 20+, tmux, Flutter, …)
```

For an offline workshop without a key, ask the agent to create an **offline practice** sheet (`"offline": true` in `sheet.json`). Practice answers are not evidence of live model quality. Connecting a key and going live may incur provider charges and sends row text to the chosen API.

## Examples and demos

- Harness ships a made-up Fernhill Cloud sample sheet and documents Question Lab walkthrough media under the harness docs paths cited in its README.
- Upstream package checks (not run on this review host): `JEV_OFFLINE=1 node --test test/*.test.mjs` inside `store/agents/jev-sheets/`.
- Upstream-reported cost/accuracy figures on made-up reviews (for example a 1,200-row sanity check dated 2026-09-20) live in the harness README—treat as vendor measurements, not catalog benchmarks.

## Limits and data handling

Live mode sends row text (and question definitions) to TypeSafe, OpenRouter, or Cloudflare per the connected route; keys stay on the machine except for API calls. The pane restricts uploads to the user’s home folder and same-origin controls. Offline practice and kept Question Lab trials must not be quoted as live Jev quality. Not legal, medical, financial, or hiring advice. OpenHarness as a whole includes many other DSHs; those are out of scope for this page.

## Review and maintenance

Reviewed on **2026-09-24** at [commit a53351bd1a2c33c2976b7df6869e3666578fdd7d](https://github.com/autonomous-ai/openharness/tree/a53351bd1a2c33c2976b7df6869e3666578fdd7d): MIT, ~813★ at review time. AI-assisted inspection of harness README, `harness.json`, `toolchain/jev.mjs`, `viewer/grammar.mjs`, root Beyond-code feature block, and the public desktop download page. **No** OpenHarness install, Flutter build, or live Jev call on the review host.

Related: [jev-table](../tools/jev-table.md), [Jev Column Race](jev-column-race.md).
