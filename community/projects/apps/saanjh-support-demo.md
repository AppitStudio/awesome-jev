# Saanjh Clothing support demo by Swastik Methi (store support bot where Jev checks every drafted reply before it is sent)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A support bot for a fictional fashion store: customers can track an order, check a refund, cancel, return or report an undelivered package. Rules draft routine replies from order records, Jev scores every draft before it is sent, a fallback LLM gets one attempt when there is no draft or Jev rejects it, and anything that cannot be verified becomes a ticket. Cancellations and returns run only after the customer confirms.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SwastikMethi/JEV-LLM) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/SwastikMethi/JEV-LLM#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build that you run locally with your own TypeSafe key and a local Ollama model. No license file, so reuse terms are not granted. Checked 2026-11-23. |
| Jev evidence | [`app/jev.py`](https://github.com/SwastikMethi/JEV-LLM/blob/b06f762653ede6576678480e3bdd2895ece0b9c5/app/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [SwastikMethi](https://github.com/SwastikMethi). Independently curated. |
| Format | Python web app (FastAPI) |
| Platform and availability | Web app (FastAPI) run locally on port 7860; Docker/Hugging Face Space-style config included. |
| Jev's role | The send gate: Jev scores each draft for whether it is supported, complete and needs a human; cutoffs, the pinned model and question wording live in `data/gate.json`. A Jev timeout or malformed answer opens a ticket instead of sending. |
| Requirements | Python 3.13, Ollama with `qwen3.5:9b` (or any OpenAI-compatible endpoint) for the fallback, and a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- See a fail-closed pattern where a decision model gates every customer-facing reply.
- Mismatch: a production helpdesk; all customers, orders and policies are fictional.

## How it works

`app/jev.py` posts to `https://api.typesafe.ai/v1/systemone` (host overridable with `TYPESAFE_BASE_URL`) with a 5-second timeout; `app/router.py` follows a six-step routing contract and `evaluation/run.py` scores the gate on labelled cases. Integration evidence: [`app/jev.py`](https://github.com/SwastikMethi/JEV-LLM/blob/b06f762653ede6576678480e3bdd2895ece0b9c5/app/jev.py).

## Get started

Create a virtualenv, add your TypeSafe key and start the app; a stub server lets you click through the flows without a key.

```sh
git clone https://github.com/SwastikMethi/JEV-LLM && cd JEV-LLM
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
echo 'TYPESAFE_API_KEY=your-key' > .env
set -a; . ./.env; set +a
.venv/bin/python -m uvicorn app.main:app --port 7860
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gate config: [github.com/SwastikMethi/JEV-LLM/blob/b06f762653ede6576678480e3bdd2895ece0b9c5/data/gate.json](https://github.com/SwastikMethi/JEV-LLM/blob/b06f762653ede6576678480e3bdd2895ece0b9c5/data/gate.json)
- Observed evaluation: [github.com/SwastikMethi/JEV-LLM/tree/b06f762653ede6576678480e3bdd2895ece0b9c5/evaluation/observed](https://github.com/SwastikMethi/JEV-LLM/tree/b06f762653ede6576678480e3bdd2895ece0b9c5/evaluation/observed)

## Limits and data handling

Customer messages and drafted replies go to TypeSafe for scoring and to the fallback LLM you configure. Demo limits: 30 messages per session, 500 characters per message. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit b06f762653ed](https://github.com/SwastikMethi/JEV-LLM/tree/b06f762653ede6576678480e3bdd2895ece0b9c5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
