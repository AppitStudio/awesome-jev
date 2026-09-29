# Movo

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Compact Linux desktop computer-use agent built for TypeSafe Jev: observe → typed decide → act → verify.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/truehannan/movo) |
| Maintainer | [truehannan](https://github.com/truehannan). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python desktop agent (PySide6 UI, AT-SPI observer). |
| Requirements | Linux Debian-family only per upstream; TypeSafe Jev access; accessibility permissions. |
| License | [MIT](https://github.com/truehannan/movo/blob/ff77d8bafbf5b7c9b2df0eb71b590bef1f2c228b/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use for Jev-native Linux desktop automation. Prefer browser-only tools (Jev Ultrafast, etc.) for web tasks.

## How it works

Builds 5–20 typed UI candidates from the accessibility tree; Jev answers structured questions; an executor applies actions with verification. Planner handles text/key arguments without Jev. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/truehannan/movo.git
cd movo
git checkout ff77d8bafbf5b7c9b2df0eb71b590bef1f2c228b
# follow upstream README for Debian/Ubuntu install and TypeSafe key
```

Pin revision `ff77d8bafbf5b7c9b2df0eb71b590bef1f2c228b` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Debian-family only. Live desktop/Jev automation not run on the review host. Desktop UI state may be sent to TypeSafe when live.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit ff77d8b](https://github.com/truehannan/movo/tree/ff77d8bafbf5b7c9b2df0eb71b590bef1f2c228b). AI-assisted README and LICENSE inspection; install/live paths not executed.
