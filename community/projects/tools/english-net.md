# English Net (prompt-injection detector of yes/no questions)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Prompt-injection detector whose seven neurons are English yes/no questions answered by Jev in one call; on a locked confirmation set it ties a single good Jev question on ranking, while every verdict names the questions behind it and a blind spot can be patched by adding one sentence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/isaacbitran/english-net) |
| Maintainer | [isaacbitran](https://github.com/isaacbitran). Independently curated. |
| Format | Research code with live web demo (Python, Next.js) |
| Requirements | Python for the experiments; `TYPESAFE_API_KEY` for new sentences (the demo ships a cache of real Jev answers). |
| License | [MIT](https://github.com/isaacbitran/english-net/blob/1bfcdf521de2124eed2954acca1d54c0dc92d627/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`web/app/api/patch/route.ts`](https://github.com/isaacbitran/english-net/blob/1bfcdf521de2124eed2954acca1d54c0dc92d627/web/app/api/patch/route.ts) at the pinned commit. |

## When to use

- Study an editable, explainable injection filter built from plain-English questions.
- Compare Jev against DeBERTa-based detectors and PIGuard on the same data.
- Mismatch: research artifact; the author reports it does not beat one well-chosen question on unseen data.

## How it works

All seven questions go to Jev in a single System One call per text; their answers are combined into the verdict, and the demo's patch route asks Jev about any new sentence you add (`web/app/api/patch/route.ts`). Integration evidence: [`web/app/api/patch/route.ts`](https://github.com/isaacbitran/english-net/blob/1bfcdf521de2124eed2954acca1d54c0dc92d627/web/app/api/patch/route.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/isaacbitran/english-net.git
cd english-net
# see the README for the experiment scripts; set TYPESAFE_API_KEY for live calls
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [english-net-chi.vercel.app](https://english-net-chi.vercel.app)
- One-page note (PDF): [github.com/isaacbitran/english-net/releases/download/v1.0/english-net-note.pdf](https://github.com/isaacbitran/english-net/releases/download/v1.0/english-net-note.pdf)

## Limits and data handling

Texts you test are sent to TypeSafe. Results and costs are the author's measurements.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 1bfcdf521de2](https://github.com/isaacbitran/english-net/tree/1bfcdf521de2124eed2954acca1d54c0dc92d627). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
