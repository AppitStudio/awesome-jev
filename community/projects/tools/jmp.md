# JMP

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local coding workspace (Joint Model Participation): TypeSafe Jev selects the next tool action; DeepSeek, OpenAI/Codex, or local Bonsai supplies open-ended arguments; OpenHands/MCP tools execute validated calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/morcoan/JMP) |
| Maintainer | [morcoan](https://github.com/morcoan). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python backend + React desktop (pywebview) and CLI; MIT. |
| Requirements | Python with locked `requirements*.txt` / OpenHands SDK pins; desktop UI; `TYPESAFE_API_KEY` or `JEV_KET` for Jev; a configured generation provider (DeepSeek, Codex, or local Bonsai). |
| License | [MIT](https://github.com/morcoan/JMP/blob/4abd336c5adf9e837bb6d636a20eb23644f36972/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and a small offline branding unit suite inspected. Full desktop install, OpenHands runtime, and live TypeSafe/generator calls were not run on the review host. |

## When to use

Use it when you want a single local agent loop that separates **decision** (Jev) from **argument generation** (text models) and real tool execution. Prefer thinner routers ([jev-codex-router](jev-codex-router.md), [Jev Model Router](jev-model-router.md)) when you only need model/effort routing inside an existing harness.

## How it works

[`jmp/models.py`](https://github.com/morcoan/JMP/blob/4abd336c5adf9e837bb6d636a20eb23644f36972/jmp/models.py) constructs `TypeSafeClient` and calls `system_one` with a Choice over candidate actions. When the tool schema already fixes arguments, code skips generation. The next turn uses observed tool results rather than a speculative plan. Desktop Settings manages provider keys (including TypeSafe/Jev).

## Get started

```sh
git clone https://github.com/morcoan/JMP.git
cd JMP
git checkout 4abd336c5adf9e837bb6d636a20eb23644f36972
python3 -m pytest test_branding.py -q
# Full desktop/CLI: follow upstream README (OpenHands SDK pins, provider keys).
# Live loops need TYPESAFE_API_KEY / JEV_KET plus a generation provider — incurs charges.
```

## Examples and demos

- Upstream README, `docs/BACKEND.md`, `RESEARCH.md`, and `SECURITY.md`.
- Review host: **`pytest test_branding.py`**: **5 passed**. Broader suites need the locked OpenHands/desktop dependency set.

## Limits and data handling

Prompts, histories, and tool I/O leave the machine toward TypeSafe and the chosen generator. Credential vault behavior is local; confirm upstream security notes. This is a research/desktop workspace, not a hosted SaaS. Model routing quality was not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 4abd336](https://github.com/morcoan/JMP/tree/4abd336c5adf9e837bb6d636a20eb23644f36972): MIT. AI-assisted source review of README, `jmp/models.py`, credentials paths, and LICENSE. Offline branding tests: **5 passed**. No live TypeSafe or generator calls.

Related: [jev-codex-router](jev-codex-router.md), [Jev Model Router](jev-model-router.md), [Distill](distill.md).
