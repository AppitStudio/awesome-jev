# Switchyard

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

macOS menu-bar app that opens every link in the right Dia/Chrome profile; TypeSafe Jev decides uncovered links and confident answers become local rules.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kevinebaugh/switchyard) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/kevinebaugh/switchyard#readme) |
| Pricing and access | Free source build; no app purchase fee. TypeSafe key for Jev routing; provider usage may incur charges. Checked 2026-10-01. |
| Jev evidence | [Upstream README](https://github.com/kevinebaugh/switchyard/blob/dd97264b1cbf4a52057f349c5091410d8b235d4d/README.md): uncovered links ask TypeSafe Jev which Dia/Chrome profile to use; confident answers become local rules. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. macOS build/live routing not run on the Linux review host. Distinct from FrancoisChastel/jev-router Switchyard-style naming. |
| Maintainer | [kevinebaugh](https://github.com/kevinebaugh). Independently curated. |
| Format | Swift · macOS menu-bar app (MIT) |
| Platform and availability | macOS menu-bar source build; Dia and Chrome supported. |
| Jev's role | Jev chooses profile + URL scope for links without a local rule; code opens the browser profile and saves rules above confidence. |
| Requirements | macOS; TypeSafe API key; Dia or Chrome. |
| License | [MIT](https://github.com/kevinebaugh/switchyard/blob/dd97264b1cbf4a52057f349c5091410d8b235d4d/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when you want every link opened in the right browser profile, with Jev learning rules you can edit.

## How it works

Switchyard is the default browser. Local rules win first; otherwise Jev answers profile + scope questions on a redacted URL; high confidence becomes a learned rule.

## Get started

```sh
git clone https://github.com/kevinebaugh/switchyard.git
cd switchyard
git checkout dd97264b1cbf4a52057f349c5091410d8b235d4d
# follow upstream README for macOS build and TypeSafe key setup
```

## Examples and demos

Upstream README describes Recent/Rules/Settings flows. No live macOS routing was run on the review host.

## Limits and data handling

Only host, short path prefixes, and query parameter *names* are sent to Jev; values stay local. Live paths not executed on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit dd97264b1cbf](https://github.com/kevinebaugh/switchyard/tree/dd97264b1cbf4a52057f349c5091410d8b235d4d). AI-assisted README + LICENSE inspection; macOS build/live paths not executed.
