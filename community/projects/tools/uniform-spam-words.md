# Spam Words Guard for Kirby Uniform by tearoom1 (contact-form spam guard that asks Jev about the close calls)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Spam protection plugin for the Kirby CMS form plugin Uniform. Weighted word lists, link counting and template signals decide the clear cases on your own server. An optional AI check sends only borderline messages (or, in `always` mode, every message) to a decision model on OpenRouter, Jev by default: it rejects spam just below the threshold and lets genuine messages just above it through. A failed or missing call never rejects a message; the word score decides as if the check were off.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tearoom1/uniform-spam-words) |
| Maintainer | [tearoom1](https://github.com/tearoom1). Independently curated. |
| Format | Kirby CMS plugin (PHP, Composer or Git submodule, MIT) |
| Requirements | Kirby with the Uniform plugin; an OpenRouter key only for the optional AI check. |
| License | [MIT](https://github.com/tearoom1/uniform-spam-words/blob/341b87e8637b2746c516691c167d2f6dcfacae45/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/guards/SpamAiCheck.php`](https://github.com/tearoom1/uniform-spam-words/blob/341b87e8637b2746c516691c167d2f6dcfacae45/src/guards/SpamAiCheck.php) at the pinned commit. |

## When to use

- Cut contact-form spam on a Kirby site while keeping most messages on your own server.
- Mismatch: sites not built on Kirby with Uniform.

## How it works

`src/guards/SpamAiCheck.php` asks OpenRouter's decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with `typesafe/jev-1.14` by default whether a message is spam; `index.php` holds the `ai.*` options (off by default). Integration evidence: [`src/guards/SpamAiCheck.php`](https://github.com/tearoom1/uniform-spam-words/blob/341b87e8637b2746c516691c167d2f6dcfacae45/src/guards/SpamAiCheck.php).

## Get started

Install with Composer, call the guard in your form controller, and enable the AI check in `config.php` if you want it.

```sh
composer require tearoom1/uniform-spam-words
# controller: $form->spamWordsGuard();
# config.php: 'tearoom1.uniform-spam-words' => ['ai.enabled' => true, 'ai.apiKey' => 'sk-or-v1-...']
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tearoom1/uniform-spam-words/blob/341b87e8637b2746c516691c167d2f6dcfacae45/README.md](https://github.com/tearoom1/uniform-spam-words/blob/341b87e8637b2746c516691c167d2f6dcfacae45/README.md)

## Limits and data handling

With the AI check on, only the checked fields and your `ai.context` go to OpenRouter and the model provider; the message can still contain personal data, so the README advises mentioning it in your privacy policy. The README measures about US$0.00002 per checked message (October 2026).

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 341b87e8637b](https://github.com/tearoom1/uniform-spam-words/tree/341b87e8637b2746c516691c167d2f6dcfacae45). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
