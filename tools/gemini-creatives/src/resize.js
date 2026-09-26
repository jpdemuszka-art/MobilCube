// Export Google Ads image sizes from the generated masters.
// Google requirements (Search image assets, PMax, Demand Gen):
//   landscape 1.91:1  -> 1200x628 (min 600x314)
//   square    1:1     -> 1200x1200 (min 300x300)
//   portrait  4:5     -> 960x1200 (min 480x600)   (PMax / Demand Gen)
//   max file size 5120 KB
import sharp from 'sharp';
import { readdir, stat } from 'node:fs/promises';
import path from 'node:path';

export const SIZES = [
  { name: 'landscape_1200x628.jpg', w: 1200, h: 628, from: '16x9' },
  { name: 'square_1200x1200.jpg', w: 1200, h: 1200, from: '1x1' },
  { name: 'portrait_960x1200.jpg', w: 960, h: 1200, from: '1x1' },
];

async function findMaster(sceneDir, tag) {
  const files = await readdir(sceneDir);
  const f = files.find((x) => x.startsWith(`master_${tag}.`));
  return f ? path.join(sceneDir, f) : null;
}

export async function exportSizes(sceneDir) {
  const out = [];
  for (const s of SIZES) {
    const master = (await findMaster(sceneDir, s.from)) || (await findMaster(sceneDir, '16x9')) || (await findMaster(sceneDir, '1x1'));
    if (!master) throw new Error(`No master image in ${sceneDir}`);
    const target = path.join(sceneDir, s.name);
    // "attention" strategy keeps the most visually salient region when cropping.
    await sharp(master)
      .resize(s.w, s.h, { fit: 'cover', position: sharp.strategy.attention })
      .jpeg({ quality: 88, mozjpeg: true })
      .toFile(target);
    const { size } = await stat(target);
    if (size > 5 * 1024 * 1024) {
      await sharp(master).resize(s.w, s.h, { fit: 'cover', position: sharp.strategy.attention }).jpeg({ quality: 72 }).toFile(target);
    }
    out.push(target);
  }
  return out;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const dir = process.argv[2];
  if (!dir) {
    console.error('usage: node src/resize.js <sceneDir>');
    process.exit(1);
  }
  exportSizes(dir).then((files) => files.forEach((f) => console.log('wrote', f)));
}
