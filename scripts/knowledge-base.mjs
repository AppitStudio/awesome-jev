import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const collectionRoot = path.join(root, 'community/knowledge-base');
const articleRoot = path.join(collectionRoot, 'articles');
const write = process.argv.includes('--write');
const errors = [];
const pendingWrites = new Map();
const projectPaths = new Set();

function readJson(file) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (error) {
    errors.push(`${path.relative(root, file)}: ${error.message}`);
    return null;
  }
}

function requireText(value, label) {
  if (typeof value !== 'string' || value.trim() === '') errors.push(`${label} must be a nonempty string`);
}

function requireDate(value, label) {
  const parsed = typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value) ? new Date(`${value}T00:00:00Z`) : null;
  if (!parsed || Number.isNaN(parsed.getTime()) || parsed.toISOString().slice(0, 10) !== value) errors.push(`${label} must be a real ISO date`);
}

function requireHttps(value, label) {
  if (typeof value !== 'string' || !/^https:\/\/[^\s/]+/i.test(value)) errors.push(`${label} must be an HTTPS URL`);
}

// Reads raster dimensions from file headers so the validator needs no image dependency.
function imageSize(file) {
  const data = fs.readFileSync(file);
  if (data.length >= 24 && data.toString('latin1', 1, 4) === 'PNG') return { width: data.readUInt32BE(16), height: data.readUInt32BE(20) };
  if (data.length >= 30 && data.toString('latin1', 0, 4) === 'RIFF' && data.toString('latin1', 8, 12) === 'WEBP') {
    const format = data.toString('latin1', 12, 16);
    if (format === 'VP8X') return { width: 1 + data.readUIntLE(24, 3), height: 1 + data.readUIntLE(27, 3) };
    if (format === 'VP8 ') return { width: data.readUInt16LE(26) & 0x3fff, height: data.readUInt16LE(28) & 0x3fff };
    if (format === 'VP8L') { const bits = data.readUInt32LE(21); return { width: (bits & 0x3fff) + 1, height: ((bits >> 14) & 0x3fff) + 1 }; }
  }
  if (data[0] === 0xff && data[1] === 0xd8) {
    for (let offset = 2; offset + 9 < data.length;) {
      if (data[offset] !== 0xff) { offset++; continue; }
      const marker = data[offset + 1];
      if (marker >= 0xc0 && marker <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(marker)) return { width: data.readUInt16BE(offset + 7), height: data.readUInt16BE(offset + 5) };
      offset += 2 + data.readUInt16BE(offset + 2);
    }
  }
  return null;
}

function managedBlock(content, kind, body, file) {
  const start = `<!-- knowledge:${kind}:start -->`;
  const end = `<!-- knowledge:${kind}:end -->`;
  const block = `${start}\n${body.trim()}\n${end}`;
  const pattern = new RegExp(`${start}[\\s\\S]*?${end}`, 'g');
  const matches = content.match(pattern) ?? [];
  if (matches.length > 1) errors.push(`${file}: duplicate ${kind} blocks`);
  const expected = matches.length ? content.replace(pattern, block) : `${content.trimEnd()}\n\n${block}\n`;
  if (write) {
    if (expected !== content) pendingWrites.set(file, expected);
  } else if (expected !== content) {
    errors.push(`${file}: generated ${kind} block is missing or stale; run node scripts/knowledge-base.mjs --write`);
  }
}

const collection = readJson(path.join(collectionRoot, 'collection.json'));
const topics = readJson(path.join(collectionRoot, 'topics.json'));
if (!topics || topics.schema_version !== 1 || !Array.isArray(topics.topics) || topics.topics.length === 0 || topics.topics.some((topic) => typeof topic !== 'string' || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(topic)) || new Set(topics.topics).size !== topics.topics.length) errors.push('topics.json must have a unique list of topic slugs');
const allowedTopics = new Set(topics?.topics ?? []);
if (!collection || collection.schema_version !== 1 || !Array.isArray(collection.articles)) errors.push('collection.json must have schema_version 1 and articles array');
const slugs = collection?.articles ?? [];
if (new Set(slugs).size !== slugs.length) errors.push('collection.json has duplicate article slugs');
if (slugs.length === 0 && collection?.retire_all !== true) errors.push('an empty collection requires retire_all: true');

const sidecars = fs.readdirSync(articleRoot).filter((name) => name.endsWith('.json')).map((name) => name.slice(0, -5));
for (const slug of sidecars) if (!slugs.includes(slug)) errors.push(`${slug}.json is not registered in collection.json`);
for (const name of fs.readdirSync(articleRoot).filter((file) => file.endsWith('.md'))) if (!slugs.includes(name.slice(0, -3))) errors.push(`${name} is not registered in collection.json`);

const published = [];
const backlinks = new Map();
for (const slug of slugs) {
  const label = `articles/${slug}`;
  if (typeof slug !== 'string' || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug)) { errors.push(`${label}: invalid slug`); continue; }
  const metadata = readJson(path.join(articleRoot, `${slug}.json`));
  const markdownPath = path.join(articleRoot, `${slug}.md`);
  if (!fs.existsSync(markdownPath)) { errors.push(`${label}.md is missing`); continue; }
  const markdown = fs.readFileSync(markdownPath, 'utf8');
  if (!metadata) continue;
  if (metadata.schema_version !== 1) errors.push(`${label}: unsupported schema_version`);
  if (metadata.id !== slug || metadata.slug !== slug) errors.push(`${label}: id, slug and filename must match`);
  for (const key of ['title', 'description', 'language']) requireText(metadata[key], `${label}.${key}`);
  if (metadata.language !== 'en') errors.push(`${label}: only en is supported by the current site`);
  if (!['draft', 'published', 'retired'].includes(metadata.status)) errors.push(`${label}: invalid status`);
  requireDate(metadata.published_at, `${label}.published_at`);
  requireDate(metadata.modified_at, `${label}.modified_at`);
  if (metadata.modified_at < metadata.published_at) errors.push(`${label}: modified_at precedes published_at`);
  if (!Array.isArray(metadata.topics) || metadata.topics.length === 0 || !metadata.topics.every((topic) => allowedTopics.has(topic)) || new Set(metadata.topics).size !== metadata.topics.length) errors.push(`${label}: topics must be unique slugs registered in topics.json`);
  const source = metadata.source ?? {};
  requireText(source.title, `${label}.source.title`);
  requireHttps(source.url, `${label}.source.url`);
  requireText(source.author?.name, `${label}.source.author.name`);
  requireHttps(source.author?.url, `${label}.source.author.url`);
  requireDate(source.published_at, `${label}.source.published_at`);
  requireDate(source.accessed_at, `${label}.source.accessed_at`);
  if (!Array.isArray(metadata.credits?.guide_authors) || metadata.credits.guide_authors.length === 0) errors.push(`${label}: guide_authors required`);
  for (const author of metadata.credits?.guide_authors ?? []) {
    requireText(author.name, `${label}.guide_author.name`); requireText(author.role, `${label}.guide_author.role`);
    if (!['Person', 'Organization'].includes(author.type)) errors.push(`${label}.guide_author.type must be Person or Organization`);
  }
  if (!Array.isArray(metadata.credits?.reviewers)) errors.push(`${label}: reviewers must be an array (empty when none)`);
  for (const reviewer of metadata.credits?.reviewers ?? []) requireText(reviewer.name, `${label}.reviewer.name`);
  for (const key of ['source', 'offline', 'live', 'review']) requireText(metadata.verification?.[key], `${label}.verification.${key}`);
  if (metadata.image !== undefined) {
    const image = metadata.image ?? {};
    if (typeof image.path !== 'string' || !/^community\/knowledge-base\/images\/[a-z0-9]+(?:-[a-z0-9]+)*\.(?:png|jpe?g|webp)$/.test(image.path) || !fs.existsSync(path.join(root, image.path))) errors.push(`${label}.image.path must be an existing PNG, JPEG or WebP in community/knowledge-base/images/`);
    else {
      const size = imageSize(path.join(root, image.path));
      if (!size || size.width < 1200) errors.push(`${label}.image must be a readable image at least 1200 pixels wide`);
    }
    for (const key of ['alt', 'credit', 'license']) requireText(image[key], `${label}.image.${key}`);
    for (const key of ['license_url', 'source_url']) if (image[key] !== undefined) requireHttps(image[key], `${label}.image.${key}`);
  }
  if (!markdown.startsWith(`# ${metadata.title}\n`)) errors.push(`${label}: Markdown H1 must match title`);
  for (const heading of ['Key takeaways', 'Validation and limits', 'Adoption questions', 'Sources, credits and corrections']) if (!markdown.includes(`## ${heading}`)) errors.push(`${label}: missing ${heading} section`);
  if (!markdown.includes(source.url) || !markdown.includes(source.author?.url ?? '\u0000')) errors.push(`${label}: source and author links must be visible`);
  if (!Array.isArray(metadata.faqs) || metadata.faqs.length === 0) errors.push(`${label}: FAQs required`);
  for (const faq of metadata.faqs ?? []) {
    requireText(faq.question, `${label}.faq.question`); requireText(faq.answer, `${label}.faq.answer`);
    if (!markdown.includes(`### ${faq.question}`)) errors.push(`${label}: FAQ question not visible in Markdown: ${faq.question}`);
    if (typeof faq.answer === 'string' && !markdown.includes(faq.answer)) errors.push(`${label}: FAQ answer not visible in Markdown: ${faq.question}`);
  }
  if (!Array.isArray(metadata.connections)) errors.push(`${label}: connections must be an array`);
  const seenConnections = new Set();
  for (const connection of metadata.connections ?? []) {
    const relation = `${label}.connection(${connection.path})`;
    if (!['project', 'resource'].includes(connection.kind)) errors.push(`${relation}: invalid kind`);
    if (!['source-mentioned', 'jevlist-suggestion'].includes(connection.origin)) errors.push(`${relation}: invalid origin`);
    if (!['implements-step', 'alternative', 'teaching-example', 'evaluation'].includes(connection.purpose)) errors.push(`${relation}: invalid purpose`);
    for (const key of ['step', 'why', 'limitations']) requireText(connection[key], `${relation}.${key}`);
    if (typeof connection.path !== 'string' || !/^(community\/projects\/(?:apps|tools)\/[a-z0-9._-]+\.md|projects\/[a-z0-9._/-]+\/README\.md)$/.test(connection.path) || !fs.existsSync(path.join(root, connection.path))) errors.push(`${relation}: missing or invalid repository path`);
    if (connection.kind === 'project' && !/^community\/projects\/(apps|tools)\//.test(connection.path)) errors.push(`${relation}: project must use a community detail page`);
    if (connection.kind === 'resource' && !connection.path?.startsWith('projects/')) errors.push(`${relation}: resource must use a native project README`);
    if (seenConnections.has(connection.path)) errors.push(`${relation}: duplicate connection`);
    seenConnections.add(connection.path);
    if (!Array.isArray(connection.evidence) || connection.evidence.length === 0) errors.push(`${relation}: evidence required`);
    for (const evidence of connection.evidence ?? []) if (!/^https:\/\//.test(evidence) && !fs.existsSync(path.join(root, evidence))) errors.push(`${relation}: invalid evidence ${evidence}`);
    if (connection.kind === 'project') {
      projectPaths.add(connection.path);
      if (metadata.status === 'published') backlinks.set(connection.path, [...(backlinks.get(connection.path) ?? []), metadata]);
    }
  }
  if (metadata.status === 'published') published.push(metadata);
}

if (published.length === 0 && collection?.retire_all !== true) errors.push('no published guides; set retire_all: true only for intentional retirement');
if (collection?.retire_all === true && published.length > 0) errors.push('retire_all conflicts with published guides');
const indexBody = published.map((guide) => `- [${guide.title}](articles/${guide.slug}.md) — ${guide.description} Based on [${guide.source.title}](${guide.source.url}) by [${guide.source.author.name}](${guide.source.author.url}).`).join('\n');
managedBlock(fs.readFileSync(path.join(collectionRoot, 'README.md'), 'utf8'), 'index', indexBody || '_No published guides._', 'community/knowledge-base/README.md');

for (const directory of ['community/projects/apps', 'community/projects/tools']) {
  for (const name of fs.readdirSync(path.join(root, directory)).filter((file) => file.endsWith('.md') && file !== 'README.md')) {
    const file = `${directory}/${name}`;
    const content = fs.readFileSync(path.join(root, file), 'utf8');
    if (!projectPaths.has(file) && !content.includes('<!-- knowledge:backlinks:start -->')) continue;
    const guides = backlinks.get(file) ?? [];
    const body = guides.length ? `## Knowledge guides\n\n${guides.map((guide) => {
      const connection = guide.connections.find((item) => item.path === file);
      const origin = connection.origin === 'source-mentioned' ? 'Mentioned in the source article' : `Independently suggested by JevList; not an endorsement by ${guide.source.author.name}`;
      return `- [${guide.title}](../../knowledge-base/articles/${guide.slug}.md) — ${origin}. ${connection.step}.`;
    }).join('\n')}` : '';
    if (guides.length) managedBlock(content, 'backlinks', body, file);
    else {
      const stripped = content.replace(/\n*<!-- knowledge:backlinks:start -->[\s\S]*?<!-- knowledge:backlinks:end -->\n?/g, '\n');
      if (write) pendingWrites.set(file, stripped);
      else if (stripped !== content) errors.push(`${file}: stale backlinks; run node scripts/knowledge-base.mjs --write`);
    }
  }
}

if (errors.length) { console.error(errors.join('\n')); process.exit(1); }
for (const [file, content] of pendingWrites) fs.writeFileSync(path.join(root, file), content);
console.log(`Knowledge base valid: ${slugs.length} registered, ${published.length} published, ${projectPaths.size} project connections${write ? '; generated blocks updated' : ''}.`);
