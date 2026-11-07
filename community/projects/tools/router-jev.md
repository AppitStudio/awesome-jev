# router-jev (Claude Code hook that uses TypeSafe Jev to route tasks across Claude, Codex and Antigravity)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hook and skill that classifies each task's weight with TypeSafe Jev and routes it to Claude, Codex or Antigravity based on subscription and quota.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alejandroparis17/router-jev) |
| Maintainer | [alejandroparis17](https://github.com/alejandroparis17). Independently curated. |
| Format | Claude Code hook + skill (Node.js, MIT) |
| Requirements | Node.js, Claude Code, optional Codex/Antigravity CLIs, and a TypeSafe API key. |
| License | [MIT](https://github.com/alejandroparis17/router-jev/blob/5a606077959b9a12b7ff9a41f29865147a5a1a47/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.js`](https://github.com/alejandroparis17/router-jev/blob/5a606077959b9a12b7ff9a41f29865147a5a1a47/jev.js) at the pinned commit. |

## When to use

- Send heavy reasoning to the strongest model and edits to cheaper ones.
- Use multiple coding subscriptions without manual switching.
- Mismatch: v0.1 single-author tool; README notes agent obedience is not proven.

## How it works

`jev.js` posts the task description to `https://api.typesafe.ai/v1/systemone` (key from ROUTER_JEV_KEY, Keychain or file) and maps typed answers to a routing tier. Integration evidence: [`jev.js`](https://github.com/alejandroparis17/router-jev/blob/5a606077959b9a12b7ff9a41f29865147a5a1a47/jev.js).

## Get started

Clone, run the installer per README, and store your TypeSafe key.

```sh
git clone https://github.com/alejandroparis17/router-jev.git && cd router-jev
export TYPESAFE_API_KEY=...
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/alejandroparis17/router-jev/blob/5a606077959b9a12b7ff9a41f29865147a5a1a47/README.md](https://github.com/alejandroparis17/router-jev/blob/5a606077959b9a12b7ff9a41f29865147a5a1a47/README.md)

## Limits and data handling

Task text is sent to TypeSafe on your key; the README documents what was and was not measured.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 5a606077959b](https://github.com/alejandroparis17/router-jev/tree/5a606077959b9a12b7ff9a41f29865147a5a1a47). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
