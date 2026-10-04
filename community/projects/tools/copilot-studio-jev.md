# Copilot Studio × Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Copilot Studio/Power Platform: MCP gates Azure AI Search passages with TypeSafe Jev yes/no questions; plus a TypeSafe custom connector (MIT).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Zakariakhchiche/copilot-studio-jev) |
| Maintainer | [Zakariakhchiche](https://github.com/Zakariakhchiche). Independently curated. |
| Format | MCP server + Power Platform connector for TypeSafe Jev (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/Zakariakhchiche/copilot-studio-jev/blob/69e1dd870236a674528b574271bfff5eb79f99b2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Independent of Microsoft/TypeSafe. MCP proposed upstream as microsoft/CopilotStudioSamples#539 (draft). Offline npm test path documented; live Copilot Studio not run on the review host. Live install/inference not run on the review host. |

## When to use

Use when building Copilot Studio / Power Platform agents over large document corpora that must cite or abstain. Prefer generic MCP Jev servers outside Microsoft stacks.

## How it works

MCP searches Azure AI Search, then Jev answers calibrated yes/no questions per passage; code applies thresholds for proof, contradiction, or reject. Connector exposes Ask/Choose/Rate/Evaluate/List models.

## Get started

```sh
git clone https://github.com/Zakariakhchiche/copilot-studio-jev.git
cd copilot-studio-jev
git checkout 69e1dd870236a674528b574271bfff5eb79f99b2
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 69e1dd870236](https://github.com/Zakariakhchiche/copilot-studio-jev/tree/69e1dd870236a674528b574271bfff5eb79f99b2). AI-assisted README and license inspection; install/live paths not executed.
