# persona-drive by Zovos AI (persona-based browser testing where Jev decides what a described person would do next)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser-testing tool: you describe a person and what they came to do, Jev picks that person's next step on each screen, Playwright carries it out, and each run is recorded as video, screenshots, a step log and a report of where the persona got confused, stuck or hit an error. No scripted paths. Ships with a sample site, example personas, Docker images and a per-run spending cap.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zovos-ai-inc/persona-drive) |
| Maintainer | [Zovos AI](https://github.com/zovos-ai-inc) (zovos-ai-inc; commits by Adam Swenson). Independently curated. |
| Format | Node.js CLI + npm package (`@zovos-ai-inc/persona-drive`) |
| Requirements | Node 22+ and Playwright Chromium, or Docker; a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/zovos-ai-inc/persona-drive/blob/7ee7ec4d6969cd42a75e9ba5f24d814054c90bb8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/zovos-ai-inc/persona-drive/blob/7ee7ec4d6969cd42a75e9ba5f24d814054c90bb8/src/jev.ts) at the pinned commit. |

## When to use

- Product and QA teams who want to see where a realistic first-time user gets lost on a site, without writing test scripts.
- Mismatch: deterministic regression tests; the path changes with Jev's choices.

## How it works

`src/jev.ts` wraps the official `@typesafe-ai/sdk` client and sends one System One request per step, with all `noul` and `choice` questions about the current screen in a single call. Each call is logged to `jev-calls.jsonl`, state is capped at 20k tokens, and the run stops once its USD budget is reached. Cookies, bearer tokens, JWTs, presigned URLs and email addresses are redacted before anything is sent to Jev or written to disk. Integration evidence: [`src/jev.ts`](https://github.com/zovos-ai-inc/persona-drive/blob/7ee7ec4d6969cd42a75e9ba5f24d814054c90bb8/src/jev.ts).

## Get started

Run the bundled sample with Docker, or install from npm into your own project.

```sh
git clone https://github.com/zovos-ai-inc/persona-drive && cd persona-drive
echo TYPESAFE_API_KEY=... > .env
docker compose run --rm persona-drive run --target targets/sample-app.yaml --persona personas/first-time-buyer.yaml
# or: npm install -D @zovos-ai-inc/persona-drive
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo runs: [github.com/zovos-ai-inc/persona-drive/tree/main/demo](https://github.com/zovos-ai-inc/persona-drive/tree/main/demo)
- Example personas: [github.com/zovos-ai-inc/persona-drive/tree/main/personas](https://github.com/zovos-ai-inc/persona-drive/tree/main/personas)

## Limits and data handling

Page text from the site under test goes to TypeSafe on every step (after the redaction above). Writing actions such as submitting forms need `--allow-writes`. Point it only at sites you are allowed to test.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 7ee7ec4d6969](https://github.com/zovos-ai-inc/persona-drive/tree/7ee7ec4d6969cd42a75e9ba5f24d814054c90bb8). Inspected the README, LICENSE, `src/jev.ts` and `package.json` at the pinned commit and confirmed `@zovos-ai-inc/persona-drive` 0.1.0 on npm; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
