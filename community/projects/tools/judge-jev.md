# judge-jev (agent-plugin harness that judges prose and code against requirements with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Installable agent plugin and skill (`sc-judge-jev`) that evaluates skills, prompts and task templates against REQ, NFR or ADR records using TypeSafe Jev typed questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/randlee/judge-jev) |
| Maintainer | [randlee](https://github.com/randlee). Independently curated. |
| Format | Agent plugin + Python skill (MIT) |
| Requirements | Python 3, a coding agent that supports agent plugins/skills, and a TypeSafe API key. |
| License | [MIT](https://github.com/randlee/judge-jev/blob/31bb15e67df16aa0321d034fd73bcfe96a199757/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/sc-judge-jev/install/templates/skills/judge-jev/scripts/jev_judge.py.j2`](https://github.com/randlee/judge-jev/blob/31bb15e67df16aa0321d034fd73bcfe96a199757/plugins/sc-judge-jev/install/templates/skills/judge-jev/scripts/jev_judge.py.j2) at the pinned commit. |

## When to use

- Check agent prompts and skills against written requirements.
- Add a fast typed review gate to docs workflows.
- Mismatch: v0.1 with draft requirements.

## How it works

The rendered `jev_judge.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, using one question set per record kind (`--req`, `--adr`, `--nfr`). Integration evidence: [`plugins/sc-judge-jev/install/templates/skills/judge-jev/scripts/jev_judge.py.j2`](https://github.com/randlee/judge-jev/blob/31bb15e67df16aa0321d034fd73bcfe96a199757/plugins/sc-judge-jev/install/templates/skills/judge-jev/scripts/jev_judge.py.j2).

## Get started

Run the installer to render the skill into a repository, set the key, and call judge-jev on a record.

```sh
git clone https://github.com/randlee/judge-jev.git && cd judge-jev
export TYPESAFE_API_KEY=...
python plugins/sc-judge-jev/install.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/randlee/judge-jev/blob/31bb15e67df16aa0321d034fd73bcfe96a199757/README.md](https://github.com/randlee/judge-jev/blob/31bb15e67df16aa0321d034fd73bcfe96a199757/README.md)

## Limits and data handling

Prose and requirement text are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 31bb15e67df1](https://github.com/randlee/judge-jev/tree/31bb15e67df16aa0321d034fd73bcfe96a199757). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
