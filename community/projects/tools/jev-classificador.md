# Jev Classificador (Obsidian note classification with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Obsidian plugin that sends one request to Jev to pick a field (13 options) and subfield (89 options) for the current note from a described taxonomy in English or Brazilian Portuguese, writes them to frontmatter, and can add 1 to 3 topic tags from a closed wordlist.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/matteoandradeboschi/jev-classificador) |
| Maintainer | [matteoandradeboschi](https://github.com/matteoandradeboschi). Independently curated. |
| Format | Obsidian plugin (TypeScript) |
| Requirements | Obsidian; a TypeSafe API key (stored in Obsidian SecretStorage). |
| License | [0BSD](https://github.com/matteoandradeboschi/jev-classificador/blob/3c3e2efa7329dcb78a17127c227cbb1c5da6c44e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main.ts`](https://github.com/matteoandradeboschi/jev-classificador/blob/3c3e2efa7329dcb78a17127c227cbb1c5da6c44e/src/main.ts) at the pinned commit. |

## When to use

- Keep a large vault consistently categorized.
- Show the top 3 options when Jev is unsure (below 0.6 by default).
- Mismatch: the taxonomy is the author's; edit the bundled JSON for your own.

## How it works

`src/main.ts` sends the note title, tags and up to 12,000 characters of body to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, using the taxonomy descriptions as criteria. Integration evidence: [`src/main.ts`](https://github.com/matteoandradeboschi/jev-classificador/blob/3c3e2efa7329dcb78a17127c227cbb1c5da6c44e/src/main.ts).

## Get started

From the upstream README (not run on the review host); install inside Obsidian:

```sh
# Obsidian > Settings > Community plugins > Browse > "Jev Classificador" > Install > Enable
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Privacy, taxonomy and commands in the README: [github.com/matteoandradeboschi/jev-classificador#readme](https://github.com/matteoandradeboschi/jev-classificador#readme)

## Limits and data handling

Note title, tags and body excerpt are sent to TypeSafe when you run the command; excluded folders are never read.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 3c3e2efa7329](https://github.com/matteoandradeboschi/jev-classificador/tree/3c3e2efa7329dcb78a17127c227cbb1c5da6c44e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
