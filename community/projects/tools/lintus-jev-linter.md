# Lintus (linter with plain-language rules judged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Linter whose rules are questions in a YAML file: for each file a rule applies to, Lintus asks Jev a true/false noul question and reports an offense with its probability, on the whole tree, changed files or staged files.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/virolea/lintus) |
| Maintainer | [virolea](https://github.com/virolea). Independently curated. |
| Format | Single-binary CLI and GitHub Action (Rust, MIT) |
| Requirements | The `lintus` binary (macOS, Linux, Windows) and a Jev key via `lintus auth login` or `JEV_API_KEY`. |
| License | [MIT](https://github.com/virolea/lintus/blob/ab509cb0feed6cb14ffe70154fda85fa130cb7a1/LICENSE.txt) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/jev/src/client.rs`](https://github.com/virolea/lintus/blob/ab509cb0feed6cb14ffe70154fda85fa130cb7a1/crates/jev/src/client.rs) at the pinned commit. |

## When to use

- Enforce architecture or style rules that are hard to express as regex or AST checks.
- Run plain-language checks in CI or a pre-commit hook.
- Mismatch: each checked file is a paid Jev call; judgments are probabilistic.

## How it works

`crates/jev/src/client.rs` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; `lintus --list` shows which files each rule would ask about without calling the API, and files over `max_file_size` are skipped. Integration evidence: [`crates/jev/src/client.rs`](https://github.com/virolea/lintus/blob/ab509cb0feed6cb14ffe70154fda85fa130cb7a1/crates/jev/src/client.rs).

## Get started

Install the binary, save your key, write a starter config and lint.

```sh
curl -fsSL https://github.com/virolea/lintus/releases/latest/download/install.sh | sh
lintus auth login && lintus init && lintus
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/virolea/lintus/blob/ab509cb0feed6cb14ffe70154fda85fa130cb7a1/README.md](https://github.com/virolea/lintus/blob/ab509cb0feed6cb14ffe70154fda85fa130cb7a1/README.md)

## Limits and data handling

The contents of every file a rule applies to go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit ab509cb0feed](https://github.com/virolea/lintus/tree/ab509cb0feed6cb14ffe70154fda85fa130cb7a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
