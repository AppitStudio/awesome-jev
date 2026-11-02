# Jev model router for GitHub Copilot (Copilot CLI and VS Code port of jev_router that sizes each message with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hooks and helper agents for GitHub Copilot CLI and VS Code that let Jev size each message as tiny, everyday, large or hardest and hand it to a helper agent pinned to a model you choose, while the main model stays in charge. Copilot port of TechPreacher's jev_router for Claude Code, using the same router.py.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TechPreacher/jev-router-copilot) |
| Maintainer | [TechPreacher](https://github.com/TechPreacher). Independently curated. |
| Format | Copilot hooks + agents (Python standard library) |
| Requirements | macOS or Linux, `python3`, GitHub Copilot CLI or VS Code with Copilot, `TYPESAFE_API_KEY` or the macOS Keychain. |
| License | [MIT](https://github.com/TechPreacher/jev-router-copilot/blob/b2ef6a52561cb096c923a6d9815be5b41c709eb8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-router-copilot/files/router.py`](https://github.com/TechPreacher/jev-router-copilot/blob/b2ef6a52561cb096c923a6d9815be5b41c709eb8/jev-router-copilot/files/router.py) at the pinned commit. |

## When to use

- Spend fewer premium requests on easy Copilot messages.
- Mismatch: if the Jev call isn't confident or times out, the message stays with the main model.

## How it works

`router.py` posts the message to `https://api.typesafe.ai/v1/systemone` with a hard timeout and maps the answer to one of four helper agents (`jev-tiny`, `jev-everyday`, `jev-large`, `jev-hardest`); typing `jev router on|off|status` in chat controls it. Integration evidence: [`jev-router-copilot/files/router.py`](https://github.com/TechPreacher/jev-router-copilot/blob/b2ef6a52561cb096c923a6d9815be5b41c709eb8/jev-router-copilot/files/router.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/TechPreacher/jev-router-copilot.git
cd jev-router-copilot/jev-router-copilot
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Original Claude Code router: [github.com/TechPreacher/jev_router](https://github.com/TechPreacher/jev_router)

## Limits and data handling

Each message you route is sent to TypeSafe for sizing. Independent project; not affiliated with TypeSafe or GitHub.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit b2ef6a52561c](https://github.com/TechPreacher/jev-router-copilot/tree/b2ef6a52561cb096c923a6d9815be5b41c709eb8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
