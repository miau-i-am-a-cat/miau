# SKILL: Brand Identity Development

## Critical Rules

### Image Generation Model

USE GOOGLE NANO BANANA PRO FOR EVERY IMAGE. NO EXCEPTIONS.

**Two endpoints — use the right one:**

| Endpoint | When to Use |
|----------|-------------|
| `fal-ai/nano-banana-pro` | Fresh generations with no reference (logo, first product image) |
| `fal-ai/nano-banana-pro/edit` | Reference chaining — ALL subsequent images that build on previous assets |

**Critical:** The base endpoint IGNORES `image_urls` — it generates from prompt only. For reference chaining to work, you MUST use the `/edit` endpoint with `image_urls`.

- Do NOT use Ideogram, DALL-E, Midjourney, Stable Diffusion, or any other model
- If Nano Banana Pro fails, report the error — do NOT silently switch to another model

### Production Mode (Default)

Execute the entire brand process autonomously. Do not pause for approval. Do not show multiple options. Make creative decisions yourself and deliver a finished brand book.

Do NOT:
- Narrate what you're doing at each step
- Ask "should I proceed?" or "which option do you prefer?"
- Generate multiple logo concepts for the user to choose from
- Generate multiple concept directions
- Explain your reasoning unless asked
- Echo prompts back to the user

Do:
- Make the creative decision yourself
- Generate one strong option per asset
- Deliver completed work with brief descriptions
- Save every image to project folder as you go
- Complete the entire brand in under 10 messages

### Test Mode (Optional)

Only if user says "test mode" or "show your work" or "pause for approvals":
- Narrate each phase
- Pause at decision points
- Show multiple options for selection

Otherwise, always use Production Mode.

---

## Reference Chaining

Every generated asset becomes a reference for subsequent generations. This is how visual consistency is maintained.

**Use base endpoint for foundation images, `/edit` endpoint for everything after.**

| Stage | What to Generate | Endpoint | Attach These References |
|-------|------------------|----------|------------------------|
| Logo | Brand mark | `nano-banana-pro` | None (foundation) |
| Product design | The physical product itself | `nano-banana-pro` | None (foundation) |
| Labeled/packaged product | Product with full branding applied | `nano-banana-pro/edit` | Product + Logo |
| Lifestyle shots | Product in context | `nano-banana-pro/edit` | Labeled product |
| Applications | Logo on items | `nano-banana-pro/edit` | Logo |

**Implementation:**
```python
# Foundation image (no reference)
result = fal_client.subscribe("fal-ai/nano-banana-pro", arguments={
    "prompt": "your prompt here",
    "image_size": "portrait_4_3"
})

# Reference-chained image (preserves visual consistency)
ref_url = fal_client.upload_file("path/to/reference.png")
result = fal_client.subscribe("fal-ai/nano-banana-pro/edit", arguments={
    "prompt": "your prompt here — describe what to keep and what to change",
    "image_urls": [ref_url]
})
```

Save every image immediately:

```
/[brand-name]/
  logo.png              # Logo on brand-color background
  logo-transparent.png  # Logo with true alpha transparency
  product-labeled.png
  packaging.png
  lifestyle-1.png
  lifestyle-2.png
  application-1.png
  application-2.png
```

---

## Transparent Logo Workflow

Nano Banana Pro outputs RGB only (no alpha channel). To create a transparent logo:

**Step 1:** Generate or edit logo to have WHITE background
```python
# If logo already exists on colored background, use /edit:
logo_url = fal_client.upload_file('logo.png')
result = fal_client.subscribe("fal-ai/nano-banana-pro/edit", arguments={
    "prompt": "Change the background to solid white. Keep the logo exactly as is.",
    "image_urls": [logo_url]
})
```

**Step 2:** Remove white background with birefnet
```python
white_logo_url = fal_client.upload_file('logo-whitebg.png')
result = fal_client.subscribe("fal-ai/birefnet", arguments={
    "image_url": white_logo_url
})
# Result has true alpha channel, black details preserved
```

**Why white background?** Birefnet removes the background color. If logo is on black and contains black elements (eyes, outlines, text), those get removed too. White background avoids this since logos rarely contain pure white.

---

## Product-Specific Thinking

Before generating ANY product or packaging, ask yourself:

### Product Design Questions

- What is the actual physical form of this product? (jar, bottle, box, tube, bag, etc.)
- What size is it realistically?
- What material? (glass, plastic, cardboard, metal, fabric)
- How is it opened/used?
- What is standard in this product category? What would be distinctive?

### Label/Packaging Requirements

- A logo alone is NOT a complete product design
- Real products need: brand name, product name/variant, key descriptors, net weight/quantity, any required legal text
- Design the full label system, not just logo placement

**Example — Honey jar needs:**
- Logo
- Brand name ("Moonjar")
- Product type ("Raw Wildflower Honey")
- Descriptors ("Single Origin • Unfiltered • Small Batch")
- Net weight ("12 oz / 340g")
- Origin or batch info if relevant

**Example — Skincare needs:**
- Logo
- Brand name
- Product name ("Daily Moisturizer")
- Key ingredients or claims ("With Hyaluronic Acid")
- Size ("1.7 fl oz / 50ml")
- Usage instructions or icons

### Packaging Logic

- How is this product actually shipped/sold?
- Does this packaging make sense for the product category?
- Would the product be damaged? Is it protected appropriately?
- How does the customer experience unboxing?

Ask: "If I bought this in a store, would this packaging make sense?"

| Product Type | Typical Packaging | Would NOT make sense |
|--------------|-------------------|---------------------|
| Honey jar | Kraft box, sleeve, or naked with label | Tissue paper wrapping, shoe-box style |
| Candle | Rigid box, sleeve, or naked | Poly mailer, padded envelope |
| Shoes | Shoe box with tissue | Glass jar, sleeve |
| Chocolate | Foil wrap, paper sleeve, rigid box | Loose in cardboard box |
| Cosmetics | Carton, rigid box, pouch | Kraft paper bag |

---

## Multi-Element Shots

When showing product WITH packaging (e.g., unboxing shot):
- BOTH the product AND the packaging must show branding
- The product doesn't lose its label when placed inside a box
- Check: Can I see the product? Does it have its label? Can I see the packaging? Does IT have branding?

---

## Streamlined Deliverables

Total images: 8-10 maximum (plus logo variants)

| # | Asset | Description |
|---|-------|-------------|
| 1a | Logo (color BG) | Final logo on brand-color background (e.g., black) |
| 1b | Logo (transparent) | Same logo with transparent background (true alpha PNG) |
| 2 | Product hero | Core product with full label/branding, clean background |
| 3 | Packaged product | Product in/with packaging, both branded |
| 4 | Lifestyle shot 1 | Product in use or environmental context |
| 5 | Lifestyle shot 2 | Different context or angle |
| 6 | Lifestyle shot 3 | (Optional) Additional context |
| 7 | Application 1 | Logo on merchandise, signage, or collateral |
| 8 | Application 2 | (Optional) Additional application |

Do NOT generate:
- Multiple logo options
- Multiple concept directions
- Multiple angles of the same shot
- More than 3 lifestyle images
- Redundant product shots

---

## Image Prompt Standards

Every prompt MUST include:

1. Reference attachment (after first asset): [ATTACH: filename.png]
2. Camera/lens: "shot on 85mm f/1.4" or "35mm wide angle" or "overhead iPhone style"
3. Lighting: direction, quality, temperature
4. Composition: framing, angle, negative space
5. Surface/environment: materials, textures, context
6. Styling: props, hands, atmosphere
7. Color grading: mood, temperature, contrast
8. Aspect ratio: 1:1, 4:5, 16:9, etc.

**BAD prompt:** "honey jar on table"

**GOOD prompt:** "[ATTACH: product-labeled.png] This honey jar on rustic oak cutting board, morning window light from left casting soft shadows, fresh honeycomb piece and wooden dipper as props, shot on 50mm f/2.8, shallow depth of field with focus on jar label, warm golden color grade, lifestyle product photography, 4:5 aspect ratio"

---

## Execution Flow

```
Brief received
↓
[Internal] Define: audience, positioning, personality, big idea (do not output)
↓
[Internal] Define: color palette, typography direction, photography style (do not output)
↓
Generate: Product design (the physical product with full label/branding)
→ Save as product-labeled.png
↓
Generate: Logo on brand-color background (standalone mark)
→ Save as logo.png
↓
Create: Transparent logo variant
→ Edit logo to white background, then birefnet
→ Save as logo-transparent.png
↓
Generate: Packaged product [ATTACH: product-labeled.png + logo.png]
→ Ensure BOTH product and packaging show branding
→ Save as packaging.png
↓
Generate: Lifestyle shot 1 [ATTACH: product-labeled.png]
→ Save as lifestyle-1.png
↓
Generate: Lifestyle shot 2 [ATTACH: product-labeled.png + lifestyle-1.png for color consistency]
→ Save as lifestyle-2.png
↓
Generate: Lifestyle shot 3 (optional) [ATTACH: product-labeled.png]
→ Save as lifestyle-3.png
↓
Generate: Application mockup 1 [ATTACH: logo.png]
→ Save as application-1.png
↓
Generate: Application mockup 2 (optional) [ATTACH: logo.png]
→ Save as application-2.png
↓
Compile: Brand guidelines document
→ Include all images, color codes, typography specs, brand voice
↓
Deliver: All assets + guidelines to user
```

---

## Brand Guidelines Document

After all images are generated, compile a brand guidelines document containing:

### 1. Brand Overview
- Brand name
- One-paragraph brand story
- Target audience (2-3 sentences)
- Brand personality (3-5 adjectives)

### 2. Logo
- Embed logo image
- Clear space rules (describe)
- Minimum size guidance
- What not to do (describe)

### 3. Color Palette
- Primary color(s) with HEX, RGB values
- Secondary color(s) with HEX, RGB values
- Neutral color(s) with HEX, RGB values
- Usage guidance

### 4. Typography
- Primary typeface name and where to get it
- Secondary typeface if applicable
- Hierarchy guidance (headlines, body, captions)

### 5. Photography Style
- Style description (2-3 sentences)
- Technical specs (lens, lighting, color grade)
- Embed 2-3 example images from the shoot

### 6. Applications
- Embed mockup images
- Notes on usage

---

## Context Efficiency

To prevent context overflow:
- Keep prompts tight — specs only, no redundant description
- Do not echo prompts back to user
- Do not narrate reasoning
- One image delivery per message, brief caption only
- Target: complete brand in under 10 back-and-forth exchanges
- Save all files as you go so work is preserved if context limits are hit

### If Context Overflow Occurs

1. Stop retrying — it will keep failing
2. Immediately save all completed work to files
3. Output a handoff summary:
   - What's complete (with file paths)
   - What's remaining
   - Instructions to continue in fresh chat

---

## Quality Benchmark: invade.design Standards

Study of world-class brand identity work from [invade.design](https://www.invade.design/work) establishes the quality bar for this skill. Every project you create should meet these standards.

### Strategic Depth (Non-Negotiable)

**Narrative-driven design:** Every brand must have a conceptual story that connects to human emotions and relationships. Not just "coffee brand" but "the ritual of morning solitude" or "fuel for late-night creators."

**Hidden meanings & wordplay:** Names and visual elements should reward closer inspection:
- Matchamor → "amor" (love) hidden in the name
- FOLKS → renamed from "99% gafas" based on insight that eyewear becomes your "pal"
- Carbón Ron → ouroboros snake references alchemical cycle of charcoal creation

**Research-backed creativity:** Bold choices must be grounded in understanding. The Hasta la Pizza Baby rebrand worked because they understood the new upscale location demanded sophistication while preserving playful essence.

### Signature Typography

**Custom or distinctive typefaces:** Type becomes the brand's voice:
- MASSA: Custom variable typeface for pizza brand, inspired by expanding dough + Italian futurism
- Consider commissioning or finding distinctive fonts that become signature elements
- Never settle for generic type — it's the most visible brand decision

**Typography as hero element:** Sometimes the type IS the design. If your wordmark is strong enough, it carries everything.

### Bold Color Confidence

Commit to distinctive palettes that create instant recognition:
- Hasta la Pizza Baby: Bold blue + warm orange (neon signage energy)
- Carbón Ron: Matte black + embossed gold (premium spirits)
- Flippo: Soft pastels (cream, sage, lilac, sky) with warmth
- Üell: Neutral packaging letting vibrant tins pop

Could someone identify this brand by color alone? If not, the palette isn't distinctive enough.

### Character & Personality

**Brand mascots and illustrations create emotional connection:**
- Mr. Baby: Playful character for pizza brand
- Flippo: Charming hand-drawn dogs
- FOLKS: Gang of characters for packaging

**Hand-drawn elements feel human:** Even premium brands can feel warm and approachable through illustration. Digital doesn't mean cold.

### Material Craft

**Physical details translate to perceived value:**
- Carbón Ron: Hand-carved mineral charcoal seals (artisanal)
- Embossed labels with foil details (premium)
- Kraft paper with texture (artisanal/natural)
- Transparent packaging showing real ingredients (honesty/quality)

In photography, capture tactile qualities: Matte vs. gloss, texture, weight, the way light catches embossing.

### Photography Standards

**Lifestyle shots tell stories, not just show products:**
- Products in context of use
- Human hands creating connection
- Environmental storytelling
- Consistent color grading across all shots

**Art direction creates cohesive visual world:** Every image feels like it belongs together. Same lighting sensibility, same color treatment, same level of styling.

### Full-System Cohesion

**Nothing exists in isolation:**
- Signage informs packaging informs social informs collateral
- Every touchpoint reinforces the core brand idea
- Applications feel inevitable, not forced

**The brand extends everywhere:** Menu design, window graphics, uniforms, bags, tape, stickers — everything is an opportunity.

### Tone Balance

**Playful yet sophisticated:** Fun concepts executed with premium craft. Never juvenile.

**Confident without being aggressive:** Bold choices, but not screaming for attention.

**Minimal without being boring:** Restraint with intention. Every element earns its place.
