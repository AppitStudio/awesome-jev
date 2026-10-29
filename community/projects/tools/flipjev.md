# FlipJev (black-box red teaming that finds universal adversarial suffixes flipping Jev's decisions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, suffixes and results for a Johns Hopkins and UW-Madison preprint: an evolutionary black-box attack that uses only returned probabilities to find short suffixes which, appended to untrusted content, flip a typed decision model's answer. The authors report that one suffix found on one dataset flips 90-100% of documents in five other tasks. Every table and figure regenerates from released results without API calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SaFo-Lab/FlipJev) |
| Maintainer | [SaFo-Lab](https://github.com/SaFo-Lab). Independently curated. |
| Format | Python research code and result files |
| Requirements | Python; an OpenRouter or TypeSafe key only to rerun attacks. |
| License | [FlipJev Research License (custom; academic research and defensive security only, not OSI open source)](https://github.com/SaFo-Lab/FlipJev/blob/38bd2509a2882f4fa6d95e00b27c42b91fd2df4e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`flipjev/api.py`](https://github.com/SaFo-Lab/FlipJev/blob/38bd2509a2882f4fa6d95e00b27c42b91fd2df4e/flipjev/api.py) at the pinned commit. |

## When to use

- Test how a Jev-based gate holds up against adversarial content before deploying it.
- Mismatch: research-use-only license; results are the authors'.

## How it works

`flipjev/api.py` queries `typesafe/jev-1.13` through OpenRouter's Decisions API (with a direct `https://api.typesafe.ai/v1/systemone` path) and scores candidate suffixes by the returned probabilities. Integration evidence: [`flipjev/api.py`](https://github.com/SaFo-Lab/FlipJev/blob/38bd2509a2882f4fa6d95e00b27c42b91fd2df4e/flipjev/api.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/SaFo-Lab/FlipJev && cd FlipJev
# see the README to regenerate tables from results/ without API calls
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Project page: [flipjev.github.io](https://flipjev.github.io)
- README: [github.com/SaFo-Lab/FlipJev#readme](https://github.com/SaFo-Lab/FlipJev#readme)

## Limits and data handling

Rerunning attacks sends crafted content to the Jev endpoint; use only on systems you are authorized to test.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 38bd2509a288](https://github.com/SaFo-Lab/FlipJev/tree/38bd2509a2882f4fa6d95e00b27c42b91fd2df4e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
