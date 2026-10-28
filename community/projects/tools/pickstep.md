# pickstep (fast browser tests where Claude Code plans, Jev picks each step and ego lite drives)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser-test runner that hands the slow look-click-look inner loop to Jev: Claude Code writes a spec of stages, inputs and budget, then for each step pickstep observes the page, Jev picks the next action from the visible options, and ego lite acts; Claude reads the report and takes over when Jev answers NONE or is unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jinjin99/pickstep) |
| Maintainer | [jinjin99](https://github.com/jinjin99). Independently curated. |
| Format | Node.js CLI |
| Requirements | Node.js, the ego-browser, Claude Code for planning, and a TypeSafe API key. |
| License | [MIT](https://github.com/jinjin99/pickstep/blob/3a088651a94776b0312dc90f4bd89a5f5ff7a4c0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.js`](https://github.com/jinjin99/pickstep/blob/3a088651a94776b0312dc90f4bd89a5f5ff7a4c0/src/jev.js) at the pinned commit. |

## When to use

- Run end-to-end browser checks faster than a large model clicking through each step.
- Mismatch: needs ego lite; Claude handles planning and fallbacks.

## How it works

`src/jev.js` posts the page observation and candidate actions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, overridable) and returns the chosen step with its confidence. Integration evidence: [`src/jev.js`](https://github.com/jinjin99/pickstep/blob/3a088651a94776b0312dc90f4bd89a5f5ff7a4c0/src/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jinjin99/pickstep.git && cd pickstep
npm install && npm link
pickstep doctor   # checks ego-browser, the key and one Jev call
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jinjin99/pickstep#readme](https://github.com/jinjin99/pickstep#readme)

## Limits and data handling

Page observations from the site under test go to TypeSafe on each step.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 3a088651a947](https://github.com/jinjin99/pickstep/tree/3a088651a94776b0312dc90f4bd89a5f5ff7a4c0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
