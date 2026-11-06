# cog-brief-router (decision Cog that routes missing-Cog briefs with System One / TypeSafe Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Example decision Cog for the Cogcloud builder suite: a System One model (TypeSafe Jev or an LLM through the System One adapter) answers five typed questions about a missing-Cog brief; task logic turns the answers into a code/context/decision recommendation with review flags.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cogcloud-ai/cog-brief-router) |
| Maintainer | [cogcloud-ai](https://github.com/cogcloud-ai). Independently curated. |
| Format | Cogcloud decision Cog (Python, Apache-2.0) |
| Requirements | Cogcloud suite with a System One binding (TypeSafe Jev or System One adapter) admitted. |
| License | [Apache-2.0](https://github.com/cogcloud-ai/cog-brief-router/blob/0f8a00f086a6d2c6232a39117829df5e10002ab7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cog.yaml`](https://github.com/cogcloud-ai/cog-brief-router/blob/0f8a00f086a6d2c6232a39117829df5e10002ab7/cog.yaml) at the pinned commit. |

## When to use

- Classify missing-Cog briefs inside Cogcloud.
- Prefer typed System One answers over free-form chat.
- Mismatch: Cogcloud-specific example; not a standalone CLI.

## How it works

The Cog admits a System One binding (TypeSafe Jev or the System One adapter) and asks five typed questions; `src/task_logic.py` maps answers to a recommendation. Integration evidence: [`cog.yaml`](https://github.com/cogcloud-ai/cog-brief-router/blob/0f8a00f086a6d2c6232a39117829df5e10002ab7/cog.yaml).

## Get started

Install into a Cogcloud suite that already admits TypeSafe Jev (or the System One adapter) per COG.md / README.

```sh
git clone https://github.com/cogcloud-ai/cog-brief-router.git && cd cog-brief-router
# follow COG.md / README inside a Cogcloud suite with System One admitted
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cogcloud-ai/cog-brief-router/blob/0f8a00f086a6d2c6232a39117829df5e10002ab7/README.md](https://github.com/cogcloud-ai/cog-brief-router/blob/0f8a00f086a6d2c6232a39117829df5e10002ab7/README.md)

## Limits and data handling

Brief text under review is sent to the admitted System One binding on your configured key.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 0f8a00f086a6](https://github.com/cogcloud-ai/cog-brief-router/tree/0f8a00f086a6d2c6232a39117829df5e10002ab7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
