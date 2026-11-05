# Invoice Assistant (local invoice review app for property managers that extracts invoice details, lets Jev pick the supplier property, and emails the PDF to your accountant after approval)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Local, attended Java app for property managers: upload invoice PDFs, extract details with a local Ollama model or OpenRouter, let a bounded decision model choose which of your configured properties the invoice belongs to (with a no-supported-property choice that forces review), then review and send the PDF through a personal Outlook.com account. Automatic approval is off by default and low-confidence decisions always need review. In OpenRouter mode the decision step uses `typesafe/jev-1.13`; the default Ollama mode uses the experimental local `tev1` model instead.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MokapotLabs/invoice-assistant) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/MokapotLabs/invoice-assistant#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (Apache-2.0); no account or product price. The Jev path needs your own OpenRouter key and is billed by OpenRouter, and all-local mode needs hardware for three Ollama models. Checked 2026-11-05. |
| Jev evidence | [`config/openrouter.yaml`](https://github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/config/openrouter.yaml) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [MokapotLabs](https://github.com/MokapotLabs). Independently curated. |
| Format | Java 25 Quarkus app built with The Pipeline Framework (local web UI; macOS first release) |
| Platform and availability | macOS (first release; built from source with Java 25), local web UI on 127.0.0.1 |
| Jev's role | Optional bounded decision step that picks the supplier property for an invoice from your configured choices, with a no-match choice and confidence rules that route doubtful invoices to a person. |
| Requirements | macOS and Java 25; Ollama 0.35+ with `qwen3.5:4b`, `qwen3-vl:4b-instruct` and `tev1` for the all-local mode, or an `OPENROUTER_API_KEY` to switch all three models (including Jev) at start; a Microsoft Entra public-client ID for Outlook sign-in. |
| License | [Apache-2.0](https://github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/LICENSE) |

## When to use

- Route supplier invoices to the right property from a bounded list of choices, with human confirmation before anything is emailed.
- See a worked example of a Jev decision step inside a typed Java pipeline.
- Mismatch: Jev is used only in the optional OpenRouter mode; the default all-local mode uses the experimental `tev1` model, not TypeSafe Jev.

## How it works

`config/openrouter.yaml` binds the `invoice-judgment-model` connector (`decision.query.jev`) to `typesafe/jev-1.13` through OpenRouter, while `config/pipeline.yaml` points the same step at Ollama's `/v1/systemone` with `tev1`; the app builds the property choice list from your catalogue and applies confidence and allowlist rules before delivery. Integration evidence: [`config/openrouter.yaml`](https://github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/config/openrouter.yaml).

## Get started

From the upstream README (not run on the review host):

```sh
export OPENROUTER_API_KEY=your-openrouter-api-key
export INVOICE_ASSISTANT_GRAPH_CLIENT_ID=your-public-client-application-id
./mvnw package
java --enable-native-access=ALL-UNNAMED -Dinvoice-assistant.http.port=8080 \
  -jar invoice-assistant-monolith/target/quarkus-app/quarkus-run.jar
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (modes, model table, Outlook setup, limits): [github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/README.md](https://github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/README.md)
- Architecture notes: [github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/docs/architecture.md](https://github.com/MokapotLabs/invoice-assistant/blob/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18/docs/architecture.md)

## Limits and data handling

OpenRouter mode sends invoice text, relevant catalogue details and any supplier images to OpenRouter and its model providers; approved PDFs go to Microsoft and the configured recipient. The README says `tev1` is experimental and decision scores are not a guarantee of correctness. Timeouts are recorded as uncertain sends and never auto-resent.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 85a0ec999e6b](https://github.com/MokapotLabs/invoice-assistant/tree/85a0ec999e6b1ecf262840dafc9e5f120d1d5d18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
