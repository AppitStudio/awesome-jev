# Kiteva (local AI motion-graphics studio where Jev ranks style directions and picks visual and audio capabilities for each film)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local creative room where an idea becomes a short motion-graphics film, built on Claude or GPT main models with narration and audio generated locally. Jev is configured separately with its own key and is used for generated style directions and for visual and audio capability selection; choosing a Motion Graphic by hand skips style ranking. It also exposes an MCP endpoint so external agents can search ideas, save a draft and start a build, and has English and Chinese interfaces.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/delexw/motion-graphics-agent) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/delexw/motion-graphics-agent#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you supply Claude or Codex access, a TypeSafe key and local compute. Checked 2026-11-04. |
| Jev evidence | [`src/server/jev/client.ts`](https://github.com/delexw/motion-graphics-agent/blob/73dafac01c7903823d187a95b5768fe9ee9cea1b/src/server/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [delexw](https://github.com/delexw). Independently curated. |
| Format | Local web app (Node, Vite; install script for speech and audio models) |
| Platform and availability | Self-hosted local web app (macOS-focused install notes; a Windows CI workflow is present). |
| Jev's role | Ranks generated style directions and chooses visual and audio capabilities for a project. |
| Requirements | Node, the install script, a Claude or Codex provider (API key or signed-in CLI) and `TYPESAFE_API_KEY` in `.env.local`. |
| License | [MIT](https://github.com/delexw/motion-graphics-agent/blob/73dafac01c7903823d187a95b5768fe9ee9cea1b/LICENSE) |

## When to use

- Make short motion-graphics films from an idea, with a decision model ranking the style combinations to try.
- Mismatch: it needs a large local install and provider keys, and Jev is one part of a bigger generative pipeline.

## How it works

`src/server/jev/client.ts` creates a `TypeSafeClient` from `TYPESAFE_API_KEY` (pinned `jev-1.14.0`), and `src/server/jev/strategies/style-combination.ts` and `bounded-choice.ts` ask it typed choice questions over compact briefs, with token-based cost reporting at the published rate. Integration evidence: [`src/server/jev/client.ts`](https://github.com/delexw/motion-graphics-agent/blob/73dafac01c7903823d187a95b5768fe9ee9cea1b/src/server/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/delexw/motion-graphics-agent.git
cd motion-graphics-agent
./install.sh   # then add TYPESAFE_API_KEY and provider keys to .env.local
npm start      # open http://127.0.0.1:18417
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the changelog, MCP guide and setup: [github.com/delexw/motion-graphics-agent#readme](https://github.com/delexw/motion-graphics-agent#readme)
- Latest release (v1.0.0 source release, 2026-10-30): [github.com/delexw/motion-graphics-agent/releases/latest](https://github.com/delexw/motion-graphics-agent/releases/latest)

## Limits and data handling

Compact creative briefs go to TypeSafe on your key, and the main model providers bill separately; the README says subscription usage reporting was not tested. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 73dafac01c79](https://github.com/delexw/motion-graphics-agent/tree/73dafac01c7903823d187a95b5768fe9ee9cea1b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
