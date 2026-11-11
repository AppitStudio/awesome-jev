# Wizard (terminal coding agent with an optional Jev prompt-section classifier)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fast terminal coding agent that, with a decision provider configured, makes one classifier call before the first step to keep only the system-prompt sections and skills a request needs; Jev is one of the supported providers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/teddytennant/wizard) |
| Maintainer | [teddytennant](https://github.com/teddytennant). Independently curated. |
| Format | Terminal agent (Rust, MIT or Apache-2.0) |
| Requirements | The Wizard binary, a chat-model provider, and `JEV_API_KEY` with the `jev` decision provider. |
| License | [MIT or Apache-2.0](https://github.com/teddytennant/wizard/blob/e4dc91a016e9adb34ed109de6427e12b46ba1e93/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions.rs`](https://github.com/teddytennant/wizard/blob/e4dc91a016e9adb34ed109de6427e12b46ba1e93/src/decisions.rs) at the pinned commit. |

## When to use

- Trim a coding agent's system prompt per request with a typed classifier.
- Compare Jev with OpenAI or SubQ as the decision provider.
- Mismatch: off unless you configure a decision provider; Jev is one of three options.

## How it works

`src/decisions.rs` pins `jev-1.13.0` and calls `/v1/systemone` with a 2 s budget; on timeout or error the full prompt goes out as before (`docs/decisions.md`). Integration evidence: [`src/decisions.rs`](https://github.com/teddytennant/wizard/blob/e4dc91a016e9adb34ed109de6427e12b46ba1e93/src/decisions.rs).

## Get started

Install Wizard, then add a `[decisions]` table naming the `jev` provider and set `JEV_API_KEY`.

```sh
curl -fsSL https://raw.githubusercontent.com/teddytennant/wizard/main/install.sh | bash
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decisions doc: [github.com/teddytennant/wizard/blob/e4dc91a016e9adb34ed109de6427e12b46ba1e93/docs/decisions.md](https://github.com/teddytennant/wizard/blob/e4dc91a016e9adb34ed109de6427e12b46ba1e93/docs/decisions.md)

## Limits and data handling

The prompt being classified goes to TypeSafe on your key; coding happens on your chat-model provider.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit e4dc91a016e9](https://github.com/teddytennant/wizard/tree/e4dc91a016e9adb34ed109de6427e12b46ba1e93). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
