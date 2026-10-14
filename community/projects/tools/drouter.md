# drouter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Rust decision API router that sends requests to Jev or an OpenAI-compatible teacher, caches verified answers and promotes audited shadow students.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timur-3c/drouter) |
| Maintainer | [timur-3c](https://github.com/timur-3c). Independently curated. |
| Format | Rust CLI server (release binaries) |
| Requirements | Linux/macOS/Windows binary; TypeSafe key for the Jev teacher. |
| License | [MIT](https://github.com/timur-3c/drouter/blob/f199decb2f401d309283989d91a069e0b885f446/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main.rs`](https://github.com/timur-3c/drouter/blob/f199decb2f401d309283989d91a069e0b885f446/src/main.rs) at the pinned commit. |

## When to use

- Reduce repeat classifier calls by reusing verified decisions.
- Audit whether a cheaper student matches the Jev teacher before activating it.
- Mismatch: v0.1 experimental; replay results do not guarantee fresh-input reliability (per upstream).

## How it works

Requests are routed to the Jev teacher; answers are persisted and three shadow students are compared against it, with the best qualified student activated only after an audit gate. Integration evidence: [`src/main.rs`](https://github.com/timur-3c/drouter/blob/f199decb2f401d309283989d91a069e0b885f446/src/main.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSLO https://raw.githubusercontent.com/timur-3c/drouter/v0.1.0/scripts/install.sh
bash install.sh 0.1.0
drouter --version
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example config: `examples/drouter.toml`.

## Limits and data handling

Requests sent to the teacher go to TypeSafe (or the configured OpenAI-compatible endpoint) and are billed to your key; cached answers are stored locally.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit f199decb2f40](https://github.com/timur-3c/drouter/tree/f199decb2f401d309283989d91a069e0b885f446). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
