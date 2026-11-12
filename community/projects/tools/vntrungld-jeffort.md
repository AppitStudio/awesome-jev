# jeffort by vntrungld (Claude Code mod where Jev sets the effort for each turn)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod that asks Jev how much effort each typed prompt needs and sends every request of that turn at that effort without changing the main model; a fork of the listed jjjjjjjjjjjjjjjjacob/jev-router that rewrites how effort is applied and masks code blocks before sending. Separate from the listed andrewstephenson-v1 Jeffort.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vntrungld/jeffort) |
| Maintainer | [vntrungld](https://github.com/vntrungld). Independently curated. |
| Format | Claude Code plugin (TypeScript, MIT) |
| Requirements | Claude Code with plugin support and a TypeSafe key; off by default until `/jev on`. |
| License | [MIT](https://github.com/vntrungld/jeffort/blob/f45228eaee06e3ffd8bdc393e8a3419fc853e586/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/lib/jev.ts`](https://github.com/vntrungld/jeffort/blob/f45228eaee06e3ffd8bdc393e8a3419fc853e586/hooks/lib/jev.ts) at the pinned commit. |

## When to use

- Save tokens by running easy turns at lower effort in Claude Code.
- Mismatch: Claude Code only; questions and policy come from upstream jev-router.

## How it works

`hooks/lib/jev.ts` posts to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0` (pinned because the upstream thresholds were tuned against it); only prompts you type are routed. Integration evidence: [`hooks/lib/jev.ts`](https://github.com/vntrungld/jeffort/blob/f45228eaee06e3ffd8bdc393e8a3419fc853e586/hooks/lib/jev.ts).

## Get started

Add the marketplace, install the plugin, then turn it on in a session.

```sh
claude plugin marketplace add vntrungld/jeffort
claude plugin install jeffort@vntrungld
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vntrungld/jeffort/blob/f45228eaee06e3ffd8bdc393e8a3419fc853e586/README.md](https://github.com/vntrungld/jeffort/blob/f45228eaee06e3ffd8bdc393e8a3419fc853e586/README.md)

## Limits and data handling

Typed prompts (pasted blocks removed, code blocks masked, truncated) go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit f45228eaee06](https://github.com/vntrungld/jeffort/tree/f45228eaee06e3ffd8bdc393e8a3419fc853e586). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
