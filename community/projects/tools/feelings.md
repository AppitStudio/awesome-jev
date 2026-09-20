# feelings

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

BAML library that adds typed `.feels()` / `.how()` / `.matches<T>()` / `.judge<T>()` / `.fill<T>()` methods on any value, powered by TypeSafe Jev (plus a separate LLM for `.ask()`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BoundaryML/feelings) |
| Maintainer | [BoundaryML](https://github.com/BoundaryML). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | BAML sources under `baml_src/` (nightly toolchain); demo scripts and offline `baml test`. |
| Requirements | BAML nightly (`baml toolchain use nightly`); `TYPESAFE_API_KEY` for Jev; `ANTHROPIC_API_KEY` only for `.ask()` text generation. |
| License | Unspecified at the reviewed commit: no project license file was found. Public source access does not establish an open-source license or reuse permission. |
| Disclosure | AI-assisted catalog review; no affiliation with BoundaryML for this listing. Listing is not an endorsement. Source inspected; live Jev/`baml run` were not executed. |

## When to use

Use it when you want the “AI if statement” as a real typed method inside BAML rather than ad-hoc HTTP clients. Prefer [Advocaat](advocaat.md) for a TypeScript `ask` client over structured data, or the official TypeSafe SDKs when you are not on BAML.

## How it works

[`baml_src/vibes.baml`](https://github.com/BoundaryML/feelings/blob/e0f07b4ad1e01b4cd1326c8bc28e6e68041602d7/baml_src/vibes.baml) defines a blanket `Vibes` interface: values serialize to Jev `state`; return types shape the questions. A `typesafeai.Client` with model `jev-latest` backs `Feels` (Noul→bool at 0.5), `How` (raw probability), Choice helpers for enums/literal unions, and class `fill`. `.ask()` uses a generative model, not Jev. Offline tests in `vibes_test.baml` assert request URL `https://api.typesafe.ai/v1/systemone` and question shapes without sending.

## Get started

```sh
git clone https://github.com/BoundaryML/feelings.git
cd feelings
git checkout e0f07b4ad1e01b4cd1326c8bc28e6e68041602d7
baml toolchain use nightly && baml toolchain update
cp .env.example .env   # TYPESAFE_API_KEY (+ ANTHROPIC_API_KEY for .ask)
baml test              # offline — inspects Jev requests, no key needed
```

Review licensing before reuse. Live `baml run` calls send state text to TypeSafe and can incur charges. This listing did not install the BAML toolchain or call live Jev.

## Examples and demos

- README inbox/urgent/demo scripts and `git log | baml run grep_with_vibes`.
- Offline `baml test` cases in `baml_src/vibes_test.baml`.

## Limits and data handling

Judged values leave the host for TypeSafe as serialized state. `.ask()` uses a separate generative provider. Missing license file means reuse terms are unclear. Upstream demo narratives were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit e0f07b4](https://github.com/BoundaryML/feelings/tree/e0f07b4ad1e01b4cd1326c8bc28e6e68041602d7). AI-assisted source review of README, `baml_src/vibes.baml`, `vibes_test.baml`, and license absence. No live TypeSafe or Anthropic calls.

Related: [Advocaat](advocaat.md), [typesafe-cli](typesafe-cli.md).
