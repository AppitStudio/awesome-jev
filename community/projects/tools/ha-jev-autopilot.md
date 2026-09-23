# HA Jev Autopilot

[All projects](../README.md) · [Home automation](README.md#home-automation)

Home Assistant integration: TypeSafe Jev decides what each room needs; deterministic code acts, with phone confirmation for risky devices—distinct from [HA-Jev](ha-jev.md) sensors/services.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davidzha712/ha-jev-autopilot) |
| Maintainer | [davidzha712](https://github.com/davidzha712). Independently curated. Not an endorsement. |
| Format | Home Assistant custom integration (HACS) `jev_autopilot`. |
| Requirements | Home Assistant 2026.9+; TypeSafe API key; rooms/devices configured. |
| License | [MIT](https://github.com/davidzha712/ha-jev-autopilot/blob/732f5d5e3ebbc9da529e6a08f66ecd996e7ec394/LICENSE). TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Live HA/Jev **not** run. Distinct from [AboveColin/HA-Jev](ha-jev.md). |

## When to use

Use it when HA should autopilot lights/climate/media per room from batched Jev answers with “ask first” for locks and high-risk outlets. Prefer [HA-Jev](ha-jev.md) when you want judgment sensors and services you wire yourself.

## How it works

Per room, the integration builds a scrubbed state (names redacted) and asks typed questions (on/off, brightness, etc.). Code applies thresholds, cooldowns, and manual-override holds. Ask-first devices notify the phone with Run/Skip; locks only propose lock, never unlock.

## Get started

HACS custom repository `https://github.com/davidzha712/ha-jev-autopilot`, or copy `custom_components/jev_autopilot` from [commit 732f5d5](https://github.com/davidzha712/ha-jev-autopilot/tree/732f5d5e3ebbc9da529e6a08f66ecd996e7ec394), then restart HA and configure.

## Examples and demos

- Upstream README behavior list and Chinese README.
- GitHub Actions tests badge (not re-run here).

## Limits and data handling

Device names/states/sensor values go to TypeSafe after redaction rules; imperfect redaction is documented. Push notifications use Apple/Google via the HA mobile app. Budget and fail-open hand back prior automations per README.

## Review and maintenance

Reviewed **2026-09-23** at [commit 732f5d5](https://github.com/davidzha712/ha-jev-autopilot/tree/732f5d5e3ebbc9da529e6a08f66ecd996e7ec394) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [ha-jev](ha-jev.md).
