# jev-preflight

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that baselines the working tree at turn start, then asks TypeSafe Jev to score eight risk axes over a redacted turn diff at Stop—optionally requesting one more investigation when risk is high.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muse0509/jev-preflight) |
| Maintainer | [muse0509](https://github.com/muse0509). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go Claude Code plugin / hook binary (`cmd/jev-preflight`), public beta **v0.1.0**. |
| Requirements | Claude Code 2.1.257+; Git; Bash; `TYPESAFE_API_KEY`. Fail-open without a key per upstream. |
| License | [MIT](https://github.com/muse0509/jev-preflight/blob/c143b921253fd814bcd3c53d638a0cc8d390d49c/LICENSE). |

## When to use

Use it when you want a bounded, single-request risk signal on what Claude Code changed this turn (behavior, auth, validation, integrity, errors, compatibility, lifecycle, tests)—not as a merge blocker or autofix. Prefer [pi-jev-sentinel](pi-jev-sentinel.md) or [toolgate](toolgate.md) for pre-tool gates; prefer [jev-pr-judge](jev-pr-judge.md) for PR-level typed verdicts.

## How it works

[`internal/jev/client.go`](https://github.com/muse0509/jev-preflight/blob/c143b921253fd814bcd3c53d638a0cc8d390d49c/internal/jev/client.go) posts one request to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with unified-diff state and eight noul questions. Hook code redacts and selects the diff; assist mode may ask Claude to investigate once when scores meet an uncalibrated default threshold (0.85). Background/cron wakeups defer evaluation.

## Get started

```sh
git clone https://github.com/muse0509/jev-preflight.git
cd jev-preflight
git checkout c143b921253fd814bcd3c53d638a0cc8d390d49c
go test ./...
# Install/enable as a Claude Code plugin per upstream README; needs TYPESAFE_API_KEY for live scoring
```

Live Stop hooks send redacted diffs to TypeSafe and can incur charges. This listing did not install the plugin into Claude Code or call live Jev.

## Examples and demos

- Upstream verification notes in `docs/verification.md` and hook smoke scripts.
- Go unit/fake-server tests under `internal/jev` and `internal/hook`.

## Limits and data handling

Selected/redacted diffs leave the host for TypeSafe. Default threshold is uncalibrated; scores are signals, not defect proof. Not a replacement for tests, linters, SAST, or secret scanning. Upstream live round-trip claims were not reproduced here.

## Review and maintenance

Reviewed on **2026-09-20** at [commit c143b92](https://github.com/muse0509/jev-preflight/tree/c143b921253fd814bcd3c53d638a0cc8d390d49c): **v0.1.0** public beta, MIT. AI-assisted source review of README, `internal/jev/client.go`, hook layout, and license. `go test` / Claude Code install / live TypeSafe were not executed on the review host.

Related: [pi-jev-sentinel](pi-jev-sentinel.md), [toolgate](toolgate.md), [jev-pr-judge](jev-pr-judge.md).
