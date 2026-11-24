# Jev Comment Triage by Per Søderlind (WordPress plugin that moderates comments with Jev in the background: relevance, spam and abuse)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

For every comment Jev answers three questions in the context of its post (on-topic, spam, abusive); plain PHP turns the answers into a decision and only confident answers act automatically, the rest are held for a person. Calls run asynchronously so commenting stays fast. On the author's 60 labelled comments Jev routed all 60 correctly versus 24 for the WordPress AI plugin's moderation with an OpenAI model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/soderlind/jev-comment-triage) |
| Maintainer | [Per Søderlind](https://github.com/soderlind). Independently curated. |
| Format | WordPress plugin (PHP 8.3, v2.3.0) |
| Requirements | WordPress 6.8+, PHP 8.3, and the AI Provider for Jev plugin configured with a TypeSafe API key. |
| License | [GPL-2.0-or-later (declared in the plugin header and readme.txt; no separate LICENSE file)](https://github.com/soderlind/jev-comment-triage/blob/e0c8e2398da0865c1b91dbb2005594a8e66392eb/jev-comment-triage.php) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`includes/class-assessment.php`](https://github.com/soderlind/jev-comment-triage/blob/e0c8e2398da0865c1b91dbb2005594a8e66392eb/includes/class-assessment.php) at the pinned commit. |

## When to use

- Moderate WordPress comments without slowing down submission, holding uncertain cases for a human.
- Mismatch: sites that cannot send comment data to a third-party API.

## How it works

`includes/class-assessment.php` builds the three Jev questions and normalizes the answers; requests go through the AI Provider for Jev plugin, and results are stored as comment meta and shown in a Jev column. Integration evidence: [`includes/class-assessment.php`](https://github.com/soderlind/jev-comment-triage/blob/e0c8e2398da0865c1b91dbb2005594a8e66392eb/includes/class-assessment.php).

## Get started

Install and configure AI Provider for Jev, then install and activate this plugin.

```sh
# wp-content/plugins
git clone https://github.com/soderlind/jev-comment-triage.git
wp plugin activate jev-comment-triage
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with benchmark: [github.com/soderlind/jev-comment-triage/blob/e0c8e2398da0865c1b91dbb2005594a8e66392eb/README.md](https://github.com/soderlind/jev-comment-triage/blob/e0c8e2398da0865c1b91dbb2005594a8e66392eb/README.md)

## Limits and data handling

Comment text, post content and (unless disabled) the commenter's name, email and URL are sent to TypeSafe; the plugin registers a privacy-policy snippet. The 60-comment benchmark is the author's own.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit e0c8e2398da0](https://github.com/soderlind/jev-comment-triage/tree/e0c8e2398da0865c1b91dbb2005594a8e66392eb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
