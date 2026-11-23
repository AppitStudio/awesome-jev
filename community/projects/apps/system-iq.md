# System IQ by Harsh Tomar (CLI that turns a project idea into a system design, with Jev making the bounded architecture choices and checking the result)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Send an idea from the command line to a small FastAPI backend: an LLM extracts the requirements, Jev decides API style, database, architecture, caching, async work and scaling as probabilities, the LLM writes a 13-section design around those decisions, and Jev then asks validation questions about the finished design. No application code is generated.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TFD666/system-iq) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://system-iq.onrender.com) |
| Pricing and access | Free source build with your own Groq and OpenCode keys. The author also runs a hosted demo on free tiers that needs an access code from the project page and has daily limits (author statement; not used for this review). No license file, so reuse terms are not granted. Checked 2026-11-23. |
| Jev evidence | [`backend/app/decision/provider.py`](https://github.com/TFD666/system-iq/blob/896e3a0c345c1666ddd32f328d3d856eb2e6e020/backend/app/decision/provider.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [TFD666](https://github.com/TFD666). Independently curated. |
| Format | Python CLI + FastAPI backend |
| Platform and availability | Python CLI with a FastAPI backend (local or the author's hosted demo). |
| Jev's role | Jev answers Choice and Noul questions for each architecture decision and for validation of the written design; the LLM writes the text. |
| Requirements | Python 3.10+; a Groq API key and an OpenCode account (for its free Jev endpoint) to run locally. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Get a first-draft system design where the key choices are explicit, repeatable decisions.
- Mismatch: better designs than an LLM alone; the author's pre-registered test found no clear quality difference once the writing voice was matched.

## How it works

`backend/app/decision/provider.py` posts to `https://opencode.ai/inference/systemone/v1/systemone` with `OPENCODE_API_KEY`; `JEV_MODEL` and `JEV_BASE_URL` are configurable. Integration evidence: [`backend/app/decision/provider.py`](https://github.com/TFD666/system-iq/blob/896e3a0c345c1666ddd32f328d3d856eb2e6e020/backend/app/decision/provider.py).

## Get started

Run the backend locally and point the CLI at it (by default the CLI talks to the hosted demo).

```sh
git clone https://github.com/TFD666/system-iq && cd system-iq
pip install -r requirements-dev.txt
cd backend && uvicorn app.main:app   # backend/.env: GROQ_API_KEY, OPENCODE_API_KEY, JEV_MODEL, JEV_BASE_URL
export SYSTEMIQ_API_URL=http://localhost:8000
python cli/systemiq.py "A web app for a small clinic where patients book appointments online"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example design: [github.com/TFD666/system-iq/blob/896e3a0c345c1666ddd32f328d3d856eb2e6e020/docs/example_design_clinic.md](https://github.com/TFD666/system-iq/blob/896e3a0c345c1666ddd32f328d3d856eb2e6e020/docs/example_design_clinic.md)
- Evaluation findings: [github.com/TFD666/system-iq/blob/896e3a0c345c1666ddd32f328d3d856eb2e6e020/eval/FINDINGS.md](https://github.com/TFD666/system-iq/blob/896e3a0c345c1666ddd32f328d3d856eb2e6e020/eval/FINDINGS.md)

## Limits and data handling

Ideas are sent to Groq and OpenCode (both US); the README says OpenCode's free tier may use submitted text to improve its service. The evaluation is six ideas rated by the author. No license file.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 896e3a0c345c](https://github.com/TFD666/system-iq/tree/896e3a0c345c1666ddd32f328d3d856eb2e6e020). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
