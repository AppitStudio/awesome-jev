# Decision Model Testing by dorkitude (reproducible experiments comparing Jev with other decision models, LLM judges and rerankers)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Set of self-contained experiments by Kyle Wild comparing Jev 1.13 and 1.14 with OpenAI Decisions, Fireworks Rune, SubQ Snap, LLM judges and a reranker: judging benchmarks, RAG result filtering before Kimi K3 and Claude, TREC passage ranking, request shaping, intent menus and order effects.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dorkitude/decision-model-testing) |
| Maintainer | [dorkitude](https://github.com/dorkitude). Independently curated. |
| Format | Research repository with Go and Python experiment code and write-ups (MIT) |
| Requirements | Go and Python per experiment; TypeSafe and other provider keys to rerun. Some source data is not redistributed and must be fetched from the linked public datasets. |
| License | [MIT](https://github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`experiments/request-shaping/internal/bench/client.go`](https://github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/experiments/request-shaping/internal/bench/client.go) at the pinned commit. |

## When to use

- Check how Jev compares with other decision models and LLM judges on public tasks before choosing one.
- Reuse the request-shaping findings when designing Jev requests.
- Mismatch: a library; this is research code and write-ups.

## How it works

Experiment clients such as `experiments/request-shaping/internal/bench/client.go` send requests to `https://api.typesafe.ai/v1/systemone`; adapters map the same requests to OpenAI Decisions, Rune and SubQ so arms share samples, prompts and scoring. Reported results are mixed: for example, no judge dominated every judging benchmark, and SubQ edged Jev on TREC ranking while Jev 1.13 and 1.14 were within noise of each other. These are author-reported figures. Integration evidence: [`experiments/request-shaping/internal/bench/client.go`](https://github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/experiments/request-shaping/internal/bench/client.go).

## Get started

Clone the repository and follow `REPRODUCTION.md` and each experiment's README.

```sh
git clone https://github.com/dorkitude/decision-model-testing.git
cd decision-model-testing
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with result synopses: [github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/README.md](https://github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/README.md)
- Reproduction guide: [github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/REPRODUCTION.md](https://github.com/dorkitude/decision-model-testing/blob/0c3f84202622c4cd24322a37be4ed92ef0522312/REPRODUCTION.md)

## Limits and data handling

Reruns send benchmark items to each provider on your keys.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 0c3f84202622](https://github.com/dorkitude/decision-model-testing/tree/0c3f84202622c4cd24322a37be4ed92ef0522312). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
