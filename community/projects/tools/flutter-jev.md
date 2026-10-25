# Flutter × Jev (measured experiments in driving a Flutter app with Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Measured experiments in driving a real 13-screen Flutter app through marionette: Jev picks every action from options built from the screen, a cheap LLM writes only the text a field needs and referees ties on undoable steps, and every run is judged by what the app stored; includes a GenUI benchmark and UI-churn tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chyiiiiiiiiiiii/flutter-jev) |
| Maintainer | [chyiiiiiiiiiiii](https://github.com/chyiiiiiiiiiiii). Independently curated. |
| Format | Python runner, Flutter demo app and benchmark scripts |
| Requirements | Flutter (macOS target), Python 3.13 and marionette_cli; a TypeSafe API key and a Gemini key for the LLM side. |
| License | [MIT](https://github.com/chyiiiiiiiiiiii/flutter-jev/blob/29ee914c2b1b7346ac53e203e77d37b8d10ea94f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`runner/jev.py`](https://github.com/chyiiiiiiiiiiii/flutter-jev/blob/29ee914c2b1b7346ac53e203e77d37b8d10ea94f/runner/jev.py) at the pinned commit. |

## When to use

- Automate a Flutter app's UI flows without brittle scripts that break on renames.
- Compare scripted, LLM-only and Jev-plus-LLM agents on the same task with stored-state verdicts.
- Mismatch: research code against a demo app; figures were measured on one machine, not verified here.

## How it works

`runner/jev.py` asks a Choice (which action) and a Noul (are we done) in one request to `https://api.typesafe.ai/v1/systemone` with `jev-latest`; options come only from actions the code found on screen, so Jev cannot pick an action that does not exist. Integration evidence: [`runner/jev.py`](https://github.com/chyiiiiiiiiiiii/flutter-jev/blob/29ee914c2b1b7346ac53e203e77d37b8d10ea94f/runner/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
export GEMINI_API_KEY=...
dart pub global activate marionette_cli
cd demo_app && flutter run -d macos   # note the ws:// URI
cd ../runner && python3.13 agent.py jev "open order 5207 and submit a return" --uri ws://... --restart
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Report: [github.com/chyiiiiiiiiiiii/flutter-jev/blob/main/results/REPORT.md](https://github.com/chyiiiiiiiiiiii/flutter-jev/blob/main/results/REPORT.md)
- README: [github.com/chyiiiiiiiiiiii/flutter-jev#readme](https://github.com/chyiiiiiiiiiiii/flutter-jev#readme)

## Limits and data handling

Compressed screen options and the task go to TypeSafe; field text and tie-break requests go to Gemini. The app, runner and verdicts run locally.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 29ee914c2b1b](https://github.com/chyiiiiiiiiiiii/flutter-jev/tree/29ee914c2b1b7346ac53e203e77d37b8d10ea94f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
