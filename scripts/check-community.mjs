// SPDX-License-Identifier: MIT
// Keep the README list, separate app/tool indexes, and detail pages connected.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import MarkdownIt from 'markdown-it';
import GithubSlugger from 'github-slugger';

const parser = new MarkdownIt();
const sourceTags = ['Open source', 'Source available', 'Closed source', 'Source unverified'];
const pricingTags = ['Free', 'Free source build', 'Freemium', 'Paid', 'Pricing unverified'];
const appTags = new Set([...sourceTags, ...pricingTags, 'Commercial', 'BYOK']);

function tableRows(tokens) {
  const rows = new Map();
  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i].type !== 'tr_open') continue;
    const cells = [];
    while (++i < tokens.length && tokens[i].type !== 'tr_close') {
      if (tokens[i].type === 'inline') cells.push(tokens[i]);
    }
    if (cells.length === 2) {
      const plain = token => (token.children ?? []).map(child => child.content).join('').trim();
      rows.set(plain(cells[0]), { text: plain(cells[1]), links: links([cells[1]]) });
    }
  }
  return rows;
}

function checkAppMetadata(tokens, name, errors) {
  const rows = tableRows(tokens);
  const tags = (rows.get('Tags')?.text ?? '').split('·').map(tag => tag.trim()).filter(Boolean);
  if (sourceTags.filter(tag => tags.includes(tag)).length !== 1) {
    errors.push(`${name}: Tags must include exactly one source-access tag.`);
  }
  if (pricingTags.filter(tag => tags.includes(tag)).length !== 1) {
    errors.push(`${name}: Tags must include exactly one pricing tag.`);
  }
  if (tags.some(tag => !appTags.has(tag)) || new Set(tags).size !== tags.length) {
    errors.push(`${name}: Tags contain unknown or duplicate values; use community/APP_TAGS.md.`);
  }
  for (const field of ['Product homepage', 'Pricing and access', 'Jev evidence', 'Disclosure']) {
    if (!rows.get(field)?.text) errors.push(`${name}: provide the ${field} metadata row.`);
  }
  for (const field of ['Product homepage', 'Jev evidence']) {
    if (!rows.get(field)?.links.some(link => sourceKey(link.href))) {
      errors.push(`${name}: ${field} needs a public HTTPS link.`);
    }
  }
  if (tags.some(tag => ['Paid', 'Freemium'].includes(tag)) && !tags.includes('Commercial')) {
    errors.push(`${name}: Paid and Freemium apps must also carry the Commercial tag.`);
  }
  if (tags.includes('Commercial') && !rows.get('Pricing and access')?.links.some(link => sourceKey(link.href))) {
    errors.push(`${name}: Commercial apps need an official pricing or access/contact link.`);
  }
  if (tags.includes('Closed source') && !/closed source/i.test(rows.get('Disclosure')?.text ?? '')) {
    errors.push(`${name}: explicitly identify Closed source in the Disclosure row and explain review limits.`);
  }
  if (tags.includes('Commercial') && !/commercial/i.test(rows.get('Disclosure')?.text ?? '')) {
    errors.push(`${name}: explicitly identify Commercial access in the Disclosure row.`);
  }
  if (tags.includes('Open source') && !rows.get('License')?.links.some(link => sourceKey(link.href))) {
    errors.push(`${name}: Open source apps need a license link.`);
  }
  return tags;
}

function visibleTags(tokens) {
  return tokens.flatMap(token => token.children ?? [])
    .filter(token => token.type === 'code_inline' && appTags.has(token.content))
    .map(token => token.content);
}

function sameTags(actual, expected) {
  return [...new Set(actual)].sort().join('|') === [...expected].sort().join('|');
}

function links(tokens) {
  const result = [];
  for (const token of tokens) {
    const children = token.children ?? [];
    for (let i = 0; i < children.length; i++) {
      if (children[i].type !== 'link_open') continue;
      let label = '';
      for (let j = i + 1; j < children.length && children[j].type !== 'link_close'; j++) {
        label += children[j].content;
      }
      result.push({ href: children[i].attrGet('href'), label });
    }
  }
  return result;
}

function sourceKey(href) {
  try {
    const url = new URL(href);
    if (url.protocol !== 'https:' || url.username || url.password) return null;
    url.hash = '';
    if (url.hostname === 'github.com') url.pathname = url.pathname.toLowerCase().replace(/\.git\/?$/, '');
    return url.href.replace(/\/$/, '');
  } catch {
    return null;
  }
}

function localTarget(base, href) {
  if (/^[a-z][a-z\d+.-]*:|^\/\//i.test(href)) return null;
  try {
    return path.resolve(base, decodeURIComponent(href.split(/[?#]/, 1)[0]));
  } catch {
    return null;
  }
}

export function checkCommunity(root) {
  root = path.resolve(root);
  const errors = [];
  const read = name => parser.parse(fs.readFileSync(path.join(root, name), 'utf8'), {});
  const projectRoot = path.join(root, 'community/projects');
  const collections = [
    { kind: 'apps', heading: 'Apps powered by Jev' },
    { kind: 'tools', heading: 'Developer projects and integrations' },
  ].map(collection => ({
    ...collection,
    directory: path.join(projectRoot, collection.kind),
    indexPath: path.join(projectRoot, collection.kind, 'README.md'),
  }));
  for (const name of fs.readdirSync(projectRoot)) {
    if (name.endsWith('.md') && name !== 'README.md') {
      errors.push(`${name}: put project pages in apps/ or tools/, not directly in community/projects/.`);
    }
  }
  const pages = new Map();
  const sources = new Map();
  for (const collection of collections) {
    const pageNames = fs.readdirSync(collection.directory)
      .filter(name => name.endsWith('.md') && name !== 'README.md');
    for (const name of pageNames) {
      const file = path.join(collection.directory, name);
      const tokens = read(path.relative(root, file));
      const references = links(tokens);
      const source = references.filter(link => link.label === 'Source');
      const key = source.length === 1 && sourceKey(source[0].href);
      if (!key) errors.push(`${name}: provide exactly one canonical HTTPS link labeled Source.`);
      if (key && sources.has(key)) errors.push(`${name}: duplicate source also used by ${sources.get(key)}.`);
      if (key) sources.set(key, `${collection.kind}/${name}`);
      if (tokens.filter(token => token.type === 'heading_open' && token.tag === 'h1').length !== 1) {
        errors.push(`${name}: provide one project title.`);
      }
      const tags = collection.kind === 'apps' ? checkAppMetadata(tokens, name, errors) : [];
      pages.set(file, { key, references, collection, tags, indexed: [] });
    }
  }

  for (const collection of collections) {
    let category = '';
    const slugger = new GithubSlugger();
    const index = read(path.relative(root, collection.indexPath));
    let tags = [];
    for (let i = 0; i < index.length; i++) {
      const token = index[i];
      if (token.type === 'heading_open' || token.type === 'tr_open') tags = [];
      tags.push(...visibleTags([token]));
      if (token.type === 'heading_open') {
        const slug = slugger.slug(index[i + 1].content);
        if (token.tag === 'h2') category = slug;
      }
      for (const link of links([token])) {
        const target = localTarget(collection.directory, link.href);
        if (!target || !target.startsWith(`${projectRoot}${path.sep}`)
          || !target.endsWith('.md') || path.basename(target) === 'README.md') continue;
        const page = pages.get(target);
        if (!page) errors.push(`Index links to missing project page: ${link.href}.`);
        else {
          if (page.collection.kind !== collection.kind) {
            errors.push(`${link.href}: belongs in the ${page.collection.kind} index, not ${collection.kind}.`);
          }
          if (page.collection.kind === 'apps' && !sameTags(tags, page.tags)) {
            errors.push(`${link.href}: app index must show the same tags as the detail page before its guide link.`);
          }
          page.indexed.push({ category, indexPath: collection.indexPath });
        }
      }
    }
  }

  const rootTokens = read('README.md');
  const sectionStart = rootTokens.findIndex((token, i) => token.type === 'heading_open'
    && token.tag === 'h2' && rootTokens[i + 1].content === 'Community projects');
  if (sectionStart < 0) errors.push('README.md: Community projects section is missing.');
  let sectionEnd = sectionStart + 1;
  while (sectionEnd < rootTokens.length && !(rootTokens[sectionEnd].type === 'heading_open'
    && rootTokens[sectionEnd].tag === 'h2')) sectionEnd++;
  const section = rootTokens.slice(sectionStart, sectionEnd);
  const entries = new Map();
  let heading = '';
  for (let i = 0; i < section.length; i++) {
    if (section[i].type === 'heading_open' && section[i].tag === 'h3') heading = section[i + 1].content;
    if (section[i].type !== 'list_item_open') continue;
    let end = i + 1;
    while (end < section.length && section[end].type !== 'list_item_close') end++;
    const refs = links(section.slice(i, end));
    const external = refs.find(link => sourceKey(link.href));
    const key = external && sourceKey(external.href);
    if (!key) errors.push('README.md: each community entry needs its canonical source link.');
    else if (entries.has(key)) errors.push(`README.md: duplicate community entry for ${external.href}.`);
    else entries.set(key, { refs, heading, tags: visibleTags(section.slice(i, end)) });
    i = end;
  }
  for (const [key] of entries) {
    if (!sources.has(key)) errors.push(`README.md: no project page for ${key}.`);
  }
  for (const [file, page] of pages) {
    const name = path.basename(file);
    const entry = entries.get(page.key);
    if (!entry) errors.push(`${name}: missing from the README community list.`);
    else {
      if (!entry.refs.some(link => localTarget(root, link.href) === file)) {
        errors.push(`${name}: README entry must also link to its project page.`);
      }
      if (entry.heading !== page.collection.heading) {
        errors.push(`${name}: README entry belongs under ${page.collection.heading}.`);
      }
      if (page.collection.kind === 'apps' && !sameTags(entry.tags, page.tags)) {
        errors.push(`${name}: README entry must show the same tags as the app detail page.`);
      }
    }
    if (page.indexed.length !== 1 || !page.indexed[0].category) {
      errors.push(`${name}: index exactly once under a category heading.`);
    } else if (page.indexed[0].indexPath !== page.collection.indexPath
      || !page.references.some(link => localTarget(path.dirname(file), link.href) === page.collection.indexPath
        && link.href.split('#')[1] === page.indexed[0].category)) {
      errors.push(`${name}: link back to its category in community/projects/${page.collection.kind}/README.md.`);
    }
  }
  return { errors, count: pages.size };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  try {
    const { errors, count } = checkCommunity(root);
    if (errors.length) {
      console.error(errors.join('\n'));
      process.exitCode = 1;
    } else console.log(`Checked ${count} community projects across README, app/tool indexes, and detail pages.`);
  } catch (error) {
    console.error(`Community directory check failed: ${error.message}`);
    process.exitCode = 1;
  }
}
