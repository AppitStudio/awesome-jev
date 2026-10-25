# Conclave (local multi-model council app with Jev routing and answer checks)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Local Windows app that sends one question to a council of up to 13 AI providers, has a chosen model synthesise their answers blind and an optional model from another company audit the result; optional Jev checks route questions, flag refusals or off-topic answers and test draft claims, in shadow (record-only) mode by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/btrischetta/conclave) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/btrischetta/conclave#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free source build. Each provider, including TypeSafe, bills your own key; Conclave shows live per-call costs. Checked 2026-10-26. |
| Jev evidence | [`conclave.py`](https://github.com/btrischetta/conclave/blob/550e1712cf59bd2788489b99c4eae179fd3fc06e/conclave.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [btrischetta](https://github.com/btrischetta). Independently curated. |
| Format | Local Streamlit app (Python) |
| Platform and availability | Windows 10/11, runs locally on 127.0.0.1 in an Edge app window; keys are stored with Windows DPAPI. |
| Jev's role | Optional: Jev routes questions, checks each council answer and the draft's claims; modes are Off, Shadow (record only, default) and Active. |
| Requirements | Windows 10 or 11, Python 3.14; keys for at least one LLM provider; optional TypeSafe key for Jev checks. |
| License | [Apache-2.0](https://github.com/btrischetta/conclave/blob/550e1712cf59bd2788489b99c4eae179fd3fc06e/LICENSE) |

## When to use

- Get one checked answer from several AI companies on a question that matters.
- Watch what Jev would have flagged in shadow mode before letting it act.
- Mismatch: Windows only; a full council run costs more than a single model.

## How it works

`conclave.py` posts to `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0` for routing (`jev_route`), answer checks with hold verdicts such as refuses, off_topic or broken at 0.85 confidence (`jev_check_answer`), and claim checks against the council's answers (`jev_claim_check`). Integration evidence: [`conclave.py`](https://github.com/btrischetta/conclave/blob/550e1712cf59bd2788489b99c4eae179fd3fc06e/conclave.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/btrischetta/conclave.git && cd conclave
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run conclave.py   # or launch_conclave.bat
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/btrischetta/conclave#readme](https://github.com/btrischetta/conclave#readme)

## Limits and data handling

Questions, files and answers go to every provider you enable, and to TypeSafe when Jev checks are on. The app listens on 127.0.0.1 only.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 550e1712cf59](https://github.com/btrischetta/conclave/tree/550e1712cf59bd2788489b99c4eae179fd3fc06e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
