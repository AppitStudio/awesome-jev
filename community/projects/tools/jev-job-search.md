# jev-job-search (job-application agent where Jev maps every form field)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Coding-agent-driven job search for software students and new grads: it ranks public postings, fills each application in a visible Chrome window, reads every value back, and submits only what you approve; Jev makes the fixed-answer decisions and a writer model writes the sentences.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qbeka/jev-job-search) |
| Maintainer | [qbeka](https://github.com/qbeka). Independently curated. |
| Format | Node.js CLI and agent skills (TypeScript, MIT) |
| Requirements | Node.js 22+, Google Chrome, Claude Code or Codex, and an OpenRouter key (Jev is called through OpenRouter). |
| License | [MIT](https://github.com/qbeka/jev-job-search/blob/4442778f4a4962e3dd80c238fe1ba7dea68f5277/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Carrie_fusa/status/2120510806668546448)). |
| Jev evidence | [`src/jev/client.ts`](https://github.com/qbeka/jev-job-search/blob/4442778f4a4962e3dd80c238fe1ba7dea68f5277/src/jev/client.ts) at the pinned commit. |

## When to use

- Split form-mapping decisions from free-text writing in a browser agent.
- Apply to many job forms with every value read back before submit.
- Mismatch: beta, aimed at software roles in Canada, the US and remote; uses Jev via OpenRouter, not TypeSafe directly.

## How it works

`src/jev/client.ts` calls the OpenRouter Decisions API with `OPENROUTER_API_KEY`; per the README, one Jev call maps the page (which profile detail goes in each box and which option is true), and `/discover` uses Jev to rate postings. Integration evidence: [`src/jev/client.ts`](https://github.com/qbeka/jev-job-search/blob/4442778f4a4962e3dd80c238fe1ba7dea68f5277/src/jev/client.ts).

## Get started

Clone, install, copy `.env.example` to `.env` with your OpenRouter key, then run `/setup` from your coding agent.

```sh
git clone https://github.com/qbeka/jev-job-search && cd jev-job-search
npm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/qbeka/jev-job-search/blob/4442778f4a4962e3dd80c238fe1ba7dea68f5277/README.md](https://github.com/qbeka/jev-job-search/blob/4442778f4a4962e3dd80c238fe1ba7dea68f5277/README.md)

## Limits and data handling

Profile details and page fields go to OpenRouter/Jev and the writer model on your keys; profile files stay git-ignored on your machine and passwords stay in the system secret store.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 4442778f4a49](https://github.com/qbeka/jev-job-search/tree/4442778f4a4962e3dd80c238fe1ba7dea68f5277). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
