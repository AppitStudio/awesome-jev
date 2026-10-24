# judgelint (lint code against plain-English conventions with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Linter that checks code against conventions you write as bullets in a README: a decision model such as Jev judges whether each file breaks each rule, and judgelint reports violations with line numbers, confidence and an exit code.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jpcamara/judgelint) |
| Maintainer | [jpcamara](https://github.com/jpcamara). Independently curated. |
| Format | Ruby CLI (Homebrew, gem, binaries) |
| Requirements | macOS or Linux; a TypeSafe key (or OpenRouter / Cloudflare provider). |
| License | [MIT](https://github.com/jpcamara/judgelint/blob/d7e478ef67f798b98f78d03b1386cadfbd1b45c0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/judgelint/providers.rb`](https://github.com/jpcamara/judgelint/blob/d7e478ef67f798b98f78d03b1386cadfbd1b45c0/lib/judgelint/providers.rb) at the pinned commit. |

## When to use

- Enforce team conventions that regex linters cannot express.
- Check only changed files in CI with --base main.
- Mismatch: answers are probabilistic; uncertain results are reported as such.

## How it works

`providers.rb` defines the TypeSafe provider (`https://api.typesafe.ai`, `jev-latest`) and an OpenRouter route (`typesafe/jev-1.13`); each file-rule pair becomes one question. Integration evidence: [`lib/judgelint/providers.rb`](https://github.com/jpcamara/judgelint/blob/d7e478ef67f798b98f78d03b1386cadfbd1b45c0/lib/judgelint/providers.rb).

## Get started

From the upstream README (not run on the review host):

```sh
brew install jpcamara/tap/judgelint   # or: gem install judgelint
judgelint init
export TYPESAFE_API_KEY=...
judgelint test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- RubyGems: [rubygems.org/gems/judgelint](https://rubygems.org/gems/judgelint)
- README: [github.com/jpcamara/judgelint#readme](https://github.com/jpcamara/judgelint#readme)

## Limits and data handling

File contents are sent to the configured provider.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit d7e478ef67f7](https://github.com/jpcamara/judgelint/tree/d7e478ef67f798b98f78d03b1386cadfbd1b45c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
