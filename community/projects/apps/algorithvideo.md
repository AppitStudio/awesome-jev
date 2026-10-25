# AlgorithVideo (open-source desktop video clipper with optional Jev clip review)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Open-source Electron desktop app that turns podcasts, interviews and streams into captioned short clips rendered on your own computer; an opt-in Jev review step, through OpenRouter's Decisions API, scores candidate moments from transcript excerpts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/algorithco/algorith-video) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/algorithco/algorith-video#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free download. AI features use your own provider keys, stored in the OS secure storage. Checked 2026-10-25. |
| Jev evidence | [`engine/clip_engine/services/jev_service.py`](https://github.com/algorithco/algorith-video/blob/80047cf2568831ffbbe5446c7a01c68b7ac27c60/engine/clip_engine/services/jev_service.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [algorithco](https://github.com/algorithco). Independently curated. |
| Format | Desktop app (Electron with a Python engine) |
| Platform and availability | Windows x64, macOS (Apple silicon and Intel) and Linux x64 packages on GitHub Releases (v0.1.0 at review); unsigned, macOS not notarized. |
| Jev's role | Optional: Jev review is off by default in automatic clipping and always on in the Review & edit workflow; it answers typed questions about each candidate clip. |
| Requirements | Windows, macOS or Linux; an OpenRouter key for Jev review and the other AI features you enable. |
| License | [MIT](https://github.com/algorithco/algorith-video/blob/80047cf2568831ffbbe5446c7a01c68b7ac27c60/LICENSE) |

## When to use

- Cut long videos into short captioned clips locally instead of in a hosted clipping service.
- Add a cheap Jev pass to review candidate moments before rendering.
- Mismatch: first packages are unsigned; expect OS warnings.

## How it works

`jev_service.py` sends bounded transcript excerpts with Noul, Choice and Score questions to `typesafe/jev-1.13` through `https://openrouter.ai/api/alpha/decisions`, with a byte budget, limited retries and a cut-off after repeated failures. Integration evidence: [`engine/clip_engine/services/jev_service.py`](https://github.com/algorithco/algorith-video/blob/80047cf2568831ffbbe5446c7a01c68b7ac27c60/engine/clip_engine/services/jev_service.py).

## Get started

From the upstream README (not run on the review host): download the package for your system from the latest release, or build from source:

```sh
# https://github.com/algorithco/algorith-video/releases/latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/algorithco/algorith-video/releases/latest](https://github.com/algorithco/algorith-video/releases/latest)
- Architecture: [github.com/algorithco/algorith-video/blob/main/docs/ARCHITECTURE.md](https://github.com/algorithco/algorith-video/blob/main/docs/ARCHITECTURE.md)

## Limits and data handling

With Jev review on, transcript excerpts go to OpenRouter and TypeSafe; rendering stays local. Optional social publishing and web research make their own network calls.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 80047cf25688](https://github.com/algorithco/algorith-video/tree/80047cf2568831ffbbe5446c7a01c68b7ac27c60). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
