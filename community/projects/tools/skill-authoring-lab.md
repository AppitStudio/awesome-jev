# Skill Authoring Lab

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Short loop for authoring a Quarkus MCP skill: edit, run one JUnit test, read a Jev-backed score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sebastienblanc/skill-authoring-lab) |
| Maintainer | [sebastienblanc](https://github.com/sebastienblanc). Independently curated. |
| Format | Quarkus / JUnit skill lab |
| Requirements | Java/Quarkus; TypeSafe API key for JevJudge. |
| License | Source available — no LICENSE file on the reviewed tip; do not claim OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. Discovered via X ([post](https://x.com/sebi2706/status/2109907849195164056)). |
| Jev evidence | [`src/test/java/org/sebi/skilllab/JevJudge.java`](https://github.com/sebastienblanc/skill-authoring-lab/blob/c8b5497b4e138578904599294aaff6ee0c6dd1e1/src/test/java/org/sebi/skilllab/JevJudge.java) at the pinned commit. |

## When to use

- Use when you need: Short loop for authoring a Quarkus MCP skill: edit, run one JUnit test, read a J…
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/test/java/org/sebi/skilllab/JevJudge.java`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/test/java/org/sebi/skilllab/JevJudge.java.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit c8b5497b4e13](https://github.com/sebastienblanc/skill-authoring-lab/tree/c8b5497b4e138578904599294aaff6ee0c6dd1e1). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
