# JEVsnap

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Screenshot hotkey that blacks out secrets and personal information (API keys, tokens, emails, phone numbers, names, internal hostnames, QR codes) before the image reaches your clipboard; on-device OCR and local rules first, with optional Jev text and Box checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brainstormity/jevsnap) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/brainstormity/jevsnap#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-17. |
| Jev evidence | [`desktop/src/core/jevClient.ts`](https://github.com/brainstormity/jevsnap/blob/b249546b25389baca0b49afc2fea8e4fa2ad8798/desktop/src/core/jevClient.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [brainstormity](https://github.com/brainstormity). Independently curated. |
| Format | macOS Swift menu-bar app and Electron app for Linux and Windows (source build, v0.2) |
| Platform and availability | macOS, Linux and Windows (source builds) |
| Jev's role | Optional Jev text and Box checks find sensitive words and regions that local rules miss. |
| Requirements | macOS, Linux or Windows; a TypeSafe API key for the optional AI checks. |
| License | [MIT](https://github.com/brainstormity/jevsnap/blob/b249546b25389baca0b49afc2fea8e4fa2ad8798/LICENSE) |

## When to use

- Share screenshots of terminals, dashboards or chats with less risk of leaking a key or a customer's details.
- Mismatch: no automatic redactor is perfect; it lowers the risk, it does not replace a quick look before posting.

## How it works

OCR and regex validators run on-device; the Jev text check sends only OCR text with known secrets masked, and the optional Box check sends the image only after earlier hits are blacked out. If OCR or rendering fails nothing is copied, and required AI checks cancel the capture when they cannot run. Integration evidence: [`desktop/src/core/jevClient.ts`](https://github.com/brainstormity/jevsnap/blob/b249546b25389baca0b49afc2fea8e4fa2ad8798/desktop/src/core/jevClient.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/brainstormity/JEVsnap.git && cd JEVsnap
# macOS: see macos/README.md · Linux/Windows: see desktop/README.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Shared detector test vectors: `shared/detector-cases.json`.
- Mock Jev server for tests: `tools/mock_jev_server.py`.

## Limits and data handling

Only masked OCR text (and, if you enable Box, a pre-redacted image) goes to TypeSafe on your key; screenshots are saved only after processing.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit b249546b2538](https://github.com/brainstormity/jevsnap/tree/b249546b25389baca0b49afc2fea8e4fa2ad8798). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
