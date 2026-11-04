# Eregion (local job-search agent that scores resume fit, with optional Jev fit scoring for speed)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Job-search agent that runs on your computer: it searches company job boards and LinkedIn, reads each posting, ranks jobs by fit to your resume with gaps listed, tailors the resume and cover letter with each claim checked against the resume, and fills application forms up to the review page without submitting. When Jev is switched on, fit scoring uses Jev while your main model keeps handling conversation and writing. The README reports 0.39 s per posting across 150 postings in 13 searches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ethany14/Eregion-Job-Finding-Agent) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ethany14/Eregion-Job-Finding-Agent#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you supply your own model and TypeSafe keys and pay their usage. No hosted plan was found. Checked 2026-11-04. |
| Jev evidence | [`backend/eregion/domain/jev_fit/transport.py`](https://github.com/ethany14/Eregion-Job-Finding-Agent/blob/6e6edecc785b52afae12577e0fd62b3822124450/backend/eregion/domain/jev_fit/transport.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ethany14](https://github.com/ethany14). Independently curated. |
| Format | Python backend with a local web workspace and Chrome form-filling |
| Platform and availability | Local web app on macOS, Linux or Windows (source build); no hosted version verified. |
| Jev's role | Optional fast yes/no scorer for how well each posting fits the resume. |
| Requirements | Python 3.12, your own model API key, and a `TYPESAFE_API_KEY` with `TYPESAFE_ENABLED=true` for Jev fit scoring. |
| License | [MIT](https://github.com/ethany14/Eregion-Job-Finding-Agent/blob/6e6edecc785b52afae12577e0fd62b3822124450/LICENSE) |

## When to use

- Rank many job postings against a resume quickly, with a visible score range when a requirement is undecided.
- Mismatch: Jev is optional, fit thresholds are validated against jev-1.13.0, and there is no fallback to the main model when TypeSafe is unreachable.

## How it works

`jev_fit/transport.py` posts batched yes/no fit questions (up to 16 jobs per batch, cached locally) to `https://api.typesafe.ai/v1/systemone`; `settings.py` pins `jev-1.13.0` even when `jev-latest` is configured. Integration evidence: [`backend/eregion/domain/jev_fit/transport.py`](https://github.com/ethany14/Eregion-Job-Finding-Agent/blob/6e6edecc785b52afae12577e0fd62b3822124450/backend/eregion/domain/jev_fit/transport.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ethany14/Eregion-Job-Finding-Agent.git
python3.12 -m venv .venv && source .venv/bin/activate
python -m pip install -r requirements.txt   # then follow the README's setup and .env steps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the Jev section, speed table and setup: [github.com/ethany14/Eregion-Job-Finding-Agent#readme](https://github.com/ethany14/Eregion-Job-Finding-Agent#readme)
- Jev benchmark notes: [github.com/ethany14/Eregion-Job-Finding-Agent/blob/6e6edecc785b52afae12577e0fd62b3822124450/docs/jev-benchmark.md](https://github.com/ethany14/Eregion-Job-Finding-Agent/blob/6e6edecc785b52afae12577e0fd62b3822124450/docs/jev-benchmark.md)

## Limits and data handling

Job posting text and resume-derived requirements go to TypeSafe on your key when Jev is on. The timing table is the author's own run and compares scale rather than identical conditions. Nothing is submitted without you. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 6e6edecc785b](https://github.com/ethany14/Eregion-Job-Finding-Agent/tree/6e6edecc785b52afae12577e0fd62b3822124450). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
