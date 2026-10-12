# ontoken-auto

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi package that adds a virtual model `ontoken/auto`: Jev classifies each user prompt and the extension picks an OnToken model slot and thinking level, optionally promoting mid-turn after tool results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/priaculun/ontoken-auto) |
| Maintainer | [priaculun](https://github.com/priaculun). Independently curated. |
| Format | Pi extension package (TypeScript) |
| Requirements | Pi coding agent; an `ontoken` provider in `~/.pi/agent/models.json`; a TypeSafe key (`TYPESAFE_API_KEY` or a secrets file). |
| License | [MIT](https://github.com/priaculun/ontoken-auto/blob/da5b59bda451160daf178858c1b0b6e1eca34e14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Route Pi turns between cheaper and stronger OnToken models automatically.
- Keep short follow-ups on the same model to preserve prompt cache.
- Mismatch: Tied to OnToken model slots; without a key it falls back to heuristics.

## How it works

Prompts (with recent context, capped by `jev.promptChars`) are classified by `typesafe/jev-latest`; the router maps the result to a slot and may promote (never downgrade) at most twice per turn. Jev integration: [`extensions/ontoken-auto/index.ts`](https://github.com/priaculun/ontoken-auto/blob/da5b59bda451160daf178858c1b0b6e1eca34e14/extensions/ontoken-auto/index.ts). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
pi install https://github.com/priaculun/ontoken-auto
# restart Pi, then:
/model ontoken/auto
```

## Limits and data handling

Conversation/tool text sent to Jev gets best-effort redaction; usage billed by TypeSafe and OnToken. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit da5b59bda451](https://github.com/priaculun/ontoken-auto/tree/da5b59bda451160daf178858c1b0b6e1eca34e14). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
