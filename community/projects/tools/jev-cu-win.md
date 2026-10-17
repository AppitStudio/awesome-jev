# jev-cu-win

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Windows port of Jev-cu (docs in Japanese and English): a Codex skill where Jev reads the UI Automation text of a window and picks the next element to click or type into, with dry runs by default.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/WorkFrameHub/jev-cu-win) |
| Maintainer | [WorkFrameHub](https://github.com/WorkFrameHub). Independently curated. |
| Format | Codex skill with Node.js and PowerShell scripts (Windows 10/11) |
| Requirements | Windows 10 or 11, Codex with skills, Git, Node.js 20+, a TypeSafe API key. |
| License | [MIT](https://github.com/WorkFrameHub/jev-cu-win/blob/6e2c9bc5e525e2805a3269be0515c0fdbe9189a6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev-decide.mjs`](https://github.com/WorkFrameHub/jev-cu-win/blob/6e2c9bc5e525e2805a3269be0515c0fdbe9189a6/scripts/jev-decide.mjs) at the pinned commit. |

## When to use

- Let Codex operate simple Windows apps (Calculator, Notepad) through accessibility text instead of screenshots.
- Study a confirm-before-acting loop where Jev recommends and the script stops for risky steps.
- Mismatch: experimental and Windows only; complex apps with poor UI Automation trees will not work well.

## How it works

The scripts read the target window's UI Automation tree, send the visible text and the goal to Jev from `jev-decide.mjs`, and act through UI Automation only after the dry run and any required confirmation. No screenshots are sent. Integration evidence: [`scripts/jev-decide.mjs`](https://github.com/WorkFrameHub/jev-cu-win/blob/6e2c9bc5e525e2805a3269be0515c0fdbe9189a6/scripts/jev-decide.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/WorkFrameHub/jev-cu-win.git
cd jev-cu-win
copy .env.example .env.local   # add TYPESAFE_API_KEY
node scripts/install-skill.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Original macOS version: [github.com/Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu)
- Calculator and Notepad walk-throughs in the README.

## Limits and data handling

Window text and your goal go to TypeSafe on your key; the README warns that even dry runs send data and can be billed.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 6e2c9bc5e525](https://github.com/WorkFrameHub/jev-cu-win/tree/6e2c9bc5e525e2805a3269be0515c0fdbe9189a6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
