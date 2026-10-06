# slophound

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Deterministic linter for prose written by language models (regex, grammar and statistics rules in TOML) where Jev resolves ambiguous findings in context — e.g. clearing a three-noun cluster that is an established term, or a semicolon splice that reads fine — and runs automatically once a TypeSafe key is configured.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JosXa/slophound) |
| Maintainer | [JosXa](https://github.com/JosXa). Independently curated. |
| Format | CLI (`uvx` from Git or checkout script), Python API, agent skill |
| Requirements | `uv` (spaCy English model downloads on first run). Jev is optional: `TYPESAFE_API_KEY` or `slophound auth set-key`. |
| License | [MIT](https://github.com/JosXa/slophound/blob/cb4c229cde13c2a54ccbb0160ec44c46344477ba/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Gate docs or agent-written text in CI on deterministic rules while letting a typed model clear context-dependent false positives.
- Give a coding agent a prose check it can run on its own output.
- Mismatch: with Jev enabled, the report and exit code can differ between runs for Jev-checked rules; disable the key for strict reproducibility.

## How it works

The deterministic core produces the same findings for the same input. For eligible rules Slophound sends the matched text, the selected words and the containing sentence(s) — at most six findings per paragraph, code and URLs masked — to Jev; for example `noun.cluster-three` is cleared when Jev gives at least 0.70 that the expression is conventional in its field. With no key it runs fully deterministic with no Jev requests.

## Get started

Run from a checkout (or `uvx` from Git per README), and store a key to enable Jev (live calls on eligible findings):

```sh
git clone https://github.com/JosXa/slophound.git && cd slophound
./slophound README.md docs/*.md
./slophound auth set-key          # stores TYPESAFE_API_KEY in the user config
echo "One sentence." | ./slophound
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Jev for contextual judgment* (noun clusters, semicolon splices).
- `./slophound test` rule and corpus tests; `--formal` output for CI logs.

## Limits and data handling

Eligible sentences are sent to TypeSafe. The key is stored as plaintext in the user config file (owner-only permissions). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit cb4c229cde13](https://github.com/JosXa/slophound/tree/cb4c229cde13c2a54ccbb0160ec44c46344477ba). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
