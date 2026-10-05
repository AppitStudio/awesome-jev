# enowx

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Early-release terminal coding agent (one Rust binary, specialist agents, any model provider) with an off-by-default decision model that can use TypeSafe Jev to decide brainstorm-vs-build, which specialist to delegate to, and when to ask the user.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/enowdev/enowxcli) |
| Product homepage | [enowx.ai](https://enowx.ai) |
| Maintainer | [enowdev](https://github.com/enowdev). Independently curated. |
| Format | Terminal coding agent; decision model optional |
| Requirements | The enowx binary (install script or release download) and a main model provider. Jev needs a TypeSafe key (`TYPESAFE_API_KEY` is read when none is stored). Enable in Settings > Decision model or `/decision`. |
| License | [Apache-2.0](https://github.com/enowdev/enowxcli/blob/86fbb7dc221cf8419894b2aa3d82d6ab3d63521b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let a decision model tell the lead agent which single specialist to delegate to, and whether a security review is needed.
- Avoid unnecessary questions to the user: Jev judges whether a question is really the user's to answer (taste, money, irreversible actions, credentials).
- Mismatch: Clef is the default provider; Jev is one of several selectable options.

## How it works

When enabled, each use (brainstorm or build at 0.8, which specialist at 0.7, when to ask the user at 0.8, plus a shell gate for risky commands) asks a typed question and acts only above its threshold; when unsure, enowx behaves as without the model. With the decision model off, none of this runs ([README: Decision model](https://github.com/enowdev/enowxcli/blob/86fbb7dc221cf8419894b2aa3d82d6ab3d63521b/README.md#decision-model)).

## Get started

Install, start enowx, and enable the decision model with Jev as the provider (live Jev calls once enabled):

```sh
curl -fsSL https://enowx.ai/install.sh | sh
export TYPESAFE_API_KEY=...
enowx
# inside enowx: /decision  -> provider Jev, then 'Test the connection'
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Decision model* section lists every decision, its default threshold, and fallback behavior.

## Limits and data handling

Early release (upstream asks users to report bugs). Decision questions send the relevant message text to the chosen provider and incur its charges. Keys are stored in `~/.enx/auth.json`.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 86fbb7dc221c](https://github.com/enowdev/enowxcli/tree/86fbb7dc221cf8419894b2aa3d82d6ab3d63521b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
