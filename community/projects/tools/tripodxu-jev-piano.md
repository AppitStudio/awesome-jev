# Jev Improv Piano (a piano that composes and plays bar by bar, with Jev choosing each bar)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Static web piano that turns a one-line idea into a piece and plays it live: once per bar, Jev answers eight questions in parallel (harmonic function, chord, left-hand texture, rhythm, direction, development, intensity, whether to breathe) from a music-theory-legal candidate set, and a deterministic engine renders the notes. Plays offline with a seeded local decider when there is no key. Modelled on cocktailpeanut/jevthoven; Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tripodxu/jev-piano) |
| Maintainer | [tripodxu](https://github.com/tripodxu). Independently curated. |
| Format | Static web app (Cloudflare Workers deploy) |
| Requirements | A browser; Python or Node for the local dev proxy; a TypeSafe key for live Jev. |
| License | [MIT](https://github.com/tripodxu/jev-piano/blob/f5b634fafa1922cf449a0dc296852aaa4da25e7f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`public/js/jev.js`](https://github.com/tripodxu/jev-piano/blob/f5b634fafa1922cf449a0dc296852aaa4da25e7f/public/js/jev.js) at the pinned commit. |

## When to use

- Hear how typed per-step decisions can drive generative music.
- Mismatch: Chinese UI and docs.

## How it works

`public/js/jev.js` posts each bar's state and eight questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) through the dev proxy or Worker. Integration evidence: [`public/js/jev.js`](https://github.com/tripodxu/jev-piano/blob/f5b634fafa1922cf449a0dc296852aaa4da25e7f/public/js/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/tripodxu/jev-piano && cd jev-piano
python dev-proxy.py --port 8000   # http://127.0.0.1:8000, offline mode needs no key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/tripodxu/jev-piano#readme](https://github.com/tripodxu/jev-piano#readme)

## Limits and data handling

Musical state per bar goes to TypeSafe only in live mode.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit f5b634fafa19](https://github.com/tripodxu/jev-piano/tree/f5b634fafa1922cf449a0dc296852aaa4da25e7f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
