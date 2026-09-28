# jev-auto-approve

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hook: TypeSafe Jev auto-approves read-only shell commands in milliseconds; everything else still prompts you (fail-open)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BasmaAbouzied0/jev-auto-approve) |
| Maintainer | [BasmaAbouzied0](https://github.com/BasmaAbouzied0). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code PreToolUse-style hook (Python). |
| Requirements | Claude Code; TypeSafe key. |
| License | [MIT](https://github.com/BasmaAbouzied0/jev-auto-approve/blob/d8e636635d00dd7b201522a6b3fe0d36efca4982/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to cut permission prompts on clearly read-only shell commands without auto-approving risky actions. Prefer stricter allowlists if you want zero model involvement.

## How it works

Hook may only allow or stay silent; silence restores Claude Code's normal prompt. Never blocks. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/BasmaAbouzied0/jev-auto-approve.git
cd jev-auto-approve
git checkout d8e636635d00dd7b201522a6b3fe0d36efca4982
```

Pin revision `d8e636635d00dd7b201522a6b3fe0d36efca4982` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit d8e6366](https://github.com/BasmaAbouzied0/jev-auto-approve/tree/d8e636635d00dd7b201522a6b3fe0d36efca4982). AI-assisted README and LICENSE inspection; install/live paths not executed.
