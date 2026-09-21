# dsh-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness (DSH) bundle that registers a `jev_ask` tool so a DSH agent can send typed noul, choice, and score questions to TypeSafe Jev. Install from GitHub with a pinned commit—not from the public npm registry name collision noted below. Not affiliated with TypeSafe or DeepSeek.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/noetion/dsh-jev) |
| Maintainer | [noetion](https://github.com/noetion). Independently curated; this entry is not an upstream submission or endorsement. Independent/unofficial—not maintained by TypeSafe. |
| Format | DSH plugin package **dsh-jev 0.1.0** (TypeScript; targets DSH `0.1.5-rc.2` / npm `next`; Node `^22.19 \|\| >=24`). |
| Requirements | DSH profile; pin `github:noetion/dsh-jev#<commit>`; allow the package `prepare` build in pnpm `allowBuilds`; `TYPESAFE_API_KEY` in the environment or DSH credentials. |
| License | [MIT](https://github.com/noetion/dsh-jev/blob/48fef197d8a9ccec7881955aa8a4891df823d75c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. **npm package name warning:** the npm registry currently publishes a *different* `dsh-jev@0.2.0` (maintainer zhangxaochen / another GitHub repo). Prefer the GitHub pin above. Offline domain/client/plugin tests passed; the apply test needs `@deepseek-ai/dsh-tools` and was not run with that peer. No live TypeSafe calls. |

## When to use

Use it when a DeepSeek Harness agent should call TypeSafe Jev as a typed tool rather than as free-form chat. Prefer [ask-jev-skill](ask-jev-skill.md) / [Hermes Jev Skills](hermes-jev-skills.md) for Hermes; prefer [jev-mcp](jev-mcp.md) for MCP clients.

## How it works

The Cordis patch registers `jev_ask`. [`src/client.ts`](https://github.com/noetion/dsh-jev/blob/48fef197d8a9ccec7881955aa8a4891df823d75c/src/client.ts) posts `state` + questions to `https://api.typesafe.ai/v1/systemone` (configurable `model` / `endpoint` / `apiKeyEnv`). A bundled `jev` skill documents the tool. The session LLM decides when to call it.

## Get started

```sh
# Pin a commit so later pushes cannot change what you run.
dsh plugin --profile web add github:noetion/dsh-jev#48fef197d8a9ccec7881955aa8a4891df823d75c
# Allow the prepare build key pnpm prints (often dsh-jev), then re-run add.
export TYPESAFE_API_KEY=...
# Restart dsh web if it is already running.
```

```sh
git clone https://github.com/noetion/dsh-jev.git
cd dsh-jev
git checkout 48fef197d8a9ccec7881955aa8a4891df823d75c
# Offline (no API key): tests that do not import @deepseek-ai/dsh-tools
node --experimental-strip-types --test tests/domain.test.ts tests/client.test.ts tests/plugin.test.ts
```

## Examples and demos

- README JSON example mixing noul + choice over a support ticket state.
- Bundled skill under `skills/jev/`.
- Review host: **9/9 passed** for domain/client/plugin tests. Full `npm test` also runs `tests/apply.test.ts`, which failed here without `@deepseek-ai/dsh-tools` installed. No live TypeSafe.

## Limits and data handling

Every live call posts `state` to TypeSafe—do not put secrets in `state`. The plugin does not force the agent to call `jev_ask`. Treat the npm name `dsh-jev` as ambiguous until upstream publishes this GitHub package under a unique name.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 48fef19](https://github.com/noetion/dsh-jev/tree/48fef197d8a9ccec7881955aa8a4891df823d75c): **0.1.0** (GitHub package.json), MIT. AI-assisted source review of README, `src/client.ts`, tests, and LICENSE. Offline subset tests: **9 passed**. No live TypeSafe or full DSH adopt-check.

Related: [ask-jev-skill](ask-jev-skill.md), [Hermes Jev Skills](hermes-jev-skills.md), [jev-mcp](jev-mcp.md), [JMP](jmp.md).
