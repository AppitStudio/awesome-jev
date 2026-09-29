# DuoMind

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenAI-compatible dual-system server: a small local LLM generates while TypeSafe Jev handles System One decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/j1s4nn/duomind) |
| Maintainer | [j1s4nn](https://github.com/j1s4nn). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python OpenAI-compatible local server (llama.cpp + TypeSafe Jev). |
| Requirements | Local GGUF / llama.cpp setup per upstream; TypeSafe API key for Jev classifications. Prompts leave the machine for Jev. |
| License | [MIT](https://github.com/j1s4nn/duomind/blob/acebeb882d1e2668d7d4103755a48f106105d981/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when you want a private small coding model boosted by TypeSafe Jev decisions. Prefer plain Ollama/llama.cpp when you do not want off-box System One calls.

## How it works

System 2 stays local via llama.cpp; System 1 calls TypeSafe Jev for typed decisions that steer generation. Aimed at Kilo Code / Cline-style coding assistants. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/j1s4nn/duomind.git
cd duomind
git checkout acebeb882d1e2668d7d4103755a48f106105d981
# follow upstream README for local model + TYPESAFE/Jev key setup
```

Pin revision `acebeb882d1e2668d7d4103755a48f106105d981` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Jev path sends prompts/context to TypeSafe. Live local+Jev runs not executed on the review host. Unofficial; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit acebeb8](https://github.com/j1s4nn/duomind/tree/acebeb882d1e2668d7d4103755a48f106105d981). AI-assisted README and LICENSE inspection; install/live paths not executed.
