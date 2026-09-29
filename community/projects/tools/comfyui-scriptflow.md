# ComfyUI-ScriptFlow

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Safe Python-like ComfyUI script node that asks TypeSafe Jev yes/no, choice, and score questions to drive workflow logic.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kantan-kanto/ComfyUI-ScriptFlow) |
| Maintainer | [kantan-kanto](https://github.com/kantan-kanto). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | ComfyUI custom node (`MultiOutputScript (Jev)` and related). |
| Requirements | ComfyUI; TypeSafe SDK/key for Jev backend or local GGUF fallback per README. |
| License | [GPL-3.0](https://github.com/kantan-kanto/ComfyUI-ScriptFlow/blob/2bb6cb8717ed2e7dde146084389c6a0803bfb0d0/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when a ComfyUI graph needs typed System One branches. Prefer standalone TypeSafe scripts when you are not in ComfyUI.

## How it works

Restricted interpreter scripts call `jev.yes` / choice / score helpers; answers feed ordinary `if` routing for resolution, filenames, and other graph logic. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
cd ComfyUI/custom_nodes
git clone https://github.com/kantan-kanto/ComfyUI-ScriptFlow.git
cd ComfyUI-ScriptFlow
git checkout 2bb6cb8717ed2e7dde146084389c6a0803bfb0d0
# restart ComfyUI; install TypeSafe SDK in the ComfyUI Python env for Jev path
```

Pin revision `2bb6cb8717ed2e7dde146084389c6a0803bfb0d0` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

GPL-3.0. Live ComfyUI/TypeSafe paths not run on the review host. Scripts are sandboxed from OS/file access per upstream.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 2bb6cb8](https://github.com/kantan-kanto/ComfyUI-ScriptFlow/tree/2bb6cb8717ed2e7dde146084389c6a0803bfb0d0). AI-assisted README and LICENSE inspection; install/live paths not executed.
