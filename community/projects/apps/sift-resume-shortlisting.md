# Sift by Nihir Dhamecha (blind resume shortlisting with Jev; names stay in the recruiter's browser)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Upload resumes against a job description; Sift parses each PDF, redacts the candidate's name before Jev sees it, and returns a match score with a Shortlisted / Not this time suggestion and requirement chips. Results show IDs only until you click Reveal names; nothing is stored server-side.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nihirdhamecha/sift) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/nihirdhamecha/sift#readme) (source-built; no separate product site verified). |
| Pricing and access | Self-deploy the source to Vercel or run it locally with your own TypeSafe key; no license file, so reuse terms are not granted. No public hosted instance verified. Checked 2026-11-21. |
| Jev evidence | [`shortlister/jev.py`](https://github.com/nihirdhamecha/sift/blob/b25acc2bbdf610f450741246e7802b384d89f4e2/shortlister/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [nihirdhamecha](https://github.com/nihirdhamecha). Independently curated. |
| Format | React web app + Python API |
| Platform and availability | Web (Vercel: React front end + Python function) and a local Python CLI. |
| Jev's role | Scores each redacted resume against the job's requirements and gives the shortlist suggestion. |
| Requirements | A TypeSafe API key and a demo password for live scores (mock mode otherwise); Vercel or local Python and Node. |
| License | no license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Get a first-pass, name-blind shortlist suggestion for a pile of resumes while a person makes every decision.
- Mismatch: automated hiring decisions; hiring is a high-stakes use and model scores can carry bias even with names hidden.

## How it works

`shortlister/jev.py` sends the redacted resume JSON and job requirements to Jev (`jev-1.13.0` pinned by default) and reads back scores; `api/index.py` runs one resume per request with no server state, and live scoring only runs when a key and password are set. Integration evidence: [`shortlister/jev.py`](https://github.com/nihirdhamecha/sift/blob/b25acc2bbdf610f450741246e7802b384d89f4e2/shortlister/jev.py).

## Get started

Run locally with the CLI (redact first to check for leaks), or deploy to Vercel with the documented environment variables.

```sh
git clone https://github.com/nihirdhamecha/sift
cd sift
export TYPESAFE_API_KEY=...
python run.py --redact-only   # inspect what Jev will see
python run.py                 # score with Jev
python run.py --mock          # dry run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nihirdhamecha/sift/blob/b25acc2bbdf610f450741246e7802b384d89f4e2/README.md](https://github.com/nihirdhamecha/sift/blob/b25acc2bbdf610f450741246e7802b384d89f4e2/README.md)

## Limits and data handling

Redacted resume content is sent to TypeSafe; names are kept in the browser. Use only as an aid with human review, and check local rules on automated hiring tools. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit b25acc2bbdf6](https://github.com/nihirdhamecha/sift/tree/b25acc2bbdf610f450741246e7802b384d89f4e2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
