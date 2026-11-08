# kimi-advisor (second-opinion advisor and stuck-loop guard for Kimi Code, screened by TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Kimi Code CLI/Web plugin (MCP server + hooks + skill) that brings in an advisor model when the main model is stuck or about to declare done, with a fast TypeSafe Jev pre-screen that skips low-stakes calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kim1232aa/kimi-advisor) |
| Maintainer | [kim1232aa](https://github.com/kim1232aa). Independently curated. |
| Format | Kimi Code plugin (Python MCP server + hooks; no SPDX license file on the reviewed commit) |
| Requirements | Kimi Code CLI or Web, Python 3, the `jev-use` CLI, and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`advisor_core.py`](https://github.com/kim1232aa/kimi-advisor/blob/6aa8454adef109b22473bb636135c54583874fc7/advisor_core.py) at the pinned commit. |

## When to use

- Get a second opinion only when a coding agent loops or claims completion.
- Cut advisor spend with a cheap Jev screen first.
- Mismatch: Kimi Code only; README in Chinese; no OSI license on the reviewed commit.

## How it works

`advisor_core.py` `jev_judge()` resolves `TYPESAFE_API_KEY` and pipes typed questions to `jev-use judge`; verdicts above a configured confidence skip the advisor call, and repeated failures put Jev in cooldown. Integration evidence: [`advisor_core.py`](https://github.com/kim1232aa/kimi-advisor/blob/6aa8454adef109b22473bb636135c54583874fc7/advisor_core.py).

## Get started

Clone, install the MCP server, hooks and skill into Kimi Code per README, and set the advisor model in config.

```sh
git clone https://github.com/kim1232aa/kimi-advisor.git && cd kimi-advisor
export TYPESAFE_API_KEY=...
python3 advisor_cli.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kim1232aa/kimi-advisor/blob/6aa8454adef109b22473bb636135c54583874fc7/README.md](https://github.com/kim1232aa/kimi-advisor/blob/6aa8454adef109b22473bb636135c54583874fc7/README.md)

## Limits and data handling

Session digests (secrets redacted by default) are sent to TypeSafe via jev-use and, when escalated, to your configured advisor model.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 6aa8454adef1](https://github.com/kim1232aa/kimi-advisor/tree/6aa8454adef109b22473bb636135c54583874fc7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
