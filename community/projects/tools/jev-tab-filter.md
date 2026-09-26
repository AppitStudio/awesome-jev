# Theme Tab Filter (jev-tab-filter)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome tab theme filter: Jev scores titles/URLs against your theme in one request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mpeddicord/jev-tab-filter) |
| Maintainer | [mpeddicord](https://github.com/mpeddicord). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Unpacked Chrome extension (`manifest.json`, `popup.html`, `popup.js`); no build step. |
| Requirements | Chrome 117+; TypeSafe API key pasted in extension settings. |
| License | [MIT](https://github.com/mpeddicord/jev-tab-filter/blob/090ce8c5c9a4c341d314987a088bb1bd4d80ebd0/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to clean a tab explosion around one project theme.

## How it works

One System One request with a noul question per tab; scores cached in session storage; active/pinned tabs never hidden or closed. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/mpeddicord/jev-tab-filter.git
cd jev-tab-filter
git checkout 090ce8c5c9a4c341d314987a088bb1bd4d80ebd0
# chrome://extensions → Developer mode → Load unpacked → select repo folder
```

Pin revision `090ce8c5c9a4c341d314987a088bb1bd4d80ebd0` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Tab titles, URLs, and theme go to api.typesafe.ai on click. Live extension path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 090ce8c](https://github.com/mpeddicord/jev-tab-filter/tree/090ce8c5c9a4c341d314987a088bb1bd4d80ebd0). AI-assisted README and LICENSE inspection; install/live paths not executed.
