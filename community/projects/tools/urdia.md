# Urdia

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local workspace for coding agents (Linux/WSL source preview) with live visibility, explicit permissions and an experimental per-task mode where Jev selects the agent/model profile.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SaulineytorX/urdia) |
| Maintainer | [SaulineytorX](https://github.com/SaulineytorX). Independently curated. |
| Format | Rust local app with browser UI |
| Requirements | Ubuntu 24.04 / WSL; agent CLIs; TypeSafe key for Jev selection. |
| License | [Apache-2.0](https://github.com/SaulineytorX/urdia/blob/572e7abb01395284d7a80848de56664434c9efc2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/urdia-decision-jev/src/lib.rs`](https://github.com/SaulineytorX/urdia/blob/572e7abb01395284d7a80848de56664434c9efc2/crates/urdia-decision-jev/src/lib.rs) at the pinned commit. |

## When to use

- Give coding agents tasks and follow their work in the browser with explicit permissions.
- Try automatic Jev profile selection per task.
- Mismatch: early preview; manual sending is the default.

## How it works

When automatic selection is enabled for a task, the Jev decision crate sends the task and available profiles to Jev and uses the chosen profile; otherwise the user picks. Integration evidence: [`crates/urdia-decision-jev/src/lib.rs`](https://github.com/SaulineytorX/urdia/blob/572e7abb01395284d7a80848de56664434c9efc2/crates/urdia-decision-jev/src/lib.rs).

## Get started

From a clone (build steps in the upstream README; not run on the review host):

```sh
git clone https://github.com/SaulineytorX/urdia.git
cd urdia
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video linked in the upstream README.

## Limits and data handling

Task text is sent to TypeSafe only in the Jev mode and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 572e7abb0139](https://github.com/SaulineytorX/urdia/tree/572e7abb01395284d7a80848de56664434c9efc2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
