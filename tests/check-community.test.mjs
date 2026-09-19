// SPDX-License-Identifier: MIT
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { checkCommunity } from '../scripts/check-community.mjs';

function tagText(tags) {
  return tags.map(tag => `\`${tag}\``).join(' · ');
}

function appPage({ tags = ['Open source', 'Free'], disclosure = 'Independent source review; no endorsement.' } = {}) {
  return `# App

[Apps](README.md#web-apps)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://example.com/app) |
| Tags | ${tagText(tags)} |
| Product homepage | [Product](https://example.com/app) |
| Pricing and access | [Pricing](https://example.com/pricing) checked on the fixture review date. |
| Jev evidence | [Integration](https://example.com/integration) |
| Disclosure | ${disclosure} |
| License | [License](https://example.com/license) |
`;
}

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'jev-directory-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  for (const kind of ['apps', 'tools']) {
    fs.mkdirSync(path.join(root, 'community/projects', kind), { recursive: true });
  }
  const write = (file, text) => fs.writeFileSync(path.join(root, file), text);
  write('README.md', '# List\n\n## Community projects\n\n### Apps powered by Jev\n\n- [App](https://example.com/app) - An app.\n\n### Developer projects and integrations\n\n- [Example](https://github.com/acme/example) - A tool. [Details](community/projects/tools/example.md).\n\n## Other\n');
  write('community/projects/tools/README.md', '# Browse\n\n## Tools\n\n| Project | Use |\n| --- | --- |\n| [Example](example.md) | A tool |\n');
  write('community/projects/tools/example.md', '# Example\n\n[Tools](README.md#tools)\n\n[Source](https://github.com/acme/example)\n');
  const setApp = ({ tags = ['Open source', 'Free'], ...options } = {}) => {
    write('community/projects/apps/README.md', `# Apps\n\n## Web apps\n\n${tagText(tags)}\n\n[App](app.md)\n`);
    write('community/projects/apps/app.md', appPage({ tags, ...options }));
    const main = path.join(root, 'README.md');
    fs.writeFileSync(main, fs.readFileSync(main, 'utf8').replace(/^- \[App\].*$/m,
      `- [App](https://example.com/app) - ${tagText(tags)}. An app. [Details](community/projects/apps/app.md).`));
  };
  setApp();
  write('community/projects/README.md', '# Projects\n\n[Apps](apps/README.md) · [Tools](tools/README.md)\n');
  return { root, write, setApp };
}

test('accepts connected pages, table entries, and canonical GitHub URL variants', t => {
  const { root, write } = fixture(t);
  write('community/projects/tools/example.md', '# Example\n\n[Tools](README.md#tools)\n\n[Source](https://github.com/ACME/Example.git)\n');
  assert.deepEqual(checkCommunity(root), { errors: [], count: 2 });
});

test('rejects a new README project without a detail page', t => {
  const { root } = fixture(t);
  const file = path.join(root, 'README.md');
  fs.writeFileSync(file, fs.readFileSync(file, 'utf8').replace('## Other', '- [New](https://github.com/acme/new) - Another tool.\n\n## Other'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('no project page for https://github.com/acme/new')));
});

test('rejects orphan pages and an omitted directory listing', t => {
  const { root, write } = fixture(t);
  write('community/projects/tools/extra.md', '# Extra\n\n[Source](https://github.com/acme/extra)\n');
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('extra.md: missing from the README')));
  assert.ok(errors.some(error => error.includes('extra.md: index exactly once')));
});

test('rejects duplicate category listings', t => {
  const { root } = fixture(t);
  fs.appendFileSync(path.join(root, 'community/projects/tools/README.md'), '\n## More\n\n[Example](example.md)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('index exactly once')));
});

test('rejects a page linked from the wrong category', t => {
  const { root, write } = fixture(t);
  write('community/projects/tools/example.md', '# Example\n\n[Other](README.md#other)\n\n[Source](https://github.com/acme/example)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('link back to its category')));
});

test('rejects an index entry whose project page is missing', t => {
  const { root } = fixture(t);
  fs.unlinkSync(path.join(root, 'community/projects/tools/example.md'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('Index links to missing project page')));
});

test('rejects a README entry without a detail-page link', t => {
  const { root, write } = fixture(t);
  write('README.md', '# List\n\n## Community projects\n\n### Developer projects and integrations\n\n- [Example](https://github.com/acme/example) - A tool.\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('README entry must also link')));
});

test('rejects duplicate sources and requires a usable canonical source', t => {
  const { root, write } = fixture(t);
  write('community/projects/tools/duplicate.md', '# Duplicate\n\n[Source](https://github.com/acme/example)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('duplicate source')));
  write('community/projects/tools/duplicate.md', '# Duplicate\n\n[Source](http://example.com)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('canonical HTTPS')));
});

test('rejects an app listed in the tools index even with a matching backlink', t => {
  const { root, write } = fixture(t);
  write('community/projects/apps/README.md', '# Apps\n');
  fs.appendFileSync(path.join(root, 'community/projects/tools/README.md'), '\n[App](../apps/app.md)\n');
  write('community/projects/apps/app.md', appPage().replace('[Apps](README.md#web-apps)', '[Tools](../tools/README.md#tools)'));
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('belongs in the apps index, not tools')));
  assert.ok(errors.some(error => error.includes('link back to its category')));
});

test('rejects an app under the developer heading in the root README', t => {
  const { root } = fixture(t);
  const main = path.join(root, 'README.md');
  fs.writeFileSync(main, fs.readFileSync(main, 'utf8').replace('### Apps powered by Jev', '### Developer projects and integrations'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('app.md: README entry belongs under Apps powered by Jev')));
});

test('rejects duplicate sources across the app and tool directories', t => {
  const { root, write } = fixture(t);
  write('community/projects/apps/app.md', appPage().replace('[Source](https://example.com/app)', '[Source](https://github.com/acme/example)'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('duplicate source')));
});

test('rejects detail pages left in the mixed project folder', t => {
  const { root, write } = fixture(t);
  write('community/projects/stray.md', '# Stray\n\n[Source](https://example.com/stray)\n');
  assert.ok(checkCommunity(root).errors.some(error => error.includes('put project pages in apps/ or tools/')));
});

test('directory navigation links are not project listings', t => {
  const { root } = fixture(t);
  fs.appendFileSync(path.join(root, 'community/projects/apps/README.md'), '\n[All projects](../README.md) · [Tools](../tools/README.md)\n');
  assert.deepEqual(checkCommunity(root), { errors: [], count: 2 });
});

test('accepts a closed-source commercial app with product, pricing, evidence and disclosure', t => {
  const { root, setApp } = fixture(t);
  setApp({ tags: ['Closed source', 'Commercial', 'Paid'],
    disclosure: 'Closed source; implementation was not inspected. Vendor documentation supports Jev use. Commercial paid product, no affiliation or endorsement.' });
  assert.deepEqual(checkCommunity(root), { errors: [], count: 2 });
});

test('open-source and commercial tags can coexist', t => {
  const { root, setApp } = fixture(t);
  setApp({ tags: ['Open source', 'Commercial', 'Freemium'], disclosure: 'Commercial hosted plans with an ongoing free tier; source inspected. No endorsement.' });
  assert.deepEqual(checkCommunity(root), { errors: [], count: 2 });
});

test('paid apps require a commercial tag and an official pricing or access link', t => {
  const { root, setApp, write } = fixture(t);
  setApp({ tags: ['Open source', 'Paid'] });
  assert.ok(checkCommunity(root).errors.some(error => error.includes('must also carry the Commercial tag')));
  const options = { tags: ['Open source', 'Commercial', 'Paid'], disclosure: 'Commercial paid product; no endorsement.' };
  setApp(options);
  write('community/projects/apps/app.md', appPage(options).replace('[Pricing](https://example.com/pricing)', 'Contact vendor'));
  assert.ok(checkCommunity(root).errors.some(error => error.includes('official pricing or access/contact link')));
});

test('closed-source apps require a visible source-review disclosure and public Jev evidence', t => {
  const { root, setApp, write } = fixture(t);
  const options = { tags: ['Closed source', 'Pricing unverified'] };
  setApp(options);
  write('community/projects/apps/app.md', appPage(options).replace('[Integration](https://example.com/integration)', 'Uses AI'));
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('Closed source in the Disclosure')));
  assert.ok(errors.some(error => error.includes('Jev evidence needs a public HTTPS link')));
});

test('rejects contradictory source tags and unlabeled pricing', t => {
  const { root, setApp } = fixture(t);
  setApp({ tags: ['Open source', 'Closed source'] });
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('exactly one source-access tag')));
  assert.ok(errors.some(error => error.includes('exactly one pricing tag')));
});

test('rejects missing product details and unsupported open-source labels', t => {
  const { root, write } = fixture(t);
  write('community/projects/apps/app.md', appPage()
    .replace('| Product homepage | [Product](https://example.com/app) |\n', '')
    .replace('| License | [License](https://example.com/license) |\n', ''));
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('Product homepage metadata row')));
  assert.ok(errors.some(error => error.includes('Open source apps need a license link')));
});

test('rejects missing or mismatched tags in either discovery listing', t => {
  const { root, setApp } = fixture(t);
  setApp({ tags: ['Closed source', 'Commercial', 'Paid'], disclosure: 'Closed source; source not inspected. Commercial paid product; no endorsement.' });
  for (const name of ['README.md', 'community/projects/apps/README.md']) {
    const file = path.join(root, name);
    fs.writeFileSync(file, fs.readFileSync(file, 'utf8').replace('`Commercial` · `Paid`', '`Free`'));
  }
  const { errors } = checkCommunity(root);
  assert.ok(errors.some(error => error.includes('app index must show the same tags')));
  assert.ok(errors.some(error => error.includes('README entry must show the same tags')));
});
