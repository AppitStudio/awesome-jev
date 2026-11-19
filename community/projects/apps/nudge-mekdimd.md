# Nudge by Mekdim Dereje (voice or text computer control for people with limited dexterity, with Jev choosing each next control)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Accessibility assistant for macOS and Windows, built at StormHacks 2026, for people with tremor, repetitive strain injuries, low vision or limited dexterity. You say or type what you want (for example, download your October bank statement); Nudge reads the app's accessibility controls, Jev chooses the next control, and a large on-screen cursor carries the action out. It asks you to pick between uncertain options, asks approval before sensitive actions, drafts text with Gemini for you to edit, and has an optional local vision fallback for controls an app does not expose. An offline demo runs without keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mekdimd/nudge) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/mekdimd/nudge#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you pay TypeSafe and Google for your own API usage. Checked 2026-11-19. |
| Jev evidence | [`nudge/core/jev.py`](https://github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/nudge/core/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [mekdimd](https://github.com/mekdimd). Independently curated. |
| Format | Desktop app (Python) |
| Platform and availability | macOS and Windows desktop, run from source with uv (prototype). |
| Jev's role | Chooses the next control to act on from the app's readable controls at each step; drafting is done by Gemini. |
| Requirements | Python 3.12 or 3.13 with uv; `TYPESAFE_API_KEY` for real tasks and `GEMINI_API_KEY` for drafting; macOS Accessibility permission. The offline demo needs no keys. |
| License | [MIT](https://github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/LICENSE) |

## When to use

- Operate everyday desktop apps by describing the task, with a large cursor and approval before sensitive actions.
- Mismatch: apps without readable accessibility controls (the local vision fallback helps only partly); it is a hackathon prototype.

## How it works

`nudge/core/jev.py` posts each step's goal and the visible controls to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, and `nudge/app.py` turns the chosen control into a cursor action or a question back to you. Integration evidence: [`nudge/core/jev.py`](https://github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/nudge/core/jev.py).

## Get started

Clone the repository and start the offline demo; add your keys to `.env` to use it on real apps.

```sh
git clone https://github.com/mekdimd/nudge
cd nudge
uv sync --frozen
uv run nudge --offline gmail   # scripted demo, no keys
# real apps: copy .env.example to .env, add TYPESAFE_API_KEY and GEMINI_API_KEY
uv run nudge
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/README.md](https://github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/README.md)
- Setup and privacy: [github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/docs/SETUP.md](https://github.com/mekdimd/nudge/blob/0f9b097681c65d2dabae7a327911c4f19981c74f/docs/SETUP.md)
- Devpost write-up: [devpost.com/software/nudge-nf7okh](https://devpost.com/software/nudge-nf7okh)

## Limits and data handling

Real tasks send your goal and the app's control details to TypeSafe, and text to be drafted to Google Gemini. It acts on your desktop with accessibility permissions; keep approvals on for sending or paying. Prototype; app support depends on readable controls.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 0f9b097681c6](https://github.com/mekdimd/nudge/tree/0f9b097681c65d2dabae7a327911c4f19981c74f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
