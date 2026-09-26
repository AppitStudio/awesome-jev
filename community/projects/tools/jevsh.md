# jevsh

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Bash wrapper: TypeSafe Jev scores shell command risk (LOW–CRITICAL) before you confirm run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/takeshiue/jevsh) |
| Maintainer | [takeshiue](https://github.com/takeshiue). Independently curated. |
| Format | Single bash script CLI. |
| Requirements | Linux bash 4.4+; curl; TypeSafe/Jev API key. |
| License | [MIT](https://github.com/takeshiue/jevsh/blob/82fab87f8b4a6684a0a845eb1b3645fb00793660/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use as an **interactive shell risk advisor** before running pasted commands. Jev advises; you still confirm.

## How it works

Sends the command line to TypeSafe Jev, prints risk level and confidence, and runs only after an explicit `y` (or `--check` for scripts).

## Get started

```sh
git clone https://github.com/takeshiue/jevsh.git
cd jevsh
git checkout 82fab87f8b4a6684a0a845eb1b3645fb00793660
# Copy jevsh onto PATH; export TypeSafe key; jevsh --check 'rm -rf /'
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 82fab87](https://github.com/takeshiue/jevsh/tree/82fab87f8b4a6684a0a845eb1b3645fb00793660). AI-assisted README and license inspection; install/live paths not executed.
