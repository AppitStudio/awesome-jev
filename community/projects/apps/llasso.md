# Llasso (draw a box round anything on your Mac and ask about it or have it changed)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac app where you hold ⌘ and drag a box round anything on screen, then type or say what you want: Llasso guesses what the box holds, picks a model for the kind of work from OpenRouter's live lists, and every change waits for your tap; Jev on OpenRouter classifies the request when it can answer within 1.5 seconds.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jamiejefferson/llasso) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/jamiejefferson/llasso#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free install. All model calls, including Jev, are billed to your OpenRouter key. Checked 2026-10-26. |
| Jev evidence | [`Sources/LlassoKit/Router.swift`](https://github.com/jamiejefferson/llasso/blob/289da825b7e2d0c2911a225c24c9c4cfcc02f0d9/Sources/LlassoKit/Router.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [jamiejefferson](https://github.com/jamiejefferson). Independently curated. |
| Format | macOS app (Swift) |
| Platform and availability | macOS 26+ on Apple silicon; install script fetches the GitHub release (v0.1.2 at review time). |
| Jev's role | Request router: Jev reads the typed request and names the kind of work (writing, coding, design and so on) so Llasso can pick a model; keyword rules decide when Jev is slow. |
| Requirements | Apple silicon Mac with macOS 26+; an OpenRouter API key; Screen Recording, Microphone and Accessibility permissions. |
| License | [MIT](https://github.com/jamiejefferson/llasso/blob/289da825b7e2d0c2911a225c24c9c4cfcc02f0d9/LICENSE) |

## When to use

- Ask about or edit something on screen without copying it anywhere first.
- Hand code changes for a local page to Claude Code with undo.
- Mismatch: Jev is only the router; answers come from other OpenRouter models.

## How it works

`Sources/LlassoKit/Router.swift` sends the request to OpenRouter's Decisions endpoint as `~typesafe/jev-latest` with the seven kinds as options and falls back to rules after 1.5 seconds. Integration evidence: [`Sources/LlassoKit/Router.swift`](https://github.com/jamiejefferson/llasso/blob/289da825b7e2d0c2911a225c24c9c4cfcc02f0d9/Sources/LlassoKit/Router.swift).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/jamiejefferson/llasso/main/install.sh | sh
# first run: paste an OpenRouter key in Settings and grant the permissions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/jamiejefferson/llasso/releases](https://github.com/jamiejefferson/llasso/releases)
- README: [github.com/jamiejefferson/llasso#readme](https://github.com/jamiejefferson/llasso#readme)

## Limits and data handling

Screenshots of the box, your request and voice go to OpenRouter and the chosen models; Jev is reached through OpenRouter. Feedback you send goes to the author's Supabase table.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 289da825b7e2](https://github.com/jamiejefferson/llasso/tree/289da825b7e2d0c2911a225c24c9c4cfcc02f0d9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
