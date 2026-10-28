# e-jev (self-hosted Jev-compatible API with a pluggable fleet of decision backends)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted service that speaks TypeSafe's System One API and serves typed, calibrated decisions from Cloudflare's Clef-Flash by default, with optional backends behind the same wire contract: a vLLM logprob reader, Laya or any other `/v1/systemone` server. The author reports WorkflowEvals, Banking77 and Spanish-intent results for the default model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/edamlabs/e-jev) |
| Maintainer | [edamlabs](https://github.com/edamlabs). Independently curated. |
| Format | Python 3.13 service |
| Requirements | A GPU host for Clef-Flash (about 6.9 GB); no TypeSafe key. |
| License | [MIT](https://github.com/edamlabs/e-jev/blob/d428c37778374281b84ea611aea20575f6f1a22d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/e_jev/adapters/decider/systemone.py`](https://github.com/edamlabs/e-jev/blob/d428c37778374281b84ea611aea20575f6f1a22d/src/e_jev/adapters/decider/systemone.py) at the pinned commit. |

## When to use

- Self-host a Jev-shaped decision endpoint and mix backends.
- Mismatch: not TypeSafe's Jev; figures are the author's.

## How it works

`src/e_jev/adapters/decider/systemone.py` forwards to native `/v1/systemone` servers in the fleet; the public endpoint accepts the same `{model, state, questions}` body as Jev. Integration evidence: [`src/e_jev/adapters/decider/systemone.py`](https://github.com/edamlabs/e-jev/blob/d428c37778374281b84ea611aea20575f6f1a22d/src/e_jev/adapters/decider/systemone.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/edamlabs/e-jev && cd e-jev
# see the README Install section (Makefile targets start the stack and run a test request)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/edamlabs/e-jev#readme](https://github.com/edamlabs/e-jev#readme)

## Limits and data handling

Runs on your infrastructure; nothing goes to TypeSafe unless you add it as a backend.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit d428c3777837](https://github.com/edamlabs/e-jev/tree/d428c37778374281b84ea611aea20575f6f1a22d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
