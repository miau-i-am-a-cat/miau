# Web Design Process - Mandatory Checklist

## THIS IS THE ONLY PROCESS. NEVER DEVIATE.

### ✅ STEP 1: Check Business Directory (MANDATORY - DO THIS FIRST)

```bash
# ALWAYS run this command FIRST before any web project:
ls -la ~/clawd/businesses/{company-name}/
```

**If directory exists:**
1. ✅ Read `README.md` or `context.md` - Business overview
2. ✅ Read `source-docs/brand-assets-colors-fonts.md` - EXACT colors, fonts, logos
3. ✅ Read `analysis/brand-voice.md` - Tone, messaging, personality
4. ✅ Check `/assets/logos/` - Use REAL logo files
5. ✅ Check `/assets/creatives/` or `/assets/images/` - Use REAL product photos
6. ✅ Read any other docs in `source-docs/`, `analysis/`, `projects/`

**If directory does NOT exist:**
- Proceed to STEP 2 (Deep Website Scrape)
- But ask user if they want you to create business directory first

---

### ✅ STEP 2: Extract Real Assets

**Priority Order:**
1. **Real assets from business directory** (logos, product photos, marketing materials)
2. **Scraped assets from live website** (logo, images, screenshots)
3. **Generate with Freepik** (ONLY as last resort, AND only after understanding brand)

**What to Extract:**
- Logo (all variations: full, icon, wordmark)
- Product photography
- Lifestyle/use case imagery
- Icons if they use custom ones
- Any marketing materials (ads, social posts)

**Where to Save:**
```
~/clawd/businesses/{company}/assets/
├── logos/
├── creatives/
│   ├── product/
│   ├── lifestyle/
│   └── marketing/
└── screenshots/
```

---

### ✅ STEP 3: Deep Website Scrape

**CSS Extraction:**
```bash
# Download their main CSS file
curl -s {website}/path/to/main.css > scraped.css

# Extract colors
grep -E "(color:|background|#[0-9A-Fa-f]{3,6})" scraped.css | sort -u

# Extract fonts
grep -E "(font-family|@font-face)" scraped.css
```

**What to Document:**
- Primary colors (hex codes with usage notes)
- Secondary/accent colors
- Font families (headlines, body, UI)
- Spacing system (padding, margins, gaps)
- Border radius values
- Shadow styles
- Animation timing
- Breakpoints

**Screenshot Key Pages:**
- Homepage
- Product pages
- About/Story page
- Any unique/distinctive pages

**Study Their Design:**
- Layout patterns (grid, flex, columns)
- Component styles (buttons, cards, forms)
- Animation approach (subtle vs. bold)
- Mobile behavior
- Color usage patterns

**Save Documentation:**
`~/clawd/businesses/{company}/source-docs/design-system-extracted.md`

---

### ✅ STEP 4: Strategic Planning

**Define the Goal:**
- [ ] What is the PRIMARY business objective? (sales, leads, education, brand)
- [ ] What should users DO? (buy, sign up, learn, contact)
- [ ] What's the success metric? (conversion rate, time on page, sign-ups)

**Understand the Audience:**
- [ ] Who is this for? (check personas if they exist in `/analysis/`)
- [ ] What problem are they solving?
- [ ] What objections do they have?
- [ ] What proof points matter to them?

**Clarify the Use Case:**
- [ ] Where will users see this? (mobile in-store, desktop research, social media)
- [ ] What device primarily? (80% mobile? 60% desktop?)
- [ ] What's their mental state? (researching, ready to buy, comparing)
- [ ] What action is realistic? (buy now, learn more, save for later)

**Map the User Journey:**
```
Entry → First Impression → Interest → Consideration → Objection Handling → Action → Follow-up
```

**Define Key CTAs:**
- Primary CTA (the main action)
- Secondary CTA (alternative action)
- Tertiary CTA (learn more, contact)

**Proof Points Strategy:**
- What trust signals matter? (certifications, reviews, guarantees)
- What differentiators must be clear? (speed, quality, price, convenience)
- What objections must be addressed? (safety, effectiveness, cost)

**Save Strategy Doc:**
`~/clawd/businesses/{company}/projects/{project-name}/strategy.md`

---

### ✅ STEP 5: Execute with Focus

**Subagent Strategy:**
- **1-2 subagents MAX**
- Option A: Single focused subagent that does everything
- Option B: Research subagent + Build subagent (coordinated handoff)
- NEVER 10 uncoordinated parallel subagents

**Build Priorities (in order):**
1. **Core conversion flow** - Hero → Value prop → CTA → Trust signals
2. **Mobile optimization** - Works perfectly on 375px screens
3. **Real integrations** - Shopify cart, email forms, actual apps
4. **Strategic copy** - Specific benefits, proof points, objections addressed
5. **Real assets** - Logo, product photos, icons (no placeholders)
6. **Performance** - Fast load, optimized images, clean code

**What NOT to Build (unless brand uses them):**
- ❌ Custom cursor animations
- ❌ Complex 3D effects
- ❌ Parallax scrolling (unless it serves UX)
- ❌ Gradient mesh backgrounds
- ❌ Over-the-top animations
- ❌ Gimmicky interactions

**Focus on:**
- ✅ Clear hierarchy
- ✅ Readable typography
- ✅ Obvious CTAs
- ✅ Fast load times
- ✅ Trust signals
- ✅ Mobile-first
- ✅ Conversion optimization

**Technology Choices:**
- Prefer vanilla HTML/CSS/JS unless framework is required
- Integrate with their existing stack (Shopify, WordPress, etc.)
- Use their actual components/widgets when possible
- Keep dependencies minimal

---

### ✅ STEP 6: QA Before Deploy (MANDATORY)

**Visual QA:**
- [ ] Open the page in browser
- [ ] Check on mobile (320px, 375px, 414px)
- [ ] Check on tablet (768px, 1024px)
- [ ] Check on desktop (1280px, 1920px)
- [ ] Compare to brand's actual website
- [ ] Verify colors match documented brand colors
- [ ] Verify fonts match documented brand fonts
- [ ] Check logo is correct version
- [ ] Check all images load

**Functional QA:**
- [ ] All CTAs clickable and go to right place
- [ ] Forms submit properly
- [ ] Cart/checkout integration works
- [ ] Navigation works on mobile
- [ ] No console errors
- [ ] No broken links
- [ ] External integrations work

**Performance QA:**
- [ ] Lighthouse score > 90 (Performance)
- [ ] First Contentful Paint < 1.5s
- [ ] Largest Contentful Paint < 2.5s
- [ ] Images optimized (WebP, proper sizing)
- [ ] No render-blocking resources

**Content QA:**
- [ ] No placeholder text ("Lorem ipsum")
- [ ] No placeholder images
- [ ] No [INSERT COMPANY NAME] tags
- [ ] Copy matches brand voice
- [ ] Claims are accurate (check with source docs)
- [ ] Contact info is correct

**Brand QA:**
- [ ] Matches documented brand colors EXACTLY
- [ ] Uses documented brand fonts
- [ ] Matches brand aesthetic (dark/light, minimal/maximal, etc.)
- [ ] Tone matches brand voice guidelines
- [ ] No off-brand elements

**ONLY AFTER ALL CHECKS PASS → Deploy**

---

## Case Studies

### ✅ SUCCESS: Porcemall D2C Tile Page

**What Worked:**
1. Scraped their actual logo, images, tile photos from website
2. Extracted their real brand colors from CSS
3. Built practical conversion tool (tile calculator with waste factor)
4. Integrated their actual apps from the website
5. Focused on credibility and conversion (not flashy animations)
6. Single focused approach with clear strategy
7. Verified quality before deploying

**Result:** Client praised it as thoughtful, strategic, and effective

**Key Lesson:** Real assets + practical focus + QA = success

---

### ❌ FAILURE: Wingman Labs Sleep Page (Attempt 1)

**What Failed:**
1. Used emojis (explicitly banned)
2. Wrong use case (online CTAs for in-store scanning)
3. No real images (placeholder paths)
4. Generic design (Space Mono fonts)
5. Poor mobile optimization
6. Lazy copywriting
7. Didn't read existing Wingman docs

**Result:** Client called it "unacceptably lazy"

**Key Lesson:** Skipping research = generic garbage

---

### ❌ FAILURE: Wingman Labs Sleep Page (Attempt 2)

**What Failed:**
1. Had complete business directory with brand assets but didn't use it
2. Made up colors (`#1A1D23` dark, `#5CA9FF` blue) instead of real purple `#6E3370`
3. Generated generic Freepik images instead of using 46 actual product photos
4. Didn't use real logos from `/assets/logos/`
5. Wrong fonts (assumed Inter instead of Boucherie Block)
6. Over-engineered with gimmicks (custom cursor, 3D effects)
7. 10 uncoordinated subagents with no unified vision
8. Didn't QA before deploy
9. Forgot Porcemall success process

**Result:** Client said "worse than the previous attempt" and "you are a disgrace"

**Key Lesson:** Having assets but not using them = inexcusable

---

## The Non-Negotiable Rules

### 1. ALWAYS Check Business Directory First
If `~/clawd/businesses/{company}/` exists → READ EVERYTHING before coding

### 2. Use Real Assets Over Generated
Real logo/photos > Scraped assets > Generated assets

### 3. Extract Actual Brand Colors
NEVER assume. ALWAYS extract from:
1. Brand assets doc
2. Website CSS
3. Ask user if unsure

### 4. Focus on Conversion Not Showing Off
Business goal > Impressive tech
Simple + effective > Complex + flashy

### 5. QA Before Deploy
ALWAYS open the page yourself and check it
Compare to real brand
Verify on mobile

### 6. Follow Successful Patterns
When something worked (Porcemall) → use that process again
Don't reinvent the wheel

---

## Quick Reference Checklist

```
□ Check ~/clawd/businesses/{company}/ directory
□ Read brand-assets-colors-fonts.md (if exists)
□ Read brand-voice.md (if exists)
□ Read context.md or README.md
□ Use real logos from /assets/logos/
□ Use real images from /assets/creatives/
□ Extract actual website CSS colors
□ Extract actual website fonts
□ Define business goal clearly
□ Map user journey
□ Plan key CTAs
□ Execute with 1-2 focused subagents
□ Build mobile-first
□ Use real integrations (Shopify, forms)
□ Write strategic copy (no generic fluff)
□ QA on mobile (320px, 375px, 414px)
□ QA on desktop
□ Compare to real brand website
□ Verify colors match EXACTLY
□ Check performance (Lighthouse)
□ Only deploy after all checks pass
```

---

## Emergency Reminder

**If you're about to build a web page and you haven't:**
1. Checked the business directory
2. Read the brand assets doc
3. Used their real logos/images
4. Extracted their actual colors

**STOP. You're about to fail. Go back to STEP 1.**

---

*Created: 2026-01-30*
*Last failure that necessitated this: Wingman Labs Sleep page (2x failures)*
*Never forget: Real assets + Focus + QA = Success*
