# TypeSafe C++ SDK

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

C++20 client for TypeSafe System One (Choice/Score/Noul) with a builder-configured `TypeSafeClient` targeting models such as Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pewriebontal/typesafe-sdk-cpp) |
| Maintainer | [pewriebontal](https://github.com/pewriebontal). Independently curated. |
| Format | C++20 library (`#include <typesafe/typesafe.h>`). |
| Requirements | C++20 toolchain; `TYPESAFE_API_KEY` (or builder-supplied key); nlohmann/json as used upstream. |
| License | [MIT](https://github.com/pewriebontal/typesafe-sdk-cpp/blob/d6db2fea4bdc2db167c1e11765cc751c3e6a7ed6/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live API calls not run on the review host. |

## When to use

Use to call **typed System One decisions from C++** without parsing free-form model text.

## How it works

Build a `SystemOneRequest` with typed `Choice`/`Score`/`Noul` questions; `client.systemOne(req)` returns structured answers.

## Get started

```sh
git clone https://github.com/pewriebontal/typesafe-sdk-cpp.git
cd typesafe-sdk-cpp
git checkout d6db2fea4bdc2db167c1e11765cc751c3e6a7ed6
# Follow README build/quickstart
```

## Examples and demos

- README C++ quickstart for ticket category/urgency.

## Limits and data handling

Request state JSON goes to TypeSafe. Bring your own HTTP/runtime integration as documented upstream.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit d6db2fe](https://github.com/pewriebontal/typesafe-sdk-cpp/tree/d6db2fea4bdc2db167c1e11765cc751c3e6a7ed6). AI-assisted README and LICENSE inspection; compile/live call not run.
