# decision-drift (open daily tracker of decision models like Jev: drift, noise, robustness and calibration)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducible tracker that sends a fixed, append-only question suite to every hosted decision model on OpenRouter (TypeSafe Jev, Cloudflare Clef, Perplexity Decider, OpenAI Luna Decisions and others) and reports drift from day 1 beyond each model's noise floor, silent snapshot swaps, sensitivity to option order and paraphrase, accuracy and calibration, latency, errors and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bomliu/decision-drift) |
| Maintainer | [bomliu](https://github.com/bomliu). Independently curated. |
| Format | TypeScript (Node.js) runner, reports and static site |
| Requirements | Node.js and an OpenRouter key to run your own suite. |
| License | [MIT](https://github.com/bomliu/decision-drift/blob/7da39185b7053a9dcb7d46cd1033951406755469/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib.ts`](https://github.com/bomliu/decision-drift/blob/7da39185b7053a9dcb7d46cd1033951406755469/src/lib.ts) at the pinned commit. |

## When to use

- Watch whether a decision model you depend on changes under the same alias.
- Mismatch: part of the suite is private; public numbers come from the author's runs.

## How it works

`src/lib.ts` calls OpenRouter's Decisions API (`https://openrouter.ai/api/alpha/decisions`) for every listed decision model, including `typesafe/jev-*`. Integration evidence: [`src/lib.ts`](https://github.com/bomliu/decision-drift/blob/7da39185b7053a9dcb7d46cd1033951406755469/src/lib.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bomliu/decision-drift && cd decision-drift
# put OPENROUTER_API_KEY=... in .env
node src/run.ts --items suite/core-v1.public.jsonl --run day1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Site: [decisiondrift.dev](https://decisiondrift.dev)
- README: [github.com/bomliu/decision-drift#readme](https://github.com/bomliu/decision-drift#readme)

## Limits and data handling

Suite items go to OpenRouter and the model providers. No user data is involved.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7da39185b705](https://github.com/bomliu/decision-drift/tree/7da39185b7053a9dcb7d46cd1033951406755469). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
