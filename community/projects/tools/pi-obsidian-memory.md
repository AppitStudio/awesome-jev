# pi-obsidian-memory (Obsidian-vault long-term memory for the Pi agent, gated by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent package that keeps preferences, project rules and lessons as Markdown notes in Obsidian, with Jev deciding which notes help each message and guarding shell commands that would edit the vault.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DavyMassoneto/pi-obsidian-memory) |
| Maintainer | [DavyMassoneto](https://github.com/DavyMassoneto). Independently curated. |
| Format | Pi package (TypeScript, MIT) |
| Requirements | Pi 1.3+, Node 22.19+, a chat model configured in Pi, and `TYPESAFE_API_KEY` for Jev (without it no notes are injected and the shell-edit guard refuses). |
| License | [MIT](https://github.com/DavyMassoneto/pi-obsidian-memory/blob/0e447d0a5b7fb4961281815fed9bdd6b40d10d98/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/domain/decision-model/endpoint.ts`](https://github.com/DavyMassoneto/pi-obsidian-memory/blob/0e447d0a5b7fb4961281815fed9bdd6b40d10d98/src/domain/decision-model/endpoint.ts) at the pinned commit. |

## When to use

- Give a Pi agent durable memory you can read and edit in Obsidian.
- Use Jev as a cheap relevance gate on which notes enter each prompt.
- Mismatch: GitHub reports the license as NOASSERTION, but the LICENSE file is the MIT text.

## How it works

The default decision model is TypeSafe `jev-latest` (`docs/config.md`); `src/usecases/relevant-memory/` asks Jev which notes are relevant using measured cutoffs, and `check-shell-edit` asks Jev once per bash/powershell call and fails closed. Integration evidence: [`src/domain/decision-model/endpoint.ts`](https://github.com/DavyMassoneto/pi-obsidian-memory/blob/0e447d0a5b7fb4961281815fed9bdd6b40d10d98/src/domain/decision-model/endpoint.ts).

## Get started

Install the package into Pi, set `TYPESAFE_API_KEY`, and follow the README's setup to point it at an Obsidian vault.

```sh
export TYPESAFE_API_KEY=...
# install per the README, then start pi
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Measured shell-edit cutoffs against jev-latest: [github.com/DavyMassoneto/pi-obsidian-memory/blob/0e447d0a5b7fb4961281815fed9bdd6b40d10d98/docs/shell-edit-cutoffs.md](https://github.com/DavyMassoneto/pi-obsidian-memory/blob/0e447d0a5b7fb4961281815fed9bdd6b40d10d98/docs/shell-edit-cutoffs.md)

## Limits and data handling

Message text and candidate note summaries go to TypeSafe on your key; notes stay in your local vault.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 0e447d0a5b7f](https://github.com/DavyMassoneto/pi-obsidian-memory/tree/0e447d0a5b7fb4961281815fed9bdd6b40d10d98). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
