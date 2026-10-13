# Jev Mail Triage

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Dry-run-first Proton Mail Bridge triage that uses TypeSafe Jev to flag spam and phishing before touching your mailbox.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/soderlind/jev-mail-triage) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/soderlind/jev-mail-triage#readme) (source-built; no separate commercial homepage verified). |
| Pricing and access | Free source build; uses your own TypeSafe (or documented provider) key. Checked 2026-10-14. |
| Jev evidence | [`src/jev_mail_triage/classifier.py`](https://github.com/soderlind/jev-mail-triage/blob/753d0646f144ac67d794ea5d9f874a33a32910fb/src/jev_mail_triage/classifier.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [soderlind](https://github.com/soderlind). Independently curated. |
| Format | Command-line app (Python) |
| Platform and availability | CLI with Proton Mail Bridge |
| Jev's role | Jev classifies messages for spam/phishing triage. |
| Requirements | Python; Proton Mail Bridge; TypeSafe API key. |
| License | [MIT](https://github.com/soderlind/jev-mail-triage/blob/753d0646f144ac67d794ea5d9f874a33a32910fb/LICENSE) |

## When to use

- Use when you need: Dry-run-first Proton Mail Bridge triage that uses TypeSafe Jev to flag spam and …
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/jev_mail_triage/classifier.py`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/jev_mail_triage/classifier.py.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 753d0646f144](https://github.com/soderlind/jev-mail-triage/tree/753d0646f144ac67d794ea5d9f874a33a32910fb). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
