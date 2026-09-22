# Cairn Jev Lab

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental memory-admission lab: TypeSafe Jev judges whether a proposed memory is supported by a source passage; inspectable policy recommends **save**, **skip**, or **defer**, with editable cases and published recorded results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Cairn-ink/cairn-jev-lab) |
| Maintainer | [Cairn-ink](https://github.com/Cairn-ink). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js ≥ 22 lab (`cairn-jev-lab` 0.1.0): zero runtime deps, CLI, local playground server, public static demo. |
| Requirements | Node **≥ 22**. Offline preview/tests need no key. Live evaluation needs `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Cairn-ink/cairn-jev-lab/blob/9127614d2f5011938e7281d11dad5c6bed8b2baa/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline `node --test` **20 passed**. Live TypeSafe / public-lab submissions not run here. Distinct from [Jev-Mem](jev-mem.md) (graph memory controller) and other Cairn memory repos. |

## When to use

Use it when you want to **test a memory-admission policy** before an agent stores claims: editable cases, retained judgments (including mistakes), and a deterministic policy over Jev answers. Prefer [Jev-Mem](jev-mem.md) for a multi-view graph that also links and retrieves; prefer [PerfectRecall](perfectrecall.md) for Hermes SQLite evidence recall without this lab UI.

## How it works

[`src/jev.mjs`](https://github.com/Cairn-ink/cairn-jev-lab/blob/9127614d2f5011938e7281d11dad5c6bed8b2baa/src/jev.mjs) posts typed questions to `https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`. Local policy turns Jev answers into save/skip/defer with inspectable reasons. The lab does not extract, rewrite, or persist long-term memory; a `save` is a recommendation only. Source and candidate text leave the host on live runs.

## Get started

```sh
git clone https://github.com/Cairn-ink/cairn-jev-lab.git
cd cairn-jev-lab
git checkout 9127614d2f5011938e7281d11dad5c6bed8b2baa
node --test
node src/cli.mjs
# Live (charges): copy .env.example → .env with TYPESAFE_API_KEY, then
# node --env-file=.env src/cli.mjs --live --input examples/my-cases.json
```

Public recorded walkthrough: [lab.cairn.ink](https://lab.cairn.ink) (no key; visitors cannot submit live evaluations).

## Examples and demos

- Offline `node --test`: **20 passed** on the review host.
- `npm run preview` / recorded playground cases without a key.
- Published evidence under `evidence/` (upstream labels; AI-authored per README—not revalidated here).

## Limits and data handling

Developer preview: upstream reports imperfect match rates on synthetic English cases; treat those as experiment notes, not production quality claims. Live calls send case text to TypeSafe. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 9127614](https://github.com/Cairn-ink/cairn-jev-lab/tree/9127614d2f5011938e7281d11dad5c6bed8b2baa): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `src/jev.mjs`, CLI/server, and tests. **`node --test`: 20 passed**. No live TypeSafe.

Related: [Jev-Mem](jev-mem.md), [PerfectRecall](perfectrecall.md), [jevmory](jevmory.md).
