# jev-fabric

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single native executable (written in Bend) that owns an agent's long-running processes with deadlines and bounded logs, and asks Jev a typed choice/noul/score question only when explicitly told to.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fabric-runtime/jev-fabric) |
| Maintainer | [fabric-runtime](https://github.com/fabric-runtime). Independently curated. |
| Format | Native CLI (macOS universal, Linux x64/arm64) + agent skill |
| Requirements | No runtime dependencies; TypeSafe API key only for explicit Jev calls. |
| License | [MIT](https://github.com/fabric-runtime/jev-fabric/blob/174af1f83f20d1c8523c5d0d4ba266808f5ed8c9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`native/JevCore.bend`](https://github.com/fabric-runtime/jev-fabric/blob/174af1f83f20d1c8523c5d0d4ba266808f5ed8c9/native/JevCore.bend) at the pinned commit. |

## When to use

- Give a coding agent dev servers and test runs it can watch for 'ready' without reading huge logs.
- Branch on a single fuzzy judgment (e.g. 'did this run fail?') with a typed answer.
- Mismatch: process orchestration first; Jev calls are opt-in.

## How it works

jev-fabric runs each child in its own process group with a deadline and bounded log receipts; a Jev call sends a bounded state plus a typed question and maps the answer onto a branch you wrote, with no free-text inference. Integration evidence: [`native/JevCore.bend`](https://github.com/fabric-runtime/jev-fabric/blob/174af1f83f20d1c8523c5d0d4ba266808f5ed8c9/native/JevCore.bend).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://raw.githubusercontent.com/fabric-runtime/jev-fabric/main/install.sh | sh
npx skills add fabric-runtime/jev-fabric
jev-fabric -- exec /bin/echo ready
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision profiles: `examples/decision-profiles.json`.

## Limits and data handling

Only the bounded state you pass to an explicit Jev call is sent to TypeSafe, billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 174af1f83f20](https://github.com/fabric-runtime/jev-fabric/tree/174af1f83f20d1c8523c5d0d4ba266808f5ed8c9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
