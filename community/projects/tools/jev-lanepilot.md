# Jev LanePilot by Daniel Pytel (asks Jev which worker lane fits a coding task in Codex or Claude Code, one worker at a time)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A dependency-free Node.js integration for Codex and Claude Code: before delegating, the main agent asks Jev which worker lane (for example Luna Low to Sol High, or Haiku, Sonnet, Opus) fits the task, applies explicit local policies for risky work and repeated failures, falls back to a fixed lane if Jev is unavailable, and runs one focused worker with a reviewable decision record.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danielmaciejpytel/jev-lanepilot) |
| Maintainer | [danielmaciejpytel](https://github.com/danielmaciejpytel). Independently curated. |
| Format | Node.js scripts + host install (agents, skills) for Codex and Claude Code |
| Requirements | Node.js 22+; Codex or Claude Code; `TYPESAFE_API_KEY` set in the host's environment. |
| License | [MIT](https://github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/src/jev.mjs) at the pinned commit. |

## When to use

- Add a small, auditable routing step in front of coding-agent delegation, with policies that override Jev for risky work.
- Mismatch: savings guarantees; the author makes no cost or accuracy promise.

## How it works

`src/jev.mjs` posts to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0` and `TYPESAFE_API_KEY`; `scripts/install.mjs` previews, then with `--apply` installs, the lane profiles into the host's config folder. Integration evidence: [`src/jev.mjs`](https://github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/src/jev.mjs).

## Get started

Run the offline tests, then preview and apply the install for one host.

```sh
git clone https://github.com/danielmaciejpytel/jev-lanepilot && cd jev-lanepilot
node --test tests/*.test.mjs
node scripts/install.mjs --host codex --target "$HOME/.codex"          # preview
node scripts/install.mjs --host codex --target "$HOME/.codex" --apply
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Validation notes: [github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/docs/VALIDATION.md](https://github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/docs/VALIDATION.md)
- Polish README: [github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/README.pl.md](https://github.com/danielmaciejpytel/jev-lanepilot/blob/42b2e5bd71204b7c1d21a7b13fa149314ca96d57/README.pl.md)

## Limits and data handling

Task descriptions are sent to TypeSafe. The author's validation was a small synthetic Codex check (7/7 Jev cases, 3/3 policy cases) on Windows; it is not evidence of production accuracy. Model IDs depend on your host account.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 42b2e5bd7120](https://github.com/danielmaciejpytel/jev-lanepilot/tree/42b2e5bd71204b7c1d21a7b13fa149314ca96d57). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
