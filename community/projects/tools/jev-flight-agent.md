# jev-flight-agent

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser-use demo agent that finds flights from a natural-language goal: TypeSafe Jev chooses each DOM operation/target from an indexed element table; a small text model only fills TYPE_TEXT.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kallurayaankit/jev-flight-agent) |
| Maintainer | [kallurayaankit](https://github.com/kallurayaankit). Independently curated. |
| Format | Python package (`jev_ultrafast` folder) with examples/tests. |
| Requirements | Python 3.12; Chrome 136+; TYPESAFE_API_KEY; OpenRouter (or similar) text-model key. |
| License | [MIT](https://github.com/kallurayaankit/jev-flight-agent/blob/6205ffa13fd043732ff2c1536b5870a933e21a26/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live flight searches not run. Upstream timing/cost figures not re-measured. |

## When to use

Use as a **teaching** Jev browser loop on flight sites. Prefer [Jev Ultrafast](jev-ultrafast.md) / [jev-ra](jev-ra.md) for fuller general browser agents.

## How it works

Observes interactive DOM as an indexed table (no screenshots to Jev). Jev returns structured action choices; code drives Playwright via CDP. Text generation is delegated to a small LLM only when typing is required.

## Get started

```sh
git clone https://github.com/kallurayaankit/jev-flight-agent.git
cd jev-flight-agent
git checkout 6205ffa13fd043732ff2c1536b5870a933e21a26
uv sync --python 3.12
# copy .env.example; launch Chrome with remote debugging; run examples per README
```

## Examples and demos

- `examples/` and `tests/` (not re-run here).
- README documents example Zurich→London style tasks.

## Limits and data handling

Sends page state and goals to TypeSafe and the text provider. Booking/payment flows can have real-world side effects—review before live use.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 6205ffa](https://github.com/kallurayaankit/jev-flight-agent/tree/6205ffa13fd043732ff2c1536b5870a933e21a26). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [Jev Ultrafast](jev-ultrafast.md), [jev-ra](jev-ra.md), [legostin-jev-mcp](legostin-jev-mcp.md).
