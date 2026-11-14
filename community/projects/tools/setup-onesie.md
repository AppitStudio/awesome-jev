# setup-onesie (GitHub Action that installs the onesie CLI and gates a workflow step on a Jev yes/no, label or rating)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action for the listed onesie CLI: it installs a checksum- and provenance-verified onesie release on any GitHub-hosted runner, and in run mode asks one question file (your own or the bundled `moderation`, `personal-data`, `prompt-injection` and `shell-safety` sets) about a text, then passes, fails or warns on the answer and exposes `result`, `exit-code` and `answer` outputs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frodi-karlsson/setup-onesie) |
| Maintainer | [frodi-karlsson](https://github.com/frodi-karlsson). Independently curated. |
| Format | GitHub Action (composite, shell; MIT) |
| Requirements | A GitHub Actions workflow and a `TYPESAFE_API_KEY` secret. |
| License | [MIT](https://github.com/frodi-karlsson/setup-onesie/blob/0e760583401e3a621455889ed701da69e5b2161a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run.sh`](https://github.com/frodi-karlsson/setup-onesie/blob/0e760583401e3a621455889ed701da69e5b2161a/run.sh) at the pinned commit. |

## When to use

- Fail a workflow step on hostile comments, leaked personal data or risky shell in a PR.
- Mismatch: workflows on forks without secrets; run mode needs the TypeSafe key.

## How it works

`run.sh` validates the run-mode inputs, passes `state` through the environment (never a shell string) and calls `onesie`, which asks TypeSafe's Jev; `install.sh` verifies the release checksum and build provenance before installing. Integration evidence: [`run.sh`](https://github.com/frodi-karlsson/setup-onesie/blob/0e760583401e3a621455889ed701da69e5b2161a/run.sh).

## Get started

Add the step with your key as a secret.

```sh
- uses: frodi-karlsson/setup-onesie@v1
  env:
    TYPESAFE_API_KEY: ${{ secrets.TYPESAFE_API_KEY }}
  with:
    file: moderation
    state: ${{ github.event.comment.body }}
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/frodi-karlsson/setup-onesie/blob/0e760583401e3a621455889ed701da69e5b2161a/README.md](https://github.com/frodi-karlsson/setup-onesie/blob/0e760583401e3a621455889ed701da69e5b2161a/README.md)
- onesie CLI: [github.com/frodi-karlsson/onesie](https://github.com/frodi-karlsson/onesie)

## Limits and data handling

The `state` text is sent to TypeSafe on your key. Calibrate cuts on your own examples before gating merges on them.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 0e760583401e](https://github.com/frodi-karlsson/setup-onesie/tree/0e760583401e3a621455889ed701da69e5b2161a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
