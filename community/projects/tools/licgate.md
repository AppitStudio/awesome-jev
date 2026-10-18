# licgate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Dependency license gate (TUI and CI CLI) for npm, Python, Go, Rust, PHP, and SBOMs that flags incompatibilities with your intended license; `--jev` sends license texts the built-in detector cannot place to Jev, keeping low-confidence answers as REVIEW.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maromocooo/licgate) |
| Maintainer | [maromocooo](https://github.com/maromocooo). Independently curated. |
| Format | Go CLI/TUI |
| Requirements | Go toolchain or release binary; optional `TYPESAFE_API_KEY` (or OpenRouter) for `--jev`. |
| License | [Apache-2.0](https://github.com/maromocooo/licgate/blob/3b011903a35d0eb1c72269600926bde257364b9f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/jev.go`](https://github.com/maromocooo/licgate/blob/3b011903a35d0eb1c72269600926bde257364b9f/internal/jev/jev.go) at the pinned commit. |

## When to use

- Check license compatibility before publishing or in CI.
- Want unknown license files classified with a confidence threshold.
- Mismatch: not legal advice; Jev is optional.

## How it works

`internal/jev/jev.go` is a minimal System One client; with `--jev`, only unrecognized license texts are classified, and answers below `--jev-threshold` (0.85 by default) stay REVIEW. Integration evidence: [`internal/jev/jev.go`](https://github.com/maromocooo/licgate/blob/3b011903a35d0eb1c72269600926bde257364b9f/internal/jev/jev.go).

## Get started

From the upstream README: install licgate, then run it with your intended license, adding `--jev` for unknown texts.

```sh
licgate -l MIT --jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README sample output

## Limits and data handling

Only license texts are sent to TypeSafe or OpenRouter. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 3b011903a35d](https://github.com/maromocooo/licgate/tree/3b011903a35d0eb1c72269600926bde257364b9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
