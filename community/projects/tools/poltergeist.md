# Poltergeist

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ghost Security's fast Go secret scanner with an opt-in advisory classification that asks Jev how likely each detected value is a real secret, without changing findings or exit codes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ghostsecurity/poltergeist) |
| Product homepage | [oss.ghostsecurity.ai](https://oss.ghostsecurity.ai/tools/poltergeist) |
| Maintainer | [ghostsecurity](https://github.com/ghostsecurity). Independently curated. |
| Format | CLI binary (install script or releases) and Go library |
| Requirements | Linux, macOS or Windows (Git Bash/MSYS2/Cygwin). Classification needs `TYPESAFE_API_KEY` *and* the `-classify` flag. |
| License | [Apache-2.0](https://github.com/ghostsecurity/poltergeist/blob/20d3fa3691e53ee034e9e209fccaa5e9df7916eb/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Triage a large set of secret-scanner hits by putting likely-real credentials first.
- Keep CI behavior unchanged while adding an advisory score to JSON reports.
- Mismatch: classification sends the raw matched values to TypeSafe; do not enable it where secrets must never leave the network.

## How it works

After detection and entropy filtering, eligible candidates — raw matched value, bounded surrounding code, rule identifiers and relative path — are sent to Jev as a Noul question about whether the value is an authentic secret. Results at or above 0.90 are `likely_real`, at or below 0.10 `likely_dummy`, otherwise `uncertain`; skipped or failed items carry a reason code. Defaults: 10-second budget, 1,000 candidates, optional 24-hour cache ([docs/classification.md](https://github.com/ghostsecurity/poltergeist/blob/20d3fa3691e53ee034e9e209fccaa5e9df7916eb/docs/classification.md), [`pkg/classification_jev.go`](https://github.com/ghostsecurity/poltergeist/blob/20d3fa3691e53ee034e9e209fccaa5e9df7916eb/pkg/classification_jev.go)).

## Get started

Install, then scan with classification enabled (live TypeSafe calls per eligible finding):

```sh
curl -sfL https://raw.githubusercontent.com/ghostsecurity/poltergeist/main/scripts/install.sh | bash
export TYPESAFE_API_KEY='your-api-key'
poltergeist -classify -format json ./source
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Classification docs](https://github.com/ghostsecurity/poltergeist/blob/20d3fa3691e53ee034e9e209fccaa5e9df7916eb/docs/classification.md): data handling, flags (`-classify-timeout`, `-classify-max-candidates`, `-classify-cache-dir`), score semantics and library use.

## Limits and data handling

Raw secret candidates are submitted even when report redaction is on — upstream states this explicitly. The score is a pretrained model judgment, not calibrated on Poltergeist's own data, and does not prove a credential is valid. Keep the cache directory outside the scanned tree. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 20d3fa3691e5](https://github.com/ghostsecurity/poltergeist/tree/20d3fa3691e53ee034e9e209fccaa5e9df7916eb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
