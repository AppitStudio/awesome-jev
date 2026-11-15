# JevClient (PowerShell module and training deck for Jev decisions in scheduled tasks, triage scripts and approval workflows)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

PowerShell 7 module that wraps the System One API: build typed questions with `New-JevChoice`, `New-JevNoul` and score helpers, call `Invoke-Jev` with a state, and branch your script on the calibrated answers. The API key is read from a SecretManagement vault and kept as a SecureString end to end. Six examples cover ticket routing, bug severity, yes/no checks, mixed fan-out, structured change requests and gating shell commands, and an HTML training deck walks through them with real outputs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chrishuffman5/jev) |
| Maintainer | [chrishuffman5](https://github.com/chrishuffman5). Independently curated. |
| Format | PowerShell 7 module with examples and training deck |
| Requirements | PowerShell 7.0+, Microsoft.PowerShell.SecretManagement with a vault (e.g. SecretStore), and a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`JevClient/JevClient.psm1`](https://github.com/chrishuffman5/jev/blob/08fe6ef84ceebccf2ac4f68fd912219382a132d9/JevClient/JevClient.psm1) at the pinned commit. |

## When to use

- Add Jev decisions to existing PowerShell automation without parsing model text.
- Mismatch: Windows PowerShell 5.1; the module needs PowerShell 7.

## How it works

`JevClient/JevClient.psm1` posts to `https://api.typesafe.ai/v1/systemone` with `Invoke-RestMethod -Authentication Bearer` and a SecureString token; examples default to `jev-latest`, and the shell-gating example pins `jev-1.14.0` for audited decisions. Integration evidence: [`JevClient/JevClient.psm1`](https://github.com/chrishuffman5/jev/blob/08fe6ef84ceebccf2ac4f68fd912219382a132d9/JevClient/JevClient.psm1).

## Get started

Install SecretManagement, store your key in a vault, import the module and run an example.

```sh
Install-Module Microsoft.PowerShell.SecretManagement, Microsoft.PowerShell.SecretStore -Scope CurrentUser
git clone https://github.com/chrishuffman5/jev && cd jev
Import-Module ./JevClient/JevClient.psd1
./examples/01-Choice-TicketRouting.ps1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/chrishuffman5/jev/blob/08fe6ef84ceebccf2ac4f68fd912219382a132d9/README.md](https://github.com/chrishuffman5/jev/blob/08fe6ef84ceebccf2ac4f68fd912219382a132d9/README.md)
- Training deck: [chrishuffman5.github.io/jev/](https://chrishuffman5.github.io/jev/)

## Limits and data handling

States go to TypeSafe on your key. The README notes the key is waitlisted early access at the time of writing. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 08fe6ef84cee](https://github.com/chrishuffman5/jev/tree/08fe6ef84ceebccf2ac4f68fd912219382a132d9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
