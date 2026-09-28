# jev-humanizer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Anti-slop skill: TypeSafe Jev flags AI-sounding paragraphs so the writing model rewrites only those spans (RU-focused humanizer)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/snjrusmn/jev-humanizer) |
| Maintainer | [snjrusmn](https://github.com/snjrusmn). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code / Codex skill (Python stdlib). |
| Requirements | Python 3; TypeSafe key; Claude Code or Codex. |
| License | [MIT](https://github.com/snjrusmn/jev-humanizer/blob/1ec645fdf27300f21aeb8c054dc0b9b49b9c4b2f/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when agents should detect and surgically rewrite AI-sounding prose with Jev paragraph judgments. Prefer English-only humanizers if you do not need the RU workflow.

## How it works

Jev scores paragraphs for neural-style tells; the host model edits only flagged spans. Based on smixs/humanizer-ru and blader/humanizer patterns. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/snjrusmn/jev-humanizer.git
cd jev-humanizer
git checkout 1ec645fdf27300f21aeb8c054dc0b9b49b9c4b2f
```

Pin revision `1ec645fdf27300f21aeb8c054dc0b9b49b9c4b2f` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 1ec645f](https://github.com/snjrusmn/jev-humanizer/tree/1ec645fdf27300f21aeb8c054dc0b9b49b9c4b2f). AI-assisted README and LICENSE inspection; install/live paths not executed.
