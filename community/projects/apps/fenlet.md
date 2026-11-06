# Fenlet (Mac window arranger with a CLI and agent skill that can ask Jev how to lay out panes)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native Mac widget, CLI and agent skill that turns open windows into non-overlapping panes. You confirm before anything moves. The agent skill can ask TypeSafe Jev typed layout questions from the current window set.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/2018kguo/fenlet) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/2018kguo/fenlet#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; TypeSafe key required for Jev-assisted agent layouts. Checked 2026-11-06. |
| Jev evidence | [`fenlet/questions.py`](https://github.com/2018kguo/fenlet/blob/48107ce4bb162d04e9a87e64005ac4990f271921/fenlet/questions.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [2018kguo](https://github.com/2018kguo). Independently curated. |
| Format | macOS widget + CLI + agent skill (MIT) |
| Platform and availability | macOS (widget, CLI, agent skill). |
| Jev's role | Optional layout judge for the agent skill: Jev answers typed questions about how to arrange panes; the widget/CLI can arrange without Jev. |
| Requirements | macOS, and a TypeSafe key when the agent skill uses Jev layout questions. |
| License | [MIT](https://github.com/2018kguo/fenlet/blob/48107ce4bb162d04e9a87e64005ac4990f271921/LICENSE) |

## When to use

- Arrange Mac windows into panes without overlapping.
- Let an agent propose a layout you still confirm.
- Mismatch: macOS-only; Jev path is for the agent skill, not required for manual arrange.

## How it works

`fenlet/questions.py` builds TypeSafe System One payloads (`typesafe-ai/jev-1.14.0`) for layout intents the agent skill can ask. Integration evidence: [`fenlet/questions.py`](https://github.com/2018kguo/fenlet/blob/48107ce4bb162d04e9a87e64005ac4990f271921/fenlet/questions.py).

## Get started

Install from source per the README, use Arrange windows in the widget, and optionally enable the agent skill with a TypeSafe key.

```sh
git clone https://github.com/2018kguo/fenlet.git && cd fenlet
# follow README get-started
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/2018kguo/fenlet/blob/48107ce4bb162d04e9a87e64005ac4990f271921/README.md](https://github.com/2018kguo/fenlet/blob/48107ce4bb162d04e9a87e64005ac4990f271921/README.md)

## Limits and data handling

Layout intent and window metadata used in Jev questions are sent to TypeSafe on your key. Nothing moves before confirmation.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 48107ce4bb16](https://github.com/2018kguo/fenlet/tree/48107ce4bb162d04e9a87e64005ac4990f271921). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
