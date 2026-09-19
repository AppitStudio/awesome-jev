# Apps powered by Jev

[All projects](../README.md) · [Tools and integrations](../tools/README.md) · [Share your app](../../../CONTRIBUTING.md#list-a-jev-powered-app)

Discover applications that use Jev to power a real user workflow. Each app has its own full page explaining what it does, how to access it, and where Jev fits. Hosted products and source-built apps are both welcome; other models may power additional features.

Read the [tag guide](../../APP_TAGS.md): **Open source** describes source licensing; **Commercial** marks a paid offering. Both can apply to the same app. Closed-source products are welcome with public Jev evidence and a clear source-review disclosure. Pricing unknowns stay visible.

## Web apps

### Jev Search

`Open source` · `Pricing unverified` · `BYOK`

Search across selected sources and explore ranked links with editable filters. Jev selects queries, sources, and time windows, then judges result relevance; Search1API retrieves the links.

**Access:** use the [hosted application](https://jev.s1.dev) or self-host from source with TypeSafe and Search1API keys. Self-hosting can incur provider and hosting charges. The hosted homepage was checked; live search and hosted access limits were not tested.

[Full Jev Search guide](jev-search.md) · [Source](https://github.com/superagents-lab/jev-search)

### Notra

`Open source` · `Commercial` · `Paid`

Track how AI answers describe and position your brand. Jev judges brand sentiment and list position within a wider analytics application; other models handle scans, general judging, and drafting.

**Access:** the [hosted product](https://www.usenotra.com) requires an account and offers [paid plans](https://www.usenotra.com/pricing), checked 2026-09-19. Trial eligibility and checkout were not tested. Self-hosting requires database, authentication, and provider setup; the guide records database initialization caveats. This commercial listing is not an endorsement.

[Full Notra guide](notra.md) · [Source](https://github.com/usenotra/notra)

## macOS apps

### macbrow

`Open source` · `Free source build` · `BYOK`

Control macOS apps and perform Chrome tasks through an experimental voice assistant. Jev routes requests, selects tool arguments, and judges follow-ups; Gradium handles speech and a separate LLM supplies generated scripts and text.

**Access:** run the [MIT source](https://github.com/timpratim/macbrow#setup) on macOS with Python 3.12+, `uv`, TypeSafe and Gradium keys, and desktop permissions. The default LLM backend also needs LiveKit credentials; LM Studio is an alternative. No app purchase fee applies to the source build; provider usage can incur charges. Browser tasks require Chrome remote debugging. All 26 upstream tests passed with network access denied; live voice, desktop actions, and browser automation were not tested.

[Full macbrow guide](macbrow.md) · [Source](https://github.com/timpratim/macbrow)

### TipTour

`Open source` · `Free source build` · `BYOK`

Use a macOS menu bar companion to act on typed click requests. Jev chooses among locally detected controls and judges completion or missing targets. A separate Gemini mode handles voice and writing.

**Access:** macOS 14.2+, a source build with Xcode, a TypeSafe key, and desktop permissions. Gemini mode needs its own key. Source is MIT licensed; provider usage can incur charges. Eight isolated decision tests passed; the full app, packaged releases, and live desktop actions were not tested.

[Full TipTour guide](tiptour.md) · [Source](https://github.com/milind-soni/tiptour-macos)

## Browser extensions

### Vibe Check for X

`Source unverified` · `Pricing unverified` · `BYOK`

Review draft X posts, replies, and quote posts with a scorecard inside the composer. Jev judges qualities such as clarity, humor, and regret risk; JavaScript combines the judgments into a verdict. Optional OpenAI vision calls describe media for Jev.

**Access:** load the source folder as an unpacked Chrome extension and supply a TypeSafe key; media descriptions need an OpenAI key. No license file or explicit app pricing terms were found. Provider calls can incur charges, auto-analysis is enabled by default, and keys use Chrome sync storage. Source and syntax were checked; Chrome installation and live scoring were not tested.

[Full Vibe Check guide](vibecheck.md) · [Source](https://github.com/RafalWilinski/vibecheck)

## Before you get started

Each guide records supported platforms, setup, accounts and keys, data recipients, costs, limitations, and the version reviewed. Follow its launch or build path. Source availability does not imply a downloadable release or free inference, and an app listing does not certify production readiness.

For components to integrate into your own project, browse [tools and integrations](../tools/README.md). For a small offline introduction, try the repository's [teaching examples](../../../examples/README.md).

## List your app

Self-submissions are welcome, including open-source, closed-source, free, and paid apps. Provide a working product or source-build link, official pricing/access information, evidence of Jev use, and your affiliation. Apply the [source/pricing tags and disclosures](../../APP_TAGS.md). Closed-source listings must identify what could not be independently inspected; commercial listings must visibly identify paid access.

Follow [List a Jev-powered app](../../../CONTRIBUTING.md#list-a-jev-powered-app) and the [project-page template](../../PROJECT_TEMPLATE.md), or [open an app suggestion](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml). App pages live in this folder, one full page per app.
