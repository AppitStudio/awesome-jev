# Year-end Award Approval Agent (Korean LangGraph demo where Jev screens AI-written awards)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Korean LangGraph + Streamlit demo: colleagues nominate peers, gpt-5-nano writes the award text, and Jev scores embarrassment, privacy exposure and tone so only risky awards wait for a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rome777/award-hitl) |
| Maintainer | [rome777](https://github.com/rome777). Independently curated. |
| Format | Python demo (no license file) |
| Requirements | Python, an OpenAI key, and optionally `TYPESAFE_API_KEY` (falls back to gpt-5-nano or keywords). |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`judge.py`](https://github.com/rome777/award-hitl/blob/b16a5ef59c81033ab16194003ec76d8980ea4417/judge.py) at the pinned commit. |

## When to use

- See a human-in-the-loop gate driven by Jev scores.
- Reuse the LangGraph interrupt/resume pattern.
- Mismatch: no license file; ask the author before reuse.

## How it works

`judge.py` asks Jev for embarrassment/offence and privacy probabilities plus a tone judgment; LangGraph `interrupt` pauses flagged awards for the organizer. Integration evidence: [`judge.py`](https://github.com/rome777/award-hitl/blob/b16a5ef59c81033ab16194003ec76d8980ea4417/judge.py).

## Get started

Clone, fill `.env` from `.env.example`, install requirements and run the Streamlit app per GUIDE.md.

```sh
git clone https://github.com/rome777/award-hitl.git && cd award-hitl
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/rome777/award-hitl/blob/b16a5ef59c81033ab16194003ec76d8980ea4417/README.md](https://github.com/rome777/award-hitl/blob/b16a5ef59c81033ab16194003ec76d8980ea4417/README.md)

## Limits and data handling

Nominations and generated text go to OpenAI and TypeSafe on your keys.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit b16a5ef59c81](https://github.com/rome777/award-hitl/tree/b16a5ef59c81033ab16194003ec76d8980ea4417). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
