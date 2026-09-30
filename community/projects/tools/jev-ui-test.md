# jev-ui-test

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Jev-driven UI test framework: natural-language cases, pytest + Allure; TypeSafe Jev scores candidate elements instead of generating next-step prose (fork of jev-ultrafast for regression testing).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/buer2233/jev-ui-test) |
| Maintainer | [buer2233](https://github.com/buer2233). Independently curated. |
| Format | Python UI automation test framework (pytest/Allure) driven by TypeSafe Jev. |
| Requirements | Python ≥ 3.12; `uv sync`; `TYPESAFE_API_KEY` and text-model key per `.env.example`; Chrome via Browser Harness. |
| License | [MIT](https://github.com/buer2233/jev-ui-test/blob/9f67479f4a88a7dbdbc747b3bce42317bfa793c1/LICENSE). TypeSafe/text-model usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream reports median ~458 ms per decision from bundled Allure demos—not re-measured here. Live paths not run on the review host. |

## When to use

Use when you want regression-style UI tests with closed-set Jev element scoring and Allure audit trails. Prefer [Jev Ultrafast](jev-ultrafast.md) for general browser agents rather than pytest suites.

## How it works

Fork of browser-use/jev-ultrafast: agent observes candidate elements; Jev returns scored action+target choices with calibrated probabilities; pytest assertions own pass/fail. Natural-language YAML cases; no pre-baked selectors.

## Get started

```sh
git clone https://github.com/buer2233/jev-ui-test.git
cd jev-ui-test
git checkout 9f67479f4a88a7dbdbc747b3bce42317bfa793c1
uv sync
cp .env.example .env   # fill TYPESAFE_API_KEY + TEXT_MODEL_API_KEY
# follow upstream README for cases and Allure
```

## Examples and demos

- Online report: [buer2233.github.io/jev-ui-test](https://buer2233.github.io/jev-ui-test/).
- Bundled Allure report and demo video/GIF under `examples/` (not re-executed here).

## Limits and data handling

Live Jev/text-model calls send page/candidate context to providers and may incur charges. Catalog checks did not run live UI tests.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 9f67479](https://github.com/buer2233/jev-ui-test/tree/9f67479f4a88a7dbdbc747b3bce42317bfa793c1). AI-assisted README and license inspection; install/live paths not executed.
