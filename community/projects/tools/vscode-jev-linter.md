# vscode-jev-linter (VS Code security linter powered by TypeSafe Jev via OpenRouter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standalone VS Code extension that sends code snippets to TypeSafe Jev through OpenRouter's System One endpoint (`~typesafe/jev-latest`) to flag potential security risks as you edit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/camegone/vscode-jev-linter) |
| Maintainer | [camegone](https://github.com/camegone). Independently curated. |
| Format | VS Code extension (TypeScript, MIT) |
| Requirements | VS Code and an OpenRouter API key with access to TypeSafe Jev / System One. |
| License | [MIT](https://github.com/camegone/vscode-jev-linter/blob/3ad85a2b8f6ffa4693425a88832afb69fa777ecf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevClient.ts`](https://github.com/camegone/vscode-jev-linter/blob/3ad85a2b8f6ffa4693425a88832afb69fa777ecf/src/jevClient.ts) at the pinned commit. |

## When to use

- Lint open files for security risks with a typed decision model.
- Prefer OpenRouter-hosted Jev without wiring TypeSafe directly.
- Mismatch: not a full SAST suite; judgments are model-assisted hints.

## How it works

`src/jevClient.ts` POSTs to `https://openrouter.ai/api/v1/systemone` with model `~typesafe/jev-latest` and returns typed findings for the extension UI. Integration evidence: [`src/jevClient.ts`](https://github.com/camegone/vscode-jev-linter/blob/3ad85a2b8f6ffa4693425a88832afb69fa777ecf/src/jevClient.ts).

## Get started

Install/build the extension per README and set an OpenRouter key in settings.

```sh
git clone https://github.com/camegone/vscode-jev-linter.git && cd vscode-jev-linter
# follow README; set OpenRouter key in VS Code settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/camegone/vscode-jev-linter/blob/3ad85a2b8f6ffa4693425a88832afb69fa777ecf/README.md](https://github.com/camegone/vscode-jev-linter/blob/3ad85a2b8f6ffa4693425a88832afb69fa777ecf/README.md)

## Limits and data handling

Selected code context is sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 3ad85a2b8f6f](https://github.com/camegone/vscode-jev-linter/tree/3ad85a2b8f6ffa4693425a88832afb69fa777ecf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
