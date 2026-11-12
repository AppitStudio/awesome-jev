# pi-out-classify (pi extension that trims large tool outputs to what matters, judged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

pi extension that keeps large tool results out of the agent's context: before a big output reaches the model, Jev judges each section (text, images via pi-jevisual, and PDFs converted with Docling) against the agent's goal, and irrelevant parts are replaced with a short marker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Piotr-Adamm/pi-out-classify) |
| Maintainer | [Piotr-Adamm](https://github.com/Piotr-Adamm). Independently curated. |
| Format | pi extension on npm (TypeScript, MIT) |
| Requirements | pi, a TypeSafe key in `TYPESAFE_API_KEY` or stored in pi, and uv for PDFs (Docling setup takes about 1.9 GB on first PDF read). |
| License | [MIT](https://github.com/Piotr-Adamm/pi-out-classify/blob/189f363328bee25d02e693c783079f7cfe1a50d5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classifier.ts`](https://github.com/Piotr-Adamm/pi-out-classify/blob/189f363328bee25d02e693c783079f7cfe1a50d5/src/classifier.ts) at the pinned commit. |

## When to use

- Save context in long agent sessions that read big logs, files or PDFs.
- Keep warnings and errors while dropping irrelevant sections.
- Mismatch: pi only; PDF support downloads a large Docling environment.

## How it works

`src/classifier.ts` splits outputs over the thresholds into sections and asks Jev whether each one is keep, uncertain or discard against the current goal (a `read` goal parameter, a codemode `// goal:` line or the latest user messages); only discarded sections are removed and failures keep the content. Integration evidence: [`src/classifier.ts`](https://github.com/Piotr-Adamm/pi-out-classify/blob/189f363328bee25d02e693c783079f7cfe1a50d5/src/classifier.ts).

## Get started

Install the package in pi; optionally tune thresholds in `~/.pi/agent/out-classify.json`.

```sh
pi install npm:pi-out-classify
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Piotr-Adamm/pi-out-classify/blob/189f363328bee25d02e693c783079f7cfe1a50d5/README.md](https://github.com/Piotr-Adamm/pi-out-classify/blob/189f363328bee25d02e693c783079f7cfe1a50d5/README.md)
- npm: [www.npmjs.com/package/pi-out-classify](https://www.npmjs.com/package/pi-out-classify)

## Limits and data handling

Sections of large tool outputs and the agent's goal are sent to TypeSafe; PDF extraction runs locally.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 189f363328be](https://github.com/Piotr-Adamm/pi-out-classify/tree/189f363328bee25d02e693c783079f7cfe1a50d5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
