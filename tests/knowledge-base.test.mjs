import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const source = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'jev-knowledge-check-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  fs.mkdirSync(path.join(root, 'scripts'), { recursive: true });
  fs.copyFileSync(path.join(source, 'scripts/knowledge-base.mjs'), path.join(root, 'scripts/knowledge-base.mjs'));
  fs.cpSync(path.join(source, 'community/knowledge-base'), path.join(root, 'community/knowledge-base'), { recursive: true });
  for (const name of ['agent-chaperone', 'agent-router', 'jev-trader']) {
    const dir = path.join(root, 'community/projects/tools');
    fs.mkdirSync(dir, { recursive: true });
    fs.copyFileSync(path.join(source, `community/projects/tools/${name}.md`), path.join(dir, `${name}.md`));
  }
  fs.mkdirSync(path.join(root, 'community/projects/apps'), { recursive: true });
  fs.mkdirSync(path.join(root, 'projects/support-router'), { recursive: true });
  for (const name of ['README.md', 'run.py']) fs.copyFileSync(path.join(source, 'projects/support-router', name), path.join(root, 'projects/support-router', name));
  return root;
}

function check(root, ...args) {
  return spawnSync(process.execPath, [path.join(root, 'scripts/knowledge-base.mjs'), ...args], { cwd: root, encoding: 'utf8' });
}

test('accepts the published guide and its generated links', (t) => {
  const root = fixture(t);
  assert.equal(check(root).status, 0);
});

test('rejects a broken project identity before rewriting any backlink', (t) => {
  const root = fixture(t);
  const file = path.join(root, 'community/knowledge-base/articles/building-a-jev-agent-harness.json');
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  data.connections[0].path = 'community/projects/tools/missing-project.md';
  fs.writeFileSync(file, JSON.stringify(data));
  const backlink = path.join(root, 'community/projects/tools/agent-chaperone.md');
  const original = fs.readFileSync(backlink, 'utf8');
  const result = check(root, '--write');
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /missing or invalid repository path/);
  assert.equal(fs.readFileSync(backlink, 'utf8'), original);
});

test('detects a stale backlink and repairs it only in write mode', (t) => {
  const root = fixture(t);
  const backlink = path.join(root, 'community/projects/tools/agent-router.md');
  fs.writeFileSync(backlink, fs.readFileSync(backlink, 'utf8').replace('## Knowledge guides', '## Outdated guides'));
  assert.match(check(root).stderr, /generated backlinks block is missing or stale/);
  assert.equal(check(root, '--write').status, 0);
  assert.equal(check(root).status, 0);
});

test('rejects an unregistered topic and an impossible publication date', (t) => {
  const root = fixture(t);
  const file = path.join(root, 'community/knowledge-base/articles/building-a-jev-agent-harness.json');
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  data.topics.push('unregistered-topic');
  data.published_at = '2026-02-31';
  fs.writeFileSync(file, JSON.stringify(data));
  const result = check(root);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /topics must be unique slugs registered/);
  assert.match(result.stderr, /must be a real ISO date/);
});

test('rejects FAQ metadata that differs from the visible answer', (t) => {
  const root = fixture(t);
  const file = path.join(root, 'community/knowledge-base/articles/building-a-jev-agent-harness.json');
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  data.faqs[0].answer = 'A different answer that is not visible.';
  fs.writeFileSync(file, JSON.stringify(data));
  assert.match(check(root).stderr, /FAQ answer not visible in Markdown/);
});

function png(width, height) {
  const header = Buffer.alloc(24);
  Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]).copy(header);
  header.write('IHDR', 12, 'latin1');
  header.writeUInt32BE(width, 16);
  header.writeUInt32BE(height, 20);
  return header;
}

function withImage(root, width) {
  fs.mkdirSync(path.join(root, 'community/knowledge-base/images'), { recursive: true });
  fs.writeFileSync(path.join(root, 'community/knowledge-base/images/harness.png'), png(width, 630));
  const file = path.join(root, 'community/knowledge-base/articles/building-a-jev-agent-harness.json');
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  data.image = { path: 'community/knowledge-base/images/harness.png', alt: 'Harness diagram', credit: 'Appit Studio', license: 'CC BY 4.0', license_url: 'https://creativecommons.org/licenses/by/4.0/' };
  fs.writeFileSync(file, JSON.stringify(data));
}

test('accepts a large guide image with credit and license', (t) => {
  const root = fixture(t);
  withImage(root, 1200);
  assert.equal(check(root).status, 0);
});

test('rejects a guide image that is too small', (t) => {
  const root = fixture(t);
  withImage(root, 800);
  assert.match(check(root).stderr, /at least 1200 pixels wide/);
});

test('rejects a guide author without a schema.org type', (t) => {
  const root = fixture(t);
  const file = path.join(root, 'community/knowledge-base/articles/building-a-jev-agent-harness.json');
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  delete data.credits.guide_authors[0].type;
  fs.writeFileSync(file, JSON.stringify(data));
  assert.match(check(root).stderr, /guide_author.type must be Person or Organization/);
});
