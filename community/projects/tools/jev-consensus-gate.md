# Jev Consensus Gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent action gate that asks Jev about each proposed action three independent ways (safety, legitimacy, adversarial) and only allows it when all three agree; any block wins and any escalation goes to a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kallurayaankit/jev-consensus-gate) |
| Maintainer | [kallurayaankit](https://github.com/kallurayaankit). Independently curated. |
| Format | Python library and demo (uv project, `.jev` question file) |
| Requirements | Python 3.12, uv, a TypeSafe API key. |
| License | [MIT](https://github.com/kallurayaankit/jev-consensus-gate/blob/e7360caff37155ad84d17f2b847fd96ef9b0d13d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/uhnkitcalorieya/status/2111278482458366243)). |
| Jev evidence | [`perspectives.jev`](https://github.com/kallurayaankit/jev-consensus-gate/blob/e7360caff37155ad84d17f2b847fd96ef9b0d13d/perspectives.jev) at the pinned commit. |

## When to use

- Put a stricter check in front of shell or file actions an agent proposes, where one framing of the question could miss a risk.
- Study an asymmetric consensus rule: a single confident veto blocks, a single allow is not enough.
- Mismatch: three calls per action triple input cost and can over-block harmless actions such as reading a log file.

## How it works

Each proposed action is described as text and sent to Jev in three separate calls, defined in `perspectives.jev` with the `jevlang` package and the TypeSafe SDK. `consensus.py` turns each answer into allow, human or block from its probabilities and severity, then requires all three to allow; any block blocks and any escalation routes to a human. Integration evidence: [`perspectives.jev`](https://github.com/kallurayaankit/jev-consensus-gate/blob/e7360caff37155ad84d17f2b847fd96ef9b0d13d/perspectives.jev).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
cp .env.example .env   # add your TypeSafe key
uv run python demo.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample output for six actions in the README (allow `read_file`, block `curl ... | bash`, escalate `rm -rf /var/log/*`).
- Author's X thread: [x.com/uhnkitcalorieya/status/2111278482458366243](https://x.com/uhnkitcalorieya/status/2111278482458366243)

## Limits and data handling

Action descriptions go to TypeSafe on your key, three calls per action. It is a demo-sized library, not a sandbox; the code still has to enforce the verdict.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit e7360caff371](https://github.com/kallurayaankit/jev-consensus-gate/tree/e7360caff37155ad84d17f2b847fd96ef9b0d13d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
