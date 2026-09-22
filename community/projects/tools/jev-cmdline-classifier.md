# jev-cmdline-classifier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable agent skill plus stdlib Python/JS reference that classifies shell commands with TypeSafe Jev Choice into `allow` / `prompt` / `forbidden` for approval wrappers—Jev is advisory; sandbox/execpolicy remain the security boundary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/liodali/jev-cmdline-classifier) |
| Maintainer | [liodali](https://github.com/liodali). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent Skill (`skills/jev-command-classifier`) + dependency-free Python 3.9+ / Node 18+ classifiers (`jev-command-classifier` **0.1.0** JS package in-tree). |
| Requirements | `TYPESAFE_API_KEY` for live classification (direct TypeSafe System One by default). `--self-test` / `--offline` need no key. Install helper copies into Codex, OpenCode, Pi, and Command Code skill dirs. |
| License | [MIT](https://github.com/liodali/jev-cmdline-classifier/blob/f47aabf5e902c4d00b30184721f61e4c7eeae434/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline: `classify_command.py --self-test` ok; JS `node --test` **47 passed**. Live TypeSafe classification not run. Approval-wrapper integration is documented, not implemented in-repo. |

## When to use

Use it when coding agents need a **shared Jev command-risk vocabulary** across Codex/OpenCode/Pi/Command Code skills. Prefer hard execpolicy / sandbox rules as the real boundary; treat Jev output as advisory. Distinct from stop-nudge mods ([cmd-mod-jev-nudge](cmd-mod-jev-nudge.md)) and skill routers.

## How it works

[`client.py`](https://github.com/liodali/jev-cmdline-classifier/blob/f47aabf5e902c4d00b30184721f61e4c7eeae434/skills/jev-command-classifier/scripts/jev_classifier/client.py) POSTs Choice questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`). A fail-closed local layer applies hard-deny rules and redacts secrets before any state is sent; `allow` never widens the sandbox.

## Get started

```sh
git clone https://github.com/liodali/jev-cmdline-classifier.git
cd jev-cmdline-classifier
git checkout f47aabf5e902c4d00b30184721f61e4c7eeae434
python3 skills/jev-command-classifier/scripts/classify_command.py --self-test
cd skills/jev-command-classifier/scripts/jev_classifier_js && npm test
# Live (charges): export TYPESAFE_API_KEY=...; classify a command via the Python or JS CLI
./install.sh   # optional: copy skill into detected harnesses
```

## Examples and demos

- Shared fixtures in `scripts/fixtures/cases.json`.
- Offline on the review host: Python `--self-test` ok; JS tests **47 passed**.

## Limits and data handling

Command text (after local redaction) leaves the host on live classification. Jev does not replace Codex sandboxing or execpolicy. No live TypeSafe spend on this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit f47aabf](https://github.com/liodali/jev-cmdline-classifier/tree/f47aabf5e902c4d00b30184721f61e4c7eeae434): MIT. AI-assisted review of README, LICENSE, `client.py`, skill layout. Offline self-test + JS **47 passed**; live not run.

Related: [hookgate](hookgate.md), [cmd-mod-jev-nudge](cmd-mod-jev-nudge.md), [clear-head](clear-head.md).
