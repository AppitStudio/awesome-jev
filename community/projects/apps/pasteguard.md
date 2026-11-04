# PasteGuard (free Windows tray agent that asks Jev how dangerous a copied command is and removes risky ones from the clipboard to stop ClickFix attacks)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Small Windows tray agent against ClickFix attacks, where a fake CAPTCHA or error page tricks you into pasting a malicious command into Win+R, a terminal or PowerShell. It watches the clipboard, sends only command-like text to Jev with a yes/no danger question, and if the risk score reaches your threshold it removes the text from the clipboard and warns you. Each block is listed under Threat activity, and it never runs anything it inspects.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ryankapa/PasteGuard) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Ryankapa/PasteGuard#readme) (source-built; no separate product site verified). |
| Pricing and access | The app is described as free; you pay TypeSafe through your own Jev key. Checked 2026-11-04. |
| Jev evidence | [`src/PasteGuard/JevClient.cs`](https://github.com/Ryankapa/PasteGuard/blob/4952aa0e37d1f409dce1e108b42062f4521eea1b/src/PasteGuard/JevClient.cs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Ryankapa](https://github.com/Ryankapa). Independently curated. |
| Format | Windows tray app (C#, single .exe; source in the repository) |
| Platform and availability | Windows tray app; no installer or admin rights, per the README. |
| Jev's role | Scores each copied command-like text for danger so risky commands can be removed from the clipboard. |
| Requirements | Windows and your own Jev API key from console.typesafe.ai. |
| License | [MIT](https://github.com/Ryankapa/PasteGuard/blob/4952aa0e37d1f409dce1e108b42062f4521eea1b/LICENSE) |

## When to use

- Add a last check between a web page and your terminal against paste-this-command scams.
- Mismatch: it only sees what lands on the clipboard and only asks Jev about command-like text; a low threshold can block harmless commands.

## How it works

`src/PasteGuard/JevClient.cs` posts the copied command to `https://api.typesafe.ai/v1/systemone` as one yes/no (`noul`) danger question and compares the probability to your threshold; `tools/Calibrate` helps tune it. Integration evidence: [`src/PasteGuard/JevClient.cs`](https://github.com/Ryankapa/PasteGuard/blob/4952aa0e37d1f409dce1e108b42062f4521eea1b/src/PasteGuard/JevClient.cs).

## Get started

From the upstream README (not run on the review host):

```sh
# download PasteGuard.exe from the repository's Releases page and check its SHA256, then add your Jev API key in Settings
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the setup and a Windows Sandbox demo description: [github.com/Ryankapa/PasteGuard#readme](https://github.com/Ryankapa/PasteGuard#readme)

## Limits and data handling

Copied command text goes to TypeSafe on your key (other clipboard content stays local). The README notes the free build is not code-signed, so SmartScreen may warn; the detection rate was not independently measured here. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 4952aa0e37d1](https://github.com/Ryankapa/PasteGuard/tree/4952aa0e37d1f409dce1e108b42062f4521eea1b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
