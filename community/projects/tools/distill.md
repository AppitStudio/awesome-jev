# Distill

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Lightweight terminal coding harness/TUI that uses TypeSafe Jev (or an OpenRouter decisions/chat backend) as a structured decision layer for model/effort routing, utility tasks, and retention—while Distill owns permissions and tool approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/samuelfaj/distill) |
| Maintainer | [Samuel Fajreldines / samuelfaj](https://github.com/samuelfaj). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust coding agent **Distill 2.0.0** (prebuilt binaries + source; installer `install.sh`). |
| Requirements | A reachable chat model (Grok, ChatGPT, OpenRouter, or local OpenAI-compatible). Jev routing needs a decision endpoint credential (`JEV_API_KEY` by default for TypeSafe `https://api.typesafe.ai`, or OpenRouter when configured). |
| License | [Apache-2.0](https://github.com/samuelfaj/distill/blob/07589b35a4ed006a271c2558ac763308c6548202/LICENSE) (upstream notes SpaceXAI copyright plus Distill modifications). |

## When to use

Use it when you want a local coding TUI that can hand bounded routing and compression choices to Jev while a separate Reasoning/Worker/Utility chat model does the writing. Prefer [Foreman](foreman.md) or [jev-gateway](jev-gateway.md) when you already supervise Codex/Claude through those stacks rather than adopting Distill as the harness. Do **not** treat Jev answers as permission grants—Distill owns plan mode, auto-approval, and YOLO policy.

## How it works

[`crates/codegen/distill-workspace/src/jev/client.rs`](https://github.com/samuelfaj/distill/blob/07589b35a4ed006a271c2558ac763308c6548202/crates/codegen/distill-workspace/src/jev/client.rs) posts typed questions to TypeSafe System One (`DEFAULT_BASE_URL` `https://api.typesafe.ai`, default model `jev-latest`) or to OpenRouter decisions/chat backends via [`provider.rs`](https://github.com/samuelfaj/distill/blob/07589b35a4ed006a271c2558ac763308c6548202/crates/codegen/distill-workspace/src/jev/provider.rs). Jev chooses among code-supplied candidates (model/effort, utility tasks, retention blocks). Failures, timeouts, and low confidence leave Distill on its normal path. Configuration lives under `[jev]` / `[jev.ladder]` in user settings (README documents `model = "~typesafe/jev-latest"` for OpenRouter decisions).

## Get started

```sh
curl -fsSL https://raw.githubusercontent.com/samuelfaj/distill/main/install.sh -o /tmp/distill-install.sh
sh /tmp/distill-install.sh
export PATH="$HOME/.local/share/distill/bin:$PATH"
distill
# or inspect the reviewed tree:
git clone https://github.com/samuelfaj/distill.git
cd distill
git checkout 07589b35a4ed006a271c2558ac763308c6548202
```

Live Jev calls need a decision credential and send harness-assembled state (prompts, tool excerpts, candidate lists) to the configured endpoint. This listing did not install Distill or call TypeSafe.

## Examples and demos

- README “How Jev routes work” with Reasoning/Worker/Utility diagram and `[jev.ladder]` switches.
- Installer path and `/tiers` / `/model` pickers for chat models.
- Workspace tests under `crates/codegen/distill-workspace/` (including `tests/jev_live.rs` for optional live paths).

## Limits and data handling

Conversation and tool payloads can leave the machine for both the chat provider and the Jev endpoint. Distill does not let Jev invent candidates or approve tools. Upstream accuracy/speed claims were not reproduced here. Pin a model version when calibrating confidence floors (`jev-latest` moves).

## Review and maintenance

Reviewed on **2026-09-20** at [commit 07589b35](https://github.com/samuelfaj/distill/tree/07589b35a4ed006a271c2558ac763308c6548202): **2.0.0**, Apache-2.0. AI-assisted source review of README, `jev/client.rs`, `jev/provider.rs`, and license. Offline unit/live Jev tests and installer runs were not executed on the review host.

Related: [Foreman](foreman.md), [jev-gateway](jev-gateway.md), [jev-use](jev-use.md).
