# pi-next-prompt

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension with Claude Code–style next-prompt suggestions: the main model may end its final message with one `<next>…</next>` line, and TypeSafe Jev (through Pi's classifier models) vets whether it is a concrete, non-generic, not-yet-done next step; it is shown under the editor at p ≥ 0.6 and `Tab` fills it in without sending.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/justmytwospence/pi-next-prompt) |
| Maintainer | [justmytwospence](https://github.com/justmytwospence). Independently curated. |
| Format | Pi extension (Pi 1.0+) |
| Requirements | Pi 1.0+; `TYPESAFE_API_KEY` for the Jev check (if Jev is unavailable, the suggestion is shown anyway). |
| License | [MIT](https://github.com/justmytwospence/pi-next-prompt/blob/b1ada906bdf978ee95a6261b46581334073179c5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Speed up obvious follow-ups in long Pi sessions.
- Filter out generic 'anything else?' suggestions.
- Mismatch: most turns intentionally show nothing.

## How it works

A ~150-token cached prompt section asks for the `<next>` line only when one step is obvious; [`src/jev.ts`](https://github.com/justmytwospence/pi-next-prompt/blob/b1ada906bdf978ee95a6261b46581334073179c5/src/jev.ts) asks Jev to vet it. `/next-prompt status` shows the last suggestion and Jev's verdict.

## Get started

Install from GitHub with Pi's standard git package source (the README gives no install command), then toggle with `/next-prompt`:

```sh
pi install git:github.com/justmytwospence/pi-next-prompt
/next-prompt status
```

One Jev check per suggestion, billed to your TypeSafe key.

## Examples and demos

- README *How it works* and *Commands*; companion [opencode-next-prompt](https://github.com/justmytwospence/opencode-next-prompt) for opencode.

## Limits and data handling

The suggestion and recent answer go to TypeSafe for vetting. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit b1ada906bdf9](https://github.com/justmytwospence/pi-next-prompt/tree/b1ada906bdf978ee95a6261b46581334073179c5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
