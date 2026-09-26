#!/usr/bin/env node
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import YAML from 'yaml';
import { generateScene } from './generate.js';
import { exportSizes } from './resize.js';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');

// Minimal .env loader (no dependency): KEY=value lines, ignores comments.
try {
  const env = await readFile(path.join(root, '.env'), 'utf8');
  for (const line of env.split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*?)\s*$/);
    if (m && !process.env[m[1]]) process.env[m[1]] = m[2].replace(/^['"]|['"]$/g, '');
  }
} catch {}

const args = process.argv.slice(2);
const flag = (name) => args.includes(name);
const opt = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : undefined;
};

const model = process.env.GEMINI_IMAGE_MODEL || 'gemini-3.1-flash-image';
const outDir = path.resolve(root, process.env.OUT_DIR || './out');
const scenes = YAML.parse(await readFile(path.join(root, 'prompts/scenes.yaml'), 'utf8')).scenes;

let selected = scenes;
if (!flag('--all')) {
  const id = opt('--scene');
  if (!id) {
    console.log('Scenes available:\n' + scenes.map((s) => `  ${s.id.padEnd(34)} ${s.segment}  ${s.title}`).join('\n'));
    console.log('\nusage: npm run gen -- --scene <id> | --all [--no-export]');
    process.exit(0);
  }
  selected = scenes.filter((s) => s.id === id);
  if (!selected.length) {
    console.error(`Unknown scene "${id}"`);
    process.exit(1);
  }
}

for (const scene of selected) {
  console.log(`\n▶ ${scene.id} (${model})`);
  const masters = await generateScene({ apiKey: process.env.GEMINI_API_KEY, model, scene, outDir });
  masters.forEach((f) => console.log('  master', path.relative(root, f)));
  if (!flag('--no-export')) {
    const files = await exportSizes(path.join(outDir, scene.id));
    files.forEach((f) => console.log('  export', path.relative(root, f)));
  }
}
console.log('\nDone. Run `npm run check` before uploading to Google Ads.');
