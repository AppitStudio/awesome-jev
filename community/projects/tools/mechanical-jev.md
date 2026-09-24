# Mechanical Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust client, `mjev` CLI, and evaluation harness for System One Noul/Choice/Score against a local Intel Phi Jev server (or compatible `/v1/systemone` endpoint).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Lasimeri/Mechanical-Jev) |
| Maintainer | [Lasimeri](https://github.com/Lasimeri). Independently curated. |
| Format | Rust library + CLI (`mjev`). |
| Requirements | Rust toolchain; companion [Intel-Phi-Jev](https://github.com/Lasimeri/Intel-Phi-Jev) server for local Xeon Phi inference (or another System One endpoint via `TYPESAFE_BASE_URL`). |
| License | [Apache-2.0](https://github.com/Lasimeri/Mechanical-Jev/blob/da49f9795dbc3ae151d74b0b118461a0ee92c323/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Local Phi server / live closeness eval not run on the review host. |

## When to use

Use to **ask System One questions from Rust** with typed builders, retries, and offline reconstruct/evidence tools. Prefer official TypeSafe SDKs for the hosted cloud API without a local Phi stack.

## How it works

`RequestBuilder` assembles Noul/Choice/Score questions; `Client::system_one` posts the System One wire format. `mjev eval` / `mjev corroborate` / `mjev evidence` support labeled harnesses and published-question closeness checks (per README).

## Get started

```sh
git clone https://github.com/Lasimeri/Mechanical-Jev.git
cd Mechanical-Jev
git checkout da49f9795dbc3ae151d74b0b118461a0ee92c323
make build
# Configure TYPESAFE_BASE_URL / companion Intel-Phi-Jev per README
./target/release/mjev query --state '$ git status' --noul 'ro=Is this command read-only?'
```

## Examples and demos

- README library snippet and `make query` / `make eval` / `make closeness` targets.

## Limits and data handling

This repo holds no model weights and runs no inference itself. Requests go to the configured server; local Phi hardware and model licenses are separate.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit da49f97](https://github.com/Lasimeri/Mechanical-Jev/tree/da49f9795dbc3ae151d74b0b118461a0ee92c323). AI-assisted README and LICENSE inspection; live Phi serve not run.
