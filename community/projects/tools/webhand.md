# webhand (Claude Code skill where Claude plans the goal and Jev picks each page operation and target; Japanese)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Claude Code skill and CLI that splits web tasks between two roles: Claude plans the goal and steps, supplies input values, checks results and revises the plan, while Jev picks the operation, target and value toward the goal one page at a time. No Anthropic API key is used. The policy is adapted from jev-ultrafast (MIT). The README is in Japanese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sakamoto66/webhand) |
| Maintainer | [sakamoto66](https://github.com/sakamoto66). Independently curated. |
| Format | Claude Code skill and Node CLI (TypeScript, npm `webhand`; drives Chrome over CDP) |
| Requirements | Claude Code, Node, Node.js 22+, Google Chrome (Linux, or Windows Chrome from WSL) and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/sakamoto66/webhand/blob/33625194dffa6e0089cac14d4bb335eaa9ec7a0f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/policies/jev.ts`](https://github.com/sakamoto66/webhand/blob/33625194dffa6e0089cac14d4bb335eaa9ec7a0f/src/policies/jev.ts) at the pinned commit. |

## When to use

- Let Claude handle intent and checking while Jev handles the fast click-and-fill choices on a web page.
- Mismatch: the content of the page you operate on is sent to TypeSafe, so avoid pages with private data.

## How it works

`src/policies/jev.ts` posts the page's indexed elements to `https://api.typesafe.ai/v1/systemone` (model from `TYPESAFE_MODEL`, default `jev-latest`) and returns the next operation, target and value. Integration evidence: [`src/policies/jev.ts`](https://github.com/sakamoto66/webhand/blob/33625194dffa6e0089cac14d4bb335eaa9ec7a0f/src/policies/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin install webhand --marketplace sakamoto66/webhand
export TYPESAFE_API_KEY=...   # then restart Claude Code
npx -y webhand@0.2 catalog
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese) with the setup and role split: [github.com/sakamoto66/webhand#readme](https://github.com/sakamoto66/webhand#readme)

## Limits and data handling

The README states that the content of the page being operated is sent to TypeSafe's API; it connects to a new or saved Chrome profile, never your everyday profile, and the key is read only from the environment. The project carries a third-party MIT notice for jev-ultrafast. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 33625194dffa](https://github.com/sakamoto66/webhand/tree/33625194dffa6e0089cac14d4bb335eaa9ec7a0f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
