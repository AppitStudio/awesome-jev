# Jev-Frame

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python framework for typed, auditable Jev decisions in agents: describe judgments, candidate sets, completion contracts and budgets, and it compiles the Jev questions, tracks evidence with provenance and returns a supported typed result or an explicit unresolved outcome.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chayan-bit/Jev-Frame) |
| Maintainer | [chayan-bit](https://github.com/chayan-bit). Independently curated. |
| Format | Python library (3.11+, typed) with LangChain and Pydantic AI extras |
| Requirements | Python 3.11+; your own `TYPESAFE_API_KEY` for live calls (offline previews need none). |
| License | [MIT](https://github.com/chayan-bit/Jev-Frame/blob/29ba1c3e10e0e386684e056b344eea70baecbfca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_frame/compiler.py`](https://github.com/chayan-bit/Jev-Frame/blob/29ba1c3e10e0e386684e056b344eea70baecbfca/src/jev_frame/compiler.py) at the pinned commit. |

## When to use

- Add Jev decision points (which source to trust, is a claim supported, may an action proceed) to an existing Python agent.
- Keep a clear line between model confidence and authorization, with budgets and no-fit handling built in.
- Mismatch: early release (v0.1.x); independent project, not an official TypeSafe SDK.

## How it works

Definitions are immutable and versioned; the compiler turns them into Choice, Noul and Score questions, and direct calls (`evaluate`, `select`, `filter`, `assess`, `score`) work without the optional shared scheduler. A companion project, jev-harness, builds on it for coding-agent harnesses. Integration evidence: [`src/jev_frame/compiler.py`](https://github.com/chayan-bit/Jev-Frame/blob/29ba1c3e10e0e386684e056b344eea70baecbfca/src/jev_frame/compiler.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "jev-frame @ git+https://github.com/chayan-bit/Jev-Frame@v0.1.1"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quickstart demo: `docs/demos/quickstart.gif`.
- Companion: [github.com/chayan-bit/jev-harness](https://github.com/chayan-bit/jev-harness)

## Limits and data handling

Whatever state you pass goes to TypeSafe on your key. The framework records evidence and decisions locally.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 29ba1c3e10e0](https://github.com/chayan-bit/Jev-Frame/tree/29ba1c3e10e0e386684e056b344eea70baecbfca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
