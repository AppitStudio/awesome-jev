# Regret Check

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that pauses you before commit-like clicks you might regret: a local server scores the page action with TypeSafe Jev (via OpenRouter) and can hold or release the click.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danilocecilia/sleep-on-it) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [sleep-on-it repository](https://github.com/danilocecilia/sleep-on-it) — source-run; no separate product site. |
| Pricing and access | MIT source; no app purchase fee, checked **2026-09-23**. Requires a self-hosted Python server and an OpenRouter key exposed to the server as `TYPESAFE_API_KEY` (`sk-or-…`). Extension must not hold the key. Provider usage billed separately. |
| Jev evidence | Inspected [`main.py`](https://github.com/danilocecilia/sleep-on-it/blob/a074e113cd701fce71f690bafecaac8fd05c83dd/main.py): `AsyncTypeSafeClient` asks regret Noul, kind Choice, and impulse/heat/exposure Scores; background script pauses when regret ≥ threshold. Live Chrome/OpenRouter path not run here. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Experimental (Gmail path noted upstream). Source inspected; extension load and live scoring were **not** executed on the review host. |
| Maintainer | [danilocecilia](https://github.com/danilocecilia). |
| Format | Chrome extension (`extension/`) + FastAPI server (`main.py`). |
| Platform and availability | Chromium via Load unpacked; local server on port **8001**. Early source prototype. |
| Jev's role | Scores whether the click is likely regretted and classifies commitment kind/impulse/heat/exposure. Code owns pause UI, alarms, and click release. |
| Requirements | Python **3.14** per README, `pip install -r requirements.txt`, OpenRouter key in `.env`, Chrome Developer mode. |
| License | [MIT](https://github.com/danilocecilia/sleep-on-it/blob/a074e113cd701fce71f690bafecaac8fd05c83dd/LICENSE). |

## When to use

Use it to **study a regret-gated click interceptor** with calibrated Jev scores and a later yes/no follow-up for calibration charts. Prefer [Focus](focus.md) for domain productivity blocking, or [Tab Bouncer](tab-bouncer.md) for task-tab ranking.

## How it works

Content script captures commit-like clicks and page state; the extension background POSTs to the local server; [`main.py`](https://github.com/danilocecilia/sleep-on-it/blob/a074e113cd701fce71f690bafecaac8fd05c83dd/main.py) calls Jev through OpenRouter Decisions (`typesafe_sdk`). High regret shows a pause card (Hold 10 minutes / Continue anyway). Draft text and page info reach your server, OpenRouter, and TypeSafe.

## Get started

```sh
git clone https://github.com/danilocecilia/sleep-on-it.git
cd sleep-on-it
git checkout a074e113cd701fce71f690bafecaac8fd05c83dd
pip install -r requirements.txt
# .env: TYPESAFE_API_KEY=sk-or-…  (OpenRouter; SDK still uses TYPESAFE_* names)
python -m uvicorn main:app --port 8001
# Chrome → Extensions → Load unpacked → extension/
```

## Examples and demos

- Calibration chart at `http://localhost:8001/calibration`.
- Upstream notes Gmail Send end-to-end testing; checkouts/iframes may ignore synthetic `click()`.

## Limits and data handling

Drafts and page metadata leave the browser for your server and providers. Keep keys only on the server. Synthetic clicks set `isTrusted=false`. EN/PT/FR label heuristics; Enter submits not covered. Experimental.

## Review and maintenance

Reviewed on **2026-09-23** at [commit a074e11](https://github.com/danilocecilia/sleep-on-it/tree/a074e113cd701fce71f690bafecaac8fd05c83dd) (MIT). AI-assisted review of README, LICENSE, `main.py`. No Chrome/live run.

Related: [Focus](focus.md), [Tab Bouncer](tab-bouncer.md), [HookMeter](hookmeter.md).
