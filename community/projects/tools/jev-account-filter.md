# Jev Account Filter

[All tools](README.md) · [Developer tools](README.md#developer-tools)

Screen video-platform accounts for domain dataset collection or research using titles, thumbnails and profile metadata rather than complete videos.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/caiweihan/jev-account-filter) |
| Maintainer | [caiweihan](https://github.com/caiweihan); self-submitted by the maintainer for the team using the project. |
| Format | Python CLI with separate collection and screening commands, plus a local HTML analysis page. |
| Platform and availability | Source-built developer tool; Windows PowerShell and macOS/Linux instructions. Douyin, Kuaishou, YouTube, Bilibili and custom collected datasets are supported. |
| Jev's role | Two-stage title ranking and multimodal account classification using OpenRouter `typesafe/jev-1.14`; endpoint, protocol and model are explicit configuration. |
| Requirements | Python 3.11+, project-local dependencies, Playwright browser for collection; an OpenRouter account, a key in `OPENROUTER_API_KEY`, and billed inference for live screening. |
| License | Public source with no project-wide source-code license declared at the reviewed revision. The separate third-party icon license does not license the application. |
| Disclosure | Maintainer self-submission; substantial OpenAI Codex assistance in development, documentation and proposal preparation. No paid placement or model-provider affiliation is claimed; a listing is not endorsement. |

## When to use

Use it to shortlist relevant creator accounts before collecting a domain dataset, or to select accounts for a research sample. Category TOML rules can be revised and rerun over the same local data. The team's current application is sign-language account screening; the tool is not a full-video content verifier.

## How it works

Collection stores account names, biographies, first-page video titles and local thumbnails in a documented dataset. The independent screening command reads those files without opening platform pages.

In pass one, Jev receives video titles only and returns one `Noul` probability per title. Code sorts these scores and retains Top-N, five by default. Pass two sends the selected titles and JPEG thumbnails together with the name and biography. It asks an independent account-category `Choice`, separate account/video `Noul` questions and a best-candidate `Choice`. The account label is the typed choice, not a threshold derived from a video score.

See the [request builder and answer validation](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/account_filter/screening/classifier.py), [screening runner](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/account_filter/screening/runner.py) and [API configuration](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/configs/api.toml). This is a third-party OpenRouter Decisions integration, not the TypeSafe SDK or its direct HTTP protocol. Other compatible models can be configured explicitly.

## Get started

For an offline first look, download the repository and open its root `analysis.html` in Edge or Chrome. It includes six authorized public examples. Select a result CSV and optional local evidence directories to inspect your own experiment; no model key is needed for this step.

For inference over the bundled sample, follow the [installation instructions](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/docs/installation.md) to create the project's `.venv` and install `requirements.txt`. Set your private `OPENROUTER_API_KEY` in the environment or `.env`; never place the key in a tracked TOML file. From the project root on macOS/Linux:

```sh
.venv/bin/python -m account_filter validate-data examples/real-demo/data
```

The following is **live**, sends the six published example accounts' metadata/titles/thumbnails to OpenRouter and its model provider, and incurs API charges:

```sh
.venv/bin/python -m account_filter screen --data examples/real-demo/data --config configs/api.toml --category sign-language --top-videos 5 --output results/first-experiment
```

The result is `results/first-experiment/results.csv` with typed model responses and request previews under `intermediate/`. On Windows use `.\.venv\Scripts\python.exe`. See [commands](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/docs/commands.md) for collection, login and resume instructions, and [data format](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/docs/data-format.md) to supply your own sources.

## Examples and demos

- [Public example dataset and publication scope](https://github.com/caiweihan/jev-account-filter/tree/c46e437491c65798bdb372e85b99b5ec9a4822b1/examples/real-demo): real, explicitly published samples, not an accuracy benchmark.
- [Offline HTML viewer](https://github.com/caiweihan/jev-account-filter/blob/c46e437491c65798bdb372e85b99b5ec9a4822b1/analysis.html): download and open locally; GitHub's source page is not a hosted dashboard.
- [Workflow and chart screenshots](https://github.com/caiweihan/jev-account-filter#visual-analysis): published aggregate experiment views and a limited public evidence sample. No separately hosted live demo was verified.
- [Offline tests](https://github.com/caiweihan/jev-account-filter/tree/c46e437491c65798bdb372e85b99b5ec9a4822b1/tests): request construction, typed-response parsing, resume behavior and image dimensions are testable without paid inference.

## Limits and data handling

Names, biographies, selected titles and thumbnails leave the local machine only during model inference; the current example route sends them through OpenRouter to the model provider. Collected evidence, raw responses, keys and browser sessions can be sensitive and should stay private. The viewer reads local files and does not require a server.

Only first-page evidence and Top-N selected candidates are evaluated, so relevant videos can be missed and thumbnails do not establish full-video content. Platform login, access restrictions and regional service availability still apply. Jev image copies are padded/resized to the provider's 280–1568 pixel edge limits; collected originals are preserved.

Missing/corrupt covers are recorded and can fall back to titles. Invalid/missing typed answers and HTTP errors produce failed CSV entries rather than fabricated classifications. Requests are not automatically retried; resume skips completed accounts and retries failed entries while reusing matching successful stage responses. Empty-video accounts follow the configured negative-label path without an API call.

## Review and maintenance

Inspected on **2026-10-17** at [c46e437](https://github.com/caiweihan/jev-account-filter/tree/c46e437491c65798bdb372e85b99b5ec9a4822b1): installation and command docs, two-stage request building, response parsing, resume behavior, Jev configuration and example publication scope. This review and proposal were AI-assisted, not an independent maintainer audit.

Earlier in the same development session, three public accounts completed six live OpenRouter Jev 1.14 requests, with five thumbnails in each second pass. The targeted offline image/pipeline/category/dataset checks passed **49 tests**. These checks establish integration behavior, not a dataset accuracy estimate. A clean installation on every documented OS was not repeated.

The team reports **2,140 Douyin accounts**, **8 hours** collecting data, **1 hour** of Jev inference and **$0.565** in API costs. Its reported **94.49%** accuracy uses 198 existing second-review labels and assumes remaining original labels are correct. This is a conditional estimate, not independent full-dataset validation; the private full dataset is not published. See the [reported results](https://github.com/caiweihan/jev-account-filter#advantages). The catalog patch is checked separately with its offline checks, not with paid inference.
