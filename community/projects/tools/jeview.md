# Jeview (local gateway and live visualizer that sits between your code and TypeSafe and draws every Jev call on a map)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial local visualizer for Jev: point your client at `127.0.0.1:4777/v1/systemone`, and Jeview forwards each request to TypeSafe with your key, stores every call in local SQLite and shows the calls and answers growing on a live map. Supports grouping by label, linking a call to the answer that triggered it, and two demo apps (Pixel Knight and a support-inbox triage).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/toasterman234/jeview) |
| Maintainer | [toasterman234](https://github.com/toasterman234). Independently curated. |
| Format | Node.js 24 local server with a browser viewer (no dependencies) |
| Requirements | Node 24+ and a TypeSafe API key entered in the viewer. |
| License | [MIT](https://github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jeview.ts`](https://github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/src/jeview.ts) at the pinned commit. |

## When to use

- Debug and explain what a Jev-driven agent is deciding step by step.
- Share a visual record of Jev calls without changing your client code.
- Mismatch: the demos make real Jev calls (about ten cents an hour per the README).

## How it works

`src/jeview.ts` proxies `POST /v1/systemone` to `https://api.typesafe.ai/v1/systemone`, answers nothing itself and records each event for the viewer. Integration evidence: [`src/jeview.ts`](https://github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/src/jeview.ts).

## Get started

From the upstream README (not run on the review host):

```sh
./launch.sh   # or npm start; viewer at http://127.0.0.1:4777/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with demos and request headers: [github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/README.md](https://github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/README.md)
- llms.txt for agents: [github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/llms.txt](https://github.com/toasterman234/jeview/blob/770059e463ea3f309380fa71e8d966e46d2edaf0/llms.txt)

## Limits and data handling

Calls and answers are stored in a local SQLite file, including request text; the project is independent and not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 770059e463ea](https://github.com/toasterman234/jeview/tree/770059e463ea3f309380fa71e8d966e46d2edaf0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
