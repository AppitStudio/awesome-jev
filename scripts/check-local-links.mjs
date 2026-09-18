// SPDX-License-Identifier: MIT
// Parse Markdown with markdown-it so fenced examples and reference links work.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import MarkdownIt from 'markdown-it';
import GithubSlugger from 'github-slugger';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const parser = new MarkdownIt({ html: true });
const excluded = new Set(['.git', 'node_modules', '.venv', 'lychee']);
const documents = new Map();

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const full = path.join(directory, entry.name);
    if (entry.isDirectory() && !excluded.has(entry.name)) walk(full);
    if (entry.isFile() && entry.name.endsWith('.md')) {
      const source = fs.readFileSync(full, 'utf8');
      const tokens = parser.parse(source, {});
      const slugger = new GithubSlugger();
      const anchors = new Set();
      for (let i = 0; i < tokens.length; i++) {
        if (tokens[i].type !== 'heading_open') continue;
        const text = (tokens[i + 1].children ?? [])
          .filter(token => ['text', 'code_inline', 'image'].includes(token.type))
          .map(token => token.content).join('');
        anchors.add(slugger.slug(text));
      }
      for (const match of source.matchAll(/<(?:a|span)\s[^>]*(?:id|name)=["']([^"']+)["']/gi)) {
        anchors.add(match[1]);
      }
      documents.set(full, { tokens, anchors });
    }
  }
}

walk(root);
const errors = [];
let checked = 0;
for (const [file, { tokens }] of documents) {
  for (const token of tokens.flatMap(item => [item, ...(item.children ?? [])])) {
    const href = token.attrGet('href') ?? token.attrGet('src');
    if (!href || /^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(href)) continue;
    checked++;
    const [rawPath, rawAnchor] = href.split('#', 2);
    let target;
    let anchor;
    try {
      target = rawPath ? path.resolve(path.dirname(file), decodeURIComponent(rawPath.split('?')[0])) : file;
      anchor = rawAnchor ? decodeURIComponent(rawAnchor) : '';
    } catch {
      errors.push(`${path.relative(root, file)}: invalid URI ${href}`);
      continue;
    }
    const relative = path.relative(root, target);
    if (relative === '..' || relative.startsWith(`..${path.sep}`) || path.isAbsolute(relative)) {
      errors.push(`${path.relative(root, file)}: link escapes repository: ${href}`);
    } else if (!fs.existsSync(target)) {
      errors.push(`${path.relative(root, file)}: missing target ${href}`);
    } else {
      if (fs.statSync(target).isDirectory()) target = path.join(target, 'README.md');
      if (anchor && documents.has(target) && !documents.get(target).anchors.has(anchor)) {
        errors.push(`${path.relative(root, file)}: missing anchor ${href}`);
      }
    }
  }
}
if (errors.length) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Checked ${checked} local links in ${documents.size} Markdown files.`);
}
