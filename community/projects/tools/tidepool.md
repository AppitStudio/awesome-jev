# Tidepool

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Tidepool/Exomonad: a live Haskell notebook and programmable agent harness where reasoning LLMs write procedures and Jev supplies cheap typed System 1 judgments inside ordinary code; ships a Jev skill for question batteries and settlement policies. Source available (PolyForm Shield).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tidepool-heavy-industries/tidepool) |
| Maintainer | [tidepool-heavy-industries](https://github.com/tidepool-heavy-industries). Independently curated. |
| Format | Agent runtime + notebook (source build) |
| Requirements | Linux, Nix, systemd user services/cgroup v2, Bubblewrap, tmux; an authenticated Codex client; `TYPESAFE_API_KEY` for Jev. |
| License | [PolyForm Shield 1.0.0](https://github.com/tidepool-heavy-industries/tidepool/blob/b896a1c12eb38f585cc82a46827a911c809a308a/LICENSE.md). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let an agent install its own tools/hooks as typed code that mixes exact checks with Jev judgments.
- Study a design where reasoning models design procedures and Jev handles semantic branch points.
- Mismatch: heavy Linux/Nix setup; PolyForm Shield is not an open-source license.

## How it works

Notebook programs and installed tools share effects such as run command, ask Jev, inspect conversation and message workers; Jev answers typed questions on command output or evidence and code selects the next step. Jev handlers live in [`bridge/handlers/src/handlers/jev.rs`](https://github.com/tidepool-heavy-industries/tidepool/blob/b896a1c12eb38f585cc82a46827a911c809a308a/bridge/handlers/src/handlers/jev.rs) and [`bridge/haskell/lib/Jev/`](https://github.com/tidepool-heavy-industries/tidepool/tree/b896a1c12eb38f585cc82a46827a911c809a308a/bridge/haskell/lib/Jev).

## Get started

Source build on Linux with Nix (see the upstream package guide before launching):

```sh
git clone --recurse-submodules https://github.com/tidepool-heavy-industries/tidepool.git
cd tidepool
bash scripts/buck2-configure.sh --tests
just exomonad-build
export TYPESAFE_API_KEY=...
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Jev skill](https://github.com/tidepool-heavy-industries/tidepool/blob/b896a1c12eb38f585cc82a46827a911c809a308a/exomonad/examples/workspace/.exomonad/skills/exomonad-jev/SKILL.md) and the example workspace package.

## Limits and data handling

PolyForm Shield 1.0.0 restricts competing uses — read `LICENSE.md`. Command output and evidence are sent to TypeSafe when Jev is called. Not built or run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit b896a1c12eb3](https://github.com/tidepool-heavy-industries/tidepool/tree/b896a1c12eb38f585cc82a46827a911c809a308a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
