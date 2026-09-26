// Gemini image generation for Google Ads creatives.
// Supports both generateContent (Gemini image models such as gemini-2.5-flash-image)
// and generateImages (Imagen models). The model is chosen with GEMINI_IMAGE_MODEL.
import { GoogleGenAI } from '@google/genai';
import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const STYLE_SUFFIX =
  ' Photorealistic, natural daylight, shot on a full-frame camera with a 35mm lens, ' +
  'shallow depth of field, editorial advertising photography, no text, no logos, no watermarks, ' +
  'no licence plates readable, no people looking at the camera.';

const NEGATIVE =
  'text, letters, words, captions, logos, brand names, watermark, blurry, low resolution, ' +
  'cartoon, illustration, 3d render look, distorted hands, extra limbs, collage, split screen, frame, border';

export function buildPrompt(scene) {
  const base = `${scene.prompt.trim()}${STYLE_SUFFIX}`;
  // Gemini image models accept negative guidance inside the prompt; Imagen accepts negativePrompt.
  return { prompt: base, negative: `${NEGATIVE}${scene.negative ? ', ' + scene.negative : ''}` };
}

function isImagen(model) {
  return /^imagen/i.test(model);
}

// Gemini image models (gemini-3.1-flash-image, gemini-3-pro-image, gemini-2.5-flash-image) accept
// generateContent with responseModalities ['IMAGE'] and an imageConfig. imageSize is '1K' | '2K' | '4K'
// (2.5-flash-image ignores it). If the SDK in use exposes the newer Interactions API instead, we fall back to it.
async function generateWithGemini(ai, model, prompt, negative, aspectRatio) {
  const imageSize = process.env.GEMINI_IMAGE_SIZE || '2K';
  const contents = `${prompt}\n\nAvoid: ${negative}.`;
  try {
    const config = { responseModalities: ['IMAGE'], imageConfig: { aspectRatio } };
    if (!/2\.5-flash-image/.test(model)) config.imageConfig.imageSize = imageSize;
    const response = await ai.models.generateContent({ model, contents, config });
    const parts = response?.candidates?.[0]?.content?.parts ?? [];
    const img = parts.find((p) => p.inlineData?.data);
    if (!img) {
      const text = parts.map((p) => p.text).filter(Boolean).join(' ');
      throw new Error(`No image returned for aspect ${aspectRatio}. Model said: ${text || '(nothing)'}`);
    }
    return { bytes: Buffer.from(img.inlineData.data, 'base64'), mime: img.inlineData.mimeType || 'image/png' };
  } catch (err) {
    if (!ai.interactions?.create) throw err;
    // Interactions API (documented for Nano Banana 2 in 2026): response_format.type 'image'.
    const interaction = await ai.interactions.create({
      model,
      input: contents,
      response_format: { type: 'image', mime_type: 'image/png', aspect_ratio: aspectRatio, image_size: imageSize },
    });
    const data = interaction?.output_image?.data || interaction?.outputs?.find?.((o) => o.type === 'image')?.data;
    if (!data) throw err;
    return { bytes: Buffer.from(data, 'base64'), mime: 'image/png' };
  }
}

async function generateWithImagen(ai, model, prompt, negative, aspectRatio) {
  const response = await ai.models.generateImages({
    model,
    prompt,
    config: { numberOfImages: 1, aspectRatio, negativePrompt: negative, outputMimeType: 'image/png' },
  });
  const g = response?.generatedImages?.[0]?.image;
  if (!g?.imageBytes) throw new Error(`Imagen returned no image for aspect ${aspectRatio}`);
  return { bytes: Buffer.from(g.imageBytes, 'base64'), mime: 'image/png' };
}

/**
 * Generate the two master images (16:9 and 1:1) for one scene.
 * @param {object} opts
 * @param {string} opts.apiKey
 * @param {string} opts.model
 * @param {object} opts.scene  { id, prompt, negative? }
 * @param {string} opts.outDir
 * @param {string[]} [opts.aspects]  defaults to ['16:9', '1:1']
 */
export async function generateScene({ apiKey, model, scene, outDir, aspects = ['16:9', '1:1'] }) {
  if (!apiKey) throw new Error('GEMINI_API_KEY is missing. Put it in tools/gemini-creatives/.env');
  const ai = new GoogleGenAI({ apiKey });
  const { prompt, negative } = buildPrompt(scene);
  const sceneDir = path.join(outDir, scene.id);
  await mkdir(sceneDir, { recursive: true });

  const written = [];
  for (const aspect of aspects) {
    const gen = isImagen(model) ? generateWithImagen : generateWithGemini;
    const { bytes, mime } = await gen(ai, model, prompt, negative, aspect);
    const ext = mime.includes('jpeg') ? 'jpg' : 'png';
    const name = `master_${aspect.replace(':', 'x')}.${ext}`;
    const file = path.join(sceneDir, name);
    await writeFile(file, bytes);
    written.push(file);
  }
  await writeFile(path.join(sceneDir, 'prompt.txt'), `${prompt}\n\nNEGATIVE: ${negative}\n`);
  return written;
}
