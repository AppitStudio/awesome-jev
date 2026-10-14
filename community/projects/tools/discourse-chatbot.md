# discourse-chatbot

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

The original Discourse AI Chatbot plugin; optional System One settings (default model `jev-latest`) let Jev decide whether a question belongs to the community and which tools the bot should use.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/merefield/discourse-chatbot) |
| Maintainer | [merefield](https://github.com/merefield). Independently curated. |
| Format | Discourse plugin (Ruby) |
| Requirements | Self-hosted Discourse; LLM provider key; System One model, URL and key for the Jev path. |
| License | [GPL-3.0](https://github.com/merefield/discourse-chatbot/blob/58466848370f10656c99e2d8d72b6f381a8421ff/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/discourse_chatbot/system_one_client.rb`](https://github.com/merefield/discourse-chatbot/blob/58466848370f10656c99e2d8d72b6f381a8421ff/lib/discourse_chatbot/system_one_client.rb) at the pinned commit. |

## When to use

- Run a community support bot in topics, PMs and chat grounded in your forum content.
- Let Jev gate off-topic questions and pick tools instead of example-embedding matching.
- Mismatch: the System One path is optional; the bot itself is LLM-driven.

## How it works

When the System One model, URL and key are configured, a client sends the question to Jev for forum-scope and tool-selection judgments; otherwise the plugin falls back to example-based embedding matching. Integration evidence: [`lib/discourse_chatbot/system_one_client.rb`](https://github.com/merefield/discourse-chatbot/blob/58466848370f10656c99e2d8d72b6f381a8421ff/lib/discourse_chatbot/system_one_client.rb).

## Get started

Install like any Discourse plugin (summarized; not run on the review host):

```sh
cd /var/discourse
# add the plugin's git URL to app.yml hooks per the Discourse plugin guide, then
./launcher rebuild app
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Settings: `chatbot_system_one_model` (default `jev-latest`) documented in the README.

## Limits and data handling

Forum questions are sent to the configured System One endpoint (TypeSafe for Jev) and LLM providers, billed to your keys.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 58466848370f](https://github.com/merefield/discourse-chatbot/tree/58466848370f10656c99e2d8d72b6f381a8421ff). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
