# factrail by DreamLab AI (fact-keeping context compaction for coding agents in Rust, with a Jev judge and fact rails)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust context compaction for coding agents (a Claude Code plugin plus a CLI) that never rewrites what the user or agent wrote. For each old tool call a typed-decision judge answers two questions: does the call still matter, and must its output stay verbatim? Only what the judge lets go is reduced, through fact rails: reproducible reads become one-line re-run notes, observations keep their head, fact lines and tail, and every reduced output is saved with secrets masked. Includes a replay eval that counts the facts the agent went on to use, a rules-only fallback and a private-tool fence.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DreamLab-AI/factrail) |
| Maintainer | [DreamLab-AI](https://github.com/DreamLab-AI). Independently curated. |
| Format | Rust CLI and Claude Code plugin (MIT or Apache-2.0) |
| Requirements | Rust toolchain to build; Claude Code for the plugin; `TYPESAFE_API_KEY` (or `FACTRAIL_API_KEY`) for the System One judge, or a local OpenAI-compatible server for the Tev judge. Rules-only mode needs no key. |
| License | [MIT OR Apache-2.0](https://github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/factrail-backend/src/judge.rs`](https://github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/crates/factrail-backend/src/judge.rs) at the pinned commit. |

## When to use

- Compact long Claude Code sessions without losing paths, errors, ids and counts, with every reduction recoverable.
- Mismatch: summarisation-style compaction; factrail deliberately keeps conversation text verbatim.

## How it works

`crates/factrail-backend/src/judge.rs` implements `SystemOneJudge`, which posts the two `noul` questions per tool call to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) carrying tool-result sizes, never their contents, and logs which model and backend answered. Integration evidence: [`crates/factrail-backend/src/judge.rs`](https://github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/crates/factrail-backend/src/judge.rs).

## Get started

Build the binary, replay your own sessions without a model, then install the plugin.

```sh
git clone https://github.com/DreamLab-AI/factrail
cd factrail
cargo build --release
./target/release/factrail eval --claude-projects ~/.claude/projects --max 40 --sim   # no model
export TYPESAFE_API_KEY=...
./target/release/factrail compact session.jsonl --out compacted.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/README.md](https://github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/README.md)
- Local judge: [github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/docs/local-judge.md](https://github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/docs/local-judge.md)
- Decision record: [github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/docs/adr/ADR-001-factrail.md](https://github.com/DreamLab-AI/factrail/blob/69692a2d23d9c8de58ace97d0925530d6c9e23c0/docs/adr/ADR-001-factrail.md)

## Limits and data handling

The judge's state carries tool-result sizes and metadata, not contents; sessions that used fenced private tools are compacted by rules only unless the endpoint is declared local. The README's retention figures are the author's measurements on their own sessions (2026-10-02), not verified here. It re-implements MIT-licensed designs from three earlier Jev compaction projects, credited in NOTICE.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 69692a2d23d9](https://github.com/DreamLab-AI/factrail/tree/69692a2d23d9c8de58ace97d0925530d6c9e23c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
