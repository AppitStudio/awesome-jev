# Eyedot · 点睛

[All projects](../README.md) · [Web apps](README.md#web-apps)

Turns your own study material (PDF, Word, text) into exams that grade themselves point by point: grading is decomposed into atomic checkable questions whose probabilities are combined in code, with TypeSafe Jev as the decision engine when `TYPESAFE_API_KEY` is set (general-LLM judge and a labelled lexical demo engine as fallbacks), plus cited follow-up answers and spaced-repetition review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Simon-zj1/eyedot) |
| Tags | `Open source` · `Freemium` · `Commercial` · `BYOK` |
| Product homepage | [exam.simon-zj.top](https://exam.simon-zj.top) (hosted, Chinese UI) · [sample report](https://www.simon-zj.top/demo/eyedot-report.html) |
| Pricing and access | [Hosted site](https://exam.simon-zj.top): free sign-up with 300 credits; platform usage is charged in credits at 1.5× official token prices, or bring your own model key. Self-host free from source. Checked 2026-10-08. |
| Jev evidence | [`src/lib/engine/typesafe.ts`](https://github.com/Simon-zj1/eyedot/blob/575d37c48765229bae49eb32830ae492793d70b9/src/lib/engine/typesafe.ts) is the Jev grading engine, tested in [`tests/unit/engine-typesafe.test.ts`](https://github.com/Simon-zj1/eyedot/blob/575d37c48765229bae49eb32830ae492793d70b9/tests/unit/engine-typesafe.test.ts). Source inspected at the pinned commit; which engine the hosted site uses was not verified. |
| Disclosure | AI-assisted catalog review; no affiliation. Commercial: the hosted site sells usage credits (1.5× official token prices); the MIT source is free to self-host. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [Simon-zj1](https://github.com/Simon-zj1). Independently curated. |
| Format | Next.js web app (hosted or self-hosted) + agent skill |
| Platform and availability | Web browser; self-host with Node/Postgres (Vercel deploy guide). |
| Jev's role | Decides each grading point (noul/choice) so the final score is auditable per point. |
| Requirements | Hosted: email sign-up. Self-host: Node/npm, an LLM key, optional `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Simon-zj1/eyedot/blob/575d37c48765229bae49eb32830ae492793d70b9/LICENSE). |

## When to use

- Self-test on your own notes with per-point feedback on what you missed.
- Audit exactly why each point was awarded.
- Mismatch: hosted UI is Chinese; offline demo grading is lexical, not Jev.

## How it works

Material is split into knowledge points, questions are generated with citations back to the source sentence, and answers are graded per point; the swappable engine uses Jev when configured.

## Get started

Run locally (README):

```sh
git clone https://github.com/Simon-zj1/eyedot.git && cd eyedot
npm install
cp .env.example .env   # optional keys; offline demo works without
npm run dev            # http://localhost:3000
```

Hosted credits or your own keys; Jev grading billed to your TypeSafe key when self-hosted.

## Examples and demos

- [Sample report](https://www.simon-zj.top/demo/eyedot-report.html) (offline demo engine).

## Limits and data handling

Uploaded material is processed by the configured model providers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 575d37c48765](https://github.com/Simon-zj1/eyedot/tree/575d37c48765229bae49eb32830ae492793d70b9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
