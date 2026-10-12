# Claims, Choices and Labels (jev-eval)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Audit of Jev (`jev-1.13.0`) and five generative models on how they handle claims, forced choices and labels about Taiwan's status in several languages, with a draft preprint, item explorer and replays.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Clementtang/jev-eval) |
| Maintainer | [Clementtang](https://github.com/Clementtang). Independently curated. |
| Format | Node.js research code + data + static site |
| Requirements | Node.js 24+; vendor API keys only to re-run models. |
| License | [MIT (code); CC BY 4.0 (data/text)](https://github.com/Clementtang/jev-eval/blob/5c644f1859b9943bea023ba27b5579a7fb95dc77/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Check how a structured decision model behaves on politically sensitive country fields before using it in forms.
- Reuse the item set and stats scripts for your own audit.
- Mismatch: Draft preprint, not peer reviewed; findings are the author's and specific to the tested items and dates.

## How it works

Provider adapters call each model (Jev via `https://api.typesafe.ai/v1/systemone`); stats scripts regenerate summaries from recorded results. Jev integration: [`lib/providers.mjs`](https://github.com/Clementtang/jev-eval/blob/5c644f1859b9943bea023ba27b5579a7fb95dc77/lib/providers.mjs). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Clementtang/jev-eval.git
cd jev-eval
npm install
node scripts/stats.mjs
```

## Limits and data handling

Re-running calls each vendor (billed). Recorded results are included. Not run on the review host. Data/text under [CC BY 4.0](https://github.com/Clementtang/jev-eval/blob/5c644f1859b9943bea023ba27b5579a7fb95dc77/LICENSE-CC-BY-4.0.txt).

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 5c644f1859b9](https://github.com/Clementtang/jev-eval/tree/5c644f1859b9943bea023ba27b5579a7fb95dc77). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
