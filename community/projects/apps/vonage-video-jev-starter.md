# Vonage Video API x Jev support demo

[All projects](../README.md) · [Web apps](README.md#web-apps)

Vonage Community demo where Jev reads a customer's chat messages for sentiment and frustration and escalates to a live Vonage video call with a human agent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Vonage-Community/demo-video-javascript-jev-starter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Vonage-Community/demo-video-javascript-jev-starter#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-15. |
| Jev evidence | [`server.js`](https://github.com/Vonage-Community/demo-video-javascript-jev-starter/blob/4b3d69f9c8645146274b8d8aa1a6122a3201b7c8/server.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Vonage-Community](https://github.com/Vonage-Community). Independently curated. |
| Format | Node.js web demo |
| Platform and availability | Web (self-hosted Node.js demo) |
| Jev's role | Jev scores frustration per message; code decides when to escalate to video. |
| Requirements | Node.js, Vonage Video API credentials, TypeSafe API key. |
| License | [Apache-2.0](https://github.com/Vonage-Community/demo-video-javascript-jev-starter/blob/4b3d69f9c8645146274b8d8aa1a6122a3201b7c8/LICENSE) |

## When to use

- Prototype frustration-based escalation from chat to video support.
- See Vonage Video signaling notify an employee dashboard.
- Mismatch: a starter demo, not a production support desk.

## How it works

Each chat message is sent to Jev with sentiment and frustration questions; above a threshold the server signals the employee dashboard and starts a video session, otherwise the message continues in chat. Integration evidence: [`server.js`](https://github.com/Vonage-Community/demo-video-javascript-jev-starter/blob/4b3d69f9c8645146274b8d8aa1a6122a3201b7c8/server.js).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
node setup.js
node server.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Blog post: [developer.vonage.com/en/blog/from-frustrated-chats-to-live-video-support-with-jev-and-vonage](https://developer.vonage.com/en/blog/from-frustrated-chats-to-live-video-support-with-jev-and-vonage)

## Limits and data handling

Chat messages go to TypeSafe and video sessions to Vonage, billed to your accounts.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 4b3d69f9c864](https://github.com/Vonage-Community/demo-video-javascript-jev-starter/tree/4b3d69f9c8645146274b8d8aa1a6122a3201b7c8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
