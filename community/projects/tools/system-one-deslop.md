# system-one-deslop (measure the 'model accent' in AI-written prose with Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research toolkit that has Jev answer narrow questions about each sentence (a general maxim? a three-part series? a disclaimer?), counts the habits per thousand words, compares them with pre-LLM technical posts, and packages a writing brief as an agent skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jomi-se/system-one-deslop) |
| Maintainer | [jomi-se](https://github.com/jomi-se). Independently curated. |
| Format | TypeScript CLI, research harness and agent skill |
| Requirements | Node.js; a TypeSafe API key. |
| License | [MIT](https://github.com/jomi-se/system-one-deslop/blob/8036fd360e7553ca95d461135873fe3fe8cf5797/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/audit.ts`](https://github.com/jomi-se/system-one-deslop/blob/8036fd360e7553ca95d461135873fe3fe8cf5797/src/audit.ts) at the pinned commit. |

## When to use

- Check a draft's rate of quotable rules and other habits against human posts.
- Reuse the question catalogues and findings for your own writing research.
- Mismatch: the author's own note says the automatic rewriting approach does not work; the check and the brief are the useful parts.

## How it works

`src/audit.ts` uses `@typesafe-ai/sdk` to ask one set of yes/no and choice questions per sentence, and code computes per-habit rates with 90% intervals against a 13-post human baseline. Integration evidence: [`src/audit.ts`](https://github.com/jomi-se/system-one-deslop/blob/8036fd360e7553ca95d461135873fe3fe8cf5797/src/audit.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
cp .env.example .env    # TYPESAFE_API_KEY
npm run check -- draft.md --genre "blog post" --audience "Backend engineers"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Findings: [github.com/jomi-se/system-one-deslop/blob/main/eval/FINDINGS.md](https://github.com/jomi-se/system-one-deslop/blob/main/eval/FINDINGS.md)
- README: [github.com/jomi-se/system-one-deslop#readme](https://github.com/jomi-se/system-one-deslop#readme)

## Limits and data handling

Draft sentences are sent to TypeSafe. Findings are the authors' own first-night results and were not reproduced.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 8036fd360e75](https://github.com/jomi-se/system-one-deslop/tree/8036fd360e7553ca95d461135873fe3fe8cf5797). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
