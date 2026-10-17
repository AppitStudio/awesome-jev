# ChatJump

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Menu-bar launcher for your AI chats: press Control-Option-Space, type what you remember, and Jev ranks open Claude, ChatGPT, Codex and Chrome chat tabs by meaning, then opens the right one.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saydus/chatjump) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/saydus/chatjump#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-17. |
| Jev evidence | [`Sources/Ranker.swift`](https://github.com/saydus/chatjump/blob/6d3ef66088df3a0ca966e6eca4231be7f6b10fb4/Sources/Ranker.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [saydus](https://github.com/saydus). Independently curated. |
| Format | Native macOS menu-bar app (Swift, built and ad-hoc signed with `build.sh`) |
| Platform and availability | macOS 14 or later (source build) |
| Jev's role | Jev ranks your open AI chats against a remembered description and flags weak matches. |
| Requirements | macOS 14+, Xcode command-line tools, Accessibility permission; optional TypeSafe API key (keyword matching without it). |
| License | [MIT](https://github.com/saydus/chatjump/blob/6d3ef66088df3a0ca966e6eca4231be7f6b10fb4/LICENSE) |

## When to use

- Find an old Claude or Codex conversation when you remember the topic but not the title.
- See a small, real Choice-plus-Noul ranking pattern with a local keyword fallback.
- Mismatch: ChatGPT and claude.ai chats match on titles only, and only chats the sidebar has loaded are visible.

## How it works

A local keyword matcher shows results instantly; after a short pause `Ranker.swift` sends one request with every open chat (title, last exchange, keyword hint) and asks a Choice over chat ids for the ranking and a Noul for whether anything matches. It reads `TYPESAFE_API_KEY` or `~/.config/chatjump/typesafe_key`. Integration evidence: [`Sources/Ranker.swift`](https://github.com/saydus/chatjump/blob/6d3ef66088df3a0ca966e6eca4231be7f6b10fb4/Sources/Ranker.swift).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/saydus/chatjump.git
cd chatjump && ./build.sh
# then grant Accessibility to /Applications/ChatJump.app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage, troubleshooting and `--dump` diagnostics in the README.

## Limits and data handling

With a key, each search sends your query plus each open chat's title, app name and last messages (about 750 characters) to `api.typesafe.ai`. Ad-hoc signing means Accessibility must be re-granted after every rebuild.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 6d3ef66088df](https://github.com/saydus/chatjump/tree/6d3ef66088df3a0ca966e6eca4231be7f6b10fb4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
