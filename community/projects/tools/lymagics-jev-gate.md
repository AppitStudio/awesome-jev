# Jev Gate (lymagics)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action and CLI that fails a pipeline when code breaks a quality rule only a reader could check: YAML yes/no questions, code picks scopes, TypeSafe Jev answers with probabilities, thresholds decide pass/fail. Distinct from other catalog "jev-gate" listings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lymagics/jev-gate) |
| Maintainer | [lymagics](https://github.com/lymagics). Independently curated. |
| Format | Python · GitHub Action / CLI |
| Requirements | Python 3; `TYPESAFE_API_KEY`; a gates YAML file. |
| License | [MIT](https://github.com/lymagics/jev-gate/blob/c0fc93165c1996582562a799974f12da98f084d1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Encode review heuristics (secrets patterns, API misuse, docs drift) as Jev questions in CI.
- Mismatch: Probabilistic—tune thresholds; not a formal verifier.

## How it works

Scopes select file/diff slices; each gate question is sent to Jev; answers below threshold fail the job. Package: [`jev_gate/`](https://github.com/lymagics/jev-gate/tree/c0fc93165c1996582562a799974f12da98f084d1/jev_gate).

## Get started

From the upstream README (not run on the review host):

```sh
pip install .
jev-gate --help
# or wire the GitHub Action per upstream README
```

## Limits and data handling

Selected code/text is sent to TypeSafe; usage billed. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit c0fc93165c19](https://github.com/lymagics/jev-gate/tree/c0fc93165c1996582562a799974f12da98f084d1). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
