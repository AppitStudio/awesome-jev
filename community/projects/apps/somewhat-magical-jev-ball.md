# Somewhat Magical Jev Ball (a Magic 8 Ball whose answer comes from twelve Jev judgments about your question)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Type a yes/no question and shake the 3D ball: twelve independent Jev yes/no judgments (tone, whether it is about a fact, whether the answer is true, which way it leans, how certain) are combined in code into one of the twenty classic answers, and safe questions are relayed live to other visitors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/raunaqgupta/somewhat-magical-jev-ball) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://somewhatmagicaljevball.com) |
| Pricing and access | Free to use at somewhatmagicaljevball.com (rate limited to 20 requests per minute per IP); source has no license file, so reuse terms are not granted. Checked 2026-11-22. |
| Jev evidence | [`lib/decide.js`](https://github.com/raunaqgupta/somewhat-magical-jev-ball/blob/ca394a7bc71a5fc85f7a8df34f241c4d4138202e/lib/decide.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [raunaqgupta](https://github.com/raunaqgupta). Independently curated. |
| Format | Web app (HTML/CSS/JS + Cloudflare Worker) |
| Platform and availability | Web (live site); Cloudflare Worker back end. |
| Jev's role | One Jev request with twelve parallel `noul` questions per ask; code maps the probabilities to an answer and hides questions that look personal. |
| Requirements | Nothing to use the live site; to deploy your own, a Cloudflare account with Workers AI and a TypeSafe key added to an AI Gateway (BYOK). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- A playful, visible demo of combining many small Jev judgments into one answer.
- Mismatch: real advice; it is a toy.

## How it works

`lib/decide.js` asks the twelve `noul` questions in one request; `src/worker.js` calls Jev as `typesafe/jev` in Cloudflare Workers AI's catalog through the `AI` binding and an AI Gateway, so the Worker holds no TypeSafe key itself. Integration evidence: [`lib/decide.js`](https://github.com/raunaqgupta/somewhat-magical-jev-ball/blob/ca394a7bc71a5fc85f7a8df34f241c4d4138202e/lib/decide.js).

## Get started

Use the live site, or run it locally with Wrangler.

```sh
git clone https://github.com/raunaqgupta/somewhat-magical-jev-ball && cd somewhat-magical-jev-ball
npm install
npm start   # wrangler dev, http://localhost:3210
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [somewhatmagicaljevball.com](https://somewhatmagicaljevball.com)
- README: [github.com/raunaqgupta/somewhat-magical-jev-ball/blob/ca394a7bc71a5fc85f7a8df34f241c4d4138202e/README.md](https://github.com/raunaqgupta/somewhat-magical-jev-ball/blob/ca394a7bc71a5fc85f7a8df34f241c4d4138202e/README.md)

## Limits and data handling

Questions are sent to Jev through Cloudflare; questions judged non-personal are shown to other visitors in the live feed, so do not type private information. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit ca394a7bc71a](https://github.com/raunaqgupta/somewhat-magical-jev-ball/tree/ca394a7bc71a5fc85f7a8df34f241c4d4138202e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
