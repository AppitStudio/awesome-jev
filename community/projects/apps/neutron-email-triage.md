# Neutron Email Triage

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Jev-first email classifier for Proton Mail through Proton Mail Bridge, with a Windows Electron GUI and a source CLI: dry-run by default, with optional moves to trash or archive above a confidence threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Geneonosis/neutron-email-triage) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Geneonosis/neutron-email-triage#readme) (source-built; no separate product site verified). |
| Pricing and access | Free preview installer and source build; you need a Proton plan with Bridge and pay your own TypeSafe usage. Checked 2026-10-17. |
| Jev evidence | [`worker.ts`](https://github.com/Geneonosis/neutron-email-triage/blob/11ab2f7df3a88a33122202f3b542dd981a8374b1/worker.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Geneonosis](https://github.com/Geneonosis). Independently curated. |
| Format | Electron desktop app (Windows x64 preview installer) and Node CLI |
| Platform and availability | Windows x64 (preview installer, v0.1.0 pre-release); source CLI elsewhere is unofficial |
| Jev's role | Jev classifies each Proton Mail message so the app can keep, archive or trash it. |
| Requirements | Windows x64 for the GUI (Node.js 20+ for the source CLI), Proton Mail Bridge with a plan that supports it, a TypeSafe API key. |
| License | [MIT](https://github.com/Geneonosis/neutron-email-triage/blob/11ab2f7df3a88a33122202f3b542dd981a8374b1/LICENSE) |

## When to use

- Triage a Proton Mail inbox without giving a cloud service your mailbox password; Bridge stays local.
- Review proposed decisions in dry-run, then let it move mail above a trash threshold of 0.9 or higher.
- Mismatch: Windows-only GUI for now; macOS and Linux GUIs are planned with no date. Independent and unofficial.

## How it works

`worker.ts` reads messages over Bridge's local IMAP and sends each to `https://api.typesafe.ai/v1/systemone` with the model pinned to `jev-1.14.0`, since thresholds are calibrated against that version; the body is included only when you enable it. Decisions are logged to a history file, and moves need `--execute`. Integration evidence: [`worker.ts`](https://github.com/Geneonosis/neutron-email-triage/blob/11ab2f7df3a88a33122202f3b542dd981a8374b1/worker.ts).

## Get started

From the upstream README (not run on the review host). A preview Windows installer is on GitHub Releases; from source:

```sh
npm ci
npm run build
# set PROTON_MAIL_BRIDGE_USERNAME, PROTON_MAIL_BRIDGE_PASSWORD and TYPESAFE_AI_API_KEY
npm run run -- --limit 20 --json   # dry-run by default
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Preview installer: [github.com/Geneonosis/neutron-email-triage/releases](https://github.com/Geneonosis/neutron-email-triage/releases)
- CLI flags and setup steps in the README.

## Limits and data handling

Email headers (and bodies only with `--include-body`) go to TypeSafe on your key. Bridge credentials are read from environment variables; the app does not load a `.env` file.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 11ab2f7df3a8](https://github.com/Geneonosis/neutron-email-triage/tree/11ab2f7df3a88a33122202f3b542dd981a8374b1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
