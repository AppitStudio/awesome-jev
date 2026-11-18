# jev-if-player by klavdiy-core (blind first-time playtest of Twine, ink and HTML5 text games with Jev as the reader)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Playtest tool for browser interactive fiction (Twine, ink, any HTML5 text game). Jev plays the game from the start in a dedicated Chrome, clicking only what a player can see, and answers the same questions every turn: which choice to take, how much it wants to keep reading, what it feels. The author gets a one-page report on where attention dropped and what to fix first, plus a turn-by-turn log. English and Russian notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/klavdiy-core/jev-if-player) |
| Maintainer | [klavdiy-core](https://github.com/klavdiy-core). Independently curated. |
| Format | Python script driving Chrome over DevTools (MIT) |
| Requirements | Python, a separate Chrome profile with remote debugging, and your own small `jev` client module with a `call()` function (pointed to by `JEV_CLIENT_DIR`) that sends requests to Jev with your key. |
| License | [MIT](https://github.com/klavdiy-core/jev-if-player/blob/d87a7fe5fadf67b76cc7f1cf4af57172e7fa1ecf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_if_player.py`](https://github.com/klavdiy-core/jev-if-player/blob/d87a7fe5fadf67b76cc7f1cf4af57172e7fa1ecf/jev_if_player.py) at the pinned commit. |

## When to use

- Get a cheap first-reader signal on where a text game loses attention before a human playtest.
- Mismatch: canvas or parser games, or a ready-made Jev client; you supply the small client module.

## How it works

`jev_if_player.py` builds a state from the visible passage and choices and calls `jev.call({"state": ..., "questions": ...})` each turn; the client module that holds the key is yours, loaded from `JEV_CLIENT_DIR`. Integration evidence: [`jev_if_player.py`](https://github.com/klavdiy-core/jev-if-player/blob/d87a7fe5fadf67b76cc7f1cf4af57172e7fa1ecf/jev_if_player.py).

## Get started

Start a playtest-only Chrome, point the script at your Jev client module, then give it the game URL.

```sh
git clone https://github.com/klavdiy-core/jev-if-player && cd jev-if-player
chrome --remote-debugging-port=9333 --user-data-dir=<new dir>
export JEV_CLIENT_DIR=/path/to/folder/with/jev.py
python -X utf8 jev_if_player.py https://someone.itch.io/some-game --name some-game --turns 40 --out runs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/klavdiy-core/jev-if-player/blob/d87a7fe5fadf67b76cc7f1cf4af57172e7fa1ecf/README.md](https://github.com/klavdiy-core/jev-if-player/blob/d87a7fe5fadf67b76cc7f1cf4af57172e7fa1ecf/README.md)

## Limits and data handling

Only the game's visible text is sent to the model. The reader's feelings are model answers, not a person's reaction, and it plays one route from the start. Tests use a stand-in reader with no network.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit d87a7fe5fadf](https://github.com/klavdiy-core/jev-if-player/tree/d87a7fe5fadf67b76cc7f1cf4af57172e7fa1ecf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
