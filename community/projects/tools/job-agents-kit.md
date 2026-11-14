# job-agents-kit (macOS kit for a careful overnight job search, with templates and an approve-before-submit patch for the listed jev-job-search)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Kit for a mostly unattended job search on a Mac: a Claude Code research shift plans emails from your own notes, a checker holds them to your writing rules, a launchd night job saves approved emails to Mail drafts, and `jev-config/` adds templates plus a patch for jev-job-search so its form filling prepares each application and submits nothing until you approve it by id.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dudailia/job-agents-kit) |
| Maintainer | [dudailia](https://github.com/dudailia). Independently curated. |
| Format | Shell, AppleScript and Python kit with a patch for jev-job-search (MIT) |
| Requirements | macOS with Apple Mail and launchd, Claude Code, and a jev-job-search checkout (with that project's own requirements) for form filling. |
| License | [MIT](https://github.com/dudailia/job-agents-kit/blob/12a2b50bb14134e1daa961be4b43dac3b03fb7d3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-config/jev-fixes.patch`](https://github.com/dudailia/job-agents-kit/blob/12a2b50bb14134e1daa961be4b43dac3b03fb7d3/jev-config/jev-fixes.patch) at the pinned commit. |

## When to use

- Run jev-job-search with a human approval step before any application is submitted.
- Mismatch: Windows, Linux or browser-only mail; it relies on macOS Mail and launchd.

## How it works

`jev-config/jev-fixes.patch` applies to jev-job-search 1.7.0 and current main, adding a default `prepare` mode where `daily` and `apply --submit` only fill and check forms and `npx jev submit <id>` sends an approved one. The Jev-backed form decisions come from jev-job-search itself. Integration evidence: [`jev-config/jev-fixes.patch`](https://github.com/dudailia/job-agents-kit/blob/12a2b50bb14134e1daa961be4b43dac3b03fb7d3/jev-config/jev-fixes.patch).

## Get started

Follow the setup guide, then apply the patch inside your jev-job-search folder.

```sh
git clone https://github.com/dudailia/job-agents-kit
# see GUIDE.md; then, in your jev-job-search checkout:
git apply /path/to/job-agents-kit/jev-config/jev-fixes.patch
npx jev doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup guide: [github.com/dudailia/job-agents-kit/blob/12a2b50bb14134e1daa961be4b43dac3b03fb7d3/GUIDE.md](https://github.com/dudailia/job-agents-kit/blob/12a2b50bb14134e1daa961be4b43dac3b03fb7d3/GUIDE.md)
- jev-job-search: [github.com/qbeka/jev-job-search](https://github.com/qbeka/jev-job-search)

## Limits and data handling

Your profile, drafts and policy stay in local files; the agents and jev-job-search send data to their configured model providers. Prepare mode is the default, so nothing is sent or submitted until you approve it.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 12a2b50bb141](https://github.com/dudailia/job-agents-kit/tree/12a2b50bb14134e1daa961be4b43dac3b03fb7d3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
