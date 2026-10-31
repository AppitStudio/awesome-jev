# jevban (fail2ban-style daemon where a Jev-style decision model judges suspicious web clients)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Single-binary Free Pascal daemon that follows Apache access logs, prefilters suspicious clients with cheap signatures, then asks a decision model whether the client is attacking, using a plain-words description of your site. It bans in the firewall like fail2ban; the model can be OpenJev run in-process on llama.cpp, your own OpenJev server, or hosted Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FMXExpress/JevBan) |
| Maintainer | [FMXExpress](https://github.com/FMXExpress). Independently curated. |
| Format | Free Pascal CLI daemon (Linux x64 / Windows x64 releases) |
| Requirements | Linux (iptables, nftables, ufw, firewalld or fail2ban actions) or Windows (netsh); ~5.6 GB download for the local OpenJev model, or a TypeSafe key for hosted Jev. |
| License | [MIT](https://github.com/FMXExpress/JevBan/blob/51f56a720a10d55b637a681f76263b3efd219372/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Ban.Config.pas`](https://github.com/FMXExpress/JevBan/blob/51f56a720a10d55b637a681f76263b3efd219372/Ban.Config.pas) at the pinned commit. |

## When to use

- Replace brittle fail2ban regexes with a judgment over a client's recent requests.
- Mismatch: false positives ban real users; start with the documented test mode.

## How it works

Suspicious clients go to `POST /v1/systemone` (in-process OpenJev, a configured server, or the `typesafe` provider at `api.typesafe.ai` with `jev-latest`, listed in `Ban.Config.pas`) and the returned P(malicious) and intent count as strikes within `findtime`. Integration evidence: [`Ban.Config.pas`](https://github.com/FMXExpress/JevBan/blob/51f56a720a10d55b637a681f76263b3efd219372/Ban.Config.pas).

## Get started

From the upstream README (not run on the review host):

```sh
./jevban --test tests/sample_access.log   # dry run against a sample log
# configure jevban.ini (mode = local | jev | rules), then run as a service
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Releases: [github.com/FMXExpress/JevBan/releases](https://github.com/FMXExpress/JevBan/releases)

## Limits and data handling

Client IPs and request lines are sent to the hosted API only in `jev` mode with a remote provider; local mode keeps them on the host. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 51f56a720a10](https://github.com/FMXExpress/JevBan/tree/51f56a720a10d55b637a681f76263b3efd219372). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
