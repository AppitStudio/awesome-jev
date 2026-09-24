# jev-browser-use (AuroraPixel)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Jev-powered browser automation for Codex and Claude: persistent Chrome daemon, CLI/MCP/extension, conditional plans, and host handoffs when reading or new text is required.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AuroraPixel/jev-browser-use) |
| Maintainer | [AuroraPixel](https://github.com/AuroraPixel). Independently curated. |
| Format | Bun-compiled CLI + MCP + Chrome extension (derived from SawyerHood/dev-browser; informed by jev-ultrafast). |
| Requirements | Bun 1.3.14 for source build (or GitHub release binary); Chrome/Chromium; macOS or glibc Linux ARM64/x64; `TYPESAFE_API_KEY` for Jev loops. |
| License | [MIT](https://github.com/AuroraPixel/jev-browser-use/blob/1701c2f69690c63d22514e74f0896c84509bbe5d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Chrome/Jev loops not run. Distinct from wy-coliney/jev-browser-use referenced by [jev-chrome-mcp](jev-chrome-mcp.md) and from [Jev Ultrafast](jev-ultrafast.md). |

## When to use

Use when Codex/Claude should keep a **warm browser** while Jev executes bounded action loops and the host model only handles reasoning/writing. Prefer [Jev Ultrafast](jev-ultrafast.md) for the Python/Browser Harness reference loop.

## How it works

Jev observes candidates and performs click/type/select/scroll/wait inside a local loop with freshness checks; the host steps in for reading, judgment, new text, or unsupported controls. Conditional plans can reuse verified bindings (per README/docs).

## Get started

```sh
git clone https://github.com/AuroraPixel/jev-browser-use.git
cd jev-browser-use
git checkout 1701c2f69690c63d22514e74f0896c84509bbe5d
bun install --frozen-lockfile
bun run build
export PATH="$PWD/dist:$PATH"
export TYPESAFE_API_KEY="<your-typesafe-key>"
jev-browser-use --version
```

## Examples and demos

- Architecture poster and docs under `docs/` (`architecture.md`, `jev.md`, `plans.md`).
- GitHub Releases binaries + extension ZIP.

## Limits and data handling

Goals, visible text, and control candidates reach TypeSafe at `/v1/systemone`. Ordinary Puppeteer scripts without Jev stay local. Windows/musl not supported yet (per README).

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 1701c2f](https://github.com/AuroraPixel/jev-browser-use/tree/1701c2f69690c63d22514e74f0896c84509bbe5d). AI-assisted README and LICENSE inspection; Bun build/live browser not run on the review host.

Related: [jev-chrome-mcp](jev-chrome-mcp.md), [Jev Ultrafast](jev-ultrafast.md).
