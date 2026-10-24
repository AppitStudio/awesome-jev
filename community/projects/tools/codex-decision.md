# Codex Decision (trim repetitive Codex tool output with OpenAI Decisions or Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

VS Code extension and native hooks for Codex that select repetitive lines for removal from local tool output while keeping errors and useful evidence visible, with a link to the full original; OpenAI Decisions is the default and TypeSafe Jev or a custom endpoint can be chosen instead.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PhilippElhaus/Codex-Decision) |
| Maintainer | [PhilippElhaus](https://github.com/PhilippElhaus). Independently curated. |
| Format | VS Code extension (VSIX) with native Rust hooks |
| Requirements | VS Code with Codex; Windows or Linux x86_64 (WSL supported); an OpenAI or TypeSafe key. |
| License | [MIT](https://github.com/PhilippElhaus/Codex-Decision/blob/255c761f0f65d123dd90a1eb2a70082abc9391d2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`rust/decision/src/provider.rs`](https://github.com/PhilippElhaus/Codex-Decision/blob/255c761f0f65d123dd90a1eb2a70082abc9391d2/rust/decision/src/provider.rs) at the pinned commit. |

## When to use

- Keep long build and test logs from filling a Codex session.
- Switch between OpenAI Decisions and Jev with saved keys and an optional fallback.
- Mismatch: Jev is optional; the default provider is OpenAI Decisions.

## How it works

`rust/decision/src/provider.rs` defines the OpenAI and TypeSafe providers; the hook sends output lines as yes/no questions (`jev-latest` for TypeSafe) and removes only the lines it selects; errors and useful evidence stay visible. Integration evidence: [`rust/decision/src/provider.rs`](https://github.com/PhilippElhaus/Codex-Decision/blob/255c761f0f65d123dd90a1eb2a70082abc9391d2/rust/decision/src/provider.rs).

## Get started

From the upstream README (not run on the review host): download the VSIX from the latest release (v0.15.0 at review), then:

```sh
code --install-extension codex-decision-0.15.0.vsix --force
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/PhilippElhaus/Codex-Decision/releases/latest](https://github.com/PhilippElhaus/Codex-Decision/releases/latest)
- README: [github.com/PhilippElhaus/Codex-Decision#readme](https://github.com/PhilippElhaus/Codex-Decision#readme)

## Limits and data handling

Tool output lines go to the chosen provider. The extension patches the Codex UI; unsupported builds show a diagnostic.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 255c761f0f65](https://github.com/PhilippElhaus/Codex-Decision/tree/255c761f0f65d123dd90a1eb2a70082abc9391d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
