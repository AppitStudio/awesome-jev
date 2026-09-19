# jev-codex-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Per-turn Codex model and reasoning routing through a local server that asks Jev to pick a tier, then relays Responses traffic through an existing Codex Router install.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/0xNatoshi/jev-codex-router) |
| Maintainer | [0xNatoshi](https://github.com/0xNatoshi) (Thibault Saint-Jean). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python local HTTP server (`server/jev_server.py`) plus Codex Router generic-provider registration; optional hook/PoC and backtest tools. **Upstream repository is archived** on GitHub as of this review (still publicly readable under MIT). |
| Requirements | macOS-oriented Codex desktop setup with a working [Codex Router](https://github.com/0xNatoshi/jev-codex-router#quickstart) checkout (`bin/codex-router`), Python 3.11+, and `TYPESAFE_API_KEY` (default env file `~/.hermes/.env`). Offline source inspection needs no account. |
| License | [MIT](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/LICENSE). ChatGPT / OpenCode tandem usage and TypeSafe inference have separate account and cost requirements. |

## When to use

Use it when Codex already runs through Codex Router and you want each turn (including tool-step continuations) classified by Jev so mechanical work can stay on cheaper tiers while hard steps keep a frontier model. Prefer a simpler fixed model when you do not want a local classification server or Codex Router dependency. Because the upstream repo is archived, expect no further upstream fixes unless the author un-archives or publishes a successor.

It is distinct from catalogued [jev-router](jev-router.md) (CLI launchers/proxies for Claude Code and Codex) and [Jev Model Router](jev-model-router.md) (Claude Code function-hook mod): this project plugs into Codex Router's generic provider and curated `jev/auto` model rather than wrapping the CLI itself.

## How it works

```text
Codex → Codex Router (:4202)
          └─ "jev/auto" → local jev_server.py (:4319)
                → Jev classifies tier + thinking depth
                → policy picks luna / sol / astra (or Codex-dry tandem)
                → relay Responses SSE via the router caller edge
```

The [server](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/server/jev_server.py) posts to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. Default policy maps mechanical work to `gpt-5.6-luna` (max thinking, priority), standard work to `gpt-5.6-sol`, and hard/ambiguous work to `gpt-6-astra`. Confidence below `0.5` holds to the middle tier rather than downgrading further. Failures fall open to astra; a kill-switch file skips Jev entirely. When native ChatGPT usage is exhausted, an optional tandem substitutes OpenCode GLM/DeepSeek flash models. Decisions are logged under `~/.codex/codex-router/jev-router-live.jsonl`.

Upstream [BACKTEST.md](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/BACKTEST.md) reports measured savings on a replay protocol; those figures are upstream research, not catalog-verified quality or cost guarantees.

## Get started

**Setup clones source and starts a local server; live routing needs a TypeSafe key and an existing Codex Router session.**

```sh
git clone https://github.com/0xNatoshi/jev-codex-router.git
cd jev-codex-router
git checkout 8292b519659280884627a962c826ac7721136a64
# provide TYPESAFE_API_KEY via the environment or ~/.hermes/.env
python3 server/jev_server.py
curl -s http://127.0.0.1:4319/health
```

Then register the generic provider and curated model with your Codex Router checkout as documented in the upstream [Quickstart](https://github.com/0xNatoshi/jev-codex-router#quickstart) and [AGENTS.md](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/AGENTS.md). Live turns send prompt/tool digests to TypeSafe and model traffic to the ChatGPT (or tandem) backends; provider charges or subscription limits can apply.

## Examples and demos

- [BACKTEST.md](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/BACKTEST.md) and `poc/` replay tools document the savings protocol and sample JSON; not re-run for this listing.
- [CI workflow](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/.github/workflows/ci.yml) is present; this catalog review did not execute it.
- No separate automated unit-test suite was found in the reviewed tree.

## Limits and data handling

Jev receives turn/tool digests as constructed by the server (including tool-output digests for continuations). Full coding traffic still flows through Codex Router and the selected backend. Thresholds and reported savings are operational/policy research, not independently validated accuracy. The Codex-dry tandem and native model IDs can change with provider availability. macOS + Codex Router prerequisites were not reproduced on the Linux review host.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 8292b51](https://github.com/0xNatoshi/jev-codex-router/tree/8292b519659280884627a962c826ac7721136a64): MIT. Upstream GitHub repository is **archived** (read-only); listing remains for discoverability of the last reviewed revision. AI-assisted source review of `server/jev_server.py`, README, BACKTEST notes, license, and repository layout. No automated offline test suite was run; no live TypeSafe calls, Codex Router install, or end-to-end routing session were performed.

Related: [jev-router](jev-router.md), [Jev Model Router](jev-model-router.md).
