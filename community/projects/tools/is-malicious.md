# is-malicious

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI codebase scanner that sends source, config, build, and CI files to TypeSafe Jev to flag deceptive or data-stealing behavior with file/line pointers. A clean report is not proof a project is safe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luantak/is-malicious) |
| Maintainer | [luantak](https://github.com/luantak). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI **is-malicious 0.1.0** (`npx is-malicious` / global `is-malicious`). |
| Requirements | Node.js ≥ 20; `TYPESAFE_API_KEY` for live scans. |
| License | [MIT](https://github.com/luantak/is-malicious/blob/b6052465eb47cf85f347596385954aa06532718a/LICENSE). TypeSafe usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; offline `vitest` run. Live TypeSafe scans were not run. |

## When to use

Use it as a second opinion before running unfamiliar code, especially when you want Jev judgments over behavior categories with line pointers. Prefer [jev-guard](jev-guard.md) or [jev-shield](jev-shield.md) for live coding-agent tool/MCP gates rather than one-shot tree scans. Do not treat exit code 0 as a security certification.

## How it works

The CLI discovers candidate files, chunks them, and asks TypeSafe Jev (see [`src/jev.ts`](https://github.com/luantak/is-malicious/blob/b6052465eb47cf85f347596385954aa06532718a/src/jev.ts)) about deceptive or data-stealing patterns. Findings include category, probability, confidence, and a short reason; documented telemetry is reported separately as `info` and does not alone fail the scan. Exit `1` means at least one high-severity finding; `2` is command failure.

## Get started

```sh
git clone https://github.com/luantak/is-malicious.git
cd is-malicious
git checkout b6052465eb47cf85f347596385954aa06532718a
npm ci
npm test
# Live (billable): export TYPESAFE_API_KEY=… && npx is-malicious /path/to/project
```

Scans send file contents to TypeSafe. This listing did not call TypeSafe.

## Examples and demos

- Fixtures under `fixtures/` (benign, suspicious-dropper, with-telemetry).
- GitHub Actions examples under `examples/github-actions/`.
- Offline unit tests on the review host (see Review).

## Limits and data handling

Source and config contents leave the host on every live scan; reports include token usage and calculated input cost. Both high and low scores can be wrong—review flagged code and coverage. Not a substitute for conventional SAST, dependency audit, or human review.

## Review and maintenance

Reviewed on **2026-09-20** at [commit b605246](https://github.com/luantak/is-malicious/tree/b6052465eb47cf85f347596385954aa06532718a): **is-malicious 0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/jev.ts`, and package metadata. Ran `npm ci` and `npm test`: **11** files, **36** tests passed. Live TypeSafe scans not executed.

Related: [jev-guard](jev-guard.md), [jev-shield](jev-shield.md), [jev-pii-checker](jev-pii-checker.md), [patdown](patdown.md).
