# IT Support Ticket Analyzer (Streamlit dashboard where Jev returns a ticket's category and urgency with probabilities)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Streamlit app: paste an IT support ticket and Jev answers two questions in one call — the issue type (network, hardware, software, account, other) and an urgency score from 0 to 3 — shown as summary cards, probability charts and a probability-weighted urgency score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV) |
| Maintainer | [dhanushkapg](https://github.com/dhanushkapg). Independently curated. |
| Format | Python Streamlit app |
| Requirements | Python 3, `streamlit`, `typesafe-sdk`, `python-dotenv` and a `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`IT_Ticket_Classifier.py`](https://github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV/blob/8337ccd1bb7ea7cf7d909e8386d687c24eee5313/IT_Ticket_Classifier.py) at the pinned commit. |

## When to use

- A minimal, readable example of Choice plus Score triage on one request.
- Mismatch: a help-desk integration; it is a single-ticket demo with fixed categories.

## How it works

`IT_Ticket_Classifier.py` uses `TypeSafeClient` from `typesafe_sdk` with a `Choice` question for the category and a `Score` question for urgency, reading `TYPESAFE_API_KEY` from the environment. Integration evidence: [`IT_Ticket_Classifier.py`](https://github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV/blob/8337ccd1bb7ea7cf7d909e8386d687c24eee5313/IT_Ticket_Classifier.py).

## Get started

Install the three packages, set your key, run the app.

```sh
git clone https://github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV && cd IT-Ticket-Analyzer-using-JEV
pip install streamlit typesafe-sdk python-dotenv
echo 'TYPESAFE_API_KEY=...' > .env
streamlit run app.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV/blob/8337ccd1bb7ea7cf7d909e8386d687c24eee5313/README.md](https://github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV/blob/8337ccd1bb7ea7cf7d909e8386d687c24eee5313/README.md)

## Limits and data handling

Ticket text is sent to TypeSafe on your key. Categories are fixed in code. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 8337ccd1bb7e](https://github.com/dhanushkapg/IT-Ticket-Analyzer-using-JEV/tree/8337ccd1bb7ea7cf7d909e8386d687c24eee5313). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
