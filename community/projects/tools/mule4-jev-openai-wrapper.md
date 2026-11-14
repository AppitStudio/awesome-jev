# Mule 4 Wrapper: Jev for OpenAI (OpenAI-compatible endpoint where Jev picks the tool call or a text reply, and a chat model writes it)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Mule 4 application exposing OpenAI Chat Completions and Responses endpoints, so OpenAI clients and MuleSoft Agent Fabric brokers can use it: Jev reads the recent conversation and offered tools and picks one tool or `respond_to_user`, then a fallback chat model writes the reply or the tool arguments; below the confidence threshold the fallback decides alone. Each response carries an `x-jev-decision` header.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI) |
| Maintainer | [A2D-Agentic-Asset-Designer](https://github.com/A2D-Agentic-Asset-Designer). Independently curated. |
| Format | Mule 4.9 application (Java 17, Maven; no license file) |
| Requirements | Java 17, Maven, a Mule 4.9 runtime and an OpenRouter key (Jev runs as `~typesafe/jev-latest` on OpenRouter). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/main/resources/config.yaml`](https://github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/blob/2c19eee4ce828f8cf5638024441e67f7068da77b/src/main/resources/config.yaml) at the pinned commit. |

## When to use

- Put a fast tool-choice decision in front of an existing OpenAI-compatible agent or MuleSoft broker.
- Mismatch: if you need a direct TypeSafe connection; this wrapper uses OpenRouter.

## How it works

`src/main/resources/config.yaml` points the Jev step at OpenRouter's `/api/alpha/decisions` with `jev.model` `~typesafe/jev-latest` and `jev.minConfidence` 0.5; `dwl/jev-request.dwl` builds the decision request and the flow in `src/main/mule/jev-openai-wrapper.xml` then calls OpenRouter chat completions with the fallback model (default `openai/gpt-4o-mini`), forcing or forbidding the tool call based on Jev's pick. Integration evidence: [`src/main/resources/config.yaml`](https://github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/blob/2c19eee4ce828f8cf5638024441e67f7068da77b/src/main/resources/config.yaml).

## Get started

Build the app, deploy it to a local Mule runtime with your OpenRouter key, then send an OpenAI-style request.

```sh
mvn -DskipTests package
cp target/jev-openai-wrapper-1.0.1-mule-application.jar $MULE_HOME/apps/
$MULE_HOME/bin/mule -M-Dopenrouter.apiKey="$OPENROUTER_API_KEY" -M-Dhttp.port=8091
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/blob/2c19eee4ce828f8cf5638024441e67f7068da77b/README.md](https://github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/blob/2c19eee4ce828f8cf5638024441e67f7068da77b/README.md)
- Defaults: [github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/blob/2c19eee4ce828f8cf5638024441e67f7068da77b/src/main/resources/config.yaml](https://github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/blob/2c19eee4ce828f8cf5638024441e67f7068da77b/src/main/resources/config.yaml)

## Limits and data handling

Up to 12 recent messages (2,000 characters) and the tool list go to OpenRouter on your key for Jev, then to the fallback model. Set `wrapper.apiKey` before exposing the endpoint; empty means no caller check.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 2c19eee4ce82](https://github.com/A2D-Agentic-Asset-Designer/Mule4-Wrapper-Jev-for-OpenAI/tree/2c19eee4ce828f8cf5638024441e67f7068da77b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
