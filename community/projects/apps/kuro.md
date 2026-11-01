# Kuro (Chrome reading aid for ADHD with bold word starts, a focus reader and optional Jev paragraph triage)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 Chrome extension that bolds the start of every word, enlarges the paragraph you are reading while the rest of the page dims, and optionally summarizes dense pages. Jev scores how dense each paragraph is and whether it carries the argument, so only the right paragraphs are turned into bullets or marked in the margin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/builtbyd3v/kuro) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/builtbyd3v/kuro#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-01. |
| Jev evidence | [`src/ai/jev.ts`](https://github.com/builtbyd3v/kuro/blob/eb96dd65cda932f4328463fae5d7ce09b0ac4f3e/src/ai/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [builtbyd3v](https://github.com/builtbyd3v). Independently curated. |
| Format | Chrome extension (TypeScript, Manifest V3) |
| Platform and availability | Chrome (load unpacked). |
| Jev's role | Scores paragraph density and importance to decide what to summarize or mark. |
| Requirements | Chrome; optional TypeSafe and Anthropic keys for AI summaries. |
| License | [MIT](https://github.com/builtbyd3v/kuro/blob/eb96dd65cda932f4328463fae5d7ce09b0ac4f3e/LICENSE) |

## When to use

- Read long articles with fewer places to lose your place.
- Mismatch: bolding and the focus reader need no AI; Jev only triages paragraphs for the optional summaries.

## How it works

`src/ai/jev.ts` calls TypeSafe `POST /v1/systemone` with `jev-latest`, asking per paragraph a density score and whether it is key to the argument; a generative model writes the summaries. Integration evidence: [`src/ai/jev.ts`](https://github.com/builtbyd3v/kuro/blob/eb96dd65cda932f4328463fae5d7ce09b0ac4f3e/src/ai/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run build
# chrome://extensions > Developer mode > Load unpacked > select dist/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README with screenshots: [github.com/builtbyd3v/kuro#readme](https://github.com/builtbyd3v/kuro#readme)

## Limits and data handling

With AI summaries on, paragraph text goes to TypeSafe and Anthropic using your keys. Off by default per site. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit eb96dd65cda9](https://github.com/builtbyd3v/kuro/tree/eb96dd65cda932f4328463fae5d7ce09b0ac4f3e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
