# judgelint by filip-a-9 (lint and fuzz typed decision questions for Jev or a local llama.cpp model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Tests your decision questions before they ship: static rules (missing escape option, overlapping options, counting or date questions), option-order bias from every rotation of the options, out-of-scope probes that should not get confident answers, and noise and injection checks. A plan command shows call count and Jev cost first, a hard spend cap per run, and a non-zero exit so CI can gate on it. Different project from the Ruby judgelint already listed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/filip-a-9/judgelint) |
| Maintainer | [filip-a-9](https://github.com/filip-a-9). Independently curated. |
| Format | Python CLI |
| Requirements | Python with uv; a TypeSafe key for the Jev backend, or llama-cpp-python for local runs. |
| License | [MIT](https://github.com/filip-a-9/judgelint/blob/547b29eacd747ac6984a1c9a519f7ac5c57d2bfe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judgelint/backends/jev.py`](https://github.com/filip-a-9/judgelint/blob/547b29eacd747ac6984a1c9a519f7ac5c57d2bfe/src/judgelint/backends/jev.py) at the pinned commit. |

## When to use

- Catch order bias and prompt-injection sensitivity in a Jev question before production.
- Mismatch: checks the question, not your data.

## How it works

`src/judgelint/backends/jev.py` sends each probe to `{jev_base_url}/v1/systemone` with your question and stops when the per-run spend cap is reached. Integration evidence: [`src/judgelint/backends/jev.py`](https://github.com/filip-a-9/judgelint/blob/547b29eacd747ac6984a1c9a519f7ac5c57d2bfe/src/judgelint/backends/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/filip-a-9/judgelint && cd judgelint
uv sync
judgelint plan examples/triage.judgelint.yaml   # cost estimate, no calls
judgelint check examples/triage.judgelint.yaml --backend jev --json report.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/filip-a-9/judgelint#readme](https://github.com/filip-a-9/judgelint#readme)

## Limits and data handling

Probe inputs and your question go to TypeSafe with the Jev backend.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 547b29eacd74](https://github.com/filip-a-9/judgelint/tree/547b29eacd747ac6984a1c9a519f7ac5c57d2bfe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
