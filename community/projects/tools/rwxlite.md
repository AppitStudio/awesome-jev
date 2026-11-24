# rwxlite by Amr Hassan (small local classifier that says whether an API operation reads, writes or can't be undone, trained with Jev-labelled data)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A local ~23 MB model that takes an API operation (method, path, name, summary, description) and returns p(read), p(write) and p(can't undo) in about 20 ms, so agents and gateways can guard risky calls. It answers in Jev's request and response shape, so the companion rwxmap tool can swap it in for Jev. Jev was used in the paid labelling passes behind the training data.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamr0/rwxlite) |
| Maintainer | [hamr0](https://github.com/hamr0). Independently curated. |
| Format | Node.js library (npm `rwxlite`) with ONNX model files |
| Requirements | Node.js; the five model files downloaded per the guide. No TypeSafe key at runtime; a TypeSafe key only to re-run the labelling scripts. |
| License | [Apache-2.0](https://github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`m0/jev-label.mjs`](https://github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/m0/jev-label.mjs) at the pinned commit. |

## When to use

- Classify API operations as read, write or irreversible before an agent calls them, locally and for free.
- Mismatch: if you want live Jev answers; rwxlite is a local stand-in trained partly from Jev labels.

## How it works

`m0/jev-label.mjs` (and the `m1/` check scripts) post operation states and noul questions to `https://api.typesafe.ai/v1/systemone` to label training rows, with a spend cap. At runtime `loadAnswerer()` answers Jev-shaped questions locally with no network calls. Integration evidence: [`m0/jev-label.mjs`](https://github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/m0/jev-label.mjs).

## Get started

Install from npm, download the model files, then call `loadAnswerer` with a Jev-shaped request.

```sh
npm install rwxlite
# download the model files: docs/wiki/guide.md#2-get-the-model-files
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README benchmark section: [github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/README.md](https://github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/README.md)
- Guide: [github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/docs/wiki/guide.md](https://github.com/hamr0/rwxlite/blob/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8/docs/wiki/guide.md)
- Companion tool rwxmap: [github.com/hamr0/rwxmap](https://github.com/hamr0/rwxmap)

## Limits and data handling

Runtime inference is local; only the labelling scripts call TypeSafe. Accuracy figures in the README come from one test on 1,821 operations labelled by two Claude models plus a human tie-break. Version 0.5.0 at review.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 92ad8ae26b3d](https://github.com/hamr0/rwxlite/tree/92ad8ae26b3d9c819e5abfaec04112fb1968e1d8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
