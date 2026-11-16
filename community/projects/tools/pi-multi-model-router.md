# Pi multi-model router by teknologist (virtual Pi models that ask Jev which physical model and thinking level each turn should use)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding agent extension that adds virtual models. When one is selected, the router asks the Jev classifier (`typesafe/jev-latest`) to match each new user turn to one of your described routes (quick, balanced, deep and so on), each naming a physical model and thinking level from your Pi catalog. Tool continuations and retries keep their target, your selected model is never changed, and a status line shows each physical model's share of output tokens and speed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/teknologist/pi-multi-model-router) |
| Maintainer | [teknologist](https://github.com/teknologist). Independently curated. |
| Format | Pi agent extension (TypeScript, MIT) |
| Requirements | Pi 1.5.0+, Node.js 22.19+, and TypeSafe credentials registered in Pi for `typesafe/jev-latest` (`/login` or `TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/teknologist/pi-multi-model-router/blob/a5cfee0c6318474102cd2be77c22ecf04f96a35f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/router.ts`](https://github.com/teknologist/pi-multi-model-router/blob/a5cfee0c6318474102cd2be77c22ecf04f96a35f/src/router.ts) at the pinned commit. |

## When to use

- Mix local and hosted models in one Pi session, sending each turn to the model it needs.
- Mismatch: other coding agents; it uses Pi's extension API.

## How it works

`src/router.ts` looks up the `typesafe`/`jev-latest` classifier in Pi's model registry and asks it to choose the route whose description fits the current request, treating recent conversation as data. Integration evidence: [`src/router.ts`](https://github.com/teknologist/pi-multi-model-router/blob/a5cfee0c6318474102cd2be77c22ecf04f96a35f/src/router.ts).

## Get started

Clone, copy the example config and load the extension in Pi.

```sh
git clone https://github.com/teknologist/pi-multi-model-router && cd pi-multi-model-router && npm ci
mkdir -p ~/.pi/agent/extensions/pi-multi-model-router
cp examples/config.toml ~/.pi/agent/extensions/pi-multi-model-router/config.toml
pi -e ./index.ts    # then /model -> a virtual model
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/teknologist/pi-multi-model-router/blob/a5cfee0c6318474102cd2be77c22ecf04f96a35f/README.md](https://github.com/teknologist/pi-multi-model-router/blob/a5cfee0c6318474102cd2be77c22ecf04f96a35f/README.md)

## Limits and data handling

The current request and recent text go to TypeSafe through Pi's classifier on your key. Route descriptions are yours to tune.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit a5cfee0c6318](https://github.com/teknologist/pi-multi-model-router/tree/a5cfee0c6318474102cd2be77c22ecf04f96a35f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
