# Jev Mail (Gmail extension)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Open-source Chrome/Brave extension that classifies Gmail with TypeSafe Jev — category, priority, important, needs-reply and junk as separate narrow questions — then applies `Jev/...` labels and previews safe, Trash-only cleanup with Undo; runs in the browser with your TypeSafe or OpenRouter key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KirtanUgreja/jev-mail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/KirtanUgreja/jev-mail#readme) (source-built app; no separate website verified). |
| Pricing and access | No extension fee (load unpacked from source; no Chrome Web Store listing verified). Requires your own TypeSafe or OpenRouter key; Jev usage billed by that provider. Optional dashboard needs your own Google OAuth client. Checked 2026-10-07. |
| Jev evidence | Inspected [`src/common/jev.js`](https://github.com/KirtanUgreja/jev-mail/blob/694c4fe24d0848da4ea7ee2115c00957ee200071/src/common/jev.js) and the README section *How the classification works*, which lists each question and how it is used. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [KirtanUgreja](https://github.com/KirtanUgreja). Independently curated. |
| Format | Manifest V3 Chrome/Brave extension (+ optional local dashboard) |
| Platform and availability | Chrome or Brave desktop, load unpacked from the repository; early open-source project. |
| Jev's role | Jev answers one batched request per email (category choice, priority, important, needs_reply, junk and spam signals); code turns those probabilities into labels, badges and cleanup candidates, and blocks cleanup for important or needs-reply mail. |
| Requirements | Chrome or Brave; a TypeSafe or OpenRouter API key; optionally a Google OAuth client for the dashboard and Gmail API mode. |
| License | [MIT](https://github.com/KirtanUgreja/jev-mail/blob/694c4fe24d0848da4ea7ee2115c00957ee200071/LICENSE). |

## When to use

- Auto-label Gmail into `Jev/<Category>`, `Jev/Priority/...` and `Jev/Needs Reply` while you scroll.
- Bulk-clean junk by sender with a preview, Trash-only deletion and Undo, protected by Jev's important/needs-reply answers.
- Mismatch: email content leaves the browser for TypeSafe/OpenRouter; not a store-distributed extension.

## How it works

For each message the extension sends one request with several narrow questions instead of a single "is this spam?" question (the README explains why). [`src/common/jev.js`](https://github.com/KirtanUgreja/jev-mail/blob/694c4fe24d0848da4ea7ee2115c00957ee200071/src/common/jev.js) calls `api.typesafe.ai/v1/systemone` or OpenRouter's `/v1/systemone`; results are stored with per-question confidence and drive labels and cleanup rules in code.

## Get started

Load the extension and paste a key:

```sh
git clone https://github.com/KirtanUgreja/jev-mail.git
# chrome://extensions → Developer mode → Load unpacked → select jev-mail/
# toolbar icon → gear → paste TypeSafe or OpenRouter key → Test → Save
# open Gmail; rows get badges as you scroll
```

Each classified email is a Jev request billed to your key.

## Examples and demos

- README *Using it*, *Labels* and *Cleanup* sections with the side-panel workflow.
- README question table under *How the classification works*.

## Limits and data handling

Email subjects/snippets/bodies are sent to the chosen provider. Cleanup only moves mail to Trash and offers Undo; starred/important mail is protected (upstream statement). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 694c4fe24d08](https://github.com/KirtanUgreja/jev-mail/tree/694c4fe24d0848da4ea7ee2115c00957ee200071). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
