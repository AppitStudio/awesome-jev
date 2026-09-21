# Jaste

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

A Mac clipboard beta with Smart Paste: select a saved text value that fits the field you are working in.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://jaste.app/) |
| Tags | `Source unverified` · `Pricing unverified` · `BYOK` |
| Product homepage | [Jaste Beta](https://jaste.app/) |
| Pricing and access | The [official download page](https://jaste.app/) provides a ZIP without a sign-in or checkout. Checked **2026-09-22**; app pricing, hosted account requirements, and usage limits remain unverified. Optional Direct Jev mode requires a TypeSafe key and can incur provider charges. |
| Jev evidence | Static inspection of the [public Mac release](https://jaste.app/Jaste.zip) found Direct Jev settings, the TypeSafe System One endpoint, and a question selecting a saved clipboard candidate for the focused field. This establishes integration evidence, not successful live execution. |
| Disclosure | No public source repository or license was linked from the homepage or included in the archive. Source implementation and hosted backend were not inspected; only release metadata and embedded strings were reviewed. Commercial terms remain unverified. The contributor confirmed no affiliation or commercial relationship with Jaste. Inclusion is not endorsement. |
| Maintainer | [Jaste](https://jaste.app/); an individual or legal publisher was not identified in the reviewed materials. |
| Format | Native macOS menu bar application distributed as a ZIP. |
| Platform and availability | Public beta for Apple silicon, macOS 14 or later, via the [Mac download](https://jaste.app/Jaste.zip). Windows and Linux are announced as coming soon. |
| Jev's role | The optional Direct Jev path asks which saved text candidate belongs in the focused field, including a no-match option. The default backend mode, hosted model, exact model identifier, and any other providers were not verified. |
| Requirements | Compatible Mac; onboarding strings request Accessibility and Input Monitoring permissions. Direct Jev mode needs a TypeSafe account/key. |
| License | No license or detailed access terms were found on the [homepage](https://jaste.app/) or in the ZIP; do not infer an open-source license or free ongoing service. |

## When to use

Consider Jaste for reusing copied text across Mac form fields or searching clipboard history. Its Jev question selects an existing value rather than requesting newly written text. It is a beta, and the review did not establish matching quality or compatibility with particular apps.

## How it works

The release contains a clipboard watcher, a suggestion panel, focused-field Accessibility identifiers, and both cloud and Direct Jev backend settings. The embedded decision question asks Jev to choose a candidate ID for the focused field or a no-match option; accompanying instructions ask for exact saved text without combining or inventing values.

The Direct Jev path references `https://api.typesafe.ai/v1/systemone`. The bundle also configures `https://api.jaste.app` and contains a device-registration route. These observations support the intended integration and distinguish direct-provider access from Jaste's service. Strings alone do not establish request payloads, active defaults, response validation, or runtime behavior.

## Get started

This path follows the public download and embedded onboarding text; it was not executed during review. Smart Paste involves remote text processing, and direct-provider use can incur charges.

1. Download the beta from the [product page](https://jaste.app/) and extract `Jaste.app` on a supported Mac.
2. Open the app and follow its Accessibility and Input Monitoring setup. Those permissions support reading field labels, inserting selected text, and detecting shortcuts in other apps.
3. For the Jev path documented here, use **Configure Direct Jev Key** to supply your TypeSafe key. The embedded settings text says it is stored in this Mac's Keychain; storage was not tested.
4. Copy non-sensitive sample text, focus an appropriate field, and invoke Smart Paste using the app's configured shortcut. Inspect the suggested value before relying on it. The bundle also offers clipboard-history search, pause/resume capture, and history clearing.

Hosted mode contains messages for access restrictions and required updates. Its account, plan, and onboarding flow were not verified.

## Examples and demos

The [homepage and downloadable beta](https://jaste.app/) are the verified public entry points. No separate tutorial, video, source example, or credential-free matching demo was linked from the reviewed page. The usage path above is based on embedded UI instructions, not a recorded successful run.

## Limits and data handling

The vendor states that clipboard history stays off Jaste's servers, Smart Paste sends relevant text for processing, and images remain local. These are [homepage claims](https://jaste.app/), not an independently audited data-flow guarantee. The binary references both Jaste's API and TypeSafe's API; exact transmitted fields, retention, and hosted subprocessors remain unverified.

A no-match option is present, but confidence thresholds, error recovery, sensitive-value filtering, and paste safeguards were not established by static inspection. The release contains local application-support and log paths; their contents and retention were not inspected. No private clipboard data, saved keys, or local app state was accessed.

## Review and maintenance

Reviewed **2026-09-22** with AI assistance. The homepage calls the product **0.1 Beta**; the downloaded app's `Info.plist` identifies **0.1.1**, build **1**, bundle ID `app.jaste.mac`. The executable is ARM64. The mutable [release URL](https://jaste.app/Jaste.zip) returned HTTP 200 and this ZIP SHA-256:

```text
c3ed70bc3a5ca325ba714fd9693ee50a2dfd69635d807eec137227e599c32335
```

Inspection used `curl`, `unzip -l`, `plutil`, `file`, and filtered `strings` output, with downloaded artifacts outside the catalog. Existing entries and open GitHub issues/PRs were checked for duplicates; none matched Jaste. No app launch, installation, permission grant, account creation, provider request, or live matching test was performed. Source, backend behavior, signing/notarization, licensing, and ongoing access terms remain unverified.

Related: [Smart Paste](smart-paste.md) is a separate open-source Chrome extension with a source-build workflow.
