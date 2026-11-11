# tonone (Claude Code agent team with an opt-in Jev skill gate)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin with specialist agents that has an opt-in skill gate asking Jev which skills fit a project, plus an opt-in Jev-driven browser exploration helper.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tonone-ai/tonone) |
| Maintainer | [tonone-ai](https://github.com/tonone-ai). Independently curated. |
| Format | Claude Code plugin (JavaScript/Python, MIT) |
| Requirements | Claude Code, plus your own TypeSafe key with `TONONE_GATE_JEV=1` (or `TONONE_JEV_ULTRAFAST=1`). |
| License | [MIT](https://github.com/tonone-ai/tonone/blob/117b48ffd82ffc8429954da42f2bf062e84e1b26/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev/client.js`](https://github.com/tonone-ai/tonone/blob/117b48ffd82ffc8429954da42f2bf062e84e1b26/lib/jev/client.js) at the pinned commit. |

## When to use

- Gate which agent skills load for a project with a typed check.
- Explore a local web app with a Jev-driven browser loop.
- Mismatch: Jev features are opt-in flags; the rest of the plugin runs on Claude.

## How it works

`lib/jev/client.js` calls `/v1/systemone`; `hooks/tonone-skill-gate.js` uses it when `TONONE_GATE_JEV=1`, and `lib/jev-ultrafast` drives `/proof-explore` when `TONONE_JEV_ULTRAFAST=1`. Integration evidence: [`lib/jev/client.js`](https://github.com/tonone-ai/tonone/blob/117b48ffd82ffc8429954da42f2bf062e84e1b26/lib/jev/client.js).

## Get started

Install the plugin in Claude Code, then set the opt-in flag and your TypeSafe key.

```sh
claude plugin install tonone@tonone-ai
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tonone-ai/tonone/blob/117b48ffd82ffc8429954da42f2bf062e84e1b26/README.md](https://github.com/tonone-ai/tonone/blob/117b48ffd82ffc8429954da42f2bf062e84e1b26/README.md)

## Limits and data handling

With the flag on, project signals (dependency names, directory shape, package description) or visited page descriptions go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 117b48ffd82f](https://github.com/tonone-ai/tonone/tree/117b48ffd82ffc8429954da42f2bf062e84e1b26). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
