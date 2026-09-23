# JevApi

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

.NET 10 tooling for TypeSafe Jev: AOT-friendly `TypeSafe.Client` plus a stdio MCP server exposing evaluate / batch / validate tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JawzoD3TH/JevApi) |
| Maintainer | [JawzoD3TH](https://github.com/JawzoD3TH). Independently curated. Not an endorsement. |
| Format | .NET libraries + MCP host (`TypeSafe.Client`, `JevMcp`). |
| Requirements | .NET 10 SDK; `TYPESAFE__ApiKey` or `TypeSafe:ApiKey` in appsettings. |
| License | [MIT](https://github.com/JawzoD3TH/JevApi/blob/0bf7aa1cdae399c4b3dc5d03f9aa003a4c07d144/LICENSE.txt). TypeSafe usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE.txt). Live MCP/Jev **not** run. Distinct from other .NET/Jev SDK listings. |

## When to use

Use it when a .NET or MCP-connected agent needs typed noul/choice/score against TypeSafe System One with retries and DI helpers.

## How it works

`TypeSafe.Client` posts to `https://api.typesafe.ai/v1/systemone` with typed answer models and backoff on 429/529. `JevMcp` wraps evaluate, evaluate_batch, validate_questions, and examples over stdio MCP.

## Get started

```sh
git clone https://github.com/JawzoD3TH/JevApi.git
cd JevApi && git checkout 0bf7aa1cdae399c4b3dc5d03f9aa003a4c07d144
dotnet build JevApi.slnx
# set TYPESAFE__ApiKey; point MCP client at built JevMcp
```

## Examples and demos

- TypeSafe.Client and MCP README usage tables.
- No separate public demo site.

## Limits and data handling

States and questions go to TypeSafe. MCP validate_questions is free/local per README. No live spend here.

## Review and maintenance

Reviewed **2026-09-23** at [commit 0bf7aa1](https://github.com/JawzoD3TH/JevApi/tree/0bf7aa1cdae399c4b3dc5d03f9aa003a4c07d144) (MIT LICENSE.txt). AI-assisted source review. No live TypeSafe spend.

Related: [go-jev](go-jev.md), [jev4k](jev4k.md), [jev4j](https://github.com/maxsumrall/jev4j).
