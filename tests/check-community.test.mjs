// SPDX-License-Identifier: MIT
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { checkCommunity } from '../scripts/check-community.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'jev-directory-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  fs.mkdirSync(path.join(root, 'community/projects'), { recursive: true });
  const write = (file, text) => fs.writeFileSync(path.join(root, file), text);
  write('README.md', '# List\n\n## Community projects\n\n- [Example](https://github.com/acme/example) - A tool. [Details](community/projects/example.md).\n\n## Other\n');
  write('community/README.md', '# Browse\n\n## Tools\n\n| Project | Use |\n| --- | --- |\n| [Example](projects/example.md) | A tool |\n');
  write('community/projects/example.md', '# Example\n\n[Tools](../README.md#tools)\n\n[Source](https://github.com/acme/example)\n');
  return { root, write };
}

test('accepts connected pages, table entries, and canonical GitHub URL variants', t => {
  const { root, write } = fixture(t);
  write('community/projects/example.md', '# Example\n\n[Tools](../README.md#tools)\n\n[Source](https://github.com/ACME/Example.git)\n');
  assert.deepEqual(checkCommunity(root), { errors: [], count: 1 });
});

test('rejects a new README project without a detail page', t => {
  const { root } = fixture(t);
  const file = path.join(root, 'README.md');
  fs.writeFileSync(file, fs.readFileSync(file, 'utf8').replace('## Other', '- [New](https://github.com/acme/new) - Another tool.\n\n## Other'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('no project page for https://github.com/acme/new')));
});

test('rejects orphan pages and an omitted directory listing', t => {
  const { root, write } = fixture(t);
  write('community/projects/extra.md', '# Extra\n\n[Source](https://github.com/acme/extra)\n');
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('extra.md: missing from the README')));
  assert.ok(errors.some(error => error.includes('extra.md: index exactly once')));
});

test('rejects duplicate category listings', t => {
  const { root } = fixture(t);
  fs.appendFileSync(path.join(root, 'community/README.md'), '\n## More\n\n[Example](projects/example.md)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('index exactly once')));
});

test('rejects a page linked from the wrong category', t => {
  const { root, write } = fixture(t);
  write('community/projects/example.md', '# Example\n\n[Other](../README.md#other)\n\n[Source](https://github.com/acme/example)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('link back to its category')));
});

test('rejects an index entry whose project page is missing', t => {
  const { root } = fixture(t);
  fs.unlinkSync(path.join(root, 'community/projects/example.md'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('Index links to missing project page')));
});

test('rejects a README entry without a detail-page link', t => {
  const { root, write } = fixture(t);
  write('README.md', '# List\n\n## Community projects\n\n- [Example](https://github.com/acme/example) - A tool.\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('README entry must also link')));
});

test('rejects duplicate sources and requires a usable canonical source', t => {
  const { root, write } = fixture(t);
  write('community/projects/duplicate.md', '# Duplicate\n\n[Source](https://github.com/acme/example)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('duplicate source')));
  write('community/projects/duplicate.md', '# Duplicate\n\n[Source](http://example.com)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('canonical HTTPS')));
});
