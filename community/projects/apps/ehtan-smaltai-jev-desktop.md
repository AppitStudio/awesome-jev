# jev-desktop

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows desktop agent that lets Jev pick the next UI action from plain-language goals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ehtan-smaltai/jev-desktop) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/ehtan-smaltai/jev-desktop#readme) |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-27**. Requires TypeSafe and OpenRouter (or equivalent) keys. Provider usage separate; free-tier eligibility not verified. |
| Jev evidence | Upstream README documents the observe→Jev decide→act loop with TypeSafe as the decision model ([README](https://github.com/ehtan-smaltai/jev-desktop/blob/56743dd564412d8cd53b5dac71520153d18086b0/README.md)). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |
| Maintainer | [ehtan-smaltai](https://github.com/ehtan-smaltai). Independently curated. |
| Format | Python Windows agent CLI (`jevd`) using UI Automation. |
| Platform and availability | Windows only; experimental source-run CLI (`jevd`). No Store package verified. |
| Jev's role | Chooses the next UI action from observed controls; a separate LLM fills typed text. Jev does not generate free-form OS commands. |
| Requirements | Windows; TypeSafe API key; OpenRouter (or compatible) key for typed text; `uv`/install script. |
| License | [MIT](https://github.com/ehtan-smaltai/jev-desktop/blob/56743dd564412d8cd53b5dac71520153d18086b0/LICENSE). |

## When to use

Use for plain-language Windows automation experiments. Prefer safer dry-run/confirm modes first.

## How it works

Observe → Jev Choice for the next control action → optional LLM for TYPE_TEXT; dry-run and confirm modes available.

## Get started

```sh
# On Windows PowerShell (not executed on the Linux review host):
irm https://raw.githubusercontent.com/ehtan-smaltai/jev-desktop/main/install.ps1 | iex
jevd --dry-run "Open Notepad"
```

Pin revision `56743dd564412d8cd53b5dac71520153d18086b0` when reproducing this review.

## Examples and demos

Upstream README shows a Notepad walkthrough. Install/live desktop control not executed on the Linux review host.

## Limits and data handling

Experimental; controls real input devices. Sends UI observations to TypeSafe and typed text to the LLM provider. Not run on the Linux review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 56743dd](https://github.com/ehtan-smaltai/jev-desktop/tree/56743dd564412d8cd53b5dac71520153d18086b0). AI-assisted README and LICENSE inspection; live paths not executed.
