# Vertika Command

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that runs your browser from spoken or typed English commands (open a site, search, scroll, find on page, click, type, switch tabs). You pick the model: Laya in the browser or on your own server for free, or TypeSafe Jev online with your own key for speed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://command.vertika.io) |
| Tags | `Closed source` · `Free` · `BYOK` |
| Product homepage | [command.vertika.io](https://command.vertika.io/) · [Chrome Web Store](https://chromewebstore.google.com/detail/vertika-command-run-your/lhjeopjappljkcdgjhiafhobjafmmhmh) |
| Pricing and access | Free on the Chrome Web Store (0.7.0, checked 2026-10-19). The default Laya model is free after a one-time download of about 528 MB. The Jev option needs your own TypeSafe or OpenRouter key; the site estimates about $0.0002 per command, billed by your provider. The free plan holds 10 shortcuts and commands. |
| Jev evidence | Product site copy: "Jev online with your own key", with a Jev vs. Laya comparison (Jev runs online via OpenRouter or TypeSafe, about 0.2 to 0.3 s per command). Submitted through the JevList share form (issue [#1780](https://github.com/AppitStudio/awesome-jev/issues/1780)). Extension code was not inspected and live Jev calls were not captured on the review host. |
| Disclosure | Closed source; Jev use is a product claim from the live site and the submission, not independently observed API traffic. AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. |
| Maintainer | [Vertika.io](https://vertika.io) (Chrome Web Store publisher). Independently curated. |
| Format | Chrome extension |
| Platform and availability | Chrome only · English commands · [demo video](https://youtu.be/YIGZAPhljC4) |
| Jev's role | Optional fast cloud model: Jev turns a spoken or typed command plus page context into the browser action to run. |
| Requirements | Chrome; microphone for voice (typing works too); a TypeSafe or OpenRouter key for the Jev option, or about 1 GB of memory for in-browser Laya. |
| License | Proprietary; no public source. The Chrome Web Store build is free. |

## When to use

- Drive everyday browsing hands-free, or by short typed commands, with your own saved shortcuts.
- Mismatch: Chrome and English only; closed source, so you cannot audit how page details are sent.

## How it works

You say or type a command; the extension sends it with page context to the model you chose and runs the returned browser action. With Jev, the site says your command, the page address, title and element names, open tab titles, and recent commands go to your chosen provider. (Summarized from [command.vertika.io](https://command.vertika.io/); not reproduced here.)

## Get started

From the product site (not run on the review host): install Vertika Command from the Chrome Web Store, allow the microphone, then either download the built-in Laya model or add your TypeSafe or OpenRouter key to use Jev, and say a command like "open gmail".

## Limits and data handling

On the Jev option, command text and page details go to TypeSafe or OpenRouter. Speech-to-text uses the browser's online speech service for both models. The site says there is no Vertika server, analytics, or ads. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) from the live product site and Chrome Web Store listing (version 0.7.0). No public source to inspect; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
