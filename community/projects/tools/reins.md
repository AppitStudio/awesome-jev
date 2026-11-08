# reins (drive your real browser from the CLI; `reins do` picks actions with TypeSafe Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

CLI plus browser extension to control your real browser; the optional `reins do` hands page state to TypeSafe Jev, which picks the operation and target element.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/karnstack/reins) |
| Maintainer | [karnstack](https://github.com/karnstack). Independently curated. |
| Format | TypeScript CLI + browser extension (MIT) |
| Requirements | Node, the reins extension, and a TypeSafe key for `reins do`. |
| License | [MIT](https://github.com/karnstack/reins/blob/acb5b225d2b046c1ea0467899e2da22fb43a57ca/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/cli/src/jev/client.ts`](https://github.com/karnstack/reins/blob/acb5b225d2b046c1ea0467899e2da22fb43a57ca/packages/cli/src/jev/client.ts) at the pinned commit. |

## When to use

- Automate simple actions in your own logged-in browser.
- Use typed Jev choices instead of a full LLM agent.
- Mismatch: page state is sent to TypeSafe; avoid sensitive pages.

## How it works

`packages/cli/src/jev/client.ts` asks Jev typed multiple-choice questions (which operation, which observed element) built in `space.ts`; other commands do not call TypeSafe. Integration evidence: [`packages/cli/src/jev/client.ts`](https://github.com/karnstack/reins/blob/acb5b225d2b046c1ea0467899e2da22fb43a57ca/packages/cli/src/jev/client.ts).

## Get started

Install per README and add your TypeSafe key in the CLI config or extension popup.

```sh
git clone https://github.com/karnstack/reins.git && cd reins
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Privacy notes: [github.com/karnstack/reins/blob/acb5b225d2b046c1ea0467899e2da22fb43a57ca/docs/PRIVACY.md](https://github.com/karnstack/reins/blob/acb5b225d2b046c1ea0467899e2da22fb43a57ca/docs/PRIVACY.md)

## Limits and data handling

Observed page state goes to TypeSafe on your account (see docs/PRIVACY.md).

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit acb5b225d2b0](https://github.com/karnstack/reins/tree/acb5b225d2b046c1ea0467899e2da22fb43a57ca). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
