# ifseen by Krish Joshi (plain-English triggers for your screen, camera and mic, judged by decision models such as Jev)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Write rules such as "the washing machine's display shows the cycle has finished"; ifseen grabs a frame or audio clip every few seconds, asks all rules at once and fires actions (ntfy, MQTT, speech, webhooks) when one comes true.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KrishJoshi/ifseen) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://krishj.com/ifseen/) |
| Pricing and access | Free MIT source and standalone binaries; hosted decision models are billed to your own TypeSafe, Google or Azure key (a local SigLIP provider is free and offline). Checked 2026-11-20. |
| Jev evidence | [`src/ifseen/providers/systemone.py`](https://github.com/KrishJoshi/ifseen/blob/c58abace0f1ef8d0afce61bf3a7d017c697dea59/src/ifseen/providers/systemone.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [KrishJoshi](https://github.com/KrishJoshi). Independently curated. |
| Format | Python CLI and server (MIT) |
| Platform and availability | macOS, Windows and Linux CLI, Docker image, Home Assistant add-on and a JS/TS client. |
| Jev's role | One of several supported providers: with the `jev` provider each rule becomes a yes/no question about the current frame, and the probability gates the action. |
| Requirements | A TypeSafe API key for the Jev provider (or keys for Gemini Decision / Azure, or the local provider); a screen, camera, microphone, snapshot URL or video source. |
| License | [MIT](https://github.com/KrishJoshi/ifseen/blob/c58abace0f1ef8d0afce61bf3a7d017c697dea59/LICENSE) |

## When to use

- Turn things with no API (a dumb appliance display, a legacy HMI screen, a camera view) into events with plain-English rules.
- Mismatch: safety-critical alarms; model judgments can be wrong and the binaries are not signed yet.

## How it works

`src/ifseen/providers/systemone.py` speaks the System One wire format to TypeSafe's `https://api.typesafe.ai/v1/systemone` (and to Microsoft-Decision or self-hosted Jev-compatible servers), sending every rule as a `noul` question about the frame and reading back per-rule probabilities; rules can require several consecutive hits before firing. Integration evidence: [`src/ifseen/providers/systemone.py`](https://github.com/KrishJoshi/ifseen/blob/c58abace0f1ef8d0afce61bf3a7d017c697dea59/src/ifseen/providers/systemone.py).

## Get started

Install a binary or the Python package, set your key and try a rule.

```sh
pipx install "ifseen[all]"
export TYPESAFE_API_KEY=...
ifseen "a pan is cooking on a lit hob and nobody is in the kitchen" --camera 0 --ntfy my-phone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/KrishJoshi/ifseen/blob/c58abace0f1ef8d0afce61bf3a7d017c697dea59/README.md](https://github.com/KrishJoshi/ifseen/blob/c58abace0f1ef8d0afce61bf3a7d017c697dea59/README.md)
- Website: [krishj.com/ifseen/](https://krishj.com/ifseen/)
- Benchmarks: [github.com/KrishJoshi/ifseen/tree/c58abace0f1ef8d0afce61bf3a7d017c697dea59/benchmarks](https://github.com/KrishJoshi/ifseen/tree/c58abace0f1ef8d0afce61bf3a7d017c697dea59/benchmarks)

## Limits and data handling

Frames or audio clips are sent to the chosen provider every interval, so continuous watching has ongoing cost and privacy implications; the local provider keeps data on the machine. The README's accuracy tables come from the author's AI-generated test scenes.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit c58abace0f1e](https://github.com/KrishJoshi/ifseen/tree/c58abace0f1ef8d0afce61bf3a7d017c697dea59). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
