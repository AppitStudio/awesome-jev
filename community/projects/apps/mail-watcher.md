# mail-watcher

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted Cloudflare Email Worker that redacts incoming mail, lets Jev pick a per-watch category, and forwards, drops, or notifies accordingly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/farhaduneci/mail-watcher) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/farhaduneci/mail-watcher#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-14. |
| Jev evidence | [`src/jev.ts`](https://github.com/farhaduneci/mail-watcher/blob/b29fa4090a874964638c242ffa2551a2be1927eb/src/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [farhaduneci](https://github.com/farhaduneci). Independently curated. |
| Format | Self-hosted Cloudflare Email Worker with a read-only dashboard (TypeScript) |
| Platform and availability | Self-hosted Cloudflare Worker (source build) |
| Jev's role | Jev picks the category for each redacted email; code executes the mapped action and fallbacks. |
| Requirements | Cloudflare domain with Email Routing, Node 22+, TypeSafe API key; an LLM key for optional notification notes. |
| License | [MIT](https://github.com/farhaduneci/mail-watcher/blob/b29fa4090a874964638c242ffa2551a2be1927eb/LICENSE) |

## When to use

- Route mail for several addresses on your own domain into forward / drop / notify actions described in one YAML file.
- Get phone notifications only for mail that matters, with redacted text sent to models.
- Mismatch: requires your own Cloudflare account and domain; not a hosted inbox service.

## How it works

A redactor replaces links, contact details, codes and account numbers with placeholders before any model sees the text. Jev then chooses one of the watch's plain-language categories with a probability for each; doubtful results take an `uncertain` path and a Jev failure falls back to `on_error` forwarding plus an alert. Code runs the category's action, and a separate LLM only writes the short notification note. Every message is recorded in a D1 ledger. Integration evidence: [`src/jev.ts`](https://github.com/farhaduneci/mail-watcher/blob/b29fa4090a874964638c242ffa2551a2be1927eb/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp mail-watcher.example.yaml mail-watcher.yaml
cp wrangler.example.jsonc wrangler.jsonc
npx wrangler login
npm run setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Daily self-test runs a canned email through the full pipeline (documented upstream).
- Example config: `mail-watcher.example.yaml`.

## Limits and data handling

Redacted mail text is sent to TypeSafe (and to the configured LLM for notes); raw `.eml` files can be kept in your R2 bucket. Runs on your Cloudflare account and bills there.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit b29fa4090a87](https://github.com/farhaduneci/mail-watcher/tree/b29fa4090a874964638c242ffa2551a2be1927eb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
