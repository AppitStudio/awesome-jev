# Sensibility

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that lets Claude ask Jev quick typed questions (does this diff match the ticket, is this command safe, did I finish) and turn the answers into an act, confirm or escalate verdict, with reusable question sets and optional risk and finish gates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rajnandan1/sensibility) |
| Maintainer | [rajnandan1](https://github.com/rajnandan1). Independently curated. |
| Format | Claude Code plugin (skill + hooks, Python helper) |
| Requirements | Claude Code, Python 3.9+, a TypeSafe API key. |
| License | [MIT](https://github.com/rajnandan1/sensibility/blob/d77be79a6d04438e873f5dfa13165853c904707f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.py`](https://github.com/rajnandan1/sensibility/blob/d77be79a6d04438e873f5dfa13165853c904707f/lib/jev.py) at the pinned commit. |

## When to use

- Check an uncommitted change against a ticket before committing.
- Turn on the risk gate so risky, destructive Bash commands stop and ask you first.
- Mismatch: both gates are off by default; verdicts are advisory checks, not a security boundary.

## How it works

The judge skill and the two hooks load a battery (saved JSON questions plus gate rules), send them to `https://api.typesafe.ai` through `lib/jev.py` with `TYPESAFE_API_KEY`, and map the probabilities to `act`, `confirm` or `escalate`. Integration evidence: [`lib/jev.py`](https://github.com/rajnandan1/sensibility/blob/d77be79a6d04438e873f5dfa13165853c904707f/lib/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
# in Claude Code:
/plugin marketplace add rajnandan1/sensibility
/plugin install sensibility@sensibility
# then in your shell profile:
export TYPESAFE_API_KEY=your-key-here
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Batteries: `batteries/`.
- Quick-start walkthrough (save and run a `comment` battery) in the README.

## Limits and data handling

Diffs, commands and ticket text you check go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit d77be79a6d04](https://github.com/rajnandan1/sensibility/tree/d77be79a6d04438e873f5dfa13165853c904707f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
