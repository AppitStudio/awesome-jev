# ModelRudder

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Free local community preview that adds model routing to the native Codex terminal: your own TypeSafe Jev key classifies each request so the strongest model is spent only where needed, while Codex keeps its tools, approvals and workspace permissions; observe, auto and pinned modes, checksum-verified release installer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cybrking/modelrudder) |
| Maintainer | [cybrking](https://github.com/cybrking). Independently curated. |
| Format | Release installer (`smart-codex-…-install.mjs` + `SHA256SUMS`) for macOS, Linux/WSL and a Windows preview |
| Requirements | Node 24+, a separately installed Codex CLI (versions 0.159.3 / 0.160.1 accepted by this preview), `codex login`, and a TypeSafe API key for observe/auto modes. |
| License | [MIT](https://github.com/cybrking/modelrudder/blob/62e7748243d68bb8767892557b8c96fbe2c78ecb/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Try per-request model routing in Codex without a hosted router account.
- Observe what Jev would route before letting it switch models.
- Mismatch: preview; full TUI compatibility is not certified and only specific Codex versions are accepted.

## How it works

[`src/adapters/jev.ts`](https://github.com/cybrking/modelrudder/blob/62e7748243d68bb8767892557b8c96fbe2c78ecb/src/adapters/jev.ts) sends each request summary to TypeSafe and maps the answer to a served model under the policy; pinned mode skips classification. Upstream notes OpenAI's terms on app-server use and does not claim permission for paid-subscription operation.

## Get started

Download the release installer and verify it (README *Install*):

```sh
# from https://github.com/cybrking/modelrudder/releases (v0.1.0-preview.3)
shasum -a 256 -c SHA256SUMS
node -- ./smart-codex-RELEASE_ID-install.mjs
```

Jev classification is billed to your TypeSafe key; Codex usage follows your ChatGPT/Codex plan.

## Examples and demos

- [Release v0.1.0-preview.3](https://github.com/cybrking/modelrudder/releases/tag/v0.1.0-preview.3).
- README *Configure and start*.

## Limits and data handling

Request summaries go to TypeSafe in observe/auto modes. Experimental preview. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 62e7748243d6](https://github.com/cybrking/modelrudder/tree/62e7748243d68bb8767892557b8c96fbe2c78ecb). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
