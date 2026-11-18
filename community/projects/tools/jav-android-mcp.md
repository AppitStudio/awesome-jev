# Jav by k4wai1 (no-root Android control runtime over MCP, with a Jev resolver that picks the on-screen element)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Accessibility-first Android app plus a Go MCP server (stdio) with 38 atomic tools for on-device UI automation and telemetry, no root needed (shell via Shizuku), over WSS on Tailnet or LAN with certificate pinning. A director model (your coding agent) runs the loop; when the screen is noisy, the `resolve_element` tool prunes the accessibility tree to a numbered table and asks Jev one choice question for the element matching a micro-intent, returning a confidence and falling back to top candidates below 0.70. Without a key the resolver degrades to that fallback and never invents options. Docs in English and Spanish.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/k4wai1/jav) |
| Maintainer | [k4wai1](https://github.com/k4wai1). Independently curated. |
| Format | Android app and Go MCP server (GPL-3.0) |
| Requirements | An Android device with the Jav app and Accessibility enabled (Shizuku for shell), the Go MCP server, an MCP client as director, and an OpenRouter key for Jev (`typesafe/jev-1.13`). |
| License | [GPL-3.0-or-later](https://github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pkg/jev/jev.go`](https://github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/pkg/jev/jev.go) at the pinned commit. |

## When to use

- Let a coding agent drive an Android phone, with Jev resolving which element to tap from a noisy screen.
- Mismatch: iOS, or a fully autonomous agent; Jav runs no loop or planner of its own.

## How it works

`pkg/jev/jev.go` sends the pruned element table to Jev through OpenRouter's decisions API (default `typesafe/jev-1.13`, `jev-latest` accepted) as one choice over row indices plus NONE; `pkg/tools/resolve.go` exposes it as `resolve_element`. Integration evidence: [`pkg/jev/jev.go`](https://github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/pkg/jev/jev.go).

## Get started

Install the app on the device, run the MCP server from your client, and add an OpenRouter key to enable the Jev resolver.

```sh
git clone https://github.com/k4wai1/jav
# install the APK from releases, enable Accessibility, then follow the README quickstart
export OPENROUTER_API_KEY=...   # or openrouter_api_key in ~/.config/jav/config.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/README.md](https://github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/README.md)
- Architecture diagram: [github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/docs/diagrams/jav-architecture.html](https://github.com/k4wai1/jav/blob/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158/docs/diagrams/jav-architecture.html)

## Limits and data handling

Pruned screen contents are sent to OpenRouter/TypeSafe on each resolution; the per-resolution cost and timing in the README were measured by the author on one device. GPL-3.0 applies to derivatives.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 5ee66fa70e47](https://github.com/k4wai1/jav/tree/5ee66fa70e47d1ac4b6b6abc2fc4dcf05945e158). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
