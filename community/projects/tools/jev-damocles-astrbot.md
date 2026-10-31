# JEV Damocles for AstrBot (group-chat plugin where Jev decides whether the bot should speak)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AstrBot plugin (Chinese) that hands the 'should the bot reply to this group message?' decision to a Jev / System One decision model plus an explicit group-chat state machine: messages are normalized, grouped into topic threads and merge windows, then asked in one multi-question call and thresholded before the LLM is allowed to answer. Distinct from the AizenvoltPrime Damocles listing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ch7flyer/astrbot_plugin_jev_damocles) |
| Maintainer | [ch7flyer](https://github.com/ch7flyer). Independently curated. |
| Format | Python · AstrBot plugin |
| Requirements | AstrBot; a System One backend (TypeSafe, TokenPlan, Venice, Abacus and others; default TokenPlan) and model `jev-latest`; WeChat needs `astrbot_plugin_qianxun`. |
| License | [MIT](https://github.com/ch7flyer/astrbot_plugin_jev_damocles/blob/4ac9c8ea3351ab9b8d32d074c903d01b0d4c52bf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/jev.py`](https://github.com/ch7flyer/astrbot_plugin_jev_damocles/blob/4ac9c8ea3351ab9b8d32d074c903d01b0d4c52bf/core/jev.py) at the pinned commit. |

## When to use

- Keep a group bot from replying to everything while still answering when addressed or useful.
- Mismatch: run with `dry_run = true` for days first, as the README advises.

## How it works

`core/jev.py` sends every question for a merge window in one `POST /v1/systemone` request (configurable path, `jev-latest` by default) and the plugin compares the probabilities with per-mode thresholds before calling `request_llm` with injected group state. Integration evidence: [`core/jev.py`](https://github.com/ch7flyer/astrbot_plugin_jev_damocles/blob/4ac9c8ea3351ab9b8d32d074c903d01b0d4c52bf/core/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
# AstrBot plugin market: search for 'JEV 达摩克利斯之剑', or copy into data/plugins/
# configure bot_names and the JEV backend; keep dry_run = true for 3-7 days
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/ch7flyer/astrbot_plugin_jev_damocles#readme](https://github.com/ch7flyer/astrbot_plugin_jev_damocles#readme)

## Limits and data handling

Group messages in each window are sent to the configured System One provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 4ac9c8ea3351](https://github.com/ch7flyer/astrbot_plugin_jev_damocles/tree/4ac9c8ea3351ab9b8d32d074c903d01b0d4c52bf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
