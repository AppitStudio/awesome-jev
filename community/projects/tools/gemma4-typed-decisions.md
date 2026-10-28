# Gemma 4 Typed Decisions (independent Jev-compatible decision API on Gemma 4, benchmarked against Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent implementation that makes Google's Gemma 4 return typed decisions with candidate probabilities (Noul, Choice, Score) through a `/v1/systemone` API, without generating text, plus a harness that compares it with the official Jev on the same inputs. The author reports 78.0% vs 79.9% accuracy on 3,300 test items with lower latency on an NVIDIA GB10. Japanese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nob-git-dev/gemma4-typed-decisions) |
| Maintainer | [nob-git-dev](https://github.com/nob-git-dev). Independently curated. |
| Format | Python API server and benchmark harness |
| Requirements | An NVIDIA GPU able to run Gemma 4; a TypeSafe API key only for the Jev comparison. |
| License | [MIT](https://github.com/nob-git-dev/gemma4-typed-decisions/blob/ecbae1c402f02dad6e17702ca1e75be7856fbc1a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`benchmark.py`](https://github.com/nob-git-dev/gemma4-typed-decisions/blob/ecbae1c402f02dad6e17702ca1e75be7856fbc1a/benchmark.py) at the pinned commit. |

## When to use

- Self-host a Jev-shaped decision endpoint and measure the gap yourself.
- Mismatch: not affiliated with Google or TypeSafe; results are the author's, on one machine.

## How it works

`benchmark.py` sends identical requests to the local server and to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`) and refuses to run the comparison without a real key. Integration evidence: [`benchmark.py`](https://github.com/nob-git-dev/gemma4-typed-decisions/blob/ecbae1c402f02dad6e17702ca1e75be7856fbc1a/benchmark.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/nob-git-dev/gemma4-typed-decisions && cd gemma4-typed-decisions
# see the README for server start-up and benchmark.py options
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese): [github.com/nob-git-dev/gemma4-typed-decisions#readme](https://github.com/nob-git-dev/gemma4-typed-decisions#readme)

## Limits and data handling

Benchmark inputs go to TypeSafe only during the comparison. The Gemma server runs locally.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit ecbae1c402f0](https://github.com/nob-git-dev/gemma4-typed-decisions/tree/ecbae1c402f02dad6e17702ca1e75be7856fbc1a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
