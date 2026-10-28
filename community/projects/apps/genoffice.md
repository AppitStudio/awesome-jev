# GenOffice (open-source AI office suite whose file search can be reranked by Jev)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Free, open-source desktop office suite for Word, Excel, PowerPoint, PDF, Markdown and HTML files with a built-in AI panel, plus a `genoffice` CLI and agent skill so Claude Code, Codex and Cursor can edit real .docx/.xlsx/.pptx files locally. Its home-screen file search can switch on Jev reranking, which reads excerpts of the top 20 local hits and moves the document that actually answers the query to the top.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/genspark-ai/genoffice) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://genoffice.ai/) |
| Pricing and access | Open source (Apache-2.0); free download. Bring your own model keys; Jev reranking is billed to your OpenRouter or TypeSafe key. Checked 2026-10-28. |
| Jev evidence | [`apps/shell/src/main/file-index/decider.ts`](https://github.com/genspark-ai/genoffice/blob/b239d2e591d3fe2e7f079354f4f3d5b61f598800/apps/shell/src/main/file-index/decider.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Found through pufuna/office, a copy of this repository; the upstream genspark-ai/genoffice is listed. |
| Maintainer | [genspark-ai](https://github.com/genspark-ai). Independently curated. |
| Format | Electron desktop app (TypeScript) with CLI and agent skill |
| Platform and availability | macOS 11+, Windows 10+ (x64 and Arm) and Linux x86_64 installers from GitHub Releases. |
| Jev's role | Optional reranker for local file search: one calibrated 0-2 relevance score per document excerpt. |
| Requirements | A desktop computer; your own AI provider key for the AI panel; an OpenRouter or TypeSafe key only for Jev search reranking. |
| License | [Apache-2.0](https://github.com/genspark-ai/genoffice/blob/b239d2e591d3fe2e7f079354f4f3d5b61f598800/LICENSE) |

## When to use

- Find the file that answers a question when keyword search ranks look-alike documents first.
- Mismatch: Jev is off by default and is one of several decision-model endpoints.

## How it works

`decider.ts` sends the query and up to 20 excerpts to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) or OpenRouter (`typesafe/jev-1.13`), and also supports Perplexity, Cloudflare, local Kev and custom `/v1/systemone` servers; any invalid response keeps the local order. Integration evidence: [`apps/shell/src/main/file-index/decider.ts`](https://github.com/genspark-ai/genoffice/blob/b239d2e591d3fe2e7f079354f4f3d5b61f598800/apps/shell/src/main/file-index/decider.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# download the installer for your platform:
# https://github.com/genspark-ai/genoffice/releases/latest
# then Settings -> AI Media & Search -> Local file search -> Jev search reranking
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README search section: [github.com/genspark-ai/genoffice#readme](https://github.com/genspark-ai/genoffice#readme)
- Homepage: [genoffice.ai/](https://genoffice.ai/)

## Limits and data handling

With Jev reranking on, excerpts of the top local hits go to the chosen endpoint; the index itself stays on the device. The AI panel sends content to your configured model provider.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit b239d2e591d3](https://github.com/genspark-ai/genoffice/tree/b239d2e591d3fe2e7f079354f4f3d5b61f598800). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
