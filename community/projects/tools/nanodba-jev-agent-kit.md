# jev-agent-kit (nanoDBA)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Give your coding agent a second opinion on risky tool calls—TypeSafe Jev as an evidence layer (shadow by default).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nanoDBA/jev-agent-kit) |
| Maintainer | [nanoDBA](https://github.com/nanoDBA). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python hooks kit for Claude Code, Codex, and Hermes Agent. |
| Requirements | Python; agent host; `TYPESAFE_API_KEY` for live scoring. |
| License | [MIT](https://github.com/nanoDBA/jev-agent-kit/blob/cd333a51c0408f8142f35fdb35b12498d1065637/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from walidboulanouar/jev-agent-kit. |

## When to use

Use when you want Jev evidence on risky tool calls without letting Jev grant permissions.

## How it works

Hooks turn tool calls into typed Jev questions (destructive/exfil/permission widen) and record evidence; agent permissions still decide. Shadow mode by default. Distinct from walidboulanouar/jev-agent-kit. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/nanoDBA/jev-agent-kit.git
cd jev-agent-kit
git checkout cd333a51c0408f8142f35fdb35b12498d1065637
# python examples/gate_walkthrough.py for offline demo; follow upstream README for hooks
```

Pin revision `cd333a51c0408f8142f35fdb35b12498d1065637` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Early/unarmed: shadow mode default; question sets not calibrated for approval. Live paths not run on the review host. Distinct from walidboulanouar/jev-agent-kit.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit cd333a5](https://github.com/nanoDBA/jev-agent-kit/tree/cd333a51c0408f8142f35fdb35b12498d1065637). AI-assisted README and LICENSE inspection; install/live paths not executed.
