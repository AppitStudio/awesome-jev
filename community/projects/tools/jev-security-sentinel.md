# jev-security-sentinel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that turns SAST/SCA/IaC/secrets/container findings into a CI gate using TypeSafe Jev (`PASS` / `WARN` / `BLOCK` / `REVIEW`) while keeping every finding visible and only allowing stricter merges with the deterministic floor.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JevForge/jev-security-sentinel) |
| Maintainer | [JevForge](https://github.com/JevForge). Independently curated. |
| Format | TypeScript GitHub Action with SARIF/Semgrep/Trivy/… parsers. |
| Requirements | GitHub Actions; Gateway/TypeSafe/custom Jev key via secrets (not Action inputs). |
| License | [MIT](https://github.com/JevForge/jev-security-sentinel/blob/fd0251b04d31a80effee1901dbc1dc0efe997062/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Actions/Jev not run. |

## When to use

Use it to **gate merges on scanner output** without burying findings. Prefer pure severity thresholds when you do not want a model in the loop.

## How it works

Reports are normalized and redacted; Jev proposes a gate; code merges with a policy floor that Jev cannot weaken. Optional Checks API runs and PR comments.

## Get started

```sh
git clone https://github.com/JevForge/jev-security-sentinel.git
cd jev-security-sentinel
git checkout fd0251b04d31a80effee1901dbc1dc0efe997062
npm ci
npm test
# uses: JevForge/jev-security-sentinel@v0.1.1 (pin SHA in production)
```

## Examples and demos

- README Action snippet; `examples/` workflows.

## Limits and data handling

Finding text (post-redaction) goes to the Jev provider. Allowlists change gate effect only—findings remain in outputs. No live CI in this review.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit fd0251b](https://github.com/JevForge/jev-security-sentinel/tree/fd0251b04d31a80effee1901dbc1dc0efe997062). AI-assisted README + Action inspection.

Related: [OpenCode Security Guard](opencode-security-guard.md), [agent-chaperone](agent-chaperone.md), [Moongate](moongate.md).
