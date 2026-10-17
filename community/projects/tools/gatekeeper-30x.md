# Gatekeeper Editorial 30X

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Hackathon web app (in Spanish) where Jev answers typed questions about each content piece and code routes it to auto-approve, LLM rewrite, human review or reject; a second flow sorts Luma event sign-ups into programs and decides whether to call them now.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Michael-Liendo/gatekeeper-30x) |
| Maintainer | [Michael-Liendo](https://github.com/Michael-Liendo). Independently curated. |
| Format | Next.js 16 web app (TypeScript) with a hosted demo |
| Requirements | Node 22.18+, npm or pnpm; `TYPESAFE_API_KEY`, plus an LLM key for the rewrite step. |
| License | [AGPL-3.0](https://github.com/Michael-Liendo/gatekeeper-30x/blob/62574094037f62c67b77f6edd91d2ecc0afe8514/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/modules/content-review/infrastructure/jev-decision-engine.ts`](https://github.com/Michael-Liendo/gatekeeper-30x/blob/62574094037f62c67b77f6edd91d2ecc0afe8514/src/modules/content-review/infrastructure/jev-decision-engine.ts) at the pinned commit. |

## When to use

- Put a cheap, fast first filter in front of a content review queue so editors only see the risky or unclear pieces.
- Borrow the editorial policy pattern: Jev answers topic, relevance, promotion and brand-risk questions, and code picks the route and explains which rule fired.
- Mismatch: built for one company's hackathon brief (30X, October 2026); the policy and labels are theirs.

## How it works

The content-review module sends each piece to Jev with typed questions and applies a calibrated editorial policy (`editorial-policy.ts`) to choose `AUTO_APPROVE`, `ENRICH_WITH_LLM`, `HUMAN_REVIEW` or `REJECT`. If Jev does not answer, the piece goes to a person; nothing is approved without an answer. The README reports 1,000 live decisions in 4.5 s for about US$0.06. Integration evidence: [`src/modules/content-review/infrastructure/jev-decision-engine.ts`](https://github.com/Michael-Liendo/gatekeeper-30x/blob/62574094037f62c67b77f6edd91d2ecc0afe8514/src/modules/content-review/infrastructure/jev-decision-engine.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install                  # or: pnpm install
cp .env.example .env.local   # fill in the keys
npm run dev                  # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo linked by the author: [gatekeeper-30x.michaelliendo.com](https://gatekeeper-30x.michaelliendo.com)
- Playbook and pitch decks in `docs/playbook/` and `docs/pitch/`.

## Limits and data handling

Content pieces and sign-up details go to TypeSafe (and to the LLM provider for rewrites) on your keys. The repository is AGPL-3.0, so running a modified version as a network service carries source-sharing obligations.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 62574094037f](https://github.com/Michael-Liendo/gatekeeper-30x/tree/62574094037f62c67b77f6edd91d2ecc0afe8514). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
