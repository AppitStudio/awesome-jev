# opencode-system-one

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that screens every `webfetch` result with Jev for junk and prompt injection before it enters context, redacts known secret formats from tool inputs and prompts with plain regex, and gives the agent cached `jev_decide` and `jev_judge_many` tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atvari-eu/opencode-system-one) |
| Maintainer | [atvari-eu](https://github.com/atvari-eu). Independently curated. |
| Format | OpenCode plugin (TypeScript, single `src/index.ts`) |
| Requirements | OpenCode; a TypeSafe API key or OpenCode console key (default model `jev-1.13-free`). |
| License | [MIT](https://github.com/atvari-eu/opencode-system-one/blob/73982a4fc877fec8739953e4c4c7a747fdbbf1ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.ts`](https://github.com/atvari-eu/opencode-system-one/blob/73982a4fc877fec8739953e4c4c7a747fdbbf1ad/src/index.ts) at the pinned commit. |

## When to use

- Annotate or block fetched pages that look like junk or prompt injection before your OpenCode agent relies on them.
- Let the agent ask Jev typed questions directly instead of spending LLM tokens on small judgments.
- Mismatch: OpenCode only; screening is a probability check with thresholds, not a guarantee against injection.

## How it works

The plugin hooks OpenCode tool calls: `webfetch` output is regex-scrubbed, sampled to 12 kB and sent to a System One endpoint with junk and injection questions, then annotated (default) or redacted fail-closed; results are cached per URL and content hash. Secret redaction is deterministic and never calls a model. `/jev-screen <url>` and `/jev-done-check` are optional commands. Integration evidence: [`src/index.ts`](https://github.com/atvari-eu/opencode-system-one/blob/73982a4fc877fec8739953e4c4c7a747fdbbf1ad/src/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
opencode plugin add github:atvari-eu/opencode-system-one
# set TYPESAFE_API_KEY (or use your OpenCode console key), then restart OpenCode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Options for annotate/redact mode, tools and commands in the README.
- Companion skills in [github.com/atvari-eu/skills](https://github.com/atvari-eu/skills).

## Limits and data handling

Sampled fetched content goes to the configured System One endpoint (OpenCode console or TypeSafe) on your key. Pin a commit hash when installing, since a bare spec tracks the default branch.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 73982a4fc877](https://github.com/atvari-eu/opencode-system-one/tree/73982a4fc877fec8739953e4c4c7a747fdbbf1ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
