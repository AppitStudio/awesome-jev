# JEV Autofill by Atharva Joshi (Chrome extension that fills job applications from a local profile, with optional Jev field mapping)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Manifest V3 Chrome extension that fills the repetitive fields of a job application (name, contact, education, links, work authorization, EEO and screening questions) from a profile file on your own machine, including Workday's multi-step flow and React or Material UI widgets. It never clicks Submit, Next or Apply and never overwrites a field that has a value. Mapping is regex rules by default; the hybrid and jev modes ask Jev to map fields the rules miss and to pick dropdown and screening answers, seeing only labels, option text and your `facts` list. A JSON report of filled and skipped fields is left on the page for agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/a3harva/jev-autofill) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/a3harva/jev-autofill#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); Jev modes use your own TypeSafe key and are billed to you. Checked 2026-11-19. |
| Jev evidence | [`native/host.py`](https://github.com/a3harva/jev-autofill/blob/64b902a2a0a99c537688e93f57fcf6520920670c/native/host.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [a3harva](https://github.com/a3harva). Independently curated. |
| Format | Chrome extension (JavaScript) with a Python native-messaging helper |
| Platform and availability | Chrome or Chromium on macOS or Linux, loaded unpacked, with a local native-messaging helper. |
| Jev's role | In hybrid/jev modes, maps unmatched form fields to profile keys and picks the best dropdown or screening option; the default static mode makes no Jev calls. |
| Requirements | Chrome or Chromium, Python 3.9+, macOS or Linux; `TYPESAFE_API_KEY` in `.env` only for the hybrid and jev modes. |
| License | [MIT](https://github.com/a3harva/jev-autofill/blob/64b902a2a0a99c537688e93f57fcf6520920670c/LICENSE) |

## When to use

- Speed through job applications from a local profile while keeping submission manual.
- Mismatch: Windows, or a store-installed extension; it is loaded unpacked with a native helper.

## How it works

`native/host.py` is the only part that reads your profile and key; in hybrid and jev modes it sends field labels and options to `https://api.typesafe.ai/v1/systemone` and returns only the values for fields the page has. Integration evidence: [`native/host.py`](https://github.com/a3harva/jev-autofill/blob/64b902a2a0a99c537688e93f57fcf6520920670c/native/host.py).

## Get started

Clone, copy the example profile, install the native helper, then load the `extension/` folder unpacked.

```sh
git clone https://github.com/a3harva/jev-autofill.git
cd jev-autofill
cp profile.example.json profile.local.json   # fill in your details
cp .env.example .env                         # optional: TYPESAFE_API_KEY for hybrid/jev modes
python3 native/install.py
# chrome://extensions → Developer mode → Load unpacked → extension/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/a3harva/jev-autofill/blob/64b902a2a0a99c537688e93f57fcf6520920670c/README.md](https://github.com/a3harva/jev-autofill/blob/64b902a2a0a99c537688e93f57fcf6520920670c/README.md)

## Limits and data handling

Profile values stay local; in hybrid and jev modes field labels, options and your `facts` sentences are sent to TypeSafe. Government IDs or bank details are filled only if you add them to the profile. Field key names derive from qbeka/jev-job-search (MIT).

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 64b902a2a0a9](https://github.com/a3harva/jev-autofill/tree/64b902a2a0a99c537688e93f57fcf6520920670c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
