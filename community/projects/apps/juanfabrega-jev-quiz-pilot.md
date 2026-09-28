# Jev Quiz Pilot

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Python CLI that lets TypeSafe Jev navigate web quizzes in Chrome and logs every pick for measurement

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/juanfabrega/jev-quiz-pilot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://juanfabrega.github.io/jev-quiz-pilot/demo/) |
| Pricing and access | Free source build; no app purchase fee. TypeSafe/provider usage billed separately (BYOK). Checked 2026-09-29. |
| Jev evidence | [Upstream README](https://github.com/juanfabrega/jev-quiz-pilot/blob/bd8303efe2ccfceca68a44d8e7be0528a45406c8/README.md) describes TypeSafe Jev selecting quiz answers in Chrome at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live Chrome/Jev paths not run on the review host. |
| Maintainer | [juanfabrega](https://github.com/juanfabrega). Independently curated. |
| Format | Python · CLI + Chrome automation (MIT). |
| Platform and availability | Command-line + Chrome automation; MIT source build. Demo: [https://juanfabrega.github.io/jev-quiz-pilot/demo/](https://juanfabrega.github.io/jev-quiz-pilot/demo/). |
| Jev's role | Jev chooses quiz answers; the CLI owns browser automation and logging. |
| Requirements | Python; Chrome; TypeSafe API key. |
| License | [MIT](https://github.com/juanfabrega/jev-quiz-pilot/blob/bd8303efe2ccfceca68a44d8e7be0528a45406c8/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when measuring how Jev performs on quiz-style choice tasks in a real browser.

## How it works

CLI drives Chrome; Jev selects answers; logs enable scoring. Demo: <\1>stream README at the pinned commit.

## Get started

```sh
git clone https://github.com/juanfabrega/jev-quiz-pilot.git
cd jev-quiz-pilot
git checkout bd8303efe2ccfceca68a44d8e7be0528a45406c8
```

Pin revision `bd8303efe2ccfceca68a44d8e7be0528a45406c8` when reproducing this review.

## Examples and demos

Demo page: [https://juanfabrega.github.io/jev-quiz-pilot/demo/](https://juanfabrega.github.io/jev-quiz-pilot/demo/). Upstream README at the pinned commit. No live quiz run on the review host.

## Limits and data handling

Live TypeSafe/Chrome paths were not executed on the review host. Treat measured quiz scores as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit bd8303e](https://github.com/juanfabrega/jev-quiz-pilot/tree/bd8303efe2ccfceca68a44d8e7be0528a45406c8). AI-assisted README and LICENSE inspection; install/live paths not executed.
