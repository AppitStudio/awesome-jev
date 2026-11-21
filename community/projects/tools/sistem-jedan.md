# sistem jedan by David Abram (MCP code mode: agents write short JavaScript that calls Jev many times)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A minimal Rust MCP server over stdio with one `execute` tool: instead of one tool call per decision, the agent (for example Claude Code) writes a short JavaScript program that calls a System 1 model as many times as it needs in a sandboxed QuickJS engine and returns only the result. The example configuration targets Jev (`typesafe/jev-1.14`) through OpenRouter's Decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davidabram/sistem-jedan) |
| Maintainer | [davidabram](https://github.com/davidabram). Independently curated. |
| Format | Rust MCP server (Nix flake) |
| Requirements | Nix with flakes (or a Rust toolchain), an MCP client, and an OpenRouter API key; the model is one line in the config. |
| License | no license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/devabram/status/2123523473373028755)). |
| Jev evidence | [`config.example.toml`](https://github.com/davidabram/sistem-jedan/blob/c961cf908f5eabfcf89e87a1130a6e764a839008/config.example.toml) at the pinned commit. |

## When to use

- Let a coding agent batch many Jev decisions in one sandboxed script instead of flooding its context with tool calls.
- Mismatch: anything you need to rely on; the author marks it experimental and the Decisions API it targets is an alpha endpoint.

## How it works

`config.example.toml` points the provider at `https://openrouter.ai/api/alpha/decisions` with `model = "typesafe/jev-1.14"`; the server exposes the model to the sandboxed script with limits on timeout, memory, concurrency and calls per execution, so 50 decisions cost one tool call in the agent's context. Integration evidence: [`config.example.toml`](https://github.com/davidabram/sistem-jedan/blob/c961cf908f5eabfcf89e87a1130a6e764a839008/config.example.toml).

## Get started

Install with Nix, copy the example config with your OpenRouter key, and register the binary as an MCP server.

```sh
nix profile install github:davidabram/sistem-jedan
mkdir -p ~/.config/sistem-jedan
# copy config.example.toml to ~/.config/sistem-jedan/config.toml and set api_key
# then add ~/.nix-profile/bin/sistem-jedan as a stdio MCP server in your client
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/davidabram/sistem-jedan/blob/c961cf908f5eabfcf89e87a1130a6e764a839008/README.md](https://github.com/davidabram/sistem-jedan/blob/c961cf908f5eabfcf89e87a1130a6e764a839008/README.md)
- Post on X: [x.com/devabram/status/2123523473373028755](https://x.com/devabram/status/2123523473373028755)

## Limits and data handling

Whatever the agent's script sends goes to OpenRouter and the configured model, with per-call cost (capped per execution). Experimental: tool interface and config format may change. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit c961cf908f5e](https://github.com/davidabram/sistem-jedan/tree/c961cf908f5eabfcf89e87a1130a6e764a839008). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
