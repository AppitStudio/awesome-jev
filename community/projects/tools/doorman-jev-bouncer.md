# Doorman (work-ping attention filter where Jev judges each Slack, email, calendar and CI event and plain code decides to interrupt, batch, delegate or drop)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Local web app that turns Slack DMs, emails, calendar changes and failed CI runs into events; Jev answers a few small judgments about each one, fixed rules decide whether it interrupts you, and an LLM only writes auto-replies, CI explanations and the evening digest. Ships on fictional demo data with an optional real Google connection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/farahabuhmaidan/jev-bouncer) |
| Maintainer | [farahabuhmaidan](https://github.com/farahabuhmaidan). Independently curated. |
| Format | Python pipeline and FastAPI server with a React frontend (MIT) |
| Requirements | Python 3, Node.js and make; an OpenRouter key for live Jev and LLM calls (the demo and `make eval` replay cached results with no network). |
| License | [MIT](https://github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/jev.py`](https://github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/pipeline/jev.py) at the pinned commit. |

## When to use

- Prototype an interruption filter that decides which work pings deserve your attention now.
- Mismatch: a production inbox tool; data is fictional by default and the real Google connection is a demo setup.

## How it works

`pipeline/jev.py` posts each event to the OpenRouter Decisions endpoint (`/api/alpha/decisions`) with model `typesafe/jev-1.14`; the policy code in `server/` turns the probabilities into interrupt, batch, delegate or drop. Integration evidence: [`pipeline/jev.py`](https://github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/pipeline/jev.py).

## Get started

Install, then serve the app on the bundled demo data.

```sh
git clone https://github.com/farahabuhmaidan/jev-bouncer && cd jev-bouncer
make install
make app      # http://localhost:8000 on demo data
make pipeline # live Jev + LLM calls (needs the OpenRouter key)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/README.md](https://github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/README.md)
- Slides: [github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/slides/index.html](https://github.com/farahabuhmaidan/jev-bouncer/blob/ea60f169f997b44cede5c87f2068ab4af26462a6/slides/index.html)

## Limits and data handling

Live runs send event text to OpenRouter (Jev and an LLM) on your key. The published numbers come from one day of fictional labelled events. Gmail/Calendar access is optional and set up separately.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit ea60f169f997](https://github.com/farahabuhmaidan/jev-bouncer/tree/ea60f169f997b44cede5c87f2068ab4af26462a6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
