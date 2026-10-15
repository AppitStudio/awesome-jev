# Frame Engineering for Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill and scripts for designing and evaluating Jev decision frames: evidence in `state`, atomic questions, answer boundaries and application policy, with ablation, sweep and token-probe scripts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nanagb/jev-frame-engineering) |
| Maintainer | [nanagb](https://github.com/nanagb). Independently curated. |
| Format | Agent skill (Claude Code plugin / Codex skill) with Python scripts |
| Requirements | Claude Code or Codex; Python and a TypeSafe key for the evaluation scripts. |
| License | [MIT](https://github.com/nanagb/jev-frame-engineering/blob/96a2c6fae0ee03c50ec6e5c6746050ea980b1772/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/jev-frame-engineering/scripts/jevlib.py`](https://github.com/nanagb/jev-frame-engineering/blob/96a2c6fae0ee03c50ec6e5c6746050ea980b1772/skills/jev-frame-engineering/scripts/jevlib.py) at the pinned commit. |

## When to use

- Review an existing Jev integration for ambiguous questions, overlapping options or missing no-match outcomes.
- Run controlled ablations to see which frame change actually helps on labelled examples.
- Mismatch: guidance and evaluation tooling for existing integrations, not a library.

## How it works

The skill walks an agent through frame design (separating no-match, low confidence and failure), and its scripts (`eval.py`, `ablate.py`, `sweep_batch.py`, `token_probe.py`) call Jev through `jevlib.py` to measure frame variants on your labelled cases. Integration evidence: [`skills/jev-frame-engineering/scripts/jevlib.py`](https://github.com/nanagb/jev-frame-engineering/blob/96a2c6fae0ee03c50ec6e5c6746050ea980b1772/skills/jev-frame-engineering/scripts/jevlib.py).

## Get started

From the upstream README (not run on the review host):

```sh
# Claude Code
/plugin marketplace add nanagb/jev-frame-engineering
/plugin install jev-frame-engineering@blue-terra
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Practice write-up: the README section 'Understanding Frame Engineering'.

## Limits and data handling

The skill sends nothing; evaluation scripts send your examples to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 96a2c6fae0ee](https://github.com/nanagb/jev-frame-engineering/tree/96a2c6fae0ee03c50ec6e5c6746050ea980b1772). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
