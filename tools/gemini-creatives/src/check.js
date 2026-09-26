// Validate exported files against Google Ads image asset limits before upload.
import sharp from 'sharp';
import { readdir, stat } from 'node:fs/promises';
import path from 'node:path';

const RULES = {
  'landscape_1200x628.jpg': { ratio: 1.91, minW: 600, minH: 314 },
  'square_1200x1200.jpg': { ratio: 1.0, minW: 300, minH: 300 },
  'portrait_960x1200.jpg': { ratio: 0.8, minW: 480, minH: 600 },
};
const MAX_BYTES = 5120 * 1024;

const outDir = process.argv[2] || process.env.OUT_DIR || './out';
let problems = 0;
for (const scene of await readdir(outDir)) {
  const sceneDir = path.join(outDir, scene);
  if (!(await stat(sceneDir)).isDirectory()) continue;
  for (const [file, rule] of Object.entries(RULES)) {
    const p = path.join(sceneDir, file);
    try {
      const meta = await sharp(p).metadata();
      const { size } = await stat(p);
      const ratio = meta.width / meta.height;
      const ok = Math.abs(ratio - rule.ratio) < 0.02 && meta.width >= rule.minW && meta.height >= rule.minH && size <= MAX_BYTES;
      console.log(`${ok ? 'OK ' : 'BAD'} ${scene}/${file} ${meta.width}x${meta.height} ${(size / 1024).toFixed(0)}KB`);
      if (!ok) problems++;
    } catch {
      console.log(`MISSING ${scene}/${file}`);
      problems++;
    }
  }
}
process.exit(problems ? 1 : 0);
