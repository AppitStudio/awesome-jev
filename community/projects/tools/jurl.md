# jurl

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

curl that reads the page for you: `jurl -q "question" <url>` fetches a page (with a headless browser when it needs JavaScript), and TypeSafe Jev picks the passages, links or code that answer, with Cloudflare Clef-flash for images; no chatbot, prose stays verbatim.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rayoplateado/jurl) |
| Product homepage | [jurl.dev](https://jurl.dev) |
| Maintainer | [rayoplateado](https://github.com/rayoplateado). Independently curated. |
| Format | Rust CLI (`jurl`, v0.1.2 release at review) via Homebrew tap, installer script or `cargo install --git` |
| Requirements | A TypeSafe API key (asked and saved on first run); Cloudflare Workers AI token only for `--vision`/`--find`; headless browser downloaded on first JavaScript page. |
| License | Dual [Apache-2.0](https://github.com/rayoplateado/jurl/blob/5df0fb3a12bfbfbc4ade3259c8220d76dc8fb6e7/LICENSE-APACHE) / [MIT](https://github.com/rayoplateado/jurl/blob/5df0fb3a12bfbfbc4ade3259c8220d76dc8fb6e7/LICENSE-MIT). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Ask one question of a documentation page and get the matching section verbatim.
- Give an agent markdown of only the relevant parts of a page, or find an image by description.
- Mismatch: page text goes to TypeSafe — avoid it for internal or private pages.

## How it works

jurl fetches and converts the page to Markdown, then [`src/decide.rs`](https://github.com/rayoplateado/jurl/blob/5df0fb3a12bfbfbc4ade3259c8220d76dc8fb6e7/src/decide.rs) asks Jev typed questions to pick passages, links or code blocks; images go to Clef-flash with `--vision`/`--find`. The README's *How it compares* bench ([`bench/`](https://github.com/rayoplateado/jurl/tree/5df0fb3a12bfbfbc4ade3259c8220d76dc8fb6e7/bench)) records tasks, scripts and answers.

## Get started

Install and ask a question:

```sh
brew install rayoplateado/tap/jurl
jurl -q "how do I install it on macOS?" github.com/BurntSushi/ripgrep
```

Upstream measured about $0.0004–0.0013 per page with Jev; images are billed by Cloudflare. Run with `-t` to see your own numbers.

## Examples and demos

- README recipes (top Hacker News stories, every chart in a post, only confident answers).
- README *Speed and cost* table (measured by the maintainer on 2026-10-04).

## Limits and data handling

Page text goes to TypeSafe; with image modes, images go to Cloudflare (upstream). Timing and cost are upstream measurements. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 5df0fb3a12bf](https://github.com/rayoplateado/jurl/tree/5df0fb3a12bfbfbc4ade3259c8220d76dc8fb6e7). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
