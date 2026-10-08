# Chirp (Tern)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Tiny robot voice for the Tern terminal: when a coding agent finishes or waits for you, Jev reads the end of its last message and answers six typed questions (mood, voice, pitch, pace, energy, and whether you're being asked something), and a small Luau synthesizer turns the probabilities into one short beep; without a key it falls back to a local reading. Inspired by Yohei Nakajima's Beep Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Noctivoro/tern-chirp) |
| Maintainer | [Noctivoro](https://github.com/Noctivoro). Independently curated. |
| Format | Tern plugin (`tern plugin install github.com/Noctivoro/tern-chirp`) |
| Requirements | Tern; a TypeSafe API key in the macOS Keychain (`typesafe-api-key`) or `TYPESAFE_API_KEY`; works without a key using a local heuristic. |
| License | [MIT](https://github.com/Noctivoro/tern-chirp/blob/1bffd5f7138f471bdb72e992a895ee2387237df9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Know from sound alone whether the agent succeeded, struggled or needs an answer.
- Small, readable example of mapping typed Jev answers to non-text output.
- Mismatch: Tern only.

## How it works

[`lib/director.luau`](https://github.com/Noctivoro/tern-chirp/blob/1bffd5f7138f471bdb72e992a895ee2387237df9/lib/director.luau) builds the six questions and maps answers; [`lib/synth.luau`](https://github.com/Noctivoro/tern-chirp/blob/1bffd5f7138f471bdb72e992a895ee2387237df9/lib/synth.luau) renders the beep deterministically, so the same message always sounds the same.

## Get started

Install the plugin and store your key (README *Install*):

```sh
tern plugin install github.com/Noctivoro/tern-chirp
security add-generic-password -s typesafe-api-key -a default -w
```

Each chirp is one Jev request billed to your key.

## Examples and demos

- README *What you hear* table (Jev answer → sound change).

## Limits and data handling

The tail of the agent's last message is sent to TypeSafe when a key is set (README *Privacy*). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 1bffd5f7138f](https://github.com/Noctivoro/tern-chirp/tree/1bffd5f7138f471bdb72e992a895ee2387237df9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
