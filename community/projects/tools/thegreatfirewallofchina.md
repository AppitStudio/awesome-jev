# thegreatfirewallofchina (sandbox and monitor for agents on your own compute, with a Jev trace check)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Sandbox and egress monitor for an agent running on your machine: a destination policy always denies metadata services and blocks published object-storage and cloud-API hosts, and one Jev System One call over the whole trace scores phone-home, reasoning mismatch and similar risks, after which code picks allow, review or block; Jev cannot overrule a static block.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AnthonyHerman/thegreatfirewallofchina) |
| Maintainer | [AnthonyHerman](https://github.com/AnthonyHerman). Independently curated. |
| Format | Python package with proxy and CLI |
| Requirements | Python; a Jev API key (or `--offline` without Jev). |
| License | [MIT](https://github.com/AnthonyHerman/thegreatfirewallofchina/blob/719ce5b06b7a33214cbf6e3548434c1f170f9d8e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gfw/judge.py`](https://github.com/AnthonyHerman/thegreatfirewallofchina/blob/719ce5b06b7a33214cbf6e3548434c1f170f9d8e/gfw/judge.py) at the pinned commit. |

## When to use

- Run an open-weight or third-party agent locally with egress controls.
- Score an agent trace before treating it as safe.
- Mismatch: the name is a joke; it does not block the .cn namespace or claim any model is a backdoor.

## How it works

`gfw/judge.py` posts the agent trace with risk questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); code combines the probabilities with the static policy. Integration evidence: [`gfw/judge.py`](https://github.com/AnthonyHerman/thegreatfirewallofchina/blob/719ce5b06b7a33214cbf6e3548434c1f170f9d8e/gfw/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AnthonyHerman/thegreatfirewallofchina && cd thegreatfirewallofchina
python -m pip install -e ".[dev]"
export JEV_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Threat model: [github.com/AnthonyHerman/thegreatfirewallofchina/blob/main/docs/threat-model.md](https://github.com/AnthonyHerman/thegreatfirewallofchina/blob/main/docs/threat-model.md)
- README: [github.com/AnthonyHerman/thegreatfirewallofchina#readme](https://github.com/AnthonyHerman/thegreatfirewallofchina#readme)

## Limits and data handling

Agent traces go to TypeSafe unless run with `--offline`. The recorded fixture results are an illustration, not a benchmark.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 719ce5b06b7a](https://github.com/AnthonyHerman/thegreatfirewallofchina/tree/719ce5b06b7a33214cbf6e3548434c1f170f9d8e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
