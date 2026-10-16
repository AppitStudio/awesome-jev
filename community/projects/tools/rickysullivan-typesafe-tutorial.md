# TypeSafe AI, from fundamentals to use cases (notebooks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Deno Jupyter notebooks that teach Jev from the basics up: what a System One model is, Choice, Score and Noul, structure and confidence, then the four documented patterns (fan-out, confidence-gated routing, composite scoring, intent routing) and cookbooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rickysullivan/typesafe-tutorial) |
| Maintainer | [rickysullivan](https://github.com/rickysullivan). Independently curated. |
| Format | Deno Jupyter notebooks |
| Requirements | Deno 2+ with the Deno Jupyter kernel, VS Code (Insiders) with the Jupyter extension, a TypeSafe API key. |
| License | [MIT](https://github.com/rickysullivan/typesafe-tutorial/blob/b433a84ae35a6767901376596a193a70e7b011c5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`assets/typesafe-client.ts`](https://github.com/rickysullivan/typesafe-tutorial/blob/b433a84ae35a6767901376596a193a70e7b011c5/assets/typesafe-client.ts) at the pinned commit. |

## When to use

- Learn the Jev primitives in order before building on them.
- Copy a pattern notebook (for example intent routing) as a starting point.
- Mismatch: learning material written for a talk; the images lesson needs TypeSafe's pre-release header.

## How it works

A shared client built on `@typesafe-ai/sdk` reads `TYPESAFE_API_KEY` (and optional `TYPESAFE_HEADERS`) from `.env`; each lesson runs real calls and a git filter strips outputs on commit. Integration evidence: [`assets/typesafe-client.ts`](https://github.com/rickysullivan/typesafe-tutorial/blob/b433a84ae35a6767901376596a193a70e7b011c5/assets/typesafe-client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/rickysullivan/typesafe-tutorial.git && cd typesafe-tutorial
deno jupyter --install && deno task setup
echo 'TYPESAFE_API_KEY=your-key-here' > .env
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Lesson index and cookbooks in the README.
- Glossary: `GLOSSARY.md`; sources: `RESOURCES.md`.

## Limits and data handling

Notebook inputs go to TypeSafe on your key; outputs stay local.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit b433a84ae35a](https://github.com/rickysullivan/typesafe-tutorial/tree/b433a84ae35a6767901376596a193a70e7b011c5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
