# KeyFlip (Windows tray app that picks the right Hebrew or English layout per text field)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows tray app for people who type in Hebrew and English: when you focus a text field it chooses the layout from what it learned for that field, the text already there, or Jev's reading of the app, site, page title and field label, and it fixes a word you typed on the wrong layout.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kivimedia/keyflip) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/kivimedia/keyflip#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls (about $0.00002 each per the README) are billed to your TypeSafe account; the optional Haiku fixer to Anthropic. Checked 2026-10-26. |
| Jev evidence | [`src/KeyFlip/Models.cs`](https://github.com/kivimedia/keyflip/blob/c7a723eb024be4425091ce04371e718735345bda/src/KeyFlip/Models.cs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [kivimedia](https://github.com/kivimedia). Independently curated. |
| Format | Windows tray app (C#/.NET) |
| Platform and availability | Windows 10/11; source build with `dotnet publish` (no published release at review time). |
| Jev's role | Layout classifier: Jev decides Hebrew or English from the field's context when local rules cannot, above a configurable threshold (default 0.70). |
| Requirements | Windows 10 or 11 with Hebrew and English layouts; .NET 8 SDK to build; a TypeSafe API key for Jev, and optionally an Anthropic key for the word fixer. |
| License | [MIT](https://github.com/kivimedia/keyflip/blob/c7a723eb024be4425091ce04371e718735345bda/LICENSE) |

## When to use

- Stop typing gibberish after switching windows between Hebrew and English.
- Let the app learn your per-field preference.
- Mismatch: Hebrew/English only; Windows only.

## How it works

`src/KeyFlip/Models.cs` pins `jev-1.13.0` and posts the app name, site, page title, field label and up to 300 characters already in the field to `https://api.typesafe.ai/v1/systemone`. Integration evidence: [`src/KeyFlip/Models.cs`](https://github.com/kivimedia/keyflip/blob/c7a723eb024be4425091ce04371e718735345bda/src/KeyFlip/Models.cs).

## Get started

From the upstream README (not run on the review host):

```sh
dotnet publish src/KeyFlip -c Release -o "%LOCALAPPDATA%\Programs\KeyFlip"
set TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kivimedia/keyflip#readme](https://github.com/kivimedia/keyflip#readme)

## Limits and data handling

The app name, site, page title, field label and up to 300 characters already in the field go to TypeSafe (and to Anthropic when Haiku is used, including a small screen strip for the image check); password fields are skipped and keystrokes stay on your PC, per the README.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit c7a723eb024b](https://github.com/kivimedia/keyflip/tree/c7a723eb024be4425091ce04371e718735345bda). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
