# opencode-jev-compaction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that compacts sessions by pruning with Jev instead of summarizing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/radqnico/opencode-jev-compaction) |
| Maintainer | [radqnico](https://github.com/radqnico). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | OpenCode plugin package. |
| Requirements | OpenCode; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/radqnico/opencode-jev-compaction/blob/1f3e97c8fc1e1620de10266fdb46808d208d7ebb/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when OpenCode summaries lose exact paths/errors. Prefer LLM summarize when you want a narrative digest.

## How it works

Compaction hook sends size-noted tool transcripts to Jev Noul questions per call; keeps verbatim text for retained content. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
opencode plugin add github:radqnico/opencode-jev-compaction
export TYPESAFE_API_KEY=…
# restart OpenCode; opencode plugin list
```

Pin revision `1f3e97c8fc1e1620de10266fdb46808d208d7ebb` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

OpenCode-only host integration. Sends session tool text to TypeSafe. Live compaction not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 1f3e97c](https://github.com/radqnico/opencode-jev-compaction/tree/1f3e97c8fc1e1620de10266fdb46808d208d7ebb). AI-assisted README and LICENSE inspection; install/live paths not executed.
