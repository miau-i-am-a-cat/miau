# Influencer Brand Website Architecture Blueprint

**Purpose:** Define the standard architecture for all influencer e-commerce sites built by The Wingman Project. Every element is designed for conversion, credibility, and long-term value.

---

## Core Principles

### 1. The Influencer IS the Brand
- Their face, voice, and story are the primary trust signals
- The product is secondary to the relationship
- Every page should feel like an extension of their content

### 2. Mobile-First, Always
- 80%+ traffic will be mobile (from social links)
- Thumb-friendly navigation
- Fast load times (<3s)
- Minimal friction checkout

### 3. Convert Visitors, Build Lists
- First goal: Purchase
- Second goal: Email/SMS capture
- Third goal: Social follow
- Never let a visitor leave empty-handed

### 4. Credibility Through Design
- Premium aesthetic = premium perceived value
- Consistent with influencer's existing brand
- Professional but personal

---

## Site Structure

```
├── Homepage (Hero + Story + Featured Products)
├── Shop
│   ├── All Products
│   ├── Collections (by category/drop)
│   └── Individual Product Pages
├── About / Story
├── Quiz (Product Finder)
├── Reviews / Social Proof
├── FAQ
├── Contact
└── Footer (Links + Newsletter + Socials)
```

---

## Page-by-Page Breakdown

### 1. HOMEPAGE

The homepage must accomplish three things in 5 seconds:
1. Communicate who this is
2. Communicate what they're selling
3. Give a clear path to purchase

#### Hero Section
```
┌─────────────────────────────────────────────┐
│  [INFLUENCER PHOTO/VIDEO - Full Width]      │
│                                             │
│     [BRAND NAME]                            │
│     [Tagline: 6-8 words max]                │
│                                             │
│     [SHOP NOW]  [TAKE THE QUIZ]             │
│                                             │
│  "As featured in [PRESS LOGOS]"             │
└─────────────────────────────────────────────┘
```

**Requirements:**
- High-quality hero image featuring the influencer
- Brand name prominent
- Tagline that captures the brand essence
- Dual CTA: Shop (buyers) + Quiz (browsers)
- Social proof strip if available

#### Story Teaser Section
```
┌─────────────────────────────────────────────┐
│  [Photo]    "Why I created [BRAND]..."      │
│             Brief 2-3 sentence hook         │
│             [Read My Story →]               │
└─────────────────────────────────────────────┘
```

**Purpose:** Humanize the brand, create curiosity, drive to About page

#### Featured Products Section
```
┌─────────────────────────────────────────────┐
│         ★ BESTSELLERS ★                     │
│  ┌───────┐  ┌───────┐  ┌───────┐           │
│  │Product│  │Product│  │Product│           │
│  │ Image │  │ Image │  │ Image │           │
│  │ $XX   │  │ $XX   │  │ $XX   │           │
│  │[ADD]  │  │[ADD]  │  │[ADD]  │           │
│  └───────┘  └───────┘  └───────┘           │
│           [SHOP ALL →]                      │
└─────────────────────────────────────────────┘
```

**Requirements:**
- 3-4 products max (decision paralysis prevention)
- Quick-add to cart functionality
- Price visible
- "Bestseller" or "Fan Favorite" badges

#### Social Proof Section
```
┌─────────────────────────────────────────────┐
│  "What [AUDIENCE NAME] Are Saying"          │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ [Customer Photo] ★★★★★               │   │
│  │ "Quote from review..."               │   │
│  │ - Name, Location                     │   │
│  └─────────────────────────────────────┘   │
│  [←] [Review 2] [Review 3] [→]             │
│                                             │
│  [READ ALL REVIEWS]                         │
└─────────────────────────────────────────────┘
```

**Requirements:**
- Real customer photos when possible
- Star ratings visible
- Carousel for multiple reviews
- UGC integration if available

#### Instagram/TikTok Feed Section
```
┌─────────────────────────────────────────────┐
│  Follow @[HANDLE] for daily [CONTENT TYPE]  │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐       │
│  │Post│ │Post│ │Post│ │Post│ │Post│       │
│  └────┘ └────┘ └────┘ └────┘ └────┘       │
│  [@HANDLE - XXK Followers]                  │
└─────────────────────────────────────────────┘
```

**Purpose:** Social proof + drives follows + keeps content fresh

#### Email Capture Section
```
┌─────────────────────────────────────────────┐
│  JOIN THE [BRAND] FAM                       │
│  Get 10% off + exclusive drops              │
│                                             │
│  [Email Input] [JOIN]                       │
│                                             │
│  "No spam, just [VALUE PROP]"               │
└─────────────────────────────────────────────┘
```

**Requirements:**
- Clear incentive (discount or exclusive access)
- Single field (email only, reduce friction)
- Privacy reassurance
- Consider SMS option for higher intent

---

### 2. PRODUCT PAGE

The product page is where money is made. Every element must reduce friction and increase desire.

#### Above the Fold
```
┌─────────────────────────────────────────────┐
│ ┌─────────────┐  PRODUCT NAME               │
│ │             │  ★★★★★ (XX reviews)          │
│ │   PRODUCT   │                             │
│ │    IMAGE    │  $XX.XX                     │
│ │  GALLERY    │                             │
│ │             │  [Size/Variant Selector]    │
│ │ [< 1 2 3 >] │                             │
│ └─────────────┘  [ADD TO CART]              │
│                  [BUY NOW - PAYPAL/APPLE]   │
│                                             │
│  ✓ Free shipping over $XX                   │
│  ✓ 30-day returns                           │
│  ✓ [UNIQUE BENEFIT]                         │
└─────────────────────────────────────────────┘
```

**Image Gallery Requirements:**
- 5-7 images minimum
- Product on white background
- Product in use/lifestyle
- Product with influencer (critical!)
- Size reference / scale shot
- Detail shots
- Video if available

**Trust Badges:**
- Free shipping threshold
- Return policy
- Payment security
- Any certifications

#### Product Description Section
```
┌─────────────────────────────────────────────┐
│  WHY I LOVE THIS                            │
│  [Influencer quote about product]           │
│                                             │
│  ─────────────────────────────              │
│                                             │
│  THE DETAILS                                │
│  • Benefit-focused bullet 1                 │
│  • Benefit-focused bullet 2                 │
│  • Benefit-focused bullet 3                 │
│                                             │
│  [INGREDIENTS/SPECS]  [HOW TO USE]          │
│     (expandable)        (expandable)        │
└─────────────────────────────────────────────┘
```

**Copy Framework:**
1. Lead with influencer's personal endorsement
2. Benefits before features
3. Scannable bullets (not paragraphs)
4. Technical details in expandable sections

#### Social Proof on Product Page
```
┌─────────────────────────────────────────────┐
│  REVIEWS (XXX)                    [WRITE]   │
│  ★★★★★ 4.8 average                          │
│                                             │
│  [Photo Reviews] [All Reviews]              │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ ★★★★★  "Review headline"             │   │
│  │ Full review text...                  │   │
│  │ [Photo] - Name, Verified Buyer       │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

#### Upsell Section
```
┌─────────────────────────────────────────────┐
│  COMPLETE THE LOOK / PAIRS WELL WITH        │
│  ┌───────┐  ┌───────┐  ┌───────┐           │
│  │Product│  │Product│  │Product│           │
│  │ $XX   │  │ $XX   │  │ $XX   │           │
│  │[ADD]  │  │[ADD]  │  │[ADD]  │           │
│  └───────┘  └───────┘  └───────┘           │
└─────────────────────────────────────────────┘
```

**Upsell Strategy:**
- Complementary products (not competing)
- Bundle discount suggestion
- "Customers also bought" data-driven

---

### 3. ABOUT / STORY PAGE

This page converts skeptics into believers. It's the emotional core of the brand.

#### Structure
```
┌─────────────────────────────────────────────┐
│  [HERO: Influencer authentic photo]         │
│                                             │
│  "MY STORY"                                 │
│  ───────────                                │
│                                             │
│  [Origin story - why they started]          │
│  [The problem they faced]                   │
│  [The solution / brand creation]            │
│  [Their mission / values]                   │
│  [What makes them different]                │
│                                             │
│  [Photo grid: Behind the scenes]            │
│                                             │
│  "This isn't just a brand. It's..."        │
│  [Emotional closing statement]              │
│                                             │
│  [SHOP MY FAVORITES]                        │
└─────────────────────────────────────────────┘
```

**Story Framework:**
1. **Hook:** Relatable struggle or moment
2. **Journey:** How they got here
3. **Mission:** What they stand for
4. **Invitation:** Join them

---

### 4. QUIZ (Product Finder)

Quizzes increase conversion by 2-3x. They create engagement, personalization, and email capture.

#### Flow
```
Page 1: Hook
"Find Your Perfect [PRODUCT] in 60 Seconds"
[START QUIZ]

Page 2-5: Questions (4-5 max)
"What's your [SKIN TYPE / GOAL / STYLE]?"
[Option A] [Option B] [Option C]

Page 6: Email Capture
"Almost there! Where should we send your results?"
[Email] → [SEE MY RESULTS]

Page 7: Results
"You're a [PERSONA TYPE]!"
"We recommend: [PRODUCT]"
[ADD TO CART - 10% OFF WITH CODE QUIZ10]
```

**Quiz Best Practices:**
- 4-5 questions maximum
- Visual answer options when possible
- Progress bar
- Email gate BEFORE results (not after)
- Personalized product recommendation
- Exclusive quiz discount

---

### 5. COLLECTION PAGES

#### Standard Collection Layout
```
┌─────────────────────────────────────────────┐
│  [COLLECTION NAME]                          │
│  [Brief description]                        │
│                                             │
│  [FILTER: Category] [SORT: Featured ▼]      │
│                                             │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  │
│  │Product│ │Product│ │Product│ │Product│  │
│  │ $XX   │ │ $XX   │ │ $XX   │ │ $XX   │  │
│  └───────┘ └───────┘ └───────┘ └───────┘  │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  │
│  │Product│ │Product│ │Product│ │Product│  │
│  └───────┘ └───────┘ └───────┘ └───────┘  │
└─────────────────────────────────────────────┘
```

**Product Card Requirements:**
- Image (swap on hover to lifestyle shot)
- Product name
- Price (show compare-at if on sale)
- Star rating
- Quick-add functionality
- "New" or "Bestseller" badges

---

### 6. SPECIAL PAGES (Conversion Boosters)

#### Limited Drop Page
```
┌─────────────────────────────────────────────┐
│  ⚡ LIMITED DROP ⚡                          │
│  [COUNTDOWN TIMER: XX:XX:XX]                │
│                                             │
│  [Hero image of drop product]               │
│                                             │
│  "[DROP NAME]"                              │
│  Only XXX units available                   │
│                                             │
│  $XX.XX                                     │
│  [GET YOURS BEFORE IT'S GONE]               │
│                                             │
│  [Stock indicator: 73% claimed]             │
└─────────────────────────────────────────────┘
```

**Purpose:** Urgency + scarcity = immediate action

#### Bundle Page
```
┌─────────────────────────────────────────────┐
│  THE [NAME] BUNDLE                          │
│  Save XX% vs buying separately              │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ [Product 1] + [Product 2] + [3]     │   │
│  │                                     │   │
│  │ $XXX value → $XX bundle price       │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  [ADD BUNDLE TO CART]                       │
│                                             │
│  ★ Most popular choice                      │
│  ★ Free shipping included                   │
└─────────────────────────────────────────────┘
```

**Purpose:** Increase AOV, showcase value

---

## Conversion Elements

### Exit Intent Popup
```
┌─────────────────────────────────────────────┐
│  WAIT! Don't leave empty-handed            │
│                                             │
│  Get 15% off your first order               │
│                                             │
│  [Email] [GET MY 15%]                       │
│                                             │
│  [No thanks, I'll pay full price]           │
└─────────────────────────────────────────────┘
```

**Trigger:** Mouse moves toward browser close
**Frequency:** Once per session

### Sticky Add-to-Cart (Mobile)
```
┌─────────────────────────────────────────────┐
│ [Product Name]  $XX  [ADD TO CART]          │
└─────────────────────────────────────────────┘
```

**Trigger:** Appears when main CTA scrolls out of view

### Cart Drawer (Not Cart Page)
```
┌─────────────────────────────────────────────┐
│  YOUR CART (X items)              [×]       │
│  ─────────────────────────                  │
│  [Product] [Qty: -1+] $XX                   │
│  [Product] [Qty: -1+] $XX                   │
│  ─────────────────────────                  │
│  Add $XX more for FREE SHIPPING             │
│  ─────────────────────────                  │
│  Subtotal: $XX                              │
│  [CHECKOUT]                                 │
│  ─────────────────────────                  │
│  You might also like:                       │
│  [Upsell Product] [ADD]                     │
└─────────────────────────────────────────────┘
```

**Key Elements:**
- Easy quantity adjustment
- Free shipping progress bar
- In-cart upsell
- Express checkout options

### Announcement Bar
```
┌─────────────────────────────────────────────┐
│ 🔥 FREE SHIPPING ON ORDERS $50+ | CODE: SHIP│
└─────────────────────────────────────────────┘
```

**Rotation Ideas:**
- Free shipping threshold
- Limited-time discount
- New product launch
- Influencer appearance/event

---

## Email/SMS Capture Strategy

### Capture Points:
1. **Homepage popup** (timed, 5-10 seconds)
2. **Exit intent** (leaving site)
3. **Quiz completion** (required for results)
4. **Footer form** (always visible)
5. **Checkout** (SMS opt-in)
6. **Post-purchase** (review request)

### Incentive Ladder:
- Popup: 10% off first order
- Exit intent: 15% off
- Quiz: Exclusive quiz discount
- SMS: Early access to drops

---

## Trust & Credibility Elements

### Trust Badges (Footer)
- Secure checkout (SSL)
- Money-back guarantee
- Payment provider logos
- "As seen in" press logos

### Social Proof Integration
- Review count in navigation
- Star ratings on all products
- UGC gallery
- Follower count display
- Real-time purchase notifications (use sparingly)

### Transparency
- Clear shipping times
- Easy-to-find return policy
- Real contact information
- Influencer responsiveness to comments

---

## Technical Requirements

### Performance
- Page load: <3 seconds
- Mobile score: >80 (PageSpeed Insights)
- Image optimization: WebP format, lazy loading
- Minimal JavaScript blocking

### SEO Basics
- Unique title tags per page
- Meta descriptions with CTAs
- Alt text on all images
- Clean URL structure
- Schema markup for products

### Analytics
- Google Analytics 4
- Facebook Pixel
- TikTok Pixel (if applicable)
- Conversion tracking on:
  - Add to cart
  - Checkout initiated
  - Purchase completed
  - Email signup
  - Quiz completion

### Integrations
- Email: Klaviyo (preferred) or Mailchimp
- SMS: Postscript or Klaviyo
- Reviews: Judge.me or Loox
- Upsells: ReConvert or CartHook
- Quiz: Octane AI or Typeform

---

## Page Templates Summary

| Page | Primary Goal | Secondary Goal |
|------|--------------|----------------|
| Homepage | Drive to product/quiz | Email capture |
| Product | Add to cart | Upsell |
| Collection | Browse products | Filter/find |
| About | Build trust | Drive to shop |
| Quiz | Email capture | Product match |
| Cart | Complete purchase | Upsell |
| Drop | Urgency purchase | FOMO creation |

---

## Launch Checklist

- [ ] Homepage complete with all sections
- [ ] Minimum 3 products live
- [ ] Product pages with 5+ images each
- [ ] About page with influencer story
- [ ] Quiz built and tested
- [ ] Email capture working (all touchpoints)
- [ ] Mobile tested on real devices
- [ ] Checkout flow tested end-to-end
- [ ] Analytics/pixels installed
- [ ] Free shipping threshold set
- [ ] Return policy published
- [ ] Contact page/form working
- [ ] Social links working
- [ ] Favicon and meta images set
- [ ] Speed test passed (>80 mobile)

---

*Every element on every page should answer: "Does this help the visitor become a customer?"*
