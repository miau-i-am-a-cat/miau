# Freepik Image Generation - Quick Guide

Generate ultra-realistic product photos and ad creatives using Freepik's Mystic AI.

## Setup Complete ✓

- API Key stored in `.credentials.json`
- Script ready: `freepik_image_gen.py`
- Model: **Mystic AI** (Freepik's exclusive photorealistic generator)

## Quick Start

### Basic Generation
```bash
python freepik_image_gen.py "your prompt here" -o output.jpg
```

### Product Photos (Recommended Settings)
```bash
python freepik_image_gen.py \
  "professional product photo of [product] on white background, studio lighting, 8k, hyperrealistic" \
  -o product.jpg \
  --resolution 4k \
  --model super_real \
  --detailing 50 \
  --aspect square_1_1
```

### Ad Creatives with Style Reference
```bash
python freepik_image_gen.py \
  "modern minimalist cafe interior, natural light, people enjoying coffee" \
  -o ad_creative.jpg \
  --style-ref reference_style.jpg \
  --aspect widescreen_16_9 \
  --resolution 2k \
  --model realism
```

### Transform Sketch/Wireframe to Photo
```bash
python freepik_image_gen.py \
  "realistic product photography" \
  -o final.jpg \
  --structure-ref sketch.jpg \
  --structure-strength 70 \
  --resolution 4k
```

## Model Selection Guide

| Model | Best For | Characteristics |
|-------|----------|-----------------|
| `super_real` | Product photos, commercial work | Highest realism, production-ready |
| `realism` | General photography, natural look | Less "AI look", versatile |
| `editorial_portraits` | Close-up portraits | State-of-the-art faces (best for headshots) |
| `flexible` | Illustrations, fantasy, creative | Best prompt adherence, versatile |
| `fluid` | Creative/artistic work | Most prompt-following, Google Imagen 3 |
| `zen` | Clean/minimal aesthetic | Smoother, simpler results |

## Resolution & Aspect Ratios

### Resolution
- `1k` - Fast, preview quality
- `2k` - Good balance (default)
- `4k` - Highest quality, production-ready

### Common Aspect Ratios
- `square_1_1` - Instagram posts, profile photos
- `widescreen_16_9` - YouTube thumbnails, banners
- `social_story_9_16` - Instagram/Facebook stories
- `portrait_2_3` - Portrait photography
- `classic_4_3` - Traditional photos

## Advanced Features

### Reference Images

**Structure Reference** (controls composition/layout):
```bash
--structure-ref path/to/image.jpg --structure-strength 50
```
- Use for: Converting sketches, maintaining composition
- Strength: 0-100 (higher = more influence)

**Style Reference** (controls aesthetic/look):
```bash
--style-ref path/to/image.jpg --adherence 50 --hdr 50
```
- Use for: Matching brand aesthetics, artistic style
- Adherence: Higher = closer to prompt, lower = closer to style
- HDR: Higher = more detail, lower = more natural

### Creative Detailing
```bash
--detailing 33  # Default
--detailing 50  # More detail (product photos)
--detailing 20  # Softer, more natural
```

### Fixed Generation
```bash
--fixed  # Same settings = same output (useful for iterations)
```

## Example Workflows

### E-commerce Product Photo
```bash
python freepik_image_gen.py \
  "white ceramic coffee mug on marble countertop, soft natural light, professional product photography, clean background, commercial shoot, 8k" \
  -o product_mug.jpg \
  --resolution 4k \
  --model super_real \
  --aspect square_1_1 \
  --detailing 50
```

### Social Media Ad Creative
```bash
python freepik_image_gen.py \
  "modern coworking space, diverse people collaborating, bright and airy, contemporary design, lifestyle photography" \
  -o social_ad.jpg \
  --resolution 2k \
  --aspect social_story_9_16 \
  --model realism
```

### Product in Context (with style reference)
```bash
python freepik_image_gen.py \
  "luxury watch on businessman's wrist in modern office" \
  -o lifestyle_shot.jpg \
  --style-ref brand_style.jpg \
  --resolution 4k \
  --aspect widescreen_16_9 \
  --model realism \
  --adherence 60
```

## Tips for Best Results

### Prompts
- **Be specific:** Include lighting, style, camera angle, quality descriptors
- **Use keywords:** "professional", "8k", "hyperrealistic", "studio lighting"
- **Product photos:** Always mention "white background" or specific background
- **Lifestyle:** Include context, people, environment details

### Text Accuracy
- For text in images, use higher `--adherence` (60-80)
- Choose `flexible` or `fluid` model for better text rendering
- Specify exact text in quotes: "sign that says 'OPEN'"

### Quality
- Use `4k` resolution for print or large format
- Use `2k` for web/social (faster, smaller files)
- Use `super_real` or `editorial_portraits` for maximum realism

### Reference Images
- Structure ref: Use sketches, wireframes, or composition guides
- Style ref: Use brand photos, mood boards, or artistic references
- Can use both together for complete control

## Available LoRAs (Styles & Characters)

List available styles and characters:
```bash
python freepik_image_gen.py --list-loras
```

## Cost & Credits

- Check your credit balance: https://www.freepik.com/developers/dashboard
- Mystic costs vary by resolution and model
- Webhook support available for async processing

## Troubleshooting

**Image not generating:**
- Check API key in `.credentials.json`
- Verify prompt isn't NSFW (filter is always on)
- Check credit balance

**Quality issues:**
- Try different model (`super_real` for products)
- Adjust `--detailing` parameter
- Use higher resolution

**Style not matching:**
- Adjust `--adherence` and `--hdr` with style reference
- Try different engines: `magnific_sharpy` for crisp, `magnific_illusio` for soft

**Text errors:**
- Use `flexible` or `fluid` model
- Increase `--adherence`
- Be very specific in prompt

## Support

- Dashboard: https://www.freepik.com/developers/dashboard
- Full docs: https://docs.freepik.com
- Discord: https://discord.com/invite/znXUEBkqM7
