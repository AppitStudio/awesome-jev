# FuZev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Jev-compatible Choice, yes/no, and Score decisions alongside text generation on vLLM/ExLlamaV3 from one loaded model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PeisongXiao/fuzev) |
| Maintainer | [PeisongXiao](https://github.com/PeisongXiao). Independently curated. |
| Format | Open model + serving notes |
| Requirements | vLLM or ExLlamaV3; Hugging Face weights; no TypeSafe key for local serving. |
| License | [Apache-2.0](https://github.com/PeisongXiao/fuzev/blob/d200f59ec87280bf3fc1a88a3fc170542b18627e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`README.md`](https://github.com/PeisongXiao/fuzev/blob/d200f59ec87280bf3fc1a88a3fc170542b18627e/README.md) at the pinned commit. |

## When to use

- Use when you need: Jev-compatible Choice, yes/no, and Score decisions alongside text generation on …
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `README.md`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: README.md.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit d200f59ec872](https://github.com/PeisongXiao/fuzev/tree/d200f59ec87280bf3fc1a88a3fc170542b18627e). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
