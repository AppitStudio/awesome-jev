# Slopless (textlint-based CLI that flags AI and human writing slop in Markdown, with optional Jev semantic checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and agent skill that checks English Markdown for slop. The default run is local textlint rules (boilerplate framing, cliches, negation reframes and more) with JSON output for writing agents to iterate on. Optional Jev checks (54 across eleven families) add semantic judgments and paragraph highlights through the TypeSafe API when you select them with `--check` and set `JEV_API_KEY`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/berelevant-ai/slopless) |
| Maintainer | [berelevant-ai](https://github.com/berelevant-ai). Independently curated. |
| Format | TypeScript npm package (CLI plus Codex and Claude Code skills) |
| Requirements | Node.js and npm or pnpm; `JEV_API_KEY` only for the optional Jev checks. |
| License | [MIT](https://github.com/berelevant-ai/slopless/blob/abfe9b99021ccf6d4c1754dc7064364f730d6fb5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/adapters/jev/client.ts`](https://github.com/berelevant-ai/slopless/blob/abfe9b99021ccf6d4c1754dc7064364f730d6fb5/src/adapters/jev/client.ts) at the pinned commit. |

## When to use

- Gate AI-assisted writing in CI or an agent loop with deterministic rules, adding semantic Jev checks only where you ask for them.
- Mismatch: the README says Jev check quality varies by check and uses experimental cutoffs; the tool is English-only.

## How it works

`src/adapters/jev/client.ts` wraps the TypeSafe SDK (`@typesafe-ai/sdk`) and sends one request per paragraph with a question and probability per selected check, splitting groups that exceed size limits; whole-text checks send the full article. Integration evidence: [`src/adapters/jev/client.ts`](https://github.com/berelevant-ai/slopless/blob/abfe9b99021ccf6d4c1754dc7064364f730d6fb5/src/adapters/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -D slopless
npx slopless "docs/**/*.md"
npx slopless --check semantic-thinness:empty-takeaway draft.md   # needs JEV_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with rules, the agent-skill loop and the Jev check list: [github.com/berelevant-ai/slopless#readme](https://github.com/berelevant-ai/slopless#readme)
- npm package: [www.npmjs.com/package/slopless](https://www.npmjs.com/package/slopless)

## Limits and data handling

Jev checks send the selected writing (the whole article for whole-text checks) to TypeSafe on your key and are billed there; the default local rules send nothing. Whole-text and paragraph answers can disagree, and a missing provider answer exits with code 2. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit abfe9b99021c](https://github.com/berelevant-ai/slopless/tree/abfe9b99021ccf6d4c1754dc7064364f730d6fb5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
