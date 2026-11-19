# kev-gate by Rvn0xsy (oh-my-pi agent extension that gates every bash command with a System One decision against your written scope)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Semantic command gate for the oh-my-pi (omp) coding agent, aimed at authorized penetration testing: before each bash command runs, a System One decision model scores how likely it is to cross the scope you wrote in `scope.md`, then the command is allowed, sent to a human or blocked by threshold. The bundled Docker service runs the open-source Kev model locally (weights about 8.5 GB from Hugging Face); pointing `GATE_URL` at TypeSafe uses hosted Jev instead. Docs are in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rvn0xsy/kev-gate) |
| Maintainer | [Rvn0xsy](https://github.com/Rvn0xsy). Independently curated. |
| Format | omp extension (TypeScript) plus a Docker gate service |
| Requirements | oh-my-pi; Docker and about 8.5 GB of disk for the local Kev service, or a TypeSafe Jev endpoint and key via `GATE_URL`. |
| License | [MIT](https://github.com/Rvn0xsy/kev-gate/blob/b8da81e21b34614357172f3fd500f7dd0fa73aac/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extension/gate.ts`](https://github.com/Rvn0xsy/kev-gate/blob/b8da81e21b34614357172f3fd500f7dd0fa73aac/extension/gate.ts) at the pinned commit. |

## When to use

- Keep an offensive-security agent inside an authorized scope that regexes cannot express.
- Mismatch: a general sandbox; it judges commands, it does not isolate them.

## How it works

`extension/gate.ts` posts each command and the scope text to `${GATE_URL}/v1/systemone` (the System One request shape that TypeSafe Jev and Kev both accept) and maps the probability to allow, ask or deny. Integration evidence: [`extension/gate.ts`](https://github.com/Rvn0xsy/kev-gate/blob/b8da81e21b34614357172f3fd500f7dd0fa73aac/extension/gate.ts).

## Get started

Start the gate service (or point it at TypeSafe), copy the extension into omp and write your scope file.

```sh
git clone https://github.com/Rvn0xsy/kev-gate && cd kev-gate
(cd docker && docker compose up -d)   # local Kev on :8010, or set GATE_URL for Jev
cp -r extension ~/.omp/agent/extensions/kev-gate
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Rvn0xsy/kev-gate/blob/b8da81e21b34614357172f3fd500f7dd0fa73aac/README.md](https://github.com/Rvn0xsy/kev-gate/blob/b8da81e21b34614357172f3fd500f7dd0fa73aac/README.md)

## Limits and data handling

Jev is one of two backends; the default Docker setup runs the local Kev model, not Jev. With TypeSafe, command text and scope go to TypeSafe on your key. Use only for authorized testing.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit b8da81e21b34](https://github.com/Rvn0xsy/kev-gate/tree/b8da81e21b34614357172f3fd500f7dd0fa73aac). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
