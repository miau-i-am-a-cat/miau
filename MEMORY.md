# MEMORY.md

## Critical Lessons Learned

### 2026-01-30: Quality Standards - NEVER AGAIN

**Incident:** Delivered an unacceptably lazy landing page for Wingman Labs in-store QR project.

**Failures:**
1. ❌ Used emojis throughout (explicitly banned per TOOLS.md)
2. ❌ Wrong use case - CTAs were "Buy Now" for someone scanning QR IN STORE (they can just pick it up!)
3. ❌ No actual images - placeholder paths that didn't exist
4. ❌ No icons - should have used Freepik, used emojis instead
5. ❌ Generic design - Space Mono/Work Sans fonts, basic layout
6. ❌ Poor mobile optimization - large cards causing endless scrolling
7. ❌ Lazy copywriting - generic benefit statements
8. ❌ Zero research - didn't read existing Wingman Labs docs before building
9. ❌ Wrong colors/design language - didn't match brand
10. ❌ No strategic planning - jumped straight to coding

**What I Should Have Done:**
1. ✅ Read relevant context files (businesses/wingman-labs/*)
2. ✅ Read frontend-design and copywriting skills
3. ✅ Understand the ACTUAL use case (in-store scanning → learn more, not buy online)
4. ✅ Generate proper images using Freepik (both product photos AND icons)
5. ✅ Follow brand voice guidelines (confident, direct, science-backed)
6. ✅ Use brand colors from existing docs
7. ✅ Mobile-first responsive design
8. ✅ Strategic copywriting following the frameworks
9. ✅ Consider deploying subagent for complex tasks
10. ✅ NEVER use emojis - always generate proper icons

**The Standard:**
> "Deep strategizing, context retrieval, subagent deployment, data scraping. [...] properly planned it, followed design principles, incorporated details, built tables, chosen and used product photos, created icons using freepik instead of emojis. [...] proper consideration for viewport, or page length. [...] completely reevaluate your skills and contexts, so that this never ever happens again when i ask you to make an app or webpage, regardless of the business or project its assigned to. everything must be done to the max."

**New Rule:**
Before building ANY web page or app:
1. Search and read relevant memory/context
2. Read applicable skills (frontend-design, copywriting, etc.)
3. Understand the use case deeply
4. Generate ALL visual assets (no placeholders, no emojis)
5. Follow brand guidelines if they exist
6. Mobile-first design
7. Strategic, specific copywriting
8. Deploy subagent if task is complex

**Never produce generic AI slop again.**

---

### 2026-01-30: Complete Failure - Sleep Product Page (Second Attempt)

**Incident:** Deployed 10 subagents to build "world-class" Sleep page. Result was worse than first attempt.

**Critical Failures:**
1. ❌ **Ignored existing business directory** - Had `~/clawd/businesses/wingman-labs/` with complete brand assets, but didn't use it
2. ❌ **Made up colors** - Used `#1A1D23` dark + `#5CA9FF` blue instead of actual brand purple `#6E3370`
3. ❌ **Didn't use real assets** - Generated generic Freepik images instead of using 46 actual product photos in assets folder
4. ❌ **Didn't use real logos** - Had logos in `/assets/logos/` but didn't use them
5. ❌ **Wrong fonts** - Assumed Inter instead of reading that it's Boucherie Block (headlines)
6. ❌ **Gimmicky over-engineering** - Custom cursor, parallax, 3D effects instead of focusing on conversion
7. ❌ **Uncoordinated subagents** - 10 parallel agents with no unified vision
8. ❌ **Didn't study actual website** - Superficial scrape instead of deep extraction of design patterns
9. ❌ **No QA before deploy** - Shipped immediately without checking
10. ❌ **Forgot previous success** - Had documentation from Porcemall D2C success but didn't follow same process

**What Porcemall D2C Did RIGHT (Case Study):**
✅ Scraped actual logo, images, tile photos from their website
✅ Used their real brand colors extracted from CSS
✅ Built practical conversion tools (calculator with waste factor)
✅ Integrated their actual apps from the website
✅ Focused on credibility and conversion, not flashy animations
✅ Single focused approach with clear strategy
✅ Verified quality before deploying

**THE MANDATORY PROCESS - NEVER DEVIATE:**

**STEP 1: Check Business Directory (MANDATORY)**
```bash
# ALWAYS run this FIRST:
ls -la ~/clawd/businesses/{company-name}/

# If directory exists, READ THESE IN ORDER:
1. README.md or context.md
2. source-docs/brand-assets-colors-fonts.md (colors, fonts, logos)
3. analysis/brand-voice.md (tone, style, messaging)
4. Any other docs in source-docs/
```

**STEP 2: Extract Real Assets**
- Logo from `/assets/logos/`
- Product images from `/assets/creatives/`
- Any existing marketing materials
- NEVER generate when real assets exist
- ONLY use Freepik when assets don't exist AND you understand the brand

**STEP 3: Deep Website Scrape (if needed)**
- Extract actual CSS colors, fonts, spacing
- Screenshot key pages for reference
- Study layout patterns, component styles
- Note animations and interactions
- Understand their actual design system

**STEP 4: Strategic Planning**
- What's the business goal? (conversion, education, brand awareness)
- Who's the audience? (reference personas if they exist)
- What's the use case? (in-store, online, mobile, desktop)
- What are the key CTAs?
- What proof points matter?

**STEP 5: Execute with Focus**
- Use 1-2 focused subagents MAX (research + build)
- Prioritize conversion over "impressive" features
- Mobile-first always
- Real integrations (Shopify, forms, etc.)
- Strategic copy with specific benefits

**STEP 6: QA Before Deploy**
- Open the page yourself
- Check mobile (320px, 375px, 414px)
- Verify colors match brand
- Check all CTAs work
- Compare to real brand website
- Test performance

**CRITICAL RULE:**
If `~/clawd/businesses/{company}/` exists with docs → READ THEM FIRST.
NEVER make assumptions about brand colors, fonts, or style.

**Never Over-Engineer:**
- Custom cursors → NO (annoying)
- 3D animations → ONLY if brand uses them
- Parallax → ONLY if it serves UX
- Gradient meshes → ONLY if brand uses them
- Focus on CONVERSION not SHOWING OFF

---

## Projects

### Wingman Labs
- **Type:** Supplement company (energy/sleep strips)
- **Brand Voice:** Confident, direct, science-backed, no BS
- **ACTUAL Colors (Sleep):** Purple `#6E3370` (primary), `#9b419c` (bright), `#bd61ff` (high contrast)
- **Base Colors:** Dark Blue `#0B1F3A`, Dark Gray `#1A1D23`, Pink White `#FFF6F1`
- **Energy Colors:** Orange `#D5480B`, `#f57b48` (bright)
- **Accent:** Light Blue `#5CA9FF`
- **Fonts:** Boucherie Block (headlines) + clean sans-serif (Inter/Liberation Sans)
- **Key Differentiator:** Oral-mucosal absorption (5-10min vs 20-45min traditional)
- **Target:** Busy professionals, travelers, fitness enthusiasts, biohackers
- **Context Location:** `~/clawd/businesses/wingman-labs/`
- **Brand Assets Doc:** `~/clawd/businesses/wingman-labs/source-docs/brand-assets-colors-fonts.md`
- **Real Product Images:** `~/clawd/businesses/wingman-labs/assets/creatives/product/sleep/` (46 images)
- **Logos:** `~/clawd/businesses/wingman-labs/assets/logos/`

### Miau
- **GitHub Account:** miau-i-am-a-cat
- **Vercel Token:** Stored in `~/.clawdbot/credentials/vercel_miau_token`
- **Auto-deploy:** Active for main branch

---

## Preferences

### Design & Development
- **NO EMOJIS** - Always generate proper icons using Freepik
- **Mobile-first** - Always optimize for phones first
- **High quality** - No generic AI aesthetics
- **Real assets** - Never use placeholders
- **Context-aware** - Read project docs before building

### Freepik Usage
- **Mystic AI:** Use for ultra-realistic photos, portraits, product shots
- **Seedream 4.5:** Use for marketing materials, icons, graphics with text
- **Always generate** icons instead of using emojis or Unicode symbols

---

## Active Projects

### Wingman Labs - Retail Acquisition Pipeline (2026-01-30)
**Location:** `businesses/wingman-labs/projects/retail-acquisition-pipeline/`
**Purpose:** Automated system to discover and contact retail partners

**Research findings:**
- 300K+ addressable US retailers, 20K+ in LA metro
- 85-90% automation achievable
- Expected 5-8% response rate (vs 1-3% industry avg)
- $20-40 CAC at scale

**Tech stack:**
- Google Places API → retailer discovery
- Apollo.io → contact enrichment
- Claude API → email personalization
- Instantly.ai → automated sequences

**Prototype built:** Working Python pipeline in demo mode
**Status:** Ready for pilot with real API keys

---

*Last updated: 2026-01-31*
