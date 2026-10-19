# doublestrain

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Grades dependency advisories into SSVC Act, Attend or Track using whether the vulnerable code is reachable in your app, with a fixed decision tree and model judges (including an optional Jev classifier) held to measured acceptance floors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/seanturner83/doublestrain) |
| Maintainer | [seanturner83](https://github.com/seanturner83). Independently curated. |
| Format | Python CLI |
| Requirements | Python with uv; optional judge backends (local models, Claude, or a TypeSafe key for the Jev judge). |
| License | [Apache-2.0](https://github.com/seanturner83/doublestrain/blob/7f652cc62cf2c630922a67b375c7e841754a73de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/doublestrain/judges/jev.py`](https://github.com/seanturner83/doublestrain/blob/7f652cc62cf2c630922a67b375c7e841754a73de/src/doublestrain/judges/jev.py) at the pinned commit. |

## When to use

- Triage lockfile or Dependabot advisories by real reachability, not CVSS alone.
- Want every grade to record where its facts came from.
- Mismatch: Jev is one optional judge; the decision tree makes the final call.

## How it works

Lockfiles (npm, pip, Cargo, Go) map to OSV advisories, and exploitation data comes from CISA KEV and FIRST EPSS. Judges supply reachability with evidence, and verdicts only count above floors measured on labelled apps. `src/doublestrain/judges/jev.py` calls the hosted Jev API with `TYPESAFE_API_KEY`. Integration evidence: [`src/doublestrain/judges/jev.py`](https://github.com/seanturner83/doublestrain/blob/7f652cc62cf2c630922a67b375c7e841754a73de/src/doublestrain/judges/jev.py).

## Get started

From the upstream README: `uv sync`, then `doublestrain scan` on an app, with or without judges.

```sh
uv sync
uv run doublestrain scan path/to/app --judge null --exposure public-internet
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/running.md
- README results section

## Limits and data handling

With the Jev judge on, abstracted code context goes to TypeSafe. A wrong "not reachable" can hide risk, which the tool treats as the stricter direction.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 7f652cc62cf2](https://github.com/seanturner83/doublestrain/tree/7f652cc62cf2c630922a67b375c7e841754a73de). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
