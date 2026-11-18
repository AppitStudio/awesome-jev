# Dealflow Triage by Honey Chawla (local read-only inbox for Instagram DMs, Gmail, Proton Mail and LinkedIn, sorted by Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

One local inbox for Instagram DMs, Gmail, Proton Mail and LinkedIn messages that only reads (never sends or changes anything). For each conversation Jev answers nine typed questions (category, real opportunity, deal value, sender credibility, urgency, written for you, reply expected, states terms, scam risk), which become a category such as Brand deal or Vendor pitch, a 0–100 score, a priority and a Needs review flag when Jev was unsure. The rubric is editable in Settings. Python standard library only, one SQLite file.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/honeyychawla/Dealflow) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/honeyychawla/Dealflow#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-18. |
| Jev evidence | [`dealflow/triage/jev.py`](https://github.com/honeyychawla/Dealflow/blob/4d0980a808660600f43d302a5ee86c84a3988c8b/dealflow/triage/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [honeyychawla](https://github.com/honeyychawla). Independently curated. |
| Format | Local Python web app (standard library, SQLite) (MIT) |
| Platform and availability | Self-hosted local web app (`http://127.0.0.1:4747`); no hosted instance |
| Jev's role | Classifies and scores every conversation with nine typed questions in one request; uncertain calls are flagged for review instead of filed silently. |
| Requirements | Python 3.11+, an OpenRouter key for Jev (keyword sorting until one is saved), and your own Instagram token, Google OAuth client or IMAP app password, Proton Bridge, or LinkedIn browser sign-in for each channel. |
| License | [MIT](https://github.com/honeyychawla/Dealflow/blob/4d0980a808660600f43d302a5ee86c84a3988c8b/LICENSE) |

## When to use

- Find the brand deals, leads and partner messages worth answering across several inboxes.
- Mismatch: a shared team inbox or a tool that replies for you; it is single-user and read-only.

## How it works

`dealflow/triage/jev.py` posts the conversation and questions to OpenRouter's Decisions API (`/api/alpha/decisions`) with `typesafe/jev-1.14`; `dealflow/triage/engine.py` turns the answers into category, score and priority. Integration evidence: [`dealflow/triage/jev.py`](https://github.com/honeyychawla/Dealflow/blob/4d0980a808660600f43d302a5ee86c84a3988c8b/dealflow/triage/jev.py).

## Get started

Run the launcher, open Settings, add your OpenRouter key and the channels you use, or load the sample conversations first.

```sh
git clone https://github.com/honeyychawla/Dealflow && cd Dealflow
./dealflow.sh    # then open http://127.0.0.1:4747 and go to Settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/honeyychawla/Dealflow/blob/4d0980a808660600f43d302a5ee86c84a3988c8b/README.md](https://github.com/honeyychawla/Dealflow/blob/4d0980a808660600f43d302a5ee86c84a3988c8b/README.md)

## Limits and data handling

Message text is sent to OpenRouter/TypeSafe for sorting; newsletters and automated mail are filed as Noise without a call. Keys, tokens and the message database stay in `.env` and `data/` on your machine. The per-conversation cost in the README is the author's estimate.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 4d0980a80866](https://github.com/honeyychawla/Dealflow/tree/4d0980a808660600f43d302a5ee86c84a3988c8b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
