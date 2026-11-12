# cljev (Clojure client for TypeSafe's System One API and Jev, for Babashka and the JVM)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Clojure client for TypeSafe's System One API that runs from the same source on Babashka and the JVM: build `noul`, `choice` and `score` questions as data and get Jev's typed answers with probabilities back as Clojure maps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/joshrotenberg/cljev) |
| Maintainer | [joshrotenberg](https://github.com/joshrotenberg). Independently curated. |
| Format | Clojure library on Clojars (MIT) |
| Requirements | Babashka 1.13.225+ or JVM 21/25 with Clojure, plus `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/joshrotenberg/cljev/blob/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/cljev/core.clj`](https://github.com/joshrotenberg/cljev/blob/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/src/cljev/core.clj) at the pinned commit. |

## When to use

- Call Jev from Clojure scripts (Babashka) or JVM services without writing HTTP glue.
- Mismatch: if you need an official SDK; this is an unofficial 0.x community client.

## How it works

`src/cljev/core.clj` covers the two endpoints in TypeSafe's OpenAPI spec, `POST /v1/systemone` and `GET /v1/models`, on `https://api.typesafe.ai`. The project is at 0.x (API may change before 1.0) and states it is not affiliated with TypeSafe. Integration evidence: [`src/cljev/core.clj`](https://github.com/joshrotenberg/cljev/blob/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/src/cljev/core.clj).

## Get started

Add the Clojars dependency to `deps.edn` or `bb.edn`, set your key, then `(jev/ask (jev/client) state questions)`.

```sh
{:deps {io.github.joshrotenberg/cljev {:mvn/version "0.1.1"}}}
;; export TYPESAFE_API_KEY=your-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README usage: [github.com/joshrotenberg/cljev/blob/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/README.md](https://github.com/joshrotenberg/cljev/blob/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/README.md)
- Examples folder: [github.com/joshrotenberg/cljev/tree/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/examples](https://github.com/joshrotenberg/cljev/tree/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade/examples)

## Limits and data handling

States and questions go to TypeSafe on your key; the library has no other network dependency.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit bd91ff7eb5e0](https://github.com/joshrotenberg/cljev/tree/bd91ff7eb5e07bf49609f43bf79e20fe9db02ade). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
