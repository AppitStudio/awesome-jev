# OntoSmith (ontology-driven knowledge-graph builder where models propose facts and Jev judges which are true enough to write into Neo4j, each with its evidence span)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python package and CLI that builds governed knowledge graphs from a document corpus: you approve an ontology (a flat extraction contract of entity and relation types with definitions), a cheaper model proposes candidate triples, deterministic gates check them, and the pinned Jev decision model decides what is written to a Neo4j graph with evidence spans and provenance. It ships keyless profile, inspect, replay and search steps, and the README publishes cost and precision figures with the audit working.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Dongbumlee/ontosmith) |
| Maintainer | [Dongbumlee](https://github.com/Dongbumlee). Independently curated. |
| Format | Python package and CLI (`pip install ontosmith`, MIT) with a Neo4j graph store |
| Requirements | Python 3.11 or newer on Linux (WSL2 on Windows), Neo4j 5.x (Community Edition is enough) for live builds, and an LLM connection key; the reference setup reaches its four models, including `typesafe/jev-1.13`, through one connection key. Profile, inspect, validate and replay steps run without a key. |
| License | [MIT](https://github.com/Dongbumlee/ontosmith/blob/1412da4d740ae6b1519ee411b28a294922321e62/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Connected_Data/status/2118300588446220717)). |
| Jev evidence | [`pipeline/decisions.py`](https://github.com/Dongbumlee/ontosmith/blob/1412da4d740ae6b1519ee411b28a294922321e62/pipeline/decisions.py) at the pinned commit. |

## When to use

- Turn a contract, paper or document corpus into an auditable graph where every written fact carries its evidence span and a judged score.
- See a worked pattern for splitting proposing from judging, with thresholds fitted stage by stage and failed experiments kept in the record.
- Mismatch: live builds need Neo4j and model keys and cost money; the README says the schema is a flat extraction contract, not an OWL ontology, and runs no reasoning.

## How it works

`pipeline/decisions.py` is the thin client for the decisions API that serves the Jev gate routes (triple, entity resolution, conflict, ontology and cascade checks); the `judge` seat is pinned to `typesafe/jev-1.13` in the reference profile and the other seats (proposer, escalation, drafting, embedder) are yours to bind. Integration evidence: [`pipeline/decisions.py`](https://github.com/Dongbumlee/ontosmith/blob/1412da4d740ae6b1519ee411b28a294922321e62/pipeline/decisions.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install ontosmith
ontosmith profile examples/corpus --family demo
ontosmith search "What is Mr. Darcy's income?"   # shipped demo build, no key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (method, reference profile, quality record): [github.com/Dongbumlee/ontosmith/blob/1412da4d740ae6b1519ee411b28a294922321e62/README.md](https://github.com/Dongbumlee/ontosmith/blob/1412da4d740ae6b1519ee411b28a294922321e62/README.md)
- Project site: [dongbumlee.github.io/ontosmith/](https://dongbumlee.github.io/ontosmith/)
- PyPI: [pypi.org/project/ontosmith/](https://pypi.org/project/ontosmith/)

## Limits and data handling

Live builds send document text and candidate facts to the model providers you bind, and the README projects cents per document for judging, with costs depending on your corpus and bindings. Published precision and recall figures are the author's own measurements. Native Windows is not a tested platform.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 1412da4d740a](https://github.com/Dongbumlee/ontosmith/tree/1412da4d740ae6b1519ee411b28a294922321e62). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
