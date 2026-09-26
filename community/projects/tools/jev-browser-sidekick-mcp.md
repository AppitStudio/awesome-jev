# jev-browser-sidekick-mcp

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP browser sidekick: you write steps; Jev chooses which control carries each one out.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TechyAditya/jev-browser-sidekick-mcp) |
| Maintainer | [TechyAditya](https://github.com/TechyAditya). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm MCP server with `run_action` and `use_jev_raw` tools. |
| Requirements | Node.js; TypeSafe or OpenRouter key via `jev-bro setup`; peer agentic-playwright-mcp recommended. |
| License | [MIT](https://github.com/TechyAditya/jev-browser-sidekick-mcp/blob/0fa3234851d19fbc4568e3f39d5b3a69d26e7239/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use for agent browser automation with typed control choice. Pair with agentic-playwright-mcp for shared cookies/sign-in.

## How it works

Attaches to Chrome on port 9223 when Playwright MCP is running; Jev selects controls from observed candidates; code clicks and waits. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
npm install -g agentic-playwright-mcp jev-browser-sidekick-mcp
jev-bro setup --provider official --api-key \"$TYPESAFE_API_KEY\"
jev-bro doctor
```

Pin revision `0fa3234851d19fbc4568e3f39d5b3a69d26e7239` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Page state and questions go to the configured provider. Live browser/MCP path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 0fa3234](https://github.com/TechyAditya/jev-browser-sidekick-mcp/tree/0fa3234851d19fbc4568e3f39d5b3a69d26e7239). AI-assisted README and LICENSE inspection; install/live paths not executed.
