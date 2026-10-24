# fast-jev-compaction (Lexus2016 maintained fork: Claude Code compaction by Jev that keeps every call)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Maintained fork of the listed fast-jev-compaction Claude Code plugin: Jev scores each tool call, stale outputs become a one-line note while every call stays, kept content stays verbatim, and community pull requests from upstream are audited and ported.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lexus2016/fast-jev-compaction) |
| Maintainer | [Lexus2016](https://github.com/Lexus2016). Independently curated. |
| Format | Claude Code plugin and npm library (TypeScript) |
| Requirements | Claude Code; a TypeSafe API key. |
| License | [MIT](https://github.com/Lexus2016/fast-jev-compaction/blob/bec4021842319827c42e4314b8468140ce34c87d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/YevMur/status/2113991483854602397)). |
| Jev evidence | [`src/request.ts`](https://github.com/Lexus2016/fast-jev-compaction/blob/bec4021842319827c42e4314b8468140ce34c87d/src/request.ts) at the pinned commit. |

## When to use

- Compact long Claude Code sessions without an LLM summary losing paths and decisions.
- Pick up fixes for upstream issues such as missing tool results after compaction.
- Mismatch: replaces an upstream install; remove that first.

## How it works

`src/request.ts` posts the history to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) with keep-call and keep-result questions; long histories are asked in windows, and secrets are redacted before sending. FORK.md logs every upstream PR reviewed. Integration evidence: [`src/request.ts`](https://github.com/Lexus2016/fast-jev-compaction/blob/bec4021842319827c42e4314b8468140ce34c87d/src/request.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add Lexus2016/fast-jev-compaction
claude plugin install fast-jev-compaction@lexus2016
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Fork audit log: [github.com/Lexus2016/fast-jev-compaction/blob/main/FORK.md](https://github.com/Lexus2016/fast-jev-compaction/blob/main/FORK.md)
- Upstream: [github.com/tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)

## Limits and data handling

Session history (with secrets redacted) is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit bec402184231](https://github.com/Lexus2016/fast-jev-compaction/tree/bec4021842319827c42e4314b8468140ce34c87d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
