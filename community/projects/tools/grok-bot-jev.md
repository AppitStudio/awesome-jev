# Grok Bot Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reference Python router and skill that put TypeSafe Jev in front of Grok Bot expensive work: reuse cache, stop retry, cap research, allow subagent, or ask a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bodila51/grok-bot-jev) |
| Maintainer | [Bodila51](https://github.com/Bodila51). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package with `src/` router, `skill/jev-usage-router.SKILL.md`, config example, and dry-run scripts. |
| Requirements | Python 3 with `typesafe-sdk` + PyYAML (see `requirements.txt`); `TYPESAFE_API_KEY` in the environment; Grok Bot skill install for active mode. |
| License | [MIT](https://github.com/Bodila51/grok-bot-jev/blob/1583e09928c138aeac0aa89818c67ea41f08e807/LICENSE). |

## When to use

Use it as a small, inspectable pattern for gating research/browser/retry/subagent work with Jev before a larger agent spends tokens. It does not replace Grok Bot’s foundation model or Cursor routing. Prefer [jev-gateway](jev-gateway.md) or [super-jev](super-jev.md) for broader coding-agent harnesses.

## How it works

[`src/jev_client.py`](https://github.com/Bodila51/grok-bot-jev/blob/1583e09928c138aeac0aa89818c67ea41f08e807/src/jev_client.py) wraps `typesafe_sdk.TypeSafeClient.system_one`. [`src/router.py`](https://github.com/Bodila51/grok-bot-jev/blob/1583e09928c138aeac0aa89818c67ea41f08e807/src/router.py) builds Choice/Noul/Score questions and returns an explicit action. `shadow` mode logs advice; `active` mode requires the pasted skill to honor `route.action`. Kill switches: `enabled: false` or a `bypass jev` marker.

## Get started

Installation downloads dependencies. The following explicitly disables Jev before running the synthetic smoke cases and writes a local `config.yaml` in the fresh checkout:

```sh
git clone https://github.com/Bodila51/grok-bot-jev.git
cd grok-bot-jev
git checkout 1583e09928c138aeac0aa89818c67ea41f08e807
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python - <<'PYTHON'
from pathlib import Path
import yaml
config = yaml.safe_load(Path("config.example.yaml").read_text())
config["enabled"] = False
Path("config.yaml").write_text(yaml.safe_dump(config))
PYTHON
.venv/bin/python scripts/dry_run.py
```

With `enabled: false`, dry-run prints `proceed_full` / `jev_used: false` without network calls. To opt into live calls, set `enabled: true` in `config.yaml` and provide `TYPESAFE_API_KEY` in the environment. The same dry-run script then processes five sample states through Jev and may incur provider charges. `mode: shadow` makes decisions advisory; it does not disable inference.

## Examples and demos

- [`skill/jev-usage-router.SKILL.md`](https://github.com/Bodila51/grok-bot-jev/blob/1583e09928c138aeac0aa89818c67ea41f08e807/skill/jev-usage-router.SKILL.md)
- Sanitized A/B notes under [`examples/`](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807/examples) (upstream proxy metrics, not catalog benchmarks)
- Media illustrations under [`media/`](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807/media)

## Limits and data handling

Active enforcement depends on the Grok Bot skill honoring actions; the router executes none of the suggested downstream work. `ask_human` depends on a model-selected account intent, and cache-reuse and retry-stop branches take precedence. Bypass markers in goal/message/notes fields skip Jev and return `proceed_full`. These are workflow controls, not permission checks; the host must independently enforce authorization for all actions.

Disabled and bypassed runs return `proceed_full`. Provider errors, malformed state, and missing answers are not caught by the router; the host integration must implement the documented fallback. The code does not add complete probability validation or a general abstention state. The SDK dependencies are unpinned, and live compatibility was not tested.

TypeSafe receives the goal, task hint, cache note, prior error, counters, and constraints. Local `logs/runs.jsonl` records goals and selected decision details without redaction; the disabled path records the supplied goal without the live path's 300-character truncation. Logs omit complete raw SDK responses. Do not include credentials or sensitive task text in these fields. Keys are read from `TYPESAFE_API_KEY`, not secret files, and local config/logs should stay uncommitted.

A/B figures are upstream proxy measurements from one local run, not independently reproduced savings or quality results. The supplied media are labeled visualizations. No Grok Bot session or model-performance evaluation was performed for this listing.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 1583e09](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807): MIT. AI-assisted source review of `jev_client.py`, `router.py`, skill, README, and license. Offline **`scripts/dry_run.py` with `enabled: false`** completed without TypeSafe calls. No live Jev or Grok Bot sessions were run. A follow-up on the same date verified the executable offline setup in a separate checkout with a credential-free environment, Python 3.12.14, `typesafe-sdk` 0.7.0, and PyYAML 6.0.3: `python -m compileall -q src scripts` passed, and all five disabled smoke cases returned `proceed_full` with `jev_used: false`. This checks imports and the disabled path, not model-driven routing or active enforcement.

Related: [jev-gateway](jev-gateway.md), [super-jev](super-jev.md), [toolgate](toolgate.md).
