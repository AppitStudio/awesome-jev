# JevRepoTriage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted GitHub issue/PR triage assistant: TypeSafe Jev classifies items; operators keep control of labels and replies via a local web UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/murongg/JevRepoTriage) |
| Maintainer | [murongg](https://github.com/murongg) / JevMate contributors. Independently curated. |
| Format | TypeScript app (workers + web UI); optional hosted demo at [triage.mrong.me](https://triage.mrong.me/). |
| Requirements | Node.js; GitHub App/token credentials; `TYPESAFE_API_KEY` (or equivalent) for System One calls. |
| License | [MIT](https://github.com/murongg/JevRepoTriage/blob/3f0d7b1044a2560cb71eaab206558ee4c90764bc/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Live GitHub/Jev triage not run. Hosted demo terms are operator-controlled. |

## When to use

Use it to **triage issues/PRs with calibrated Jev labels** on your own host. Prefer a one-shot Actions labeler ([Jev GitHub Action](jev-action.md)) when you do not want a standing service.

## How it works

[`src/triage.ts`](https://github.com/murongg/JevRepoTriage/blob/3f0d7b1044a2560cb71eaab206558ee4c90764bc/src/triage.ts) and [`src/pull-triage.ts`](https://github.com/murongg/JevRepoTriage/blob/3f0d7b1044a2560cb71eaab206558ee4c90764bc/src/pull-triage.ts) POST to `https://api.typesafe.ai/v1/systemone`. Account helpers probe `/v1/models`. UI/workers apply operator-approved outcomes.

## Get started

```sh
git clone https://github.com/murongg/JevRepoTriage.git
cd JevRepoTriage
git checkout 3f0d7b1044a2560cb71eaab206558ee4c90764bc
# follow README / docs/deployment.md for env, GitHub App, and start
```

## Examples and demos

- [triage.mrong.me](https://triage.mrong.me/) (third-party host; treat as untrusted for private repos).
- Tests under `tests/` (not executed here).

## Limits and data handling

Issue/PR text leaves the host on live Jev calls. GitHub tokens and TypeSafe keys must stay in server env—not in the public tree.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 3f0d7b1](https://github.com/murongg/JevRepoTriage/tree/3f0d7b1044a2560cb71eaab206558ee4c90764bc). AI-assisted README/LICENSE/`src/triage.ts` inspection. No live deploy.

Related: [Jev GitHub Action](jev-action.md), [agent-fastpath](agent-fastpath.md).
