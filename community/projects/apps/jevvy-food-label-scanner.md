# Jevvy AI: Food Label Scanner by Yash Patidar (iPhone app that scores a food label with Jev and gives a verdict, reasons and swaps)

[All projects](../README.md) · [iOS apps](README.md#ios-apps)

A friendly food-label scanner for iPhone. Point the camera at a barcode, or snap the nutrition label and ingredients, and Jevvy answers with Yum or bleh, a score out of 100 and one plain line about why. You pick who you're scanning for (baby and toddler, kid, teen, adult or senior) and the limits change with it; you can add goals and rules such as vegan, no nuts or sugar under 10 g, ask a question about a product, compare two packs, judge a whole basket and share a result card. Product data comes from Open Food Facts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://jevvyai.app) |
| Tags | `Closed source` · `Free` |
| Product homepage | [jevvyai.app](https://jevvyai.app) |
| Pricing and access | Free, with no account, ads or tracking ([App Store](https://apps.apple.com/us/app/jevvy-ai-food-label-scanner/id6836675657); the [site](https://jevvyai.app) FAQ says "Jevvy is free to use"; checked 2026-11-23). No sign-up or download was done for this listing. |
| Jev evidence | Vendor statements: the [App Store listing](https://apps.apple.com/us/app/jevvy-ai-food-label-scanner/id6836675657) says "Scores are made by the Jev AI", the [website](https://jevvyai.app) says the label is "Scored by Jev AI", and the maker's [launch post on X](https://x.com/yash_patidar_ai/status/2124664321011769806) (2026-11-23) thanks @typesafeai. The implementation was not inspected. |
| Disclosure | Closed source, free app. Source was not inspected; Jev use is the maker's public statement, not independently observed API traffic. Independently curated for Awesome Jev; no affiliation or commercial relationship with the maker. Inclusion is not an endorsement. Discovered via X ([post](https://x.com/yash_patidar_ai/status/2124664321011769806)). |
| Maintainer | Yash Patidar (App Store seller; [@yash_patidar_ai](https://x.com/yash_patidar_ai/status/2124664321011769806) on X). |
| Format | iPhone app (App Store). |
| Platform and availability | iPhone (iOS 26 or later; also listed for Apple silicon Macs and visionOS); App Store release. No Android app yet. |
| Jev's role | Per the maker: Jev weighs the whole label (Open Food Facts data or a label photo) and produces the score, checked against UK traffic-light limits for sugar, salt and fat. Which other models, if any, write the explanations or answer questions was not stated. |
| Requirements | An iPhone on iOS 26 or later; camera access, and permission to send scan details and photos to Jevvy's server for scoring. |
| License | Proprietary app. No public repository found. |

## When to use

Use Jevvy if you want a quick, explained verdict on a packaged food at the shelf, tuned to the age of the person eating it. It is a consumer app, not a library. Mismatch: allergy or medical decisions; the maker says it gives general guidance only and can make mistakes.

## How it works

Per the App Store listing, scan details and photos are sent, with your permission, to Jevvy's server, where the Jev AI makes the score; photos are not stored and scan history stays on the phone. Scores follow published nutrition guidance (UK traffic-light limits), and the result shows the reasons (sugar, salt, saturated fat, protein, fibre and more) plus better picks from the same shelf. No API calls, questions or thresholds were observed for this listing.

## Get started

This path follows the public App Store listing; it was not executed.

1. Install [Jevvy AI: Food Label Scanner](https://apps.apple.com/us/app/jevvy-ai-food-label-scanner/id6836675657) from the App Store.
2. Choose who you're scanning for and any goals or rules.
3. Scan a barcode, or take a photo of the label when there isn't one, and read the verdict and reasons.

## Examples and demos

- [Product website with example verdicts](https://jevvyai.app) (vendor material).
- [Launch post on X](https://x.com/yash_patidar_ai/status/2124664321011769806) (maker's post with screenshots).

## Limits and data handling

Closed source: how Jev is called, which questions it gets and how the score and lines are produced were not inspected, and "Jev AI" is the maker's wording. Scan details and photos go to Jevvy's server when you allow it, and you can turn this off or delete your data in Settings ([privacy policy](https://jevvyai.app/privacy)). Guidance only, not medical advice; always read the pack for allergies.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) with AI assistance. Primary sources: the [App Store listing](https://apps.apple.com/us/app/jevvy-ai-food-label-scanner/id6836675657) and [jevvyai.app](https://jevvyai.app) (both fetched 2026-11-23) and the maker's [X post](https://x.com/yash_patidar_ai/status/2124664321011769806) (2026-11-23). No download, sign-up or live use. Catalog de-dupe found an unrelated existing tool also named Jevvy (timbrinded/jevvy); this is a different product.
