# klint (semantic linter and architecture auditor that checks code against plain-English rule packs with a local Kev model or hosted Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Declarative semantic linter: rules are plain-English entries in `klint.json`, and a System One judge evaluates a file, a package tree or an AI agent's summary of its own change against a whole rule pack in one forward pass with no generated tokens. Suites add unit types, extractors and rule packs for other languages or audits; there is a GitHub Action and a pre-commit gate, and answers are cached by model version, text and question. It runs fully local with open-weight Kev, on a `kev.serve` server, or on TypeSafe's hosted Jev with measured character budgets and a 0.8 commit threshold for Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/skydiving94/klint) |
| Maintainer | [skydiving94](https://github.com/skydiving94). Independently curated. |
| Format | Python CLI and GitHub Action (Apache-2.0) |
| Requirements | Python; for hosted Jev a TypeSafe key in `KLINT_JUDGE_API_KEY` (the local Kev mode needs a GPU or Apple Silicon instead). |
| License | [Apache-2.0](https://github.com/skydiving94/klint/blob/c335ca17feedd17842f3bf57ef75fdb7f0b830fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`klint/infra/system_one/http_judge.py`](https://github.com/skydiving94/klint/blob/c335ca17feedd17842f3bf57ef75fdb7f0b830fc/klint/infra/system_one/http_judge.py) at the pinned commit. |

## When to use

- Catch architectural and semantic rule breaks that syntax linters miss, without an LLM reviewer.
- Mismatch: if code must stay local, use the Kev mode; hosted Jev sends code to TypeSafe.

## How it works

`klint/infra/system_one/http_judge.py` posts rule questions to `{base_url}/v1/systemone` and resolves the model version from `/v1/models`; the README's hosted-Jev section sets `https://api.typesafe.ai` with `jev-latest`, and `klint/app/commit_threshold.py` holds the Jev-specific threshold. Integration evidence: [`klint/infra/system_one/http_judge.py`](https://github.com/skydiving94/klint/blob/c335ca17feedd17842f3bf57ef75fdb7f0b830fc/klint/infra/system_one/http_judge.py).

## Get started

Install klint, point the judge at TypeSafe's hosted Jev and lint your code.

```sh
git clone https://github.com/skydiving94/klint && cd klint
pip install -e .
export KLINT_JUDGE_MODE=remote KLINT_JUDGE_BASE_URL=https://api.typesafe.ai KLINT_JUDGE_MODEL=jev-latest
export KLINT_JUDGE_API_KEY=...
klint examples/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/skydiving94/klint/blob/c335ca17feedd17842f3bf57ef75fdb7f0b830fc/README.md](https://github.com/skydiving94/klint/blob/c335ca17feedd17842f3bf57ef75fdb7f0b830fc/README.md)

## Limits and data handling

Jev is optional: the default judge is local Kev-4B. With hosted Jev, each audited unit's code and the rule questions go to TypeSafe on your key. The maker measured that Jev's answers vary between runs on long structure units at low confidence; accuracy figures are the maker's own test sets.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit c335ca17feed](https://github.com/skydiving94/klint/tree/c335ca17feedd17842f3bf57ef75fdb7f0b830fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
