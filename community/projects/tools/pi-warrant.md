# pi-warrant (permission gate for pi where Jev clears routine tool calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One-file permission gate for the pi coding agent: static rules block or always ask for risky commands, and Jev answers three narrow yes/no questions about every other tool call so routine calls run, clear no's are blocked, and ambiguous ones are sent to you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amitkumardubey/pi-warrant) |
| Maintainer | [amitkumardubey](https://github.com/amitkumardubey). Independently curated. |
| Format | pi extension (single TypeScript file, MIT) |
| Requirements | pi and a decision-model key: `TYPESAFE_API_KEY` (`typesafe/jev-latest`) or `OPENROUTER_API_KEY` (`openrouter/typesafe/jev-1.13`). Without a key every call asks. |
| License | [MIT](https://github.com/amitkumardubey/pi-warrant/blob/f2e913eef02a558c013674cef9e2e62bf766c12a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`warrant.ts`](https://github.com/amitkumardubey/pi-warrant/blob/f2e913eef02a558c013674cef9e2e62bf766c12a/warrant.ts) at the pinned commit. |

## When to use

- Keep a check before risky agent commands without approving routine ones all day.
- Mismatch: pi only; static rules still decide the riskiest commands.

## How it works

`warrant.ts` runs deny and always-ask rules first, then asks Jev three yes/no checks against the call and current task: every check at or above 0.90 allows, any at or below 0.10 blocks, anything else asks; errors or timeouts fall back to asking. Integration evidence: [`warrant.ts`](https://github.com/amitkumardubey/pi-warrant/blob/f2e913eef02a558c013674cef9e2e62bf766c12a/warrant.ts).

## Get started

Drop the file into pi's extensions folder, set a key and reload pi.

```sh
mkdir -p ~/.pi/agent/extensions
curl -o ~/.pi/agent/extensions/warrant.ts https://raw.githubusercontent.com/amitkumardubey/pi-warrant/main/warrant.ts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/amitkumardubey/pi-warrant/blob/f2e913eef02a558c013674cef9e2e62bf766c12a/README.md](https://github.com/amitkumardubey/pi-warrant/blob/f2e913eef02a558c013674cef9e2e62bf766c12a/README.md)

## Limits and data handling

Tool-call details and your current task go to TypeSafe or OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit f2e913eef02a](https://github.com/amitkumardubey/pi-warrant/tree/f2e913eef02a558c013674cef9e2e62bf766c12a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
