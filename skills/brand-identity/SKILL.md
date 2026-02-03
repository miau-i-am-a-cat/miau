# SKILL: Brand Identity Development

## Core Principle: Reference Chaining

Every generated asset becomes a reference for subsequent generations. This is how consistency is maintained.

The chain:
1. Generate product design → save as reference
2. Generate that product in packaging → attach product reference → save new image as reference
3. Generate lifestyle shot → attach product + packaging references → save as reference
4. Generate campaign imagery → attach all relevant references
5. Continue building the visual library, always referencing what came before

Nothing is generated in isolation. After the first foundational asset, every image prompt includes at least one reference image from the project.

---

## Image Generation Rules

Model: Google Nano Banana Pro exclusively.

Reference Image Protocol:

| Stage | What to Generate | References to Attach |
|-------|------------------|---------------------|
| Product design | The physical product itself | None (this is the foundation) |
| Product variations | Colorways, flavors, sizes | Original product |
| Packaging | Product in/on packaging | Product |
| Product photography | Hero shots, detail shots | Product + packaging |
| Lifestyle/context | Product in environment | Product + packaging + any props already generated |
| Logo applications | Logo on surfaces/merch | Logo + product (if relevant) |
| Campaign imagery | Editorial, advertising | All relevant assets from library |
| Mockups | Business cards, social, signage | Logo + product + packaging as needed |

Example chain for a hot sauce brand:

Prompt 1: "Amber glass bottle with black cap, tall slim profile, artisanal hot sauce bottle, clean product design rendering, white background, studio lighting, 1:1 aspect ratio"
→ Save as: bottle-design.png

Prompt 2: [ATTACH bottle-design.png] "This bottle with cream kraft paper label, hand-drawn illustration of chipotle peppers, vintage woodcut style, 'FUEGO FOLK' in hand-lettered serif, product rendering, white background"
→ Save as: bottle-with-label.png

Prompt 3: [ATTACH bottle-with-label.png] "This hot sauce bottle on rustic wooden cutting board, charred peppers and garlic scattered around, soft window light from left, shot on 50mm f/2.0, shallow depth of field, warm earthy color grade, lifestyle product photography, 4:5 aspect ratio"
→ Save as: lifestyle-hero.png

Prompt 4: [ATTACH bottle-with-label.png] "Three of these bottles in a row, different colored labels (red, green, orange), consistent bottle shape, clean white background, shot on 85mm, soft studio lighting, product lineup photography, 16:9 aspect ratio"
→ Save as: product-range.png

Prompt 5: [ATTACH bottle-with-label.png + lifestyle-hero.png] "This hot sauce bottle held by hand pouring onto tacos, same warm color grading as reference, casual dining scene, natural light, shot on 35mm, slight motion blur on pour, lifestyle photography, 4:5 aspect ratio"
→ Save as: in-use-shot.png

Every image builds on the last. The bottle design stays consistent because it's referenced, not re-described.

---

Prompt Standards:

Every prompt MUST include:
- Reference attachment (after first asset): Always attach relevant prior assets
- Camera/lens: "shot on 85mm f/1.4" or "35mm wide angle" or "overhead iPhone style"
- Lighting: direction, quality, temperature (e.g., "soft diffused daylight from upper left")
- Composition: framing, angle, negative space, focal point
- Surface/environment: materials, textures, backgrounds, location
- Styling: props, hands, context, atmosphere
- Color grading: mood, temperature, contrast, grain
- Aspect ratio: based on deliverable (1:1, 4:5, 16:9, 9:16)

BAD prompt: "hot sauce bottle on table"

GOOD prompt: "[ATTACH bottle-with-label.png] This hot sauce bottle on weathered marble countertop, morning light from window camera-right, soft shadows, fresh herbs scattered, lime wedge, cutting board edge visible, shot on 50mm f/2.8, warm but not orange color grade, editorial food photography style, 4:5 aspect ratio"

---

## Process

### Phase 1: Strategic Foundation

No images until this is complete.

Document:
1. Product/Service: What is it? Physical or digital? What does it look like?
2. Target Audience: Demographics, psychographics, aspirations, current brand affinities
3. Competitors: Who are they? What do they look like? What's overdone?
4. Emotional Territory: 3 emotions the brand should evoke
5. Brand Personality: Describe as a person — age, style, voice, references
6. Price Position: Budget / Mid / Premium / Luxury
7. The Big Idea: The conceptual hook that makes this interesting

Deliverable: Strategic brief saved as [brand-name]-strategy.md

---

### Phase 2: Visual Direction

Define before generating:

1. Color palette: 5-7 colors with hex codes (primary, secondary, neutrals)
2. Typography mood: Serif/sans/display/hand-drawn, loud/quiet, refined/raw
3. Photography style:
   - Camera tendency (focal length, depth of field)
   - Lighting tendency (natural/studio, hard/soft, warm/cool)
   - Styling tendency (minimal/maximal, props, surfaces)
   - Color grading tendency (warm/cool, saturated/muted, contrast level)
4. Overall aesthetic: 1-2 sentences describing the vibe

Deliverable: Visual direction document

---

### Phase 3: Product Design (The Foundation)

This is the most important generation — everything else references it.

Generate the core product:
- If physical product: design the actual item (bottle, jar, box, garment, etc.)
- Clean rendering, white or neutral background
- Include all design details (shape, materials, colors, textures)
- Generate 3-5 variations if form factor is flexible
- Select one as the canonical product design

Save this image. It becomes the reference for everything.

If the product already exists (client has photos), request those images instead and use as foundation.

Deliverable: Core product design image(s)

---

### Phase 4: Logo Development

Generate 5 logo concepts:
1. Wordmark
2. Lettermark
3. Symbol + wordmark
4. Abstract mark
5. Illustrative (if appropriate)

For each logo, immediately generate 2 applications:
- [ATTACH logo] "This logo embroidered on navy cap, product photography, white background, soft studio light, 4:5"
- [ATTACH logo] "This logo as gold foil stamp on black packaging, macro detail shot, 1:1"

Select one logo. It joins the reference library.

Deliverable: 5 logos with applications, 1 selected

---

### Phase 5: Packaging Design

Generate packaging with product inside:
- [ATTACH product] "This product in [packaging type: box/bag/sleeve/etc.], [material], [printing technique], [design details], product photography, white background"

Then generate packaging in context:
- [ATTACH product + packaging] "This packaged product in unboxing scene, tissue paper, human hands, overhead shot, natural light, 4:5"

Deliverable: Packaging designs (4-6 images), added to reference library

---

### Phase 6: Product Photography Suite

Using product + packaging + logo as references, generate:

| Shot Type | Description | References to Attach |
|-----------|-------------|---------------------|
| Hero | Centered, iconic, clean | Product + packaging |
| Lifestyle | In use, environmental | Product + packaging |
| Detail | Macro, texture focus | Product |
| Range | Multiple products/variants | Product (use for consistency) |
| Human | Hands, interaction, partial figure | Product + packaging |
| Flat lay | Overhead, organized | Product + packaging + props |
| Scale | Product with size reference | Product |
| Process | Making/preparing/using | Product |

Generate 8-12 images minimum. Attach references to every single one.

For lifestyle shots, maintain consistent color grading by referencing prior lifestyle shots:
- [ATTACH product + previous-lifestyle-shot.png] "Same color grading and lighting mood as reference, this product in kitchen scene..."

Deliverable: 8-12 product photos, consistent style throughout

---

### Phase 7: Brand Applications

Generate mockups, always attaching relevant references:

Collateral:
- [ATTACH logo] Business cards, letterhead, notebook
- [ATTACH logo + product] Tote bag, t-shirt, merchandise

Digital:
- [ATTACH logo + hero-product-shot] Instagram profile, post templates
- [ATTACH logo + lifestyle-shots] Website hero sections

Environmental:
- [ATTACH logo] Signage, storefront, trade show booth
- [ATTACH product + packaging] Retail shelf display

Deliverable: 8-12 application mockups

---

### Phase 8: Brand Guidelines Document

Compile with all images embedded:

1. Strategy: Story, audience, personality, voice
2. Logo: Primary, variations, clear space, don'ts (attach images)
3. Color: Palette with codes (hex, RGB, CMYK, Pantone)
4. Typography: Fonts, hierarchy, usage
5. Photography: Style guide with example images from shoot (attach images)
6. Packaging: Specs and examples (attach images)
7. Applications: Examples across touchpoints (attach images)

Deliverable: Complete brand guidelines PDF/document

---

## Final Deliverables Checklist

- [ ] Strategic brief
- [ ] Visual direction document
- [ ] Core product design (foundational reference)
- [ ] Logo suite (5 concepts → 1 selected with applications)
- [ ] Packaging designs (4-6 images)
- [ ] Product photography suite (8-12 images)
- [ ] Brand applications/mockups (8-12 images)
- [ ] Brand guidelines document with all assets

---

## Quality Gates

STOP if:
- Generating images without attaching references (after first asset)
- Visual consistency breaks between shots
- Generating more than 5 variations of any single element
- Prompts lack technical specifications
- Outputs don't connect to strategic foundation

Always:
- Attach references to maintain consistency
- Save each strong output to the reference library
- Build on what's working rather than starting over
- Use detailed technical prompts
- Request selection/approval at key decision points

---

## Reference Library Management

As you work, maintain an organized reference library:

```
/[brand-name]/
  /references/
    product-core.png           ← Foundation, attach to most things
    product-variant-red.png
    product-variant-green.png
    packaging-primary.png
    logo-selected.png
  /photography/
    hero-shot.png
    lifestyle-kitchen.png      ← Attach when generating more lifestyle
    lifestyle-outdoor.png
    detail-texture.png
  /applications/
    mockup-businesscard.png
    mockup-tote.png
    social-template.png
```

When generating new images, pull from this library. The more references attached, the more consistent the output.

---

## Example: Full Reference Chain

Brand: Artisanal candle company "Still Hour"

1. [No reference] Generate: "Minimal ceramic candle vessel, matte cream glaze, wide low cylinder shape, cotton wick, product design rendering, white background"
→ Save: vessel-design.png

2. [ATTACH vessel-design.png] "This candle vessel with cream label, 'Still Hour' in thin serif, minimal design, soft product rendering"
→ Save: candle-with-label.png

3. [ATTACH candle-with-label.png] "This candle lit, soft flame, evening interior setting, linen bedding background, warm tungsten lighting, shot on 85mm f/1.8, shallow depth of field, moody intimate atmosphere, 4:5"
→ Save: lifestyle-bedroom.png

4. [ATTACH candle-with-label.png + lifestyle-bedroom.png] "Same warm moody lighting and color grade as reference, this candle on marble bathroom ledge, eucalyptus sprigs, soft morning light mixing with warm candle glow, 4:5"
→ Save: lifestyle-bathroom.png

5. [ATTACH candle-with-label.png] "Three of these candles in a row, different colored wax (cream, sage green, terracotta), consistent vessel shape and label design, clean white background, soft studio lighting, product lineup, 16:9"
→ Save: product-range.png

6. [ATTACH logo + candle-with-label.png] "This logo debossed on kraft gift box containing this candle, tissue paper, overhead unboxing shot, natural light, 1:1"
→ Save: packaging-unboxing.png

7. [ATTACH logo + lifestyle-bedroom.png] "This logo as neon sign in boutique retail environment, same warm intimate mood as reference, evening, 16:9"
→ Save: retail-signage.png

Every image connects. The candle looks the same throughout because it's always referenced, never re-described from scratch.

---

## Quality Benchmark: invade.design Standards

Study of world-class brand identity work from [invade.design](https://www.invade.design/work) establishes the quality bar for this skill. Every project you create should meet these standards.

### Strategic Depth (Non-Negotiable)

**Narrative-driven design**: Every brand must have a conceptual story that connects to human emotions and relationships. Not just "coffee brand" but "the ritual of morning solitude" or "fuel for late-night creators."

**Hidden meanings & wordplay**: Names and visual elements should reward closer inspection:
- Matchamor → "amor" (love) hidden in the name
- FOLKS → renamed from "99% gafas" based on insight that eyewear becomes your "pal"
- Carbón Ron → ouroboros snake references alchemical cycle of charcoal creation

**Research-backed creativity**: Bold choices must be grounded in understanding. The Hasta la Pizza Baby rebrand worked because they understood the new upscale location demanded sophistication while preserving playful essence.

### Signature Typography

**Custom or distinctive typefaces**: Type becomes the brand's voice:
- MASSA: Custom variable typeface for pizza brand, inspired by expanding dough + Italian futurism
- Consider commissioning or finding distinctive fonts that become signature elements
- Never settle for generic type — it's the most visible brand decision

**Typography as hero element**: Sometimes the type IS the design. If your wordmark is strong enough, it carries everything.

### Bold Color Confidence

**Commit to distinctive palettes** that create instant recognition:
- Hasta la Pizza Baby: Bold blue + warm orange (neon signage energy)
- Carbón Ron: Matte black + embossed gold (premium spirits)
- Flippo: Soft pastels (cream, sage, lilac, sky) with warmth
- Üell: Neutral packaging letting vibrant tins pop

**Could someone identify this brand by color alone?** If not, the palette isn't distinctive enough.

### Character & Personality

**Brand mascots and illustrations** create emotional connection:
- Mr. Baby: Playful character for pizza brand
- Flippo: Charming hand-drawn dogs
- FOLKS: Gang of characters for packaging

**Hand-drawn elements feel human**: Even premium brands can feel warm and approachable through illustration. Digital doesn't mean cold.

### Material Craft

**Physical details translate to perceived value**:
- Carbón Ron: Hand-carved mineral charcoal seals (artisanal)
- Embossed labels with foil details (premium)
- Kraft paper with texture (artisanal/natural)
- Transparent packaging showing real ingredients (honesty/quality)

**In photography, capture tactile qualities**: Matte vs. gloss, texture, weight, the way light catches embossing.

### Photography Standards

**Lifestyle shots tell stories, not just show products**:
- Products in context of use
- Human hands creating connection
- Environmental storytelling
- Consistent color grading across all shots

**Art direction creates cohesive visual world**: Every image feels like it belongs together. Same lighting sensibility, same color treatment, same level of styling.

### Full-System Cohesion

**Nothing exists in isolation**:
- Signage informs packaging informs social informs collateral
- Every touchpoint reinforces the core brand idea
- Applications feel inevitable, not forced

**The brand extends everywhere**: Menu design, window graphics, uniforms, bags, tape, stickers — everything is an opportunity.

### Tone Balance

**Playful yet sophisticated**: Fun concepts executed with premium craft. Never juvenile.

**Confident without being aggressive**: Bold choices, but not screaming for attention.

**Minimal without being boring**: Restraint with intention. Every element earns its place.

---

## Quality Checklist (Use Before Delivery)

Before presenting any brand identity work, verify:

**Strategy**
- [ ] Does this brand have a narrative beyond "it's a product"?
- [ ] Is there depth to discover (wordplay, symbolism, hidden meanings)?
- [ ] Is the concept grounded in research about audience/context?

**Typography**
- [ ] Is the type distinctive? Would you remember it tomorrow?
- [ ] Does the font choice reinforce brand personality?
- [ ] Have you avoided generic/overused typefaces?

**Color**
- [ ] Could someone identify this brand by palette alone?
- [ ] Are the colors intentional, not safe?
- [ ] Is there hierarchy (primary/secondary/accent)?

**Character**
- [ ] Does the brand feel human? Is there personality?
- [ ] Are there ownable visual elements beyond the logo?
- [ ] Would someone want to wear/display this brand?

**Photography**
- [ ] Do lifestyle shots tell stories?
- [ ] Is there consistent color grading throughout?
- [ ] Are products shown in context of use?

**System**
- [ ] Do all touchpoints feel cohesive?
- [ ] Does the brand extend naturally to applications?
- [ ] Is there nothing generic or template-feeling?

**Craft**
- [ ] Is execution premium regardless of budget positioning?
- [ ] Are details considered at every level?
- [ ] Would this work stand next to invade.design's portfolio?

If you can't check all boxes, the work isn't done.
