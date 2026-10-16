# is-lesion

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

npm package that evaluates MRI and other medical scan images against Hugging Face dataset labels with Jev 1.14 (Noul, Choice, Score and Box), or local OpenJev vision models, returning a label, probability and bounding box; can score dataset rows directly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hemanth/is-lesion) |
| Maintainer | [hemanth](https://github.com/hemanth). Independently curated. |
| Format | npm package (`is-lesion`) |
| Requirements | Node.js; `TYPESAFE_API_KEY` for the Jev engine (local engines need a local model). |
| License | [MIT](https://github.com/hemanth/is-lesion/blob/011658df486453b42c012016bf907e8de5a63095/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.js`](https://github.com/hemanth/is-lesion/blob/011658df486453b42c012016bf907e8de5a63095/src/index.js) at the pinned commit. |

## When to use

- Experiment with image-grounded Jev questions on public medical imaging datasets and compare against ground truth.
- Mismatch: research and experimentation only; not a medical device and not for diagnosis or clinical decisions.

## How it works

`isLesion()` sends the image with the dataset's ClassLabel choices to Jev 1.14 (`jev-preview`) with visual exemplars when `TYPESAFE_API_KEY` is set; `fromHF()` evaluates a Hugging Face dataset row and `engines()` lists the cloud and local engines. Integration evidence: [`src/index.js`](https://github.com/hemanth/is-lesion/blob/011658df486453b42c012016bf907e8de5a63095/src/index.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm install is-lesion
export TYPESAFE_API_KEY=...
node -e "import('is-lesion').then(async m => console.log(await m.default('./mri-slice.jpg')))"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start and engine selection in the README.

## Limits and data handling

Scan images go to TypeSafe on your key when the Jev engine is used. Do not send identifiable patient data.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 011658df4864](https://github.com/hemanth/is-lesion/tree/011658df486453b42c012016bf907e8de5a63095). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
