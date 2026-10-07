# ChatJevPT

[All projects](../README.md) · [Web apps](README.md#web-apps)

Chat app that makes TypeSafe Jev 'generate' an answer one character at a time by asking the same choice question over and over (next character or END), shows each letter's top-five probabilities, lets Jev grade its own answer, and meters cost; several 'model levels' compare naive and fuller pipelines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samkoosh/ChatJevPT) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [chatjevpt.vercel.app](https://chatjevpt.vercel.app) (reachable 2026-10-08; operator's hosted instance, not used on the review host). |
| Pricing and access | No fee for the MIT source; self-hosting needs your own TypeSafe key (usage billed by TypeSafe; Vercel hosting optional). The hosted instance is funded by its operator and may require sign-in or run out of credits. Checked 2026-10-08. |
| Jev evidence | [`lib/jev.js`](https://github.com/samkoosh/ChatJevPT/blob/425fab30b9b1b9e966533f25cd8dc4228d9637ad/lib/jev.js) and [`api/next.js`](https://github.com/samkoosh/ChatJevPT/blob/425fab30b9b1b9e966533f25cd8dc4228d9637ad/api/next.js) send the per-character choice question; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [samkoosh](https://github.com/samkoosh). Independently curated. |
| Format | Static web UI + Vercel functions (Node) |
| Platform and availability | Web browser; deploy on Vercel or run locally with Node.js 20+. |
| Jev's role | Picks every next character and grades the final answer; the app assembles text and enforces budgets. |
| Requirements | Node.js 20+ and a `TYPESAFE_API_KEY`; optional Postgres and Google sign-in for accounts and budgets. |
| License | [MIT](https://github.com/samkoosh/ChatJevPT/blob/425fab30b9b1b9e966533f25cd8dc4228d9637ad/LICENSE). |

## When to use

- See what a typed decision model does when forced to act like a generator.
- Teach how choice questions, ties and runoffs work.
- Mismatch: a deliberate toy; answers are capped at 200 characters and slow by design.

## How it works

For each character the server asks Jev a Choice over A–Z, 0–9, space, newline, punctuation or END with the question and answer so far as state; ties go to a runoff. A final Score question rates the answer. `/api/next` is public unless accounts are enabled, so the README recommends turning on accounts and budgets.

## Get started

Run locally (README *Setup*):

```sh
git clone https://github.com/samkoosh/ChatJevPT && cd ChatJevPT
npm install
cp .env.example .env   # paste TYPESAFE_API_KEY
npm run dev
```

Every character is one Jev request; the README's content test costs about $0.07 per run. Usage billed to your TypeSafe key.

## Examples and demos

- [Hosted instance](https://chatjevpt.vercel.app).
- README *Features* (model levels, memory toggle, self-grading).

## Limits and data handling

Questions, chat history (with memory on) and accounts data go to TypeSafe and your deployment's store. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 425fab30b9b1](https://github.com/samkoosh/ChatJevPT/tree/425fab30b9b1b9e966533f25cd8dc4228d9637ad). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
