# pi-titlewise (Pi extension that auto-names sessions; optional TypeSafe Jev picks the title)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that proposes session titles from a short synopsis and, when the `typesafe` provider is logged in, asks TypeSafe Jev to pick among candidates (otherwise uses the first valid candidate).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Battlelamb/pi-titlewise) |
| Maintainer | [Battlelamb](https://github.com/Battlelamb). Independently curated. |
| Format | Pi coding-agent extension (TypeScript, MIT) |
| Requirements | Pi coding agent; optional TypeSafe login via `pi auth print-api-key --provider typesafe`. |
| License | [MIT](https://github.com/Battlelamb/pi-titlewise/blob/47e4c170bbc0ee1718e4518358fdc8dd755a3f0b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`selector.ts`](https://github.com/Battlelamb/pi-titlewise/blob/47e4c170bbc0ee1718e4518358fdc8dd755a3f0b/selector.ts) at the pinned commit. |

## When to use

- Auto-name Pi sessions without sending the raw transcript.
- Optionally let Jev pick among generated titles.
- Mismatch: titles work without Jev; Jev only selects among candidates.

## How it works

`selector.ts` POSTs to `https://api.typesafe.ai/v1/systemone` with model `jev-1.13.0` over the Pi typesafe provider key and returns a choice/keep/abstain decision. Integration evidence: [`selector.ts`](https://github.com/Battlelamb/pi-titlewise/blob/47e4c170bbc0ee1718e4518358fdc8dd755a3f0b/selector.ts).

## Get started

Install the extension into Pi per README; log in the typesafe provider if you want Jev selection.

```sh
git clone https://github.com/Battlelamb/pi-titlewise.git && cd pi-titlewise
# follow README Pi extension install
# optional: pi auth login --provider typesafe
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Battlelamb/pi-titlewise/blob/47e4c170bbc0ee1718e4518358fdc8dd755a3f0b/README.md](https://github.com/Battlelamb/pi-titlewise/blob/47e4c170bbc0ee1718e4518358fdc8dd755a3f0b/README.md)

## Limits and data handling

Only a short generated synopsis and candidate titles go to TypeSafe when Jev is enabled—never the raw transcript (per SECURITY.md).

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 47e4c170bbc0](https://github.com/Battlelamb/pi-titlewise/tree/47e4c170bbc0ee1718e4518358fdc8dd755a3f0b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
