# Booksmith (Calibre ebooks to Plex audiobooks, with Jev-planned pauses)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Early Windows-first app that turns DRM-free Calibre ebooks into chaptered audiobooks narrated locally with Kokoro and imports them into Plex; optional Jev annotation proposes sentence pauses, reviews them in paragraph context and suggests pronunciations for ambiguous words.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/neuralcataccel/booksmith) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/neuralcataccel/booksmith#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; public source with no license file (no open-source license granted). Jev calls go to the decision endpoint you configure, with your own key and monthly spend limits in config. Checked 2026-10-25. |
| Jev evidence | [`jev_client.py`](https://github.com/neuralcataccel/booksmith/blob/667fdd31edb6c5e5b9d3bfd9ebba261623478633/jev_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/NeuralCatAccel/status/2114146837670052042)). |
| Maintainer | [neuralcataccel](https://github.com/neuralcataccel). Independently curated. |
| Format | Local web app and service (Python) |
| Platform and availability | Windows (service lock, scheduled task and Plex credential discovery are Windows-only); source release, not an installer. |
| Jev's role | Optional: when contextual pauses or pronunciation help are enabled, Jev picks pause boundaries and timing variants and suggests pronunciations; narration itself is local and Jev never rewrites the text. |
| Requirements | Windows, Python 3.12, ffmpeg, a Calibre library and a Plex Media Server; a Jev decision endpoint and your own key only for the optional annotation. |
| License | No LICENSE file on the reviewed commit on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Turn your own DRM-free ebooks into chaptered Plex audiobooks without a hosted TTS service.
- Let Jev plan natural pauses at paragraph level for a small cost.
- Mismatch: Windows-only, early and tied to the author's setup; no license file, so reuse terms are not granted.

## How it works

`jev_client.py` sends typed choice questions (`typesafe/jev-1.13`) to the `jev_url` you configure, validates every probability distribution, reserves budget before each send and does not retry after an uncertain billing result; failures keep the baseline timing. Integration evidence: [`jev_client.py`](https://github.com/neuralcataccel/booksmith/blob/667fdd31edb6c5e5b9d3bfd9ebba261623478633/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv && .venv\Scripts\pip install -r requirements.lock
python download_models.py
python configure_plex.py
python run.py   # then open http://127.0.0.1:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Creator's X post: [x.com/NeuralCatAccel/status/2114146837670052042](https://x.com/NeuralCatAccel/status/2114146837670052042)
- README: [github.com/neuralcataccel/booksmith#readme](https://github.com/neuralcataccel/booksmith#readme)

## Limits and data handling

With annotation on, ebook passages are sent to the decision endpoint you configure; the public config ships with it off and no provider URL. `configure_plex.py` creates or validates a dedicated Plex library; check the target first.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit 667fdd31edb6](https://github.com/neuralcataccel/booksmith/tree/667fdd31edb6c5e5b9d3bfd9ebba261623478633). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
