// SPDX-License-Identifier: MIT
// Keep the existing README list, category index, and project pages connected.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import MarkdownIt from 'markdown-it';
import GithubSlugger from 'github-slugger';

const parser = new MarkdownIt();

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
  const directory = path.join(root, 'community/projects');
  const indexPath = path.join(root, 'community/README.md');
  const pageNames = fs.readdirSync(directory).filter(name => name.endsWith('.md'));
  const pages = new Map();
  const sources = new Map();
  for (const name of pageNames) {
    const file = path.join(directory, name);
    const tokens = read(`community/projects/${name}`);
    const references = links(tokens);
    const source = references.filter(link => link.label === 'Source');
    const key = source.length === 1 && sourceKey(source[0].href);
    if (!key) errors.push(`${name}: provide exactly one canonical HTTPS link labeled Source.`);
    if (key && sources.has(key)) errors.push(`${name}: duplicate source also used by ${sources.get(key)}.`);
    if (key) sources.set(key, name);
    if (tokens.filter(token => token.type === 'heading_open' && token.tag === 'h1').length !== 1) {
      errors.push(`${name}: provide one project title.`);
    }
    pages.set(file, { key, references, indexed: [] });
  }

  let category = '';
  const slugger = new GithubSlugger();
  const index = read('community/README.md');
  for (let i = 0; i < index.length; i++) {
    const token = index[i];
    if (token.type === 'heading_open') {
      const slug = slugger.slug(index[i + 1].content);
      if (token.tag === 'h2') category = slug;
    }
    for (const link of links([token])) {
      const target = localTarget(path.dirname(indexPath), link.href);
      if (!target || path.dirname(target) !== directory || !target.endsWith('.md')) continue;
      if (!pages.has(target)) errors.push(`Index links to missing project page: ${link.href}.`);
      else pages.get(target).indexed.push(category);
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
  for (let i = 0; i < section.length; i++) {
    if (section[i].type !== 'list_item_open') continue;
    let end = i + 1;
    while (end < section.length && section[end].type !== 'list_item_close') end++;
    const refs = links(section.slice(i, end));
    const external = refs.find(link => sourceKey(link.href));
    const key = external && sourceKey(external.href);
    if (!key) errors.push('README.md: each community entry needs its canonical source link.');
    else if (entries.has(key)) errors.push(`README.md: duplicate community entry for ${external.href}.`);
    else entries.set(key, refs);
    i = end;
  }
  for (const [key] of entries) {
    if (!sources.has(key)) errors.push(`README.md: no project page for ${key}.`);
  }
  for (const [file, page] of pages) {
    const name = path.basename(file);
    const entry = entries.get(page.key);
    if (!entry) errors.push(`${name}: missing from the README community list.`);
    else if (!entry.some(link => localTarget(root, link.href) === file)) {
      errors.push(`${name}: README entry must also link to its project page.`);
    }
    if (page.indexed.length !== 1 || !page.indexed[0]) {
      errors.push(`${name}: index exactly once under a category heading.`);
    } else if (!page.references.some(link => localTarget(path.dirname(file), link.href) === indexPath
      && link.href.split('#')[1] === page.indexed[0])) {
      errors.push(`${name}: link back to its category in community/README.md.`);
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
    } else console.log(`Checked ${count} community projects across README, category index, and detail pages.`);
  } catch (error) {
    console.error(`Community directory check failed: ${error.message}`);
    process.exitCode = 1;
  }
}
