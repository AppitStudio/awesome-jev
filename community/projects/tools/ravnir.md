# Ravnir (persistent AI agents on your own server with one reviewable shared memory, and optional Jev for browser actions)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Self-hosted agent workspace in public beta: give each agent a job, a model and its own browser, let it keep working when you close the tab and run routines on your server, and have what it learns land in a shared vault of Markdown notes in git that you can read, review and revert. Browser and desktop use can choose actions with the agent's model, a quick model, or Jev as an optional speed-up.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ravnir-ai/ravnir) |
| Maintainer | [ravnir-ai](https://github.com/ravnir-ai). Independently curated. |
| Format | Node.js server with web UI |
| Requirements | A Linux server, your model provider keys; a TypeSafe API key only for Jev. |
| License | [MIT](https://github.com/ravnir-ai/ravnir/blob/461e3c4bd76eb796124d2f8c172299823a39e566/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.js`](https://github.com/ravnir-ai/ravnir/blob/461e3c4bd76eb796124d2f8c172299823a39e566/server/jev.js) at the pinned commit. |

## When to use

- Run long-lived agents with memory you can audit and undo.
- Mismatch: beta (0.1.0); Jev is optional.

## How it works

`server/jev.js` posts the current page options to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`, overridable) when `RAVNIR_TYPESAFE_KEY` is set, so Jev picks the next click, key or field. Integration evidence: [`server/jev.js`](https://github.com/ravnir-ai/ravnir/blob/461e3c4bd76eb796124d2f8c172299823a39e566/server/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSL https://ravnir.dev/install.sh | bash   # Linux install script from the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Site and walkthrough: [ravnir.dev](https://ravnir.dev)
- README: [github.com/ravnir-ai/ravnir#readme](https://github.com/ravnir-ai/ravnir#readme)

## Limits and data handling

With Jev on, browser and desktop action options go to TypeSafe. Notes stay in your git vault.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 461e3c4bd76e](https://github.com/ravnir-ai/ravnir/tree/461e3c4bd76eb796124d2f8c172299823a39e566). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
