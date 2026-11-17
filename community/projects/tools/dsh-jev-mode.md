# JEV decision mode for DeepSeek Harness by QI-seven33 (optional Desktop preset where Jev selects bounded file reads and checks authorization)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial, optional preset for DeepSeek Harness Desktop that keeps the standard capabilities and your main model and adds two Jev uses: bounded selection between a few project files (both confidence and selected probability must reach 0.9, otherwise normal planning continues) and, for operations classified at risk 2 or above, a Noul check of human authorization after the hard rules, with native permission vetoes still authoritative. Without a key, explicit reads still work and unavailable authorization checks ask or deny. The README states that no general speed or safety improvement is established and that false-allow/false-block rates are unmeasured.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/QI-seven33/dsh-jev-mode) |
| Maintainer | [QI-seven33](https://github.com/QI-seven33). Independently curated. |
| Format | DeepSeek Harness Desktop plugin (JavaScript, MIT) |
| Requirements | DeepSeek Harness Desktop 0.2.2-rc.3 (verified on Windows) and your own TypeSafe key saved in Harness settings. |
| License | [MIT](https://github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.js`](https://github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/index.js) at the pinned commit. |

## When to use

- Add a Jev authorization check to risky operations in DeepSeek Harness without changing your main model.
- Mismatch: other Harness versions or operating systems, which the author has not validated.

## How it works

`index.js` configures the TypeSafe backend at `https://api.typesafe.ai/v1/systemone` with the model pinned to `jev-1.13.0` (OpenRouter or the host's model are alternative backends) and runs the selection and authorization questions. Integration evidence: [`index.js`](https://github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/index.js).

## Get started

Install the release in Harness Desktop's Plugins page, restart, and pick JEV decision mode in a new session.

```sh
# Harness Desktop -> Plugins -> install:
github:QI-seven33/dsh-jev-mode#v0.4.6
# restart, choose "JEV decision mode", then Settings -> Models -> JEV decision model -> add your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Validation notes: [github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/VALIDATION.md](https://github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/VALIDATION.md)
- README: [github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/README.md](https://github.com/QI-seven33/dsh-jev-mode/blob/6b45308f498220296ef5fa674ac2704c4c7bf34a/README.md)

## Limits and data handling

Operation summaries and the file choices it asks about go to TypeSafe on your key. The classifier has known gaps; real-world authorization error rates are unmeasured, per the README.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 6b45308f4982](https://github.com/QI-seven33/dsh-jev-mode/tree/6b45308f498220296ef5fa674ac2704c4c7bf34a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
