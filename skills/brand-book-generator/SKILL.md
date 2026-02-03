# Brand Book Generator

## Philosophy

**Every spread is a poster. The document IS the brand.**

A streetwear brand's guidelines should feel like a zine stapled to a telephone pole at 2am. A luxury brand's should feel like a Taschen monograph. A tech startup's should feel like the deck that raised $50M.

The brand book is not documentation—it's a design object. Clients should say "holy shit" when they open it. They should show people. They should feel like they got more than they paid for.

---

## Technical Approach

**HTML/CSS → PDF** via headless Chrome or Puppeteer.

Why not reportlab/FPDF/traditional PDF libraries:
- Built for invoices, not editorial design
- Fighting the tool for every creative decision
- Limited layout, typography, and effects

Why HTML/CSS:
- CSS Grid and Flexbox for any layout imaginable
- Transforms for rotation, skew, scale
- Blend modes, filters, masks, gradients
- Custom fonts via @font-face
- Print media queries
- Natural text flow
- Full creative control

### Conversion

```bash
# Chrome headless
google-chrome --headless --disable-gpu --no-sandbox \
  --print-to-pdf=output.pdf \
  --print-to-pdf-no-header \
  input.html

# Or Puppeteer (Node.js)
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('file://input.html');
await page.pdf({
  path: 'output.pdf',
  format: 'A4',
  printBackground: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 }
});
```

### Base HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    @page {
      size: A4;
      margin: 0;
    }
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    html, body {
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    
    .page {
      width: 210mm;
      height: 297mm;
      position: relative;
      overflow: hidden;
      page-break-after: always;
    }
    
    .page:last-child {
      page-break-after: avoid;
    }
  </style>
</head>
<body>
  <!-- Pages -->
</body>
</html>
```

---

## Content Requirements

**The brand book must include ALL content generated during brand strategy.**

Not summaries. Not excerpts. Everything. The client paid for that thinking.

### Brand Foundation
```yaml
brand_name: "Azúcar Muerta"
tagline: "It's candy that hits different."
```

### Brand Story
Full narrative. Every sentence matters.
```yaml
story: |
  Azúcar Muerta is a Mexican-American candy company channeling the 
  irreverent energy of street culture through spicy-sweet treats. 
  The brand fuses Day of the Dead iconography with hypebeast 
  aesthetics—think bodega shelves meeting Travis Scott merch drops.
  
  This isn't your abuela's dulcería. It's candy that hits different.
  
  Born in East LA but built for anyone who wants their snacks with 
  some edge, Azúcar Muerta doesn't whisper. It makes noise. Every 
  bag is designed to stand out on the shelf, in your hand, on your feed.
```

### Target Audience
Full description, not bullet points.
```yaml
audience:
  description: |
    Gen Z consumers who live at the intersection of Chicano heritage 
    and contemporary streetwear culture. They shop at bodegas, follow 
    sneaker drops, and appreciate brands that don't take themselves 
    too seriously while delivering premium quality.
    
    They're the kids photographing their hauls for Instagram. They 
    know what's hyped before it blows up. They want products that 
    feel like them—bold, authentic, unapologetic.
    
  demographics: "Ages 16-28, urban/suburban, digitally native"
  
  psychographics: |
    Values authenticity over polish. Speaks in memes and references.
    Proud of their heritage but not defined by it. Skeptical of 
    corporate but loyal to brands that get it.
```

### Brand Personality
Each word with WHY and HOW.
```yaml
personality:
  - word: "Loud"
    description: |
      Not aggressive, but impossible to ignore. The brand speaks at 
      full volume. Visually, verbally, experientially. A bag of Azúcar 
      Muerta doesn't blend in—it demands attention.
      
  - word: "Irreverent" 
    description: |
      We don't take ourselves too seriously, and we don't expect you 
      to either. We make jokes. We break rules. We think candy that 
      takes itself seriously is weird.
      
  - word: "Unapologetic"
    description: |
      We know who we are. We don't dilute the message or soften the 
      edges for mass appeal. The right people get it. Everyone else 
      can keep scrolling.
      
  - word: "Playful"
    description: |
      At the end of the day, it's candy. It should be fun. Our brand 
      should make you smile, whether that's the packaging, the social 
      media, or the candy itself.
      
  - word: "Confrontational"
    description: |
      Not angry, but direct. We say what we mean. We challenge 
      expectations. When the category zigs, we zag.
```

### Brand Voice
Tone, examples, guardrails.
```yaml
voice:
  tone: |
    Speak like you're texting your coolest friend. Short sentences. 
    Slang welcome. Never corporate, never try-hard. Bilingual flexes 
    (Spanglish) are encouraged. We're in on the joke.
    
  examples:
    - context: "Product description"
      wrong: "Our confectionery products utilize premium ingredients sourced from quality suppliers."
      right: "Real sugar. Real spice. No cap."
      
    - context: "Call to action"
      wrong: "Now available for purchase at select retailers."
      right: "Copped yet?"
      
    - context: "Social caption"
      wrong: "We're excited to announce our newest flavor!"
      right: "new drop just hit different 🔥"
      
  guardrails:
    - "Never use 'excited to announce'"
    - "Never explain the joke"
    - "Never use corporate speak"
    - "Never be mean-spirited (irreverent ≠ cruel)"
```

### Logo
Full concept and all usage rules.
```yaml
logo:
  description: |
    The primary mark features a stylized skull with tongue out and 
    dripping effect—a nod to both Día de los Muertos calaveras and 
    the melting, sticky nature of the candy itself.
    
    The distorted streetwear typography integrates with the skull 
    form, creating a mark that feels alive and hungry. The drip 
    elements connect to both the candy's gooey textures and graffiti 
    aesthetics of street culture.
    
    This isn't a friendly mascot. It's a mark with attitude.
    
  clear_space: |
    Maintain clear space equal to the height of the 'A' in AZÚCAR 
    on all sides. This ensures the mark has room to breathe and 
    isn't crowded by other elements.
    
  minimum_size: |
    Print: 1 inch width minimum
    Digital: 100px width minimum
    Below these sizes, details become unclear.
    
  donts:
    - rule: "Never stretch, rotate, or skew"
      why: "Distorts the carefully designed proportions"
      
    - rule: "Never add drop shadows or effects"
      why: "The drip elements already create depth—effects muddy it"
      
    - rule: "Never place on busy backgrounds without contrast"
      why: "The mark has fine details that get lost"
      
    - rule: "Never separate the skull from the wordmark"
      why: "They're designed as one unit—separation weakens impact"
      
    - rule: "Never recolor outside the approved palette"
      why: "The neon colors are core to brand recognition"
```

### Color Palette
Every color with full context.
```yaml
colors:
  - name: "Hot Pink"
    hex: "#FF1493"
    rgb: [255, 20, 147]
    category: "primary"
    usage: |
      THE brand color. Use for maximum impact—hero sections, primary 
      CTAs, packaging faces, anywhere you want attention NOW.
    pairing: "Always pair with Void Black or Toxic Lime. Never alone on white."
    ratio: "40% of brand presence"
    
  - name: "Toxic Lime"
    hex: "#39FF14"
    rgb: [57, 255, 20]
    category: "secondary"
    usage: |
      The one-two punch with Hot Pink. Creates the signature neon 
      energy. Use for accents, secondary elements, flavor callouts.
    pairing: "Primary pairing partner for Hot Pink. Strong on black backgrounds."
    ratio: "25% of brand presence"
    
  - name: "Void Black"
    hex: "#000000"
    rgb: [0, 0, 0]
    category: "neutral"
    usage: |
      The foundation. Makes the neons pop. Use as primary background 
      for packaging, digital, signage. The darkness creates the drama.
    pairing: "Base for all neon colors. Creates depth and contrast."
    ratio: "25% of brand presence"
    
  - name: "Sunset Orange"
    hex: "#FF6B35"
    rgb: [255, 107, 53]
    category: "accent"
    usage: |
      Flavor accent. Used for specific product lines (e.g., mango, 
      tamarindo). Never as primary brand color—reserved for product 
      differentiation.
    pairing: "Works with black backgrounds. Sparingly alongside pink/green."
    ratio: "5% of brand presence"
    
  - name: "Tamarindo Brown"
    hex: "#8B4513"
    rgb: [139, 69, 19]
    category: "accent"
    usage: |
      Earthy anchor for food photography. Grounds the neon palette 
      in appetizing warmth. Used in ingredient shots, recipe content, 
      and flavor-forward contexts.
    pairing: "Pairs with product photography. Not for brand graphics."
    ratio: "5% of brand presence"
```

### Typography
Full specifications and rationale.
```yaml
typography:
  primary:
    name: "Monument Extended"
    foundry: "Pangram Pangram"
    weights: ["Ultra Bold", "Bold"]
    usage: |
      Headlines, display text, packaging titles, social media headers.
      This is the LOUD voice. Use LARGE and CONFIDENT.
      
    personality: |
      The stretched, aggressive letterforms capture the brand's 
      confrontational energy. These aren't friendly letters—they 
      demand attention. The extended width creates natural drama.
      
    acquisition: |
      Commercial license required. Available at pangrampangram.com
      Font files should be embedded for PDF generation.
      
  secondary:
    name: "Helvetica Neue"
    weights: ["Regular", "Medium", "Bold"]
    usage: |
      Body copy, ingredient lists, legal text, extended reading.
      Clean and readable. Doesn't compete with display type.
      
    personality: |
      The neutral workhorse. Lets Monument Extended be the star 
      while ensuring everything else is legible and professional.
      
  hierarchy:
    h1:
      font: "Monument Extended Ultra Bold"
      size: "48-72px"
      case: "uppercase"
      usage: "Main headlines, hero text"
      
    h2:
      font: "Monument Extended Bold"
      size: "32-40px"
      case: "uppercase"
      usage: "Section titles, subheadlines"
      
    h3:
      font: "Helvetica Neue Bold"
      size: "20-24px"
      case: "sentence case"
      usage: "Subsection headers, card titles"
      
    body:
      font: "Helvetica Neue Regular"
      size: "14-16px"
      leading: "1.5"
      usage: "Paragraphs, descriptions, general content"
      
    caption:
      font: "Helvetica Neue Medium"
      size: "10-12px"
      usage: "Photo credits, footnotes, legal"
```

### Photography
Style direction for shoots and sourcing.
```yaml
photography:
  style: |
    Neon-lit urban environments. Bodega shelves, concrete textures, 
    chain-link fences, brick walls. The candy should feel like 
    contraband—desirable, slightly illicit, exciting.
    
    Hands should have rings, tattoos, nail art. Real people, not 
    models. Diversity without being performative.
    
    Mix gritty lifestyle shots with clean product photography on 
    black backgrounds. The contrast between street and studio 
    creates tension and interest.
    
  mood: |
    2am in a convenience store. A concert afterparty. A skateboard 
    session. The feeling of finding something no one else knows about.
    
  lighting: |
    Neon preferred. Harsh shadows acceptable. Avoid flat, even 
    lighting. Drama over documentation.
    
  avoid:
    - "Plain white backgrounds"
    - "Stock photography energy"
    - "Overhead flat-lays without context"
    - "Overly styled 'Instagram flat-lays'"
    - "Sterile studio shots"
    - "Models with perfect teeth and fake smiles"
```

### Applications
How the brand lives in the world.
```yaml
applications:
  packaging:
    description: |
      Matte black pouches with neon print. Clear window to show 
      product. Resealable for sharing (or not). Packaging should 
      feel premium without being precious.
      
  digital:
    description: |
      Dark mode only. Motion graphics > static posts. Website feels 
      like a destination, not a catalog. Micro-interactions that 
      surprise.
      
  social:
    description: |
      Instagram is primary. TikTok for reach. No Facebook. Post like 
      a human, not a brand. UGC > produced content. Memes welcome.
      
  merchandise:
    description: |
      Hoodies, beanies, skate decks, socks. Never polo shirts or 
      corporate swag. Should feel like streetwear, not promotional 
      products. People should want to wear it.
      
  retail:
    description: |
      Neon signage, black fixtures, concrete floors. If we ever have 
      a flagship store, it's a bodega meets gallery meets skate shop.
      
  environmental:
    description: |
      Murals, wheat-paste posters, stickers. The brand should exist 
      in the wild, not just in stores. Partner with street artists.
```

---

## Page Concepts

These are MOVES, not templates. Combine and adapt.

### COVER: The Bleed

Brand name so large it bleeds off multiple edges. You only see partial letters. Power through restraint.

```css
.cover-bleed {
  background: var(--dark);
  position: relative;
  overflow: hidden;
}

.cover-bleed .hero-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.7;
}

.cover-bleed::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 40%;
  background: linear-gradient(to top, var(--dark), transparent);
}

.cover-bleed .title {
  position: absolute;
  bottom: -0.12em;
  left: -0.03em;
  font-size: 18vw;
  font-weight: 900;
  color: white;
  line-height: 0.8;
  text-transform: uppercase;
  text-shadow: 0 0 80px var(--primary);
  z-index: 1;
}

.cover-bleed .subtitle {
  position: absolute;
  bottom: 5%;
  right: 5%;
  font-size: 11px;
  letter-spacing: 0.25em;
  color: rgba(255,255,255,0.6);
  text-transform: uppercase;
  z-index: 1;
}
```

### OPENING: The Word Pair

Two facing pages. Each is solid color with single word. Immediate emotional impact.

```html
<div class="page word-page" style="background: var(--primary);">
  <span class="word">LOUD</span>
</div>
<div class="page word-page" style="background: var(--secondary);">
  <span class="word">SWEET</span>
</div>
```

```css
.word-page {
  display: flex;
  align-items: center;
  justify-content: center;
}

.word-page .word {
  font-size: 15vw;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--dark);
}

/* Adjust text color for dark backgrounds */
.word-page.on-dark .word {
  color: white;
}
```

### STORY: The Sidebar

Vertical color bar anchors the page. Content floats in generous whitespace.

```html
<div class="page story-sidebar">
  <div class="bar"></div>
  <div class="content">
    <span class="label">THE STORY</span>
    <p class="story-text">...</p>
  </div>
</div>
```

```css
.story-sidebar {
  display: grid;
  grid-template-columns: 10px 1fr;
}

.story-sidebar .bar {
  background: var(--primary);
}

.story-sidebar .content {
  padding: 70px 50px 70px 50px;
  max-width: 520px;
}

.story-sidebar .label {
  display: block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: var(--primary);
  margin-bottom: 20px;
}

.story-sidebar .story-text {
  font-size: 15px;
  line-height: 1.7;
  color: var(--dark);
}

.story-sidebar .story-text p + p {
  margin-top: 1.2em;
}
```

### PERSONALITY: The Stack

Each personality word as a distinct block. Visual hierarchy through size and color.

```html
<div class="page personality-stack">
  <div class="trait">
    <span class="word">Loud</span>
    <p class="description">Not aggressive, but impossible to ignore...</p>
  </div>
  <!-- More traits -->
</div>
```

```css
.personality-stack {
  padding: 50px;
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.trait {
  padding-left: 20px;
  border-left: 4px solid var(--primary);
}

.trait .word {
  font-size: 28px;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--primary);
  display: block;
  margin-bottom: 8px;
}

.trait .description {
  font-size: 13px;
  line-height: 1.6;
  color: var(--dark);
  opacity: 0.8;
  max-width: 450px;
}
```

### LOGO: The Shrine

Black page. Logo enormous. Centered. Nothing else. Command attention.

```css
.logo-shrine {
  background: var(--dark);
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-shrine img {
  max-width: 70%;
  max-height: 70%;
  object-fit: contain;
  filter: drop-shadow(0 0 60px var(--primary));
}
```

### LOGO: The Contexts

Three horizontal bands—brand color, white, black. Logo centered in each.

```css
.logo-contexts {
  display: grid;
  grid-template-rows: 1fr 1fr 1fr;
}

.logo-contexts .band {
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-contexts .band img {
  height: 45%;
  object-fit: contain;
}

.logo-contexts .band-primary { background: var(--primary); }
.logo-contexts .band-white { 
  background: white;
  border-top: 1px solid #eee;
  border-bottom: 1px solid #eee;
}
.logo-contexts .band-dark { background: var(--dark); }
```

### COLOR: The Immersion

One color. Entire page. Experience the color at scale. Info tiny in corner.

```css
.color-immersion {
  position: relative;
}

.color-immersion .info {
  position: absolute;
  bottom: 40px;
  left: 40px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.color-immersion .color-name {
  font-size: 20px;
  font-weight: 700;
}

.color-immersion .color-hex {
  font-family: 'SF Mono', monospace;
  font-size: 13px;
  opacity: 0.8;
}

.color-immersion .color-rgb {
  font-size: 11px;
  opacity: 0.6;
}

/* Text color based on background */
.color-immersion.light-bg .info { color: var(--dark); }
.color-immersion.dark-bg .info { color: white; }
```

### COLOR: The Usage

After individual color pages, show how they work together.

```css
.color-usage {
  padding: 50px;
  background: var(--dark);
  color: white;
}

.color-usage .section {
  margin-bottom: 40px;
}

.color-usage .label {
  font-size: 10px;
  letter-spacing: 0.15em;
  color: var(--secondary);
  margin-bottom: 15px;
}

.color-usage .combo {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}

.color-usage .swatch {
  width: 60px;
  height: 60px;
  border-radius: 4px;
}

.color-usage .combo-note {
  font-size: 13px;
  opacity: 0.8;
  max-width: 350px;
}
```

### TYPOGRAPHY: The Letterform

Single letter at maximum size. Bleeds off page. The shape IS the design.

```css
.type-letterform {
  position: relative;
  background: white;
  overflow: hidden;
}

.type-letterform .letter {
  position: absolute;
  bottom: -0.15em;
  left: -0.08em;
  font-size: 180vw;
  font-weight: 900;
  color: var(--primary);
  line-height: 0.75;
}

.type-letterform .font-name {
  position: absolute;
  top: 40px;
  right: 40px;
  font-size: 12px;
  font-weight: 700;
  color: var(--dark);
}
```

### TYPOGRAPHY: The Specimen

Full character set, hierarchy, usage notes. Functional but designed.

```css
.type-specimen {
  padding: 50px;
  background: var(--dark);
  color: white;
}

.type-specimen .font-name {
  font-size: 11px;
  letter-spacing: 0.15em;
  color: var(--secondary);
  margin-bottom: 20px;
}

.type-specimen .display-preview {
  font-size: 80px;
  line-height: 0.9;
  margin-bottom: 30px;
}

.type-specimen .charset {
  font-size: 18px;
  letter-spacing: 0.03em;
  opacity: 0.6;
  margin-bottom: 10px;
}

.type-specimen .usage-note {
  font-size: 12px;
  opacity: 0.5;
  margin-top: 25px;
  max-width: 400px;
}
```

### PHOTO: The Full Bleed

Image fills page. No margins. No captions. Let it breathe.

**CRITICAL**: Use `object-fit: contain` to preserve composition. NEVER crop AI-generated images.

```css
.photo-full {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--dark); /* Letterbox color */
}

.photo-full img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain; /* NEVER use 'cover' */
}
```

### PHOTO: The Editorial

Image with small caption. Magazine feel.

```css
.photo-editorial {
  padding: 30px;
  background: white;
  display: flex;
  flex-direction: column;
}

.photo-editorial img {
  flex: 1;
  width: 100%;
  object-fit: contain;
  object-position: center;
}

.photo-editorial .caption {
  margin-top: 15px;
  font-size: 10px;
  color: #999;
  letter-spacing: 0.05em;
}
```

### SECTION: The Divider

Full page of color with section name. Creates rhythm and pause.

```css
.section-divider {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--primary);
}

.section-divider .title {
  font-size: 11vw;
  font-weight: 900;
  text-transform: uppercase;
  color: var(--dark);
}
```

### VOICE: The Before/After

Split layout showing wrong vs right. Immediate understanding.

```css
.voice-comparison {
  padding: 50px;
}

.voice-comparison .example {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  padding: 25px 0;
  border-bottom: 1px solid #eee;
}

.voice-comparison .context {
  grid-column: span 2;
  font-size: 10px;
  letter-spacing: 0.1em;
  color: var(--primary);
  margin-bottom: 10px;
}

.voice-comparison .before {
  color: #999;
}

.voice-comparison .before::before {
  content: '✗ ';
  color: #ff4444;
}

.voice-comparison .after {
  color: var(--dark);
  font-weight: 600;
}

.voice-comparison .after::before {
  content: '✓ ';
  color: var(--secondary);
}
```

### APPLICATION: The Gallery

One application per page. Let each shine.

```css
.application-page {
  padding: 30px;
  background: #f5f5f5;
  display: flex;
  flex-direction: column;
}

.application-page .label {
  font-size: 10px;
  letter-spacing: 0.15em;
  color: #999;
  margin-bottom: 15px;
}

.application-page img {
  flex: 1;
  width: 100%;
  object-fit: contain;
}
```

---

## Document Structure

### Recommended Flow

```
PAGE 1:   Cover (Hero image + brand name bleeding)
PAGE 2:   Word spread left (personality word 1 on primary)
PAGE 3:   Word spread right (personality word 2 on secondary)
PAGE 4:   Brand story (full text)
PAGE 5:   Personality words (all 5 with descriptions)
PAGE 6:   Target audience (full description)
PAGE 7:   Brand voice (tone + examples + guardrails)
PAGE 8:   Logo hero (logo large on black)
PAGE 9:   Logo description (concept and meaning)
PAGE 10:  Logo usage (contexts + clear space + sizes)
PAGE 11:  Logo don'ts (rules with explanations)
PAGE 12:  Color divider ("COLOR" on primary)
PAGE 13:  Color 1 - full page
PAGE 14:  Color 2 - full page
PAGE 15:  Color 3 - full page
PAGE 16:  Color 4 - full page (if applicable)
PAGE 17:  Color usage (relationships + pairings)
PAGE 18:  Typography hero (letterform)
PAGE 19:  Primary typeface (specimen + notes)
PAGE 20:  Secondary typeface (specimen + notes)
PAGE 21:  Type hierarchy (H1-caption examples)
PAGE 22:  Photography divider ("PHOTOGRAPHY" on secondary)
PAGE 23:  Photo 1 - full bleed
PAGE 24:  Photo 2 - full bleed
PAGE 25:  Photo 3 - full bleed
PAGE 26:  Photography style (full guidelines)
PAGE 27:  Voice divider ("VOICE & TONE")
PAGE 28:  Voice examples (before/after)
PAGE 29:  Voice guardrails
PAGE 30:  Applications divider ("APPLICATIONS")
PAGE 31:  Application 1 - full page
PAGE 32:  Application 2 - full page
PAGE 33:  Application 3 - full page
PAGE 34:  Application notes (context for each)
PAGE 35:  Back cover (logo small + tagline)
```

~35 pages. Adjust based on content volume.

---

## Brand Energy Modes

Adapt visual intensity to brand personality.

### LOUD (streetwear, youth, challenger)
- Black backgrounds dominant
- Neon accents
- Type bleeds aggressively
- Maximum asymmetry
- Tight leading
- Hard shadows

```css
:root {
  --page-bg: var(--dark);
  --text-primary: white;
  --accent-glow: 0 0 60px var(--primary);
}
```

### REFINED (luxury, premium, heritage)
- White backgrounds dominant
- Muted accents
- Generous whitespace
- Centered moments
- Loose leading
- No shadows

```css
:root {
  --page-bg: white;
  --text-primary: var(--dark);
  --accent-glow: none;
}
```

### BOLD (tech, modern, confident)
- Strong color blocks
- Sans-serif only
- Geometric precision
- Confident statements
- Medium whitespace

### WARM (food, lifestyle, wellness)
- Soft backgrounds
- Organic color palette
- Rounded elements
- Approachable typography
- Photography-forward

---

## Image Handling

### Embedding for PDF

All images must be base64 encoded for reliable PDF generation:

```python
import base64

def embed_image(path: str) -> str:
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode()
    ext = path.split('.')[-1].lower()
    mime = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'webp': 'image/webp'
    }.get(ext, 'image/png')
    return f'data:{mime};base64,{data}'
```

### Preserving Composition

**NEVER crop or distort images.** The AI composed them intentionally.

```css
/* CORRECT */
img {
  object-fit: contain;
  max-width: 100%;
  max-height: 100%;
}

/* WRONG - destroys composition */
img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}
```

Letterboxing with black or brand color is always preferable to cropping.

---

## Quality Standards

### Content Completeness
- [ ] Full brand story (every paragraph)
- [ ] All personality words with descriptions
- [ ] Complete audience description
- [ ] Full voice guidelines with examples
- [ ] All colors with usage notes
- [ ] Complete typography specifications
- [ ] Full photography direction
- [ ] All logo rules with explanations

### Design Quality  
- [ ] Cover creates immediate impact
- [ ] Opening spread sets emotional tone
- [ ] Every color has presence (full page or major element)
- [ ] Typography specimen is dramatic
- [ ] Images are NEVER cropped
- [ ] Pacing alternates loud/quiet
- [ ] No page feels cramped
- [ ] Every spread could be framed

### Technical
- [ ] All images embedded as base64
- [ ] PDF renders correctly
- [ ] Colors print accurately
- [ ] Fonts fallback gracefully
- [ ] File size < 50MB

### Brand Alignment
- [ ] Document FEELS like the brand
- [ ] Energy matches personality
- [ ] Nothing looks generic or templated
- [ ] Client would want to show this off

---

## Anti-Patterns

**DON'T** do these:

- Grid of equal rectangles for images
- 50/50 splits (use 35/65 or 70/30)
- Tiny color swatches
- "Template" layouts that could be any brand
- Cropping images to fit
- Centering everything
- Explaining obvious things ("This is our logo")
- Corporate section headers ("Section 3.2: Logo Guidelines")
- Safe, forgettable design choices
- Walls of text without visual relief
- Clip art or stock elements

---

## Integration

After Moltbot generates brand identity:

```python
from brand_book import create_brand_book

# Moltbot provides:
# - Complete brand strategy
# - Generated logo
# - Generated imagery
# - Color palette
# - Typography selections

config = {
    'name': brand_strategy['name'],
    'tagline': brand_strategy['tagline'],
    'story': brand_strategy['story'],
    'personality': brand_strategy['personality'],
    'audience': brand_strategy['audience'],
    'voice': brand_strategy['voice'],
    'logo': {
        'path': assets['logo'],
        'description': brand_strategy['logo_concept'],
        'rules': brand_strategy['logo_rules'],
    },
    'colors': brand_strategy['colors'],
    'typography': brand_strategy['typography'],
    'photography': brand_strategy['photography'],
    'images': {
        'hero': assets['hero_image'],
        'lifestyle': assets['lifestyle_images'],
        'product': assets['product_images'],
        'applications': assets['application_images'],
    },
    'energy': determine_energy(brand_strategy['personality']),
}

create_brand_book(config, output='brand-guidelines.pdf')
```

---

## Final Note

The brand book is not documentation. It's a design object. It should make clients feel like they got more than they paid for.

Every decision—margins, type sizes, color placement, pacing—should be intentional. If you can't articulate why, it's probably wrong.

The goal: When someone opens this PDF, they say "holy shit."

Make it unforgettable.
