# jev-lgtm

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that sends a pull request diff to TypeSafe Jev and returns one of two verdicts: approve with LGTM, or leave Review Advised for a human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bobbydeveaux/jev-lgtm) |
| Maintainer | [bobbydeveaux](https://github.com/bobbydeveaux). Independently curated. |
| Format | TypeScript · GitHub Action |
| Requirements | GitHub Actions; a TypeSafe API key as a repository secret (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/bobbydeveaux/jev-lgtm/blob/58c1a644d0b468720687e08383ed1f18b78becb6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Fast first-pass review on small PRs where a typed yes/no is enough.
- Mismatch: Not a substitute for security review or tests; Jev only sees the diff text you configure.

## How it works

The action loads the PR diff, asks Jev typed questions about whether human review is needed, and either approves or comments. Jev integration: [`src/jev.ts`](https://github.com/bobbydeveaux/jev-lgtm/blob/58c1a644d0b468720687e08383ed1f18b78becb6/src/jev.ts). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
Uses: bobbydeveaux/jev-lgtm@main
with:
  typesafe-api-key: ${{ secrets.TYPESAFE_API_KEY }}
```

## Limits and data handling

PR diff text is sent to api.typesafe.ai and billed by TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 58c1a644d0b4](https://github.com/bobbydeveaux/jev-lgtm/tree/58c1a644d0b468720687e08383ed1f18b78becb6). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
