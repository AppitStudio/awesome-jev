# android-jev (FZ2000)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server and skill that let an agent drive an Android phone naturally over adb with Jev action choice.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FZ2000/android-jev) |
| Maintainer | [FZ2000](https://github.com/FZ2000). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | MCP server (`run_task`) + agent skill over adb. |
| Requirements | USB-debugging Android device; Python 3.11+ / uv; macOS Vision optional for picture route; TypeSafe key per upstream. |
| License | [MIT](https://github.com/FZ2000/android-jev/blob/9383a1054171754fef5ba216e2010fd839218ea5/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from listed jev-android and jevdevice. |

## When to use

Use when an MCP client should drive a physical Android device with Jev selecting actions.

## How it works

Reads the phone UI, asks Jev for the next action, executes over adb, and reports whether the goal was achieved. Distinct from listed jev-android and jevdevice. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/FZ2000/android-jev.git
cd android-jev
git checkout 9383a1054171754fef5ba216e2010fd839218ea5
# follow upstream README for adb + MCP client setup; configure credentials as documented
```

Pin revision `9383a1054171754fef5ba216e2010fd839218ea5` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Verified upstream mainly on Pixel 8a. Live phone/Jev paths not run on the review host. Distinct from jev-android and jevdevice.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 9383a10](https://github.com/FZ2000/android-jev/tree/9383a1054171754fef5ba216e2010fd839218ea5). AI-assisted README and LICENSE inspection; install/live paths not executed.
