# steam-heroic-library (Epic and GOG games from Heroic in your Steam library on Linux, with Jev sorting new games into genre collections)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Linux script that adds every owned Heroic (Epic and GOG) game to Steam as a shortcut with store art and an in-Steam install button, and builds genre collections. Games not in your curated list can be sorted by Jev and cached so each is classified once. The author calls it vibe-coded for personal use.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WSeubring/steam-heroic-library) |
| Maintainer | [WSeubring](https://github.com/WSeubring). Independently curated. |
| Format | Python script |
| Requirements | Linux, Steam and Heroic; optional TypeSafe API key (`TYPESAFE_API_KEY` or a Bitwarden item). |
| License | [MIT](https://github.com/WSeubring/steam-heroic-library/blob/041798c8373b88549386675083dd189369e5fbbf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/heroic-steam-sync`](https://github.com/WSeubring/steam-heroic-library/blob/041798c8373b88549386675083dd189369e5fbbf/bin/heroic-steam-sync) at the pinned commit. |

## When to use

- Sort a large game library into Steam collections automatically.
- Mismatch: personal-use script with no support.

## How it works

`bin/heroic-steam-sync --classify` calls `https://api.typesafe.ai/v1/systemone` to pick a collection for each game not in `categories.json` and caches the answers in `~/.cache/heroic-steam-sync/jev.json`; the curated list always wins. Integration evidence: [`bin/heroic-steam-sync`](https://github.com/WSeubring/steam-heroic-library/blob/041798c8373b88549386675083dd189369e5fbbf/bin/heroic-steam-sync).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/WSeubring/steam-heroic-library && cd steam-heroic-library
bin/heroic-steam-sync --classify
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/WSeubring/steam-heroic-library#readme](https://github.com/WSeubring/steam-heroic-library#readme)

## Limits and data handling

Game titles are sent to TypeSafe when classifying. Edits Steam shortcut files; back them up first. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 041798c8373b](https://github.com/WSeubring/steam-heroic-library/tree/041798c8373b88549386675083dd189369e5fbbf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
