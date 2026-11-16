# PowerJev by huntsman95 (PowerShell module that builds Jev decision requests in the pipeline and returns typed JevResponse objects)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

PowerShell 7.2+ module for System One decision requests: create a connection with `Set-JevConnection` (TypeSafe, OpenRouter or a local endpoint), pipe it through `Add-JevQuestion` for Choice, Noul or Score questions and `Set-JevState`, then `Invoke-JevDecision` sends all questions in one call. Each response becomes a `JevResponse` object with a default display of decisions, model and provider, so you can filter results with standard PowerShell commands.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/huntsman95/PowerJev) |
| Maintainer | [huntsman95](https://github.com/huntsman95). Independently curated. |
| Format | PowerShell 7.2+ module |
| Requirements | PowerShell 7.2 or later and a TypeSafe or OpenRouter API key (or a local endpoint that accepts decision requests). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Jev.psm1`](https://github.com/huntsman95/PowerJev/blob/bd6d630805ed34ffe5f37be31ec3708f39eed9cc/Jev.psm1) at the pinned commit. |

## When to use

- Add typed decisions to PowerShell scripts with pipeline-friendly objects.
- Mismatch: Windows PowerShell 5.1; it needs PowerShell 7.2+.

## How it works

`Jev.psm1` defaults to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, switches to OpenRouter's `~typesafe/jev-latest` route, or takes a full local endpoint URL; the key is passed as a SecureString. Integration evidence: [`Jev.psm1`](https://github.com/huntsman95/PowerJev/blob/bd6d630805ed34ffe5f37be31ec3708f39eed9cc/Jev.psm1).

## Get started

Import the module, create a connection and send a decision.

```sh
git clone https://github.com/huntsman95/PowerJev && cd PowerJev
Import-Module ./Jev.psd1
$jev = Set-JevConnection -Provider TypeSafe -ApiKey (Read-Host 'TypeSafe API key' -AsSecureString)
$jev | Add-JevQuestion -Name urgent -Noul -Instructions 'Does this need immediate action?' | Set-JevState -State 'The payment system is down.' | Invoke-JevDecision
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/huntsman95/PowerJev/blob/bd6d630805ed34ffe5f37be31ec3708f39eed9cc/README.md](https://github.com/huntsman95/PowerJev/blob/bd6d630805ed34ffe5f37be31ec3708f39eed9cc/README.md)

## Limits and data handling

States go to TypeSafe, OpenRouter or your local endpoint on your key. New, small module (four files). No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit bd6d630805ed](https://github.com/huntsman95/PowerJev/tree/bd6d630805ed34ffe5f37be31ec3708f39eed9cc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
