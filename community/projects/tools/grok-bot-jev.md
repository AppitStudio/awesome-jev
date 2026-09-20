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

```sh
git clone https://github.com/Bodila51/grok-bot-jev.git
cd grok-bot-jev
git checkout 1583e09928c138aeac0aa89818c67ea41f08e807
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp config.example.yaml config.yaml   # set enabled: false for offline smoke
.venv/bin/python scripts/dry_run.py
```

With `enabled: false`, dry-run prints `proceed_full` / `jev_used: false` without network calls. Live mode needs `TYPESAFE_API_KEY` and sends task metadata to TypeSafe.

## Examples and demos

- [`skill/jev-usage-router.SKILL.md`](https://github.com/Bodila51/grok-bot-jev/blob/1583e09928c138aeac0aa89818c67ea41f08e807/skill/jev-usage-router.SKILL.md)
- Sanitized A/B notes under [`examples/`](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807/examples) (upstream proxy metrics, not catalog benchmarks)
- Media illustrations under [`media/`](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807/media)

## Limits and data handling

Active enforcement depends on the Grok Bot skill honoring actions; the router cannot intercept a bot that ignores it. It does not send, pay, delete, or change permissions without an ask-human path. A/B figures in the README are one local run’s proxies. Keys must stay in the environment (`src/secrets.py` does not read secret files).

## Review and maintenance

Reviewed on **2026-09-20** at [commit 1583e09](https://github.com/Bodila51/grok-bot-jev/tree/1583e09928c138aeac0aa89818c67ea41f08e807): MIT. AI-assisted source review of `jev_client.py`, `router.py`, skill, README, and license. Offline **`scripts/dry_run.py` with `enabled: false`** completed without TypeSafe calls. No live Jev or Grok Bot sessions were run.

Related: [jev-gateway](jev-gateway.md), [super-jev](super-jev.md), [toolgate](toolgate.md).
