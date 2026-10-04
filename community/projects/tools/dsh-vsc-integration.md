# DeepSeek Harness for VS Code

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VS Code extension for DeepSeek Harness with a built-in, optional Laya/Jev decision layer: loop guard, large-output shaping, done-gate, tool pruning, and skill routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HarcoChen/dsh-vsc-integration) |
| Product homepage | [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=HarcoChen.dsh-vsc-integration) |
| Maintainer | [HarcoChen](https://github.com/HarcoChen). Independently curated. |
| Format | VS Code / Open VSX extension bundling the `dsh-jev-integration` runtime plugin |
| Requirements | VS Code, the DeepSeek Desktop app (`dsh` command) and DeepSeek API key; for Jev, enable `dsh.jev.enabled` and run `DSH: Configure Jev API Key`. |
| License | [MIT](https://github.com/HarcoChen/dsh-vsc-integration/blob/deb8d8f882586c42a20abfbb5609cb0643fac309/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Use DeepSeek Harness inside VS Code with native diffs and tool approvals.
- Add System One checks (loop guard, result shaper, done-gate) to the agent loop without extra installs.
- Mismatch: Jev features are off by default; DeepSeek usage is billed separately from Jev.

## How it works

The extension ships the IDE-neutral [dsh-jev-integration](https://github.com/HarcoChen/dsh-jev-integration) runtime plugin. When enabled, agent state is sent to Jev (or Laya) for typed decisions such as semantic-loop detection after tool execution and folding repetitive output; DeepSeek generates code.

## Get started

Install from the Marketplace or Open VSX (search `harcochen.dsh-vsc-integration`), then optionally enable Jev in settings and set the key via the command palette.

```sh
code --install-extension HarcoChen.dsh-vsc-integration
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README feature tables for the Laya/Jev settings (`dsh.jev.loopGuard.enabled`, `dsh.jev.resultShaper.enabled`, …).

## Limits and data handling

Enabling Jev sends agent state to TypeSafe (or your Laya endpoint) and may incur charges; DeepSeek charges are separate.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit deb8d8f88258](https://github.com/HarcoChen/dsh-vsc-integration/tree/deb8d8f882586c42a20abfbb5609cb0643fac309). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
