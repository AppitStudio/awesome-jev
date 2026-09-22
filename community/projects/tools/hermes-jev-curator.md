# hermes-jev-curator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin that uses TypeSafe Jev for typed skill-relationship judgments and safe archive/guard plans for the background skill curator (experimental 0.1.0).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anpicasso/hermes-jev-curator) |
| Maintainer | [anpicasso](https://github.com/anpicasso). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Hermes plugin under `plugin/` (Python); experimental release **0.1.0**. |
| Requirements | Hermes Agent with plugins enabled; TypeSafe or OpenRouter credentials for live Jev (`TYPESAFE_API_KEY` / OpenRouter). Offline unit suite runs without live keys. |
| License | [MIT](https://github.com/anpicasso/hermes-jev-curator/blob/4e8626c7d394a9cbef8594993ec4b208ffb3395f/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline pytest mostly green on the review host (see Review); live TypeSafe and full Hermes `plugins doctor` against a real Hermes install were not run here. Distinct from [Hermes Jev Skills](hermes-jev-skills.md). |

## When to use

Use it when you want **typed Jev relation evidence** before Hermes Curator merges/absorbs/archives skills, with dry observe/guard modes and explicit apply gates. Prefer [Hermes Jev Skills](hermes-jev-skills.md) for general routing/memory/compaction skills rather than curator governance.

## How it works

[`plugin/transport.py`](https://github.com/anpicasso/hermes-jev-curator/blob/4e8626c7d394a9cbef8594993ec4b208ffb3395f/plugin/transport.py) routes to `https://api.typesafe.ai/v1/systemone` or OpenRouter Decisions. The plugin registers `jev_skill_relations`, curator prompt injection, lifecycle debounce refresh, and optional pre-tool guards. Apply mutations require explicit terminal `hermes jev-curator run --apply` with `mode=apply`.

## Get started

```sh
git clone https://github.com/anpicasso/hermes-jev-curator.git
cd hermes-jev-curator
git checkout 4e8626c7d394a9cbef8594993ec4b208ffb3395f
python3 -m pytest plugin/tests -q
# Install as a Hermes plugin per upstream README; then:
# hermes plugins validate plugin
# hermes jev-curator doctor
```

Live scans send skill content to TypeSafe/OpenRouter when egress is allowed and may incur charges. This listing did not run live Jev or Hermes doctor against a full Hermes install.

## Examples and demos

- Offline on the review host: `python3 -m pytest plugin/tests -q` → **304 passed**, 5 failed (missing `hermes_cli` import on bare host), 1 skipped — failures are environment/Hermes-install dependent, not catalog packaging.
- Upstream README mode matrix (`observe` / `guard` / `apply`) and synthetic corpus notes.

## Limits and data handling

Skill text can leave the host when `allow_content_egress` and mode are enabled. Automatic runs never apply/archive in observe; apply is terminal-gated. Experimental 0.1.0; debounce is a workaround over Hermes lifecycle events.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 4e8626c](https://github.com/anpicasso/hermes-jev-curator/tree/4e8626c7d394a9cbef8594993ec4b208ffb3395f): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `plugin/transport.py`, `plugin/__init__.py`. Offline pytest 304 passed / 5 failed (`hermes_cli` absent). No live TypeSafe on the review host.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [ask-jev-skill](ask-jev-skill.md).
