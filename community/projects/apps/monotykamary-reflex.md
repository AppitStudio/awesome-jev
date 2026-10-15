# Reflex (monotykamary)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac menu-bar app to see, answer and talk to every coding agent running in herdr; Jev (via jev-fabric) routes each request to the right session or folder and asks you to confirm when unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/monotykamary/reflex) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/monotykamary/reflex#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-16. |
| Jev evidence | [`daemon/Route.bend`](https://github.com/monotykamary/reflex/blob/edcca81ef000e9bc2c52b17ede336ce00f9b02a4/daemon/Route.bend) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [monotykamary](https://github.com/monotykamary). Independently curated. |
| Format | macOS app (Swift) + Bend daemon; phone web page over Tailscale |
| Platform and availability | macOS 26+ (Apple Silicon), source build |
| Jev's role | Jev picks the destination session/folder for each request; code delivers it or asks you to confirm. |
| Requirements | Apple Silicon Mac on macOS 26+, herdr 0.9+, at least one coding agent, jev-fabric and a System One provider key (TypeSafe Jev by default); Bend 2.0.37 and Xcode to build. |
| License | [MIT](https://github.com/monotykamary/reflex/blob/edcca81ef000e9bc2c52b17ede336ce00f9b02a4/LICENSE) |

## When to use

- Send a request from one bar and let it land in the right live agent session without retyping.
- Reply to agents from your phone over Tailscale.
- Mismatch: Jev routing is optional; without it you pick destinations yourself.

## How it works

Reflex builds candidate sessions and folders itself, asks Jev through jev-fabric typed questions (which session, which folder, side question, continuation) and delivers your text verbatim; when Jev is unsure nothing is sent automatically, and routing laws are machine-checked in `daemon/LAWS.bend`. Integration evidence: [`daemon/Route.bend`](https://github.com/monotykamary/reflex/blob/edcca81ef000e9bc2c52b17ede336ce00f9b02a4/daemon/Route.bend).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/monotykamary/reflex.git && cd reflex
scripts/build-app.sh   # builds build/Reflex.app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Routing laws: `daemon/LAWS.bend`.

## Limits and data handling

Request text and candidate session/folder names go to the System One provider you configure, on your key; agents keep running on your own subscriptions.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit edcca81ef000](https://github.com/monotykamary/reflex/tree/edcca81ef000e9bc2c52b17ede336ce00f9b02a4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
