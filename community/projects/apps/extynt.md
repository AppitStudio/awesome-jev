# extynt (After Effects plugin and MCP server: plain-language motion design with optional Jev checks)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Native After Effects plugin for macOS and Windows: describe a motion-design change in plain language, a model proposes a typed plan, and extynt validates, previews, applies it in one undo group and verifies the result; Claude Code and Codex can drive the same project over MCP, and small closed questions can optionally be answered by Jev when it is confident.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/extynt-plugin/extynt) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://github.com/extynt-plugin/extynt/releases) |
| Pricing and access | Open source (MIT); signed installers are a free download. Model and optional Jev usage is billed by your providers. Checked 2026-10-27. |
| Jev evidence | [`packages/decide/src/jev.ts`](https://github.com/extynt-plugin/extynt/blob/51017b3ca43073e3b1c27cd43f77a163be0fd3b5/packages/decide/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [extynt-plugin](https://github.com/extynt-plugin). Independently curated. |
| Format | After Effects plugin with local service and MCP server |
| Platform and availability | macOS and Windows; After Effects 25 and 26; signed installers on GitHub Releases (0.1.0, early). |
| Jev's role | Optional decision model for small closed questions (which effect was named, is the job finished); deterministic code answers by default. |
| Requirements | After Effects 25 or 26; a model provider of your choice (or local Ollama); a TypeSafe API key only for the optional Jev decisions. |
| License | [MIT](https://github.com/extynt-plugin/extynt/blob/51017b3ca43073e3b1c27cd43f77a163be0fd3b5/LICENSE) |

## When to use

- Make After Effects changes from plain language with preview and undo.
- Let coding agents edit motion-design projects safely over MCP.
- Mismatch: Jev is optional; version 0.1.0.

## How it works

`packages/decide/src/jev.ts` targets `https://api.typesafe.ai` with `jev-latest` through the System One dialect in `packages/decide/src/system-one.ts`; answers below the confidence bar fall back to deterministic code. Integration evidence: [`packages/decide/src/jev.ts`](https://github.com/extynt-plugin/extynt/blob/51017b3ca43073e3b1c27cd43f77a163be0fd3b5/packages/decide/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# install the signed build from the Releases page, restart After Effects, open Window > extynt
# optional: add TYPESAFE_API_KEY under Settings → Model → Decision model
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/extynt-plugin/extynt/releases](https://github.com/extynt-plugin/extynt/releases)
- README: [github.com/extynt-plugin/extynt#readme](https://github.com/extynt-plugin/extynt#readme)

## Limits and data handling

Project data goes only to the model provider you configure, and to Jev only if a key is set. The Adobe SDK is not redistributed.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 51017b3ca430](https://github.com/extynt-plugin/extynt/tree/51017b3ca43073e3b1c27cd43f77a163be0fd3b5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
