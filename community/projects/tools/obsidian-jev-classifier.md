# Jev Classifier for Obsidian

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Obsidian plugin: classify note properties with TypeSafe Jev using an editable guide (one note or whole vault).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ItsBen321/obsidian-jev-classifier) |
| Maintainer | [ItsBen321](https://github.com/ItsBen321). Independently curated. |
| Format | Obsidian community plugin classifying note properties with TypeSafe Jev and an editable guide note. |
| Requirements | Obsidian; TypeSafe/Jev API key in plugin settings. |
| License | [MIT](https://github.com/ItsBen321/obsidian-jev-classifier/blob/532d3b52a6b7c4b8771f601565d887876ec251a5/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use to bulk-tag vault notes with constrained properties. Prefer manual tags for tiny vaults.

## How it works

Plugin sends note text + guide definitions to Jev and writes properties; includes classify-entire-vault.

## Get started

```sh
git clone https://github.com/ItsBen321/obsidian-jev-classifier.git
cd obsidian-jev-classifier
git checkout 532d3b52a6b7c4b8771f601565d887876ec251a5
# install release zip into .obsidian/plugins per upstream
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit 532d3b5](https://github.com/ItsBen321/obsidian-jev-classifier/tree/532d3b52a6b7c4b8771f601565d887876ec251a5). AI-assisted README and license inspection; install/live paths not executed.
