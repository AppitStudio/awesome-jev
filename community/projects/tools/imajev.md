# imajev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open Jev-style multimodal typed-decision models (photos+records+text → options with can't-tell).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mohit67890/imajev) |
| Maintainer | [mohit67890](https://github.com/mohit67890). Independently curated. |
| Format | Open multimodal typed-decision models (2B/4B/9B) with HF weights and local serve path. |
| Requirements | Python/serve stack per upstream; local weights—not TypeSafe-hosted Jev. |
| License | [Apache-2.0](https://github.com/mohit67890/imajev/blob/7a0e6a11eab8f38e6c005c7137d7ae47f7339613/LICENSE). Independent open-weight / self-hosted path—not TypeSafe-hosted Jev. |
| Disclosure | Independent of hosted TypeSafe Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Independent open weights—not TypeSafe-hosted Jev (similar disclosure class to PostHog/jeeves). |

## When to use

Use when you need an open, self-hosted typed-decision model that can take images and business records. Prefer hosted TypeSafe Jev when you want the commercial System One API.

## How it works

imajev is an independent open model family with a Jev-like typed-question interface over multimodal inputs. Catalog listing discloses it is not TypeSafe-hosted Jev. Independent of hosted TypeSafe Jev.

## Get started

```sh
git clone https://github.com/mohit67890/imajev.git
cd imajev
git checkout 7a0e6a11eab8f38e6c005c7137d7ae47f7339613
# follow upstream README for weight download / local serve
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 7a0e6a1](https://github.com/mohit67890/imajev/tree/7a0e6a11eab8f38e6c005c7137d7ae47f7339613). AI-assisted README and license inspection; install/live paths not executed.
