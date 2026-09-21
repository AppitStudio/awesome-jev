# JevTape

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Record / replay / inspect tool for TypeSafe Jev HTTP decisions: a local proxy writes JSON cassettes (state, question contracts, answers, usage), then replays them offline for development and CI without an API key or network.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Hugo-DDT/JevTape) |
| Maintainer | [Hugo-DDT](https://github.com/Hugo-DDT). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Java 21 Maven CLI **`io.jevtape:jevtape` 0.5.0** (CLI: record, replay, inspect, verify, diff, simulate). |
| Requirements | JDK 21+ and Maven to build. Record mode needs a live TypeSafe key and network; replay defaults to offline cassette hits. |
| License | [Apache-2.0](https://github.com/Hugo-DDT/JevTape/blob/71d8ff42b96e907140dea400bb8bff250c10d7c8/LICENSE). TypeSafe usage billed separately when recording. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source + fixtures inspected; `mvn verify` was not run (no JDK in this environment). |

## When to use

Use it when Jev-backed tests should assert against frozen decision contracts instead of live API calls. Prefer ordinary HTTP VCRs only when you do not need Decision Contract fingerprint miss diagnosis (state / questions / model mismatches).

## How it works

`jevtape record` listens locally (default `http://127.0.0.1:8787`), forwards to `https://api.typesafe.ai`, and stores cassettes under `.jevtape/cassettes`. Replay matches on decision context (state, Choice/Score/Noul definitions, model) and can return structured miss reasons when the contract drifts. `onMiss` defaults to `error`; `live` / `record` miss policies are opt-in and touch the network.

## Get started

```sh
git clone https://github.com/Hugo-DDT/JevTape.git
cd JevTape
git checkout 71d8ff42b96e907140dea400bb8bff250c10d7c8
mvn verify   # offline suite per README; not executed in this listing environment
# then point your Jev client at the local proxy for record/replay
```

Live record sessions send full Jev request bodies to TypeSafe and can incur charges. Commit cassettes carefully—they contain judged state.

## Examples and demos

- README quick-start record/replay transcript and miss diagnosis example.
- Fixture cassettes under `fixtures/cassette-v1/`.

## Limits and data handling

Cassettes may hold application state text and decision answers. Replay quality depends on stable Decision Contracts; changing criteria intentionally produces misses. Simulate (edge cases) is documented as v0.5.0.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 71d8ff4](https://github.com/Hugo-DDT/JevTape/tree/71d8ff42b96e907140dea400bb8bff250c10d7c8): **0.5.0**, Apache-2.0. AI-assisted source review of README, LICENSE, `pom.xml`, cassette/CLI packages, and fixtures. No JDK available here—Maven tests not run. No live TypeSafe calls.

Related: [jevals](jevals.md), [JevScope](jevscope.md), [prompt2jev](prompt2jev.md).
