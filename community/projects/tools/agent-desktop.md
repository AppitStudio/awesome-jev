# agent-desktop

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Rust CLI for desktop computer use via OS accessibility trees, with an optional bundled **jev-desktop** skill and Node scripts that ask TypeSafe Jev for target/command choices without putting the a11y tree in the calling agent's context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lahfir/agent-desktop) |
| Maintainer | [lahfir](https://github.com/lahfir). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust CLI / npm package **`agent-desktop` 0.9.2**; bundled agent skills (`agent-desktop`, `jev-desktop`) plus `scripts/jev/*.mjs`. |
| Requirements | macOS 13+ with Accessibility (Screen Recording / Automation for some features); Rust 1.89+ to build from source, or Node ≥18 for the npm binary wrapper. Jev scripts need `TYPESAFE_API_KEY` (BYOK). Chrome install is not required for the core a11y path. |
| License | [Apache-2.0](https://github.com/lahfir/agent-desktop/blob/7a8e4a10281c7319733aa200fd79501f34529716/LICENSE). TypeSafe usage for jev scripts billed separately. |
| Disclosure | AI-assisted independent curation. Listing is not an endorsement. Live Jev/desktop automation was not run on the Linux review host. |

## When to use

Use the **CLI** when an agent (or your own code) should observe and operate macOS apps through stable accessibility refs and JSON—Jev is not required for raw snapshots or actions. Use the **jev-desktop** skill / `scripts/jev` path when you want TypeSafe Jev to choose which element and operation to run while keeping the tree out of the LLM context.

Prefer [typesafe-computer-use](typesafe-computer-use.md) for a Python OCR + Accessibility study loop, or [jev-macos-loop](jev-macos-loop.md) for OmniParser/Vision perception with text-only Jev action choice. Prefer browser agents when the target is the web DOM rather than native a11y.

## How it works

The product core is a Rust accessibility automation CLI: snapshot, ref-qualified actions, progressive skeleton traversal, and related commands. Separately, [`skills/jev-desktop/SKILL.md`](https://github.com/lahfir/agent-desktop/blob/7a8e4a10281c7319733aa200fd79501f34529716/skills/jev-desktop/SKILL.md) describes a goal/step desktop loop that never puts the a11y tree in the agent context.

[`scripts/jev/act.mjs`](https://github.com/lahfir/agent-desktop/blob/7a8e4a10281c7319733aa200fd79501f34529716/scripts/jev/act.mjs) posts Choice questions for target and command to `https://api.typesafe.ai/v1/systemone` with model `jev-latest`. [`scripts/jev/run.mjs`](https://github.com/lahfir/agent-desktop/blob/7a8e4a10281c7319733aa200fd79501f34529716/scripts/jev/run.mjs) runs a multi-turn observe → decide → act loop until stop conditions. Code gates risk/confidence and executes via the CLI; Jev returns choices and probabilities, not free-form strings (text comes from `--text`).

## Get started

### CLI (no TypeSafe key)

```sh
npm install -g agent-desktop
# or from source at the reviewed commit:
git clone https://github.com/lahfir/agent-desktop.git
cd agent-desktop
git checkout 7a8e4a10281c7319733aa200fd79501f34529716
cargo build --release
```

Requires a Mac with Accessibility permission for live snapshots/actions. This Linux review host did not build the CLI or drive a desktop.

### Jev scripts (BYOK)

Set `TYPESAFE_API_KEY` privately. From a checkout that can run `agent-desktop`:

```sh
node scripts/jev/run.mjs --app Finder "open the Applications folder"
node scripts/jev/act.mjs --app TextEdit --execute --text "hello" "type this text into the main writing area"
```

Live runs send screen-derived text (roles, names, optional field values, window title, recent actions) to TypeSafe and can incur charges. Secure text fields are withheld by the CLI; `--no-values` withholds other values as well.

## Examples and demos

- Upstream README demos and architecture notes for the CLI path.
- Offline Node tests: `node --test scripts/jev/act.test.mjs scripts/jev/run.test.mjs` (no API key; mocked screen/policy assertions).
- Skill docs under `skills/jev-desktop/` and `skills/agent-desktop/`.

## Limits and data handling

The CLI itself does not call TypeSafe. Jev scripts require a key and send structured UI text off-machine each turn. Destructive-rated steps need higher confidence; low confidence stops rather than acting. Held-input verbs fail closed in the stateless CLI. Windows/Linux adapters are planned against the same contracts; this review checked the macOS-oriented Jev path in source only.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 7a8e4a1](https://github.com/lahfir/agent-desktop/tree/7a8e4a10281c7319733aa200fd79501f34529716) (`agent-desktop` **0.9.2**, Apache-2.0). AI-assisted source review of README, LICENSE, `skills/jev-desktop/SKILL.md`, `scripts/jev/act.mjs`, `scripts/jev/run.mjs`. Offline: `node --test scripts/jev/act.test.mjs scripts/jev/run.test.mjs` → **2 passed**. No live TypeSafe calls, no macOS Accessibility session, no Chrome install on the Linux review host.

Related: [typesafe-computer-use](typesafe-computer-use.md), [jev-macos-loop](jev-macos-loop.md), [Jev-cu](jev-cu.md).
