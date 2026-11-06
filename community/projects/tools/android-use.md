# android-use (Android control for Dim Agent / MCP with optional TypeSafe Jev decisions)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Android control stack for Dim Agent and local MCP clients with a live screen and native UI automation; optional TypeSafe Choice transport (`src/android_use/jev.py`) for paid decision calls that never retry implicitly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arcships/android-use) |
| Maintainer | [arcships](https://github.com/arcships). Independently curated. |
| Format | Python Android automation toolkit (MIT) |
| Requirements | Android device/emulator, Dim Agent or MCP client, and optionally a TypeSafe API key for Jev decisions. |
| License | [MIT](https://github.com/arcships/android-use/blob/0baab86554d537996fe93fbd00086809403b956c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/android_use/jev.py`](https://github.com/arcships/android-use/blob/0baab86554d537996fe93fbd00086809403b956c/src/android_use/jev.py) at the pinned commit. |

## When to use

- Drive Android UI from Dim Agent / MCP.
- Optionally ask TypeSafe Jev for choices on screen state.
- Mismatch: Jev is opt-in; core automation works without it.

## How it works

`src/android_use/jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` (configurable base URL) with a TypeSafe key from screen settings and never retries a paid decision implicitly. Integration evidence: [`src/android_use/jev.py`](https://github.com/arcships/android-use/blob/0baab86554d537996fe93fbd00086809403b956c/src/android_use/jev.py).

## Get started

Install per README against your emulator/device; enable Jev in screen settings with a TypeSafe key when desired.

```sh
git clone https://github.com/arcships/android-use.git && cd android-use
# follow README Dim Agent / MCP setup
# optional: configure TypeSafe API key in screen settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/arcships/android-use/blob/0baab86554d537996fe93fbd00086809403b956c/README.md](https://github.com/arcships/android-use/blob/0baab86554d537996fe93fbd00086809403b956c/README.md)

## Limits and data handling

When Jev is enabled, screen/state questions are sent to TypeSafe on your key. Paid decisions are not retried automatically.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 0baab86554d5](https://github.com/arcships/android-use/tree/0baab86554d537996fe93fbd00086809403b956c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
