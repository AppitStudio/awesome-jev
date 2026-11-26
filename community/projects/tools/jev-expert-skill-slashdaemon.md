# jev-expert by Slash Daemon (Claude Code skill: a reference on Jev's API, calibration, weak spots, integration patterns and gateway dialects, with a Java client)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill that loads a reference for building with Jev whenever TypeSafe or Jev comes up: the API contract and primitives, confidence calibration and its quirks, where Jev is weak, patterns (classify, route, rerank, gate, guard an LLM), real-time loops with case studies, gateway dialects (OpenRouter, Vercel, Cloudflare), an audit of community SDKs and a dependency-free Java client. Not the unrelated Nostoi/jev-expert plugin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/slashdaemon/jev-expert) |
| Maintainer | [Slash Daemon](https://github.com/slashdaemon). Independently curated. |
| Format | Claude Code skill (Markdown references + Java example + verify script) |
| Requirements | Claude Code; a TypeSafe API key only for `scripts/verify.sh`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/verify.sh`](https://github.com/slashdaemon/jev-expert/blob/9db50d3c7e83437b46c0e190c46218916a02e9be/scripts/verify.sh) at the pinned commit. |

## When to use

- Coding agents writing Jev integrations that should follow the documented API and known pitfalls rather than guess.
- Mismatch: an official or always-current reference; the 2026-09-27 refresh material is tagged as not re-run against the live API.

## How it works

`SKILL.md` triggers on TypeSafe/Jev work and points the agent at the `references/` files. `scripts/verify.sh` replays the captured fixtures in `examples/verified/` against `https://api.typesafe.ai/v1/systemone` and fails on schema drift (captured against jev-1.13.0 on 2026-09-19). Integration evidence: [`scripts/verify.sh`](https://github.com/slashdaemon/jev-expert/blob/9db50d3c7e83437b46c0e190c46218916a02e9be/scripts/verify.sh).

## Get started

Clone into your Claude Code skills folder; Claude Code picks it up and you can call `/jev-expert`.

```sh
git clone https://github.com/slashdaemon/jev-expert ~/.claude/skills/jev-expert
export TYPESAFE_API_KEY=...   # optional, for the live check
bash ~/.claude/skills/jev-expert/scripts/verify.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Java client: [github.com/slashdaemon/jev-expert/blob/9db50d3c7e83437b46c0e190c46218916a02e9be/examples/JevClient.java](https://github.com/slashdaemon/jev-expert/blob/9db50d3c7e83437b46c0e190c46218916a02e9be/examples/JevClient.java)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Reference content is the author's: claims were live-verified on 2026-09-19, and the later material from TypeSafe's spec, SDK changelogs and about 80 independent projects is tagged `[INDEP]` or `[DOC]` and was not re-run. Check current TypeSafe docs for prices and limits.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 9db50d3c7e83](https://github.com/slashdaemon/jev-expert/tree/9db50d3c7e83437b46c0e190c46218916a02e9be). Inspected the README, SKILL.md, the reference files list and `scripts/verify.sh` at the pinned commit; the verify script was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
