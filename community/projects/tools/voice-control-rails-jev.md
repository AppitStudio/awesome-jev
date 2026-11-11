# voice_control (voice and typed commands for Rails, matched by Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rails engine that adds a voice and typed command widget to your app: you define commands in Ruby, and Jev picks which allowed command (or discovered page action) a free-form phrase means, while the server checks arguments and permissions before anything runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/igorkasyanchuk/voice_control) |
| Maintainer | [igorkasyanchuk](https://github.com/igorkasyanchuk). Independently curated. |
| Format | Rails engine gem (Ruby, MIT) |
| Requirements | Rails 8.x, Ruby 3.2+, a shared cache in production, and a server-side `JEV_API_KEY` for free-form matching. |
| License | [MIT](https://github.com/igorkasyanchuk/voice_control/blob/0faab0b46a9fbc449020c5b729abc5a57ed1d648/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/voice_control/jev.rb`](https://github.com/igorkasyanchuk/voice_control/blob/0faab0b46a9fbc449020c5b729abc5a57ed1d648/lib/voice_control/jev.rb) at the pinned commit. |

## When to use

- Let users say or type shortcuts to actions your Rails app already has.
- Keep authorization in Ruby while a typed model maps phrases to commands.
- Mismatch: unreleased; commands run immediately once arguments are complete.

## How it works

`lib/voice_control/jev.rb` posts to `https://api.typesafe.ai/v1/systemone` with the transcript and available commands as choices (at most 254 commands per request); the README says exact help selections work without a key and a confidence score is a routing signal, not an authorization check. Integration evidence: [`lib/voice_control/jev.rb`](https://github.com/igorkasyanchuk/voice_control/blob/0faab0b46a9fbc449020c5b729abc5a57ed1d648/lib/voice_control/jev.rb).

## Get started

Add the gem from a local build (not on RubyGems yet), run the installer, set the key in the server environment and restart Rails.

```sh
gem "voice_control"   # local build until released
bundle install --local
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/igorkasyanchuk/voice_control/blob/0faab0b46a9fbc449020c5b729abc5a57ed1d648/README.md](https://github.com/igorkasyanchuk/voice_control/blob/0faab0b46a9fbc449020c5b729abc5a57ed1d648/README.md)
- Demo video: [youtu.be/Zz1Ibx8R7WI](https://youtu.be/Zz1Ibx8R7WI)

## Limits and data handling

The transcript, page context (URL/path by default) and command descriptions go to TypeSafe; with page discovery, control labels and IDs too. Field values, Ruby code and page HTML are not sent per the README.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 0faab0b46a9f](https://github.com/igorkasyanchuk/voice_control/tree/0faab0b46a9fbc449020c5b729abc5a57ed1d648). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
