# Gemini ad-creative generator

Generates photorealistic image assets for Google Ads (Search image assets, Performance Max, Demand Gen, Display) from a prompt library tuned for a Montreal mobile self-storage business, then exports every Google-required size.

## Setup

```bash
cd tools/gemini-creatives
npm install
cp .env.example .env   # paste your GEMINI_API_KEY
```

## Generate

```bash
# one scene, all sizes
npm run gen -- --scene winter-car-container

# every scene in prompts/scenes.yaml (FR text-free images, safe for Quebec)
npm run gen:all

# only produce the raw 16:9 master and 1:1 master without the ad-size exports
npm run gen -- --scene boat-trailer-loading --no-export
```

Outputs land in `out/<scene>/`:

| File | Size | Used for |
|---|---|---|
| `landscape_1200x628.jpg` | 1.91:1 | Search image assets, PMax, Demand Gen, Display |
| `square_1200x1200.jpg` | 1:1 | Search image assets, PMax, Demand Gen |
| `portrait_960x1200.jpg` | 4:5 | PMax, Demand Gen (mobile feeds) |
| `logo_1200x1200.png` and `logo_1200x300.png` | 1:1 and 4:1 | PMax logos (drop your own logo here, not generated) |
| `master_16x9.png`, `master_1x1.png` | native | archive |

`npm run check` validates every exported file against Google's size, aspect and 5 MB limits before you upload.

## Rules baked in

- No text rendered inside images (Google rejects images with heavy text overlays, and text in images shown in Quebec would have to be in French; keeping images text-free avoids both problems).
- Every prompt describes a Montreal-style setting (duplex with exterior staircase, brick triplex, Plateau alley, South Shore bungalow, Old Port restaurant terrace) so the creative reads as local.
- SynthID watermark is applied by Google automatically to generated images; that is fine for ads.
- Images are photorealistic, never depict a competitor's branding, and never show a real licence plate.
