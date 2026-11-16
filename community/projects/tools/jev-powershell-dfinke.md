# Jev PowerShell module by dfinke (typed yes/no, choice and score decisions from the PowerShell pipeline)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

PowerShell module that turns messy pipeline input into decisions scripts can act on. `New-JevYesNoQuestion` and `New-JevQuestion` build Noul, Choice and Score questions; `Invoke-Jev` sends each piped object as state and returns objects with the answers as properties, and helpers such as `Get-JevChoice`, `Get-JevScore`, `Get-JevRanking`, `Select-Jev`, `Find-Jev`, `Add-JevTag` and `Test-Jev` cover common patterns. Examples include incident and refund triage, semantic log triage, stand-up reports and release notes. By Doug Finke.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dfinke/Jev) |
| Maintainer | [dfinke](https://github.com/dfinke). Independently curated. |
| Format | PowerShell module (`Jev` 0.4.0, MIT; PowerShell Gallery) |
| Requirements | PowerShell 7 and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/dfinke/Jev/blob/cf1fd0671433dd147574ecb6477726a6903ff074/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/dfinke/status/2122331621642981819)). |
| Jev evidence | [`Private/Invoke-JevDecision.ps1`](https://github.com/dfinke/Jev/blob/cf1fd0671433dd147574ecb6477726a6903ff074/Private/Invoke-JevDecision.ps1) at the pinned commit. |

## When to use

- Add typed triage and routing decisions to PowerShell scripts and automation.
- Mismatch: generating text; Jev only answers the questions you define.

## How it works

`Private/Invoke-JevDecision.ps1` (called by `Public/Invoke-Jev.ps1`) posts the questions to `https://api.typesafe.ai/v1/systemone` with `Invoke-RestMethod` and maps the answers back onto the pipeline objects. Integration evidence: [`Private/Invoke-JevDecision.ps1`](https://github.com/dfinke/Jev/blob/cf1fd0671433dd147574ecb6477726a6903ff074/Private/Invoke-JevDecision.ps1).

## Get started

Install the module, set the key and pipe text into a question.

```sh
Install-Module Jev
$env:TYPESAFE_API_KEY = '...'
$q = New-JevYesNoQuestion -Name pageOnCall -Question 'Should the on-call engineer be paged now?' -TrueCriteria 'Customers cannot complete purchases' -FalseCriteria 'Purchases are working normally'
'Checkout is returning HTTP 503 errors.' | Invoke-Jev -Question $q
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/dfinke/Jev/blob/cf1fd0671433dd147574ecb6477726a6903ff074/README.md](https://github.com/dfinke/Jev/blob/cf1fd0671433dd147574ecb6477726a6903ff074/README.md)
- Examples: [github.com/dfinke/Jev/tree/cf1fd0671433dd147574ecb6477726a6903ff074/Examples](https://github.com/dfinke/Jev/tree/cf1fd0671433dd147574ecb6477726a6903ff074/Examples)

## Limits and data handling

Each piped object goes to TypeSafe on your key. The README output is illustrative.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit cf1fd0671433](https://github.com/dfinke/Jev/tree/cf1fd0671433dd147574ecb6477726a6903ff074). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
