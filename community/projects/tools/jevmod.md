# jevmod

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Moderation toolkit powered by TypeSafe Jev: CLI/SDK/HTTP API/MCP plus optional Discord, Telegram, Reddit, Twitch, and YouTube bots with per-category probabilities and thresholds you own.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ohernandezdev/jevmod) |
| Maintainer | [ohernandezdev](https://github.com/ohernandezdev). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package `jevmod` **0.2.1** (CLI, FastAPI, bots, optional MCP); product site [jevmod.dev](https://jevmod.dev). |
| Requirements | Python ≥ 3.10; `TYPESAFE_API_KEY` (or keyring / `.env`). Platform extras for Discord/Telegram/Reddit/etc. |
| License | [MIT](https://github.com/ohernandezdev/jevmod/blob/01063f3e927ddbc3c7de923b73f56dcc33034ca9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Distinct from catalogued Discord [Jev Moderation Bot](../apps/jev-moderation-bot.md) and Telegram [jev_antispam_bot](../apps/jev-antispam-bot.md). Offline pytest: **151 passed**, 3 failed (missing optional modules in this environment), 32 skipped. No live TypeSafe or connected Discord. Upstream benchmark AUROC figures were not re-run. |

## When to use

Use it when you want reusable moderation judgments (spam/scam/harassment/nsfw/off-topic/self-harm/doxxing/minors + plain-English rules) across a CLI, API, MCP, or chat bots. Prefer the simpler Discord-only [Jev Moderation Bot](../apps/jev-moderation-bot.md) for a minimal self-hosted bot. Flag-only defaults; destructive actions are opt-in.

## How it works

Jev answers category Noul questions; application code owns thresholds and actions (`off` / `flag` / `delete` / `timeout`). Fails open if Jev is unreachable. Self-harm stays flag-only by design. Bots can tune thresholds from log reactions. MCP and Claude Code skill paths help agents wire jevmod into apps.

## Get started

```sh
pip install "jevmod[keys]"
jevmod init   # stores a verified key in the OS keyring
jevmod check "FREE NITRO for the first 100!! claim at discord-gifts.ru/nitro"
```

From source (offline subset):

```sh
git clone https://github.com/ohernandezdev/jevmod.git
cd jevmod
git checkout 01063f3e927ddbc3c7de923b73f56dcc33034ca9
pip install -e ".[dev]"
pytest tests/ -q
```

Live checks send message text to TypeSafe and may incur charges (~vendor-stated $0.04 / 1k messages with all categories—verify current pricing).

## Examples and demos

- CLI `jevmod check` sample in README; terminal GIF on upstream docs.
- Discord/Telegram/Reddit setup sections; developer HTTP API and MCP.
- Offline unit tests for judge/CLI/budget/API paths.

## Limits and data handling

Message text goes to TypeSafe on live classification. Bot delete/timeout actions can affect real communities—start with flag-only. Keyring/`.env` handling is documented; never commit keys. Benchmark comparisons are upstream research—read BENCHMARK.md caveats.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 01063f3](https://github.com/ohernandezdev/jevmod/tree/01063f3e927ddbc3c7de923b73f56dcc33034ca9): **0.2.1**, MIT. AI-assisted review of README, `pyproject.toml`, LICENSE, and tests. Offline pytest: **151 passed** / 3 failed / 32 skipped in this environment. No live TypeSafe.

Related: [Jev Moderation Bot](../apps/jev-moderation-bot.md), [jev_antispam_bot](../apps/jev-antispam-bot.md), [jev-shield](jev-shield.md).
