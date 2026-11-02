# PR wall (a repo's open PRs on one wall, each with Jev's typed read on the change and its tests)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Java web app that lists a repository's open pull requests and shows Jev's answers about each one: what kind of change it is, which area it touches, its size and blast radius, whether the changed tests run and assert the change, and whether tests were loosened. Answers are never combined into a score, and Right/Wrong buttons record your verdicts so you can measure Jev's calibration. Quarkus is the default repo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/House-elves/pr-wall) |
| Maintainer | [House-elves](https://github.com/House-elves). Independently curated. |
| Format | JBang Java app with a web UI (House Elves elf) |
| Requirements | Java with JBang, a GitHub login, `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/House-elves/pr-wall/blob/6563ddb52629a36d847105dededce3299a6fda14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Jev.java`](https://github.com/House-elves/pr-wall/blob/6563ddb52629a36d847105dededce3299a6fda14/Jev.java) at the pinned commit. |

## When to use

- Triage a busy repo's open PRs with typed, inspectable judgments.
- Mismatch: the PR title and body are not sent, so the kind is judged from code only.

## How it works

`Jev.java` posts one System One request per PR to `https://api.typesafe.ai/v1/systemone` with noul and choice questions; `Config.java` reads the key and model (`jev-latest` by default). Facts like test-file deletions are read from paths and given to Jev as input. Integration evidence: [`Jev.java`](https://github.com/House-elves/pr-wall/blob/6563ddb52629a36d847105dededce3299a6fda14/Jev.java).

## Get started

From the upstream README (not run on the review host):

```sh
mkdir -p ~/.config/pr-wall && printf 'GITHUB_USER=your-login\nTYPESAFE_API_KEY=...\n' > ~/.config/pr-wall/config
jbang PrWall.java   # shows what it would send; sends nothing
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- House Elves organization: [github.com/House-elves](https://github.com/House-elves)

## Limits and data handling

PR diffs from the target repo are sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 6563ddb52629](https://github.com/House-elves/pr-wall/tree/6563ddb52629a36d847105dededce3299a6fda14). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
