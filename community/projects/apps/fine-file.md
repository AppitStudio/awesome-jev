# fine-file (Windows file explorer with optional Jev risk badges)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Korean-language Windows file explorer with folder sizes, instant search from an NTFS MFT scan and live updates, plus optional AI clean-up plans where Jev adds fast safe, caution or risky badges and a second risk check on each step.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/toxh13/fine-file) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://github.com/toxh13/fine-file/releases) |
| Pricing and access | Free MIT/Apache-2.0 app; Jev calls are billed to your own key. Checked 2026-10-22. |
| Jev evidence | [`src-tauri/src/ai.rs`](https://github.com/toxh13/fine-file/blob/0eb6084d5c9d6b831dc9f93c2f5b5a6bef200d0c/src-tauri/src/ai.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [toxh13](https://github.com/toxh13). Independently curated. |
| Format | Windows desktop app (Rust, Tauri) |
| Platform and availability | Windows (installer on GitHub Releases); interface in Korean. |
| Jev's role | Optional: Jev scores whether each item is safe to delete and whether a program recreates it; the explorer works fully without it. |
| Requirements | Windows; optional Jev API key for risk badges (other AI features use Claude, OpenAI, Ollama or local CLIs). |
| License | [MIT OR Apache-2.0](https://github.com/toxh13/fine-file/blob/0eb6084d5c9d6b831dc9f93c2f5b5a6bef200d0c/LICENSE-MIT) |

## When to use

- See which folders are taking space and clean them up with a second opinion on risk.
- Get quick, cheap risk badges for a whole folder listing.
- Mismatch: interface and docs are in Korean.

## How it works

`src-tauri/src/ai.rs` sends only file metadata (path, name, size, date, category, never contents) in batches of 40 to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with two questions per item; keys stay in Windows Credential Manager. Integration evidence: [`src-tauri/src/ai.rs`](https://github.com/toxh13/fine-file/blob/0eb6084d5c9d6b831dc9f93c2f5b5a6bef200d0c/src-tauri/src/ai.rs).

## Get started

From the upstream README (not run on the review host):

```sh
# Download fine-file_<version>_x64-setup.exe from GitHub Releases and run it
# then add a Jev key in the AI settings to enable risk badges
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Feature list and AI settings in the README: [github.com/toxh13/fine-file#readme](https://github.com/toxh13/fine-file#readme)

## Limits and data handling

With Jev enabled, file and folder metadata is sent to TypeSafe; a preview shows what will be sent. File contents are never sent, per the source.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 0eb6084d5c9d](https://github.com/toxh13/fine-file/tree/0eb6084d5c9d6b831dc9f93c2f5b5a6bef200d0c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
