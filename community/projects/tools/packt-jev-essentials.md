# TypeSafe AI: Jev Essentials code (companion code for Packt's book on building decision systems with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Companion code repository for Packt's book TypeSafe AI: Jev Essentials - Building Decision Systems, with chapter projects including a 100K-row customer classification notebook, a resume evaluator (starter and finished Node server), and a Swift Tiny Chat app with Jev intent models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems) |
| Maintainer | [PacktPublishing](https://github.com/PacktPublishing). Independently curated. |
| Format | Book companion code: Jupyter notebook, Node.js servers and a Swift app (MIT) |
| Requirements | Python/Jupyter, Node.js or Xcode depending on the chapter, plus a TypeSafe key; the book itself is a paid Packt title. |
| License | [MIT](https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems/blob/3b42446545ead99b6b419d3e972091b896bda3c5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. The book is a commercial Packt publication; the code repository is MIT. |
| Jev evidence | [`20 ResumeEvaluator/ResumeEvaluator/Server/app.js`](https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems/blob/3b42446545ead99b6b419d3e972091b896bda3c5/20%20ResumeEvaluator/ResumeEvaluator/Server/app.js) at the pinned commit. |

## When to use

- Follow worked chapter projects while learning to build decision systems with Jev.
- Mismatch: standalone tutorials without the book; the README is minimal and the explanations live in the paid book.

## How it works

The chapter projects call Jev through TypeSafe's official SDKs and API (`@typesafe-ai/sdk` in the resume evaluator's `Server/app.js`, `https://api.typesafe.ai` in the notebook and Swift app); the code is published by Packt alongside the book. Integration evidence: [`20 ResumeEvaluator/ResumeEvaluator/Server/app.js`](https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems/blob/3b42446545ead99b6b419d3e972091b896bda3c5/20%20ResumeEvaluator/ResumeEvaluator/Server/app.js).

## Get started

Clone the repository and open the chapter folder you are following; set your TypeSafe key as each chapter describes.

```sh
git clone https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository tree: [github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems/tree/3b42446545ead99b6b419d3e972091b896bda3c5](https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems/tree/3b42446545ead99b6b419d3e972091b896bda3c5)

## Limits and data handling

Each project sends its inputs to TypeSafe on your key. The 100K classification notebook can incur noticeable usage charges.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 3b42446545ea](https://github.com/PacktPublishing/TypeSafe-AI-Jev-Essentials---Building-Decision-Systems/tree/3b42446545ead99b6b419d3e972091b896bda3c5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
