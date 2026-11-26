# Note Triage for WooCommerce by Hamza Ahmad Aslam (WordPress plugin that sorts checkout notes into gifts, delivery instructions, questions, complaints and fraud signals with Jev)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

WooCommerce plugin that sends each order's customer note to Jev and sorts it into gift message, delivery instruction, question, complaint, fraud signal or other, with an urgency score from 0 to 3. Confident answers become order meta, a private order note and an orders-list filter; uncertain ones go to a "Needs review" list with the two likeliest categories.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hamzaahmadaslam/woo-note-triage) |
| Maintainer | [Hamza Ahmad Aslam](https://github.com/hamzaahmadaslam). Independently curated. |
| Format | WordPress / WooCommerce plugin (PHP) |
| Requirements | WordPress 6.5+, WooCommerce 8.0+, PHP 8.1+ (HPOS or posts storage, classic or block checkout) and a TypeSafe API key. |
| License | [MIT](https://github.com/hamzaahmadaslam/woo-note-triage/blob/f402d4e4b96d1c129df17134f0c346b946842329/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`includes/class-jev-client.php`](https://github.com/hamzaahmadaslam/woo-note-triage/blob/f402d4e4b96d1c129df17134f0c346b946842329/includes/class-jev-client.php) at the pinned commit. |

## When to use

- Shops where most order notes are routine but a complaint or a "ship it to my forwarder" note must not be missed.
- Mismatch: stores that cannot send note text to TypeSafe, or that want automatic actions; a fraud signal is only a flag for a person.

## How it works

`includes/class-jev-client.php` posts one request per note to `https://api.typesafe.ai/v1/systemone` through the WordPress HTTP API with two fixed questions: a `category` choice and an `urgency` score. Below the confidence threshold (0.80 by default) the order gets no category. The plugin never changes order status, writes to the customer, cancels or refunds. Integration evidence: [`includes/class-jev-client.php`](https://github.com/hamzaahmadaslam/woo-note-triage/blob/f402d4e4b96d1c129df17134f0c346b946842329/includes/class-jev-client.php).

## Get started

Install from the GitHub archive with WP-CLI, activate it, then save your TypeSafe key in the plugin settings.

```sh
wp plugin install https://github.com/hamzaahmadaslam/woo-note-triage/archive/refs/heads/main.zip --activate
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example request body: [github.com/hamzaahmadaslam/woo-note-triage/blob/f402d4e4b96d1c129df17134f0c346b946842329/examples/request.json](https://github.com/hamzaahmadaslam/woo-note-triage/blob/f402d4e4b96d1c129df17134f0c346b946842329/examples/request.json)

## Limits and data handling

Only the cleaned note leaves the site: email addresses and long digit runs are masked, invisible characters removed and at most 2,000 characters sent; no name, address, product or other order data (per the README). Notes are customer-written, so wording can steer answers; check fraud and complaint flags yourself.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit f402d4e4b96d](https://github.com/hamzaahmadaslam/woo-note-triage/tree/f402d4e4b96d1c129df17134f0c346b946842329). Inspected the README, LICENSE and the Jev client and question classes at the pinned commit; the plugin was not installed on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
