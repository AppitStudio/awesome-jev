# Jev Sift

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Screen candidate files, public webpages, or tool descriptions with Jev, then let an agent inspect the items that merit attention.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kbhuw/jev-sift) |
| Maintainer | [Kush Bhuwalka / kbhuw](https://github.com/kbhuw). Community project. |
| Format | JavaScript classification core, stdio MCP server, and agent plugin with a Codex compatibility manifest. |
| Requirements | Node.js 20+ documented upstream, an MCP-capable client, and a TypeSafe account/key for live classification. Uses `JEV_API_KEY` or `TYPESAFE_API_KEY`; provider charges may apply. |
| License | Unspecified at the reviewed commit: no project license file or package license field was found. Public source access does not establish an open-source license or reuse permission. |
| Disclosure | AI-assisted catalog review, not an upstream submission or endorsement. Contributor affiliation and commercial relationships were not supplied. |

## When to use

- Select which files or retrieved webpages an agent should read in full for a particular task.
- Compare supplied tool descriptions against a task before deciding which tool to call.
- Reuse a small classification core with your own content readers and evaluator.

The main benefit is keeping full candidate content out of the main agent's context when paths or URLs are supplied directly. Inline text that the agent has already read cannot recover that context cost. Tool-description judgments concern the supplied description; they do not predict unseen results or execute candidate tools.

## How it works

The [`classify` core](https://github.com/kbhuw/jev-sift/blob/966de12e2bb5f94d47886ee51f30a07ec8ef1607/src/classify.js) accepts up to 50 items with unique IDs and exactly one of `text`, `path`, or `url` per item. A `query` becomes one relevance question; alternatively, supply one to eight typed questions. Each successfully loaded item gets a separate Jev request, with at most eight requests running concurrently.

The [provider](https://github.com/kbhuw/jev-sift/blob/966de12e2bb5f94d47886ee51f30a07ec8ef1607/src/provider.js) calls the native TypeSafe `/v1/systemone` endpoint with the fixed moving alias `jev-latest`. Its public `boolean` question maps to Noul and returns `probability`, the probability of yes. Choice and Score answers retain returned distributions and confidence; Score also retains its legend. The request mapping matches the [HTTP API](https://docs.typesafe.ai/api) inspected during this review.

Code loads content, bounds concurrency, validates answer types and ranges, preserves input order, and reports individual failures. Structured results retain returned model identifiers, truncation flags, resolved webpage URLs, and summed input-token usage. The caller chooses what to read or do next; Jev does not generate an explanation or authorize downstream actions.

## Get started

Review the unspecified licensing before adopting or redistributing the code. From a separate working directory, obtain the inspected version:

```sh
git clone https://github.com/kbhuw/jev-sift.git
cd jev-sift
git checkout 966de12e2bb5f94d47886ee51f30a07ec8ef1607
```

The committed `dist/server.mjs` bundles its dependencies, so the MCP server does not require `npm install`. Configure your client's stdio MCP connection, replacing the example path with the absolute checkout path:

```json
{
  "mcpServers": {
    "jev-sift": {
      "command": "node",
      "args": ["/absolute/path/to/jev-sift/dist/server.mjs"]
    }
  }
}
```

Call `classify_status` first. It makes no network request and reports key presence and allowed file roots; it does not establish provider connectivity. Configure the key privately through the MCP host environment, using `JEV_API_KEY` or `TYPESAFE_API_KEY`. Desktop clients that do not inherit shell variables can use the private key-file path described in the [upstream setup](https://github.com/kbhuw/jev-sift#setup-one-jev-api-key). Do not paste keys into agent conversations.

**File access defaults to the home directory.** Before supplying paths, restrict `roots` in `~/.config/jev-sift/config.json` to the directories you intend to classify. Set `roots` to `[]` to disable file access. See [optional settings](https://github.com/kbhuw/jev-sift#optional-settings).

**Live example:** the following `classify` tool input uses synthetic text but makes one real provider request, sends that text to TypeSafe, and may incur charges:

```json
{
  "query": "Find evidence of software sold to hospitals",
  "items": [
    { "id": "sample", "text": "We build appointment software for hospitals." }
  ]
}
```

Inspect `results[0].answers.relevant.probability` or the item's `error`. No particular probability is guaranteed. Open uncertain items for review, and do not interpret an error or truncated result as evidence of irrelevance.

For **offline development checks** after downloading dependencies:

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm test
npm run build
```

Tests use synthetic inputs and mocked model responses, including a loopback HTTP fixture for the bundled MCP server. They do not require a real API key. The optional plugin installation path is documented [upstream](https://github.com/kbhuw/jev-sift#install-as-a-plugin-or-mcp-server); installed-host compatibility was not tested here.

## Examples and demos

- [Typed request](https://github.com/kbhuw/jev-sift/blob/966de12e2bb5f94d47886ee51f30a07ec8ef1607/examples/request.json): synthetic company descriptions with Boolean, Choice, and Score questions. Passing it to `classify` makes live requests.
- [Screening request](https://github.com/kbhuw/jev-sift/blob/966de12e2bb5f94d47886ee51f30a07ec8ef1607/examples/sift.json): a public documentation URL and a tool description. Executing it fetches the webpage and calls Jev.
- [Offline tests](https://github.com/kbhuw/jev-sift/tree/966de12e2bb5f94d47886ee51f30a07ec8ef1607/test): request mapping, validation, ordering, cancellation, file boundaries, URL handling, and the bundled MCP exchange.

No separate hosted demo was identified; the requests above are the inspected usage examples.

## Limits and data handling

File text, extracted webpage text, and inline text go to TypeSafe. Keeping them out of the main agent's context does not keep them local. The plugin does not persist source content or classification results itself; client and provider handling are separate. Webpage fetches do not receive the Jev credential.

File and extracted page inputs are truncated at 60,000 JavaScript characters with a flag; oversized inline text is rejected. Web downloads are limited to 2 MB, use a 20-second timeout, and follow at most three redirects. The reader supports public text/HTML pages, not PDFs, authenticated browsing, or JavaScript rendering. A successful response may still contain a login or challenge page instead of the intended article.

The [web reader](https://github.com/kbhuw/jev-sift/blob/966de12e2bb5f94d47886ee51f30a07ec8ef1607/src/web.js) checks public addresses at each redirect and pins validated DNS results to connections. The [file reader](https://github.com/kbhuw/jev-sift/blob/966de12e2bb5f94d47886ee51f30a07ec8ef1607/src/files.js) resolves symlinks before checking roots. These inspected measures do not constitute a comprehensive security audit.

Transport failures become per-item errors, with no automatic provider retry. Thresholds and model quality need evaluation on the intended workload. Mocked tests do not establish accuracy, prompt-injection resistance, or net cost and latency savings.

## Review and maintenance

Reviewed on **2026-09-19** at [commit 966de12](https://github.com/kbhuw/jev-sift/tree/966de12e2bb5f94d47886ee51f30a07ec8ef1607), package version 0.2.0. AI-assisted inspection covered the README, source modules, plugin manifests, build script, examples, upstream skill, tests, and missing licensing information. On Node.js 22.19.0, **all 15 offline tests passed**; `npm run build` reproduced the committed bundle without a diff. Tests ran with a stripped environment and synthetic credentials.

No live Jev request, real webpage-fetch exercise, installed-host plugin test, or model-quality benchmark was performed. See [validation scope](../../../docs/validation.md#community-project-checks).

Related: [fast-jev-compaction](fast-jev-compaction.md) prunes existing conversation content; [RAG triage](../../../examples/rag-triage/README.md) demonstrates a smaller offline context-selection workflow.
