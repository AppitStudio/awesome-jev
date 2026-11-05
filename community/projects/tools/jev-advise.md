# jev-advise (Claude Code plugin that shows Jev's probability next to each choice Claude offers, with optional auto-select)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that tags the options of AskUserQuestion and plain-text questions with `[jev 0.80]` probabilities and marks a `jev pick` above a confidence threshold. By default it only displays them; `auto_select` can answer for you. Claude and Jev never see each other's recommendation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PeesukaGu/jev-advise) |
| Maintainer | [PeesukaGu](https://github.com/PeesukaGu). Independently curated. |
| Format | Claude Code plugin (Node.js hook script) |
| Requirements | Claude Code, Node.js 20.12+, the `jev` CLI (`jevctl`) on PATH and a TypeSafe API key. |
| License | [MIT](https://github.com/PeesukaGu/jev-advise/blob/a91e405e553a95fd6ab2741183d168c63da5c3fd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev-advise.mjs`](https://github.com/PeesukaGu/jev-advise/blob/a91e405e553a95fd6ab2741183d168c63da5c3fd/scripts/jev-advise.mjs) at the pinned commit. |

## When to use

- Get a second, calibrated opinion on the choices Claude asks you to make.
- See how often Jev agrees with you before turning on auto-select.
- Mismatch: shipped measurements (221 answers) are the author's own; treat them as a single data point.

## How it works

A hook script reads the conversation up to your last prompt (last 3,000 characters), strips Claude's `(Recommended)` marks and asks Jev through the `jev` CLI, then adds the probability tags to what you see; `pick_threshold` defaults to 0.6. Integration evidence: [`scripts/jev-advise.mjs`](https://github.com/PeesukaGu/jev-advise/blob/a91e405e553a95fd6ab2741183d168c63da5c3fd/scripts/jev-advise.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g jevctl && jev auth login
claude plugin install jev-advise --marketplace PeesukaGu/jev-advise
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with settings and the author's agreement figures: [github.com/PeesukaGu/jev-advise/blob/a91e405e553a95fd6ab2741183d168c63da5c3fd/README.md](https://github.com/PeesukaGu/jev-advise/blob/a91e405e553a95fd6ab2741183d168c63da5c3fd/README.md)

## Limits and data handling

Recent conversation text is sent to TypeSafe on your key. `auto_select` lets Jev answer for you, so keep it off unless you trust the threshold.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit a91e405e553a](https://github.com/PeesukaGu/jev-advise/tree/a91e405e553a95fd6ab2741183d168c63da5c3fd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
