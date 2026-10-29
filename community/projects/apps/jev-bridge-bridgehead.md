# Jev · Bridge by Bridgehead (hosted MCP connector that puts Jev's choices, scores and yes/no checks in Claude, ChatGPT and other MCP apps)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Hosted connector you add once to claude.ai, ChatGPT, Claude Code, Codex or another MCP app: sign in, store your own Jev key in Bridgehead's vault, and Jev's choice, score and yes/no questions become tools, plus ranking of up to 50 candidates, questions over files (with Gemini transcribing recordings, videos and scans), a three-way allow/ask/block gate for agents, people search (is this the person you mean?), ready-made triage, screening, writing-review, claim-check and routing recipes, extraction and saved question sets. Every answer is kept with its confidence so you can mark it right or wrong.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://jevbridge.fyi/) |
| Tags | `Closed source` · `Pricing unverified` · `BYOK` |
| Product homepage | [jevbridge.fyi](https://jevbridge.fyi/) |
| Pricing and access | Sign-in at [connect.bridgehead.cloud](https://connect.bridgehead.cloud/c/jevbridge) with your own TypeSafe Jev key (and optionally Gemini, Exa or Serper keys); Jev usage is billed to your key. Bridgehead's own pricing was not published on the pages reviewed. Checked **2026-10-29**. |
| Jev evidence | The [product page](https://jevbridge.fyi/) and [connector page](https://jevbridge.fyi/key) describe Jev questions run on your key, including Jev 1.14 picture questions (beta); the connector page states "Not made by TypeSafe; it connects to TypeSafe's Jev API with your own key." Implementation was **not** inspected (no public source); no live calls were made on the review host. |
| Disclosure | Closed source. Capabilities are vendor descriptions, not independently tested. Not made by or affiliated with TypeSafe. AI-assisted catalog review; no affiliation with the vendor. Listing is not an endorsement. Discovered via X ([post](https://x.com/roguevoice/status/2115675183402901703)). |
| Maintainer | Bridgehead by NoIfs ([bridgehead.cloud](https://bridgehead.cloud/)). Independently curated. |
| Format | Hosted MCP connector with a web account page. |
| Platform and availability | Any MCP client that supports remote connectors (claude.ai, ChatGPT, Claude Code, Codex); pages returned HTTP 200 on review. |
| Jev's role | Vendor description: answers every choice, score, yes/no, ranking and gate question; Gemini handles transcription and pictures Jev cannot take. |
| Requirements | A Bridgehead sign-in, a TypeSafe Jev key, and an MCP-capable assistant. |
| License | Proprietary hosted service; no public repository. |

## When to use

- Ask Jev typed questions from a chat assistant or coding agent without running a local MCP server.
- Mismatch: your Jev key is held in a third-party vault; picture questions are beta.

## How it works

Per the product page: the connector exposes Jev's question types as MCP tools, with Bridgehead code around them (ranking, a two-stage path for long files, a gate whose thresholds turn four Jev answers into allow, ask or block, extraction where code finds candidates and Jev picks). Files that are not text are transcribed by Gemini on your Gemini key. Source was not inspected.

## Get started

1. Open [jevbridge.fyi](https://jevbridge.fyi/) and choose set up, or go to [connect.bridgehead.cloud/c/jevbridge](https://connect.bridgehead.cloud/c/jevbridge).
2. Sign in, add your TypeSafe Jev key, then add the connector to your MCP app.

## Examples and demos

- Product page with demo video: [jevbridge.fyi](https://jevbridge.fyi/)
- Use cases: [jevbridge.fyi/use-cases](https://jevbridge.fyi/use-cases)
- Announcement on X: [x.com/roguevoice/status/2115675183402901703](https://x.com/roguevoice/status/2115675183402901703)

## Limits and data handling

Questions, files and pictures you send go through Bridgehead to TypeSafe (and to Gemini for transcription); readings and answers are kept in your account. See the [privacy page](https://bridgehead.cloud/privacy.html).

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia). Primary sources: product, connector, use-case and privacy pages (HTTP 200) and the X announcement. AI-assisted curation; no account, key or live call was used. De-dupe: no existing Awesome Jev listing for jevbridge.fyi or Bridgehead.

**X attribution:** `https://x.com/roguevoice/status/2115675183402901703`
