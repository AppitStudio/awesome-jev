# Omni Mail by BradWMorris (read-only Gmail inbox that labels mail Action or No Action with Jev or local Liquid AI models)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local Mac app that syncs Gmail threads read-only into SQLite and labels the newest received message in each thread **Action** or **No Action**. You choose Jev (through TypeSafe or OpenRouter) or a local Liquid AI model (d1-2B or Omni 600M); an optional lab tests small weight edits of the local models on your own labelled mail.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bradwmorris/omni-mail) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/bradwmorris/omni-mail#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-25. |
| Jev evidence | [`omni_mail/jev.py`](https://github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/omni_mail/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/bradwmorris/status/2125453997704356292)). |
| Maintainer | [BradWMorris](https://github.com/bradwmorris). Independently curated. |
| Format | Python app with a React and TypeScript UI |
| Platform and availability | macOS (verified by the author on Apple silicon with macOS 26); a local Python server serves the React UI at 127.0.0.1:8765. |
| Jev's role | With a Jev provider selected, Omni Mail sends the sender, subject and up to 12,000 characters of body text to Jev and uses its probability with a 0.50 cutoff to label the message Action or No Action. |
| Requirements | Node.js 22 and Python 3.12 (uv); a Google Cloud OAuth client for Gmail read-only access; a TypeSafe or OpenRouter key for Jev, or local model weights from Hugging Face. |
| License | [Apache-2.0](https://github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/LICENSE) |

## When to use

- Triage a Gmail inbox into mail that needs action and mail that does not, while keeping Gmail as the place you reply.
- Compare Jev against small local models on your own labelled mail.
- Mismatch: if you want an app that replies, moves or deletes mail; Omni Mail is read-only.

## How it works

`omni_mail/jev.py` defines two hosted Jev providers: TypeSafe (`https://api.typesafe.ai/v1/systemone`, model `jev-1.14.0`) and OpenRouter's decisions API (`typesafe/jev-1.14`). Keys are stored locally per provider. Local models run on the Mac instead. Integration evidence: [`omni_mail/jev.py`](https://github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/omni_mail/jev.py).

## Get started

Build the web UI, set up the Python environment, then connect Gmail and a model in the app (see the install guide).

```sh
git clone https://github.com/bradwmorris/omni-mail
cd omni-mail
npm --prefix web ci && npm --prefix web run build
# then follow docs/install.md to create the uv environment and start the app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results and method: [github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/docs/experiment.md](https://github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/docs/experiment.md)
- Decision models: [github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/docs/models.md](https://github.com/bradwmorris/omni-mail/blob/8c33194761f2c2d430636e170e0bc3f518b6950b/docs/models.md)

## Limits and data handling

With Jev, message content goes to TypeSafe or to OpenRouter (a third-party host), whichever you pick, and each processed message is a paid call. The author's 400-email comparison (Jev 1.14 at 94.6% weighted score, 45 of 47 actions caught) is their own, on mail that also informed prompt development, so it is not an independent test.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 8c33194761f2](https://github.com/bradwmorris/omni-mail/tree/8c33194761f2c2d430636e170e0bc3f518b6950b). Inspected the README, install and models docs, and the Jev provider code at the pinned commit; the app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
