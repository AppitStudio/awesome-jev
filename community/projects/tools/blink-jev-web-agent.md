# Blink (multi-site research web agent where an LLM plans parallel browser branches and Jev drives each step from screenshots)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Jevathon web agent: an LLM turns a goal into independent branches that run in parallel Chromium tabs, and Jev decides every step from screenshots — the page state (choice), where the element is (box) and whether the action worked (yes/no). The LLM returns only to extract values from crops, recover from failures and write the answer. It pauses on CAPTCHAs and logins and hard-stops on payments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Saadtamari/blink-jev-agent) |
| Maintainer | [Saadtamari](https://github.com/Saadtamari). Independently curated. |
| Format | Python FastAPI backend with Playwright and a Next.js frontend |
| Requirements | Python 3.12 via uv, Node 20+, Playwright Chromium, and one OpenRouter key for both Jev and the LLM. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`backend/app/clients/jev_client.py`](https://github.com/Saadtamari/blink-jev-agent/blob/7ea2f41fdc1367e95528f16183bcd56811dbf1ea/backend/app/clients/jev_client.py) at the pinned commit. |

## When to use

- Research tasks that span several websites, where per-step screenshot decisions dominate cost.
- Mismatch: logged-in or payment flows; Blink hands those to you or stops.

## How it works

`backend/app/clients/jev_client.py` sends screenshots and typed questions to the OpenRouter Decisions API (`/api/alpha/decisions`) with model `typesafe/jev-1.14`; `scripts/jev_smoke.py` checks which endpoint and image mode work. Integration evidence: [`backend/app/clients/jev_client.py`](https://github.com/Saadtamari/blink-jev-agent/blob/7ea2f41fdc1367e95528f16183bcd56811dbf1ea/backend/app/clients/jev_client.py).

## Get started

Install backend and frontend, check Jev with the smoke script, then run both.

```sh
git clone https://github.com/Saadtamari/blink-jev-agent && cd blink-jev-agent/backend
uv venv --python 3.12 .venv && uv pip install --python .venv -r requirements.txt
.venv/bin/python -m playwright install chromium
cp .env.example .env   # OpenRouter key
.venv/bin/python scripts/jev_smoke.py
.venv/bin/python serve.py   # then: cd ../frontend && npm install && npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Saadtamari/blink-jev-agent/blob/7ea2f41fdc1367e95528f16183bcd56811dbf1ea/README.md](https://github.com/Saadtamari/blink-jev-agent/blob/7ea2f41fdc1367e95528f16183bcd56811dbf1ea/README.md)
- Demo notes: [github.com/Saadtamari/blink-jev-agent/blob/7ea2f41fdc1367e95528f16183bcd56811dbf1ea/DEMO.md](https://github.com/Saadtamari/blink-jev-agent/blob/7ea2f41fdc1367e95528f16183bcd56811dbf1ea/DEMO.md)

## Limits and data handling

Screenshots of the pages it visits go to OpenRouter on your key. The maintainer's benchmark is six live tasks on one machine. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 7ea2f41fdc13](https://github.com/Saadtamari/blink-jev-agent/tree/7ea2f41fdc1367e95528f16183bcd56811dbf1ea). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
