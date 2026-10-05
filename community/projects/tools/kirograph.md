# KiroGraph

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local semantic code knowledge graph and MCP server for Kiro (experimental support for other agents) whose opt-in memory-relation, wiki-contradiction and auth-detection modes can use TypeSafe Jev typed classification.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/davide-desio-eleva/kirograph) |
| Maintainer | [davide-desio-eleva](https://github.com/davide-desio-eleva). Independently curated. |
| Format | CLI and MCP server with opt-in modules; Jev modes are experimental |
| Requirements | Node.js and npm; install from source (the README notes it is not yet on the npm registry). Jev modes need `JEV_API_KEY` in `.kirograph/.env` or the environment. |
| License | [MIT](https://github.com/davide-desio-eleva/kirograph/blob/3457727b99e1a43b4cd95d1c0e3e5e23d753c6f5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Auto-classify whether a new memory observation supersedes, conflicts with or is compatible with an old one instead of spending an agent turn.
- Replace a keyword heuristic for wiki contradictions or custom-named auth wrappers with a calibrated judgment.
- Mismatch: full support is for Kiro; other agent integrations are experimental. Use `'strands'` if nothing may leave the machine.

## How it works

Each Jev-enabled mode sends a narrow Choice/Score/Noul question (e.g. relation between two observations, whether an FTS-similar page pair contradicts, whether a route is authenticated) and acts only above a confidence threshold (defaults 0.8 for memory relations, 0.6 for auth). Unset or unreachable backends fall back to existing behavior ([configuration](https://github.com/davide-desio-eleva/kirograph/blob/3457727b99e1a43b4cd95d1c0e3e5e23d753c6f5/docs/guide/configuration.md)).

## Get started

Build from source, install the integration, and enable one Jev mode (live Jev calls when the mode runs):

```sh
git clone https://github.com/davide-desio-eleva/kirograph && cd kirograph
npm install && npm run build && npm install -g .
kirograph install --target kiro
echo 'JEV_API_KEY=...' >> .kirograph/.env
# .kirograph/config.json: "memoryRelationMode": "jev"
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `test/jev/test.sh` exercises the Jev path against a bundled mock server, or the real API when `JEV_API_KEY` is set (not run here).

## Limits and data handling

Upstream marks Jev modes experimental and not yet exercised in production; Jev is the only KiroGraph feature that needs a paid external API. Content of the judged observations, pages or route/call-path names goes to TypeSafe. The rest of KiroGraph runs locally.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 3457727b99e1](https://github.com/davide-desio-eleva/kirograph/tree/3457727b99e1a43b4cd95d1c0e3e5e23d753c6f5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
