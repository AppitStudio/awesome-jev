# NiceNovember (Discord bot that uses Jev to judge hostile chat and voice)

[All projects](../README.md) · [Discord bots](README.md#discord-bots)

Discord bot that listens in voice and text, asks TypeSafe Jev whether speech or messages are hostile toward a person (not just swear words), and applies short server-mute timeouts with an announce-channel quote and audit log.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SAUCE-2/NiceNovember) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/SAUCE-2/NiceNovember#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; Discord and TypeSafe usage on your keys. Checked 2026-11-06. |
| Jev evidence | [`src/ai/jev.rs`](https://github.com/SAUCE-2/NiceNovember/blob/e5c54e6c6b555cdb7768638b9840f891edee2576/src/ai/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [SAUCE-2](https://github.com/SAUCE-2). Independently curated. |
| Format | Rust Discord bot (MIT) |
| Platform and availability | Self-hosted Discord bot (Rust). |
| Jev's role | Judges whether chat, edits, reactions and transcribed speech are hostile toward a person via typed questions to TypeSafe Jev (`jev-latest` at api.typesafe.ai/v1/systemone). |
| Requirements | A Discord bot token and a TypeSafe API key for Jev judgments. |
| License | [MIT](https://github.com/SAUCE-2/NiceNovember/blob/e5c54e6c6b555cdb7768638b9840f891edee2576/LICENSE) |

## When to use

- Moderate a Discord call where hostility is about targeting people, not vocabulary.
- Keep an audit log of timeouts for month-end stats.
- Mismatch: needs always-on listening permissions; not a keyword filter.

## How it works

`src/ai/jev.rs` POSTs multipart System One requests to `https://api.typesafe.ai/v1/systemone` with model `jev-latest` and returns typed probabilistic answers used by the timeout policy. Integration evidence: [`src/ai/jev.rs`](https://github.com/SAUCE-2/NiceNovember/blob/e5c54e6c6b555cdb7768638b9840f891edee2576/src/ai/jev.rs).

## Get started

Clone, configure Discord and TypeSafe credentials per README, and run the bot in a test guild first.

```sh
git clone https://github.com/SAUCE-2/NiceNovember.git && cd NiceNovember
export TYPESAFE_API_KEY=...
# follow README for Discord token and run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/SAUCE-2/NiceNovember/blob/e5c54e6c6b555cdb7768638b9840f891edee2576/README.md](https://github.com/SAUCE-2/NiceNovember/blob/e5c54e6c6b555cdb7768638b9840f891edee2576/README.md)

## Limits and data handling

Voice transcripts, message text, reply context and reaction targets are sent to TypeSafe on your key. Timeouts are bot-enforced mute/deafen, not Discord native timeouts.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit e5c54e6c6b55](https://github.com/SAUCE-2/NiceNovember/tree/e5c54e6c6b555cdb7768638b9840f891edee2576). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
