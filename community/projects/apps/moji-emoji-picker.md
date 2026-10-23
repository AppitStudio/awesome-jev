# Moji (macOS emoji picker with optional Jev ranking)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS emoji picker: type `:` and a few letters in any app. Search runs locally; with a TypeSafe key, Jev reorders the suggestions to the emoji you most likely mean.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/beckyisj/moji) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/beckyisj/moji#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev ranking uses your own TypeSafe key (the README estimates about $0.0001 per lookup). Checked 2026-10-24. |
| Jev evidence | [`Sources/MojiCore/Jev.swift`](https://github.com/beckyisj/moji/blob/199e56d87d34d43bfa5268a322abcfa8fa669313/Sources/MojiCore/Jev.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [beckyisj](https://github.com/beckyisj). Independently curated. |
| Format | Native macOS app (Swift) |
| Platform and availability | macOS 14+, built from source with `scripts/bundle.sh`. |
| Jev's role | Optional: one choice question over about 200 local candidates reorders suggestions a moment after local results appear. |
| Requirements | macOS 14+ and Xcode to build; optional TypeSafe API key. |
| License | [MIT](https://github.com/beckyisj/moji/blob/199e56d87d34d43bfa5268a322abcfa8fa669313/LICENSE) |

## When to use

- Get Slack-style emoji shortcodes in every macOS app.
- Find emoji from slang or loose words.
- Mismatch: needs Accessibility permission and a source build.

## How it works

`Jev.swift` posts the typed letters and candidate list to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; with no key, offline or on error it keeps the local ranking. Integration evidence: [`Sources/MojiCore/Jev.swift`](https://github.com/beckyisj/moji/blob/199e56d87d34d43bfa5268a322abcfa8fa669313/Sources/MojiCore/Jev.swift).

## Get started

From the upstream README (not run on the review host):

```sh
./scripts/bundle.sh
swift run moji-search --jev awkward ship_it proud
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/beckyisj/moji#readme](https://github.com/beckyisj/moji#readme)

## Limits and data handling

Only the letters after `:` are sent, after a pause and for 3+ letters. The key is stored in the login Keychain.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 199e56d87d34](https://github.com/beckyisj/moji/tree/199e56d87d34d43bfa5268a322abcfa8fa669313). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
