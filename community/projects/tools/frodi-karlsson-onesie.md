# onesie

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unix-pipeable System One CLI for TypeSafe Jev (also OpenRouter/Berget): pipe text, ask a typed question, script the answer

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frodi-karlsson/onesie) |
| Maintainer | [frodi-karlsson](https://github.com/frodi-karlsson). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go CLI (Unix-pipeable System One client). |
| Requirements | Go toolchain or released binary; TypeSafe, OpenRouter, or Berget credentials per README. |
| License | [MIT](https://github.com/frodi-karlsson/onesie/blob/96ed118e6cf3ee3e934b08bc931fe198208cb00f/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when shell pipelines or scripts need a fast typed System One answer. Prefer SDKs when embedding Jev inside an application.

## How it works

CLI wraps System One providers with pipe-friendly I/O. Integration evidence: upstream README at the pinned commit. HN Show HN noted 2026-09-28.

## Get started

```sh
git clone https://github.com/frodi-karlsson/onesie.git
cd onesie
git checkout 96ed118e6cf3ee3e934b08bc931fe198208cb00f
```

Pin revision `96ed118e6cf3ee3e934b08bc931fe198208cb00f` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 96ed118](https://github.com/frodi-karlsson/onesie/tree/96ed118e6cf3ee3e934b08bc931fe198208cb00f). AI-assisted README and LICENSE inspection; install/live paths not executed.
