# jev-enforce

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that checks every reply and edit against your AGENTS.md with TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/erkamyaman/jev-enforce) |
| Maintainer | [erkamyaman](https://github.com/erkamyaman). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code plugin + CLI (`npx jev-enforce`). |
| Requirements | Node.js 18+; Claude Code; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/erkamyaman/jev-enforce/blob/ed9c7d79bad2bfdea474df5e414b8b601c0e92cd/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when Claude Code should treat CLAUDE.md/AGENTS.md as enforceable constraints rather than soft context.

## How it works

Stop and PostToolUse hooks turn project rules into typed Jev questions; broken rules return as block decisions so Claude fixes them before you see them. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/erkamyaman/jev-enforce.git
cd jev-enforce
git checkout ed9c7d79bad2bfdea474df5e414b8b601c0e92cd
# or: claude plugin marketplace add erkamyaman/jev-enforce && claude plugin install jev-enforce@jev-enforce
# set TYPESAFE_API_KEY; follow upstream README
```

Pin revision `ed9c7d79bad2bfdea474df5e414b8b601c0e92cd` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe checks not run on the review host. Without a key, checks are skipped.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit ed9c7d7](https://github.com/erkamyaman/jev-enforce/tree/ed9c7d79bad2bfdea474df5e414b8b601c0e92cd). AI-assisted README and LICENSE inspection; install/live paths not executed.
