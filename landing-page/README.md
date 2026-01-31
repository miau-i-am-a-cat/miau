# Wingman Labs - In-Store QR Landing Page

**Mobile-first landing page for customers scanning QR codes from retail product boxes.**

## 🎯 Purpose

This page is designed for customers who scan QR codes while standing in front of Wingman Labs products in retail stores. It provides:

- **Product education** - Understanding bioavailability and why strips work faster
- **Detailed information** - Ingredients, certifications, use cases
- **Social proof** - Real customer reviews and testimonials
- **CTA for in-store purchase** - Encourages picking up the product at checkout
- **Online alternative** - Offers 20% discount code for web orders

## ✨ Key Features

### Design
- **Mobile-first responsive design** - Optimized for phone screens (primary use case)
- **Distinctive pharmaceutical aesthetic** - Matches Wingman Labs brand
- **Brand colors** - Orange (#FF6B35) and black (#0A0A0A)
- **No emojis** - Uses Freepik-generated icons and graphics
- **Fast loading** - Minimal dependencies, optimized images
- **Accessible** - WCAG compliant, reduced motion support

### Content
- **Brand voice aligned** - Confident, direct, science-backed (no BS)
- **Strategic copywriting** - Specific benefits, proof points, objection handling
- **Comparison tables** - Clear differentiation vs coffee/drinks/pills
- **FAQ section** - Addresses common questions
- **Use cases** - Specific moments when to use the product

### Technical
- **Modern CSS** - Grid, custom properties, mobile-first media queries
- **Vanilla JS** - No framework dependencies
- **Performance optimized** - Lazy loading, efficient animations
- **SEO ready** - Semantic HTML, meta tags

## 📱 Mobile Optimization

- Viewport-optimized for all phone sizes
- Touch-friendly tap targets (minimum 44px)
- Smooth scrolling and animations
- Readable typography at mobile sizes
- No horizontal scroll
- Fast CSS-only animations

## 🎨 Design Principles

Following the **frontend-design** skill:
- Bold, distinctive aesthetic (not generic AI slop)
- Clear hierarchy and spacing
- Intentional color use (orange as primary accent)
- Typography pairing (Space Grotesk + Inter)
- Subtle animations that enhance UX
- Dark hero with gradient overlay
- Clean white content sections

Following the **copywriting** skill:
- Benefit-focused headlines
- Specific numbers and data
- Customer language (not corporate speak)
- Clear, concise explanations
- Objection handling in FAQ
- Strategic CTA placement

## 📂 Structure

```
landing-page/
├── index.html              # Main page
├── styles.css              # Mobile-first CSS
├── script.js               # Minimal interactions
├── images/
│   ├── product-hero.jpg    # Generated product photo
│   ├── icons-set.png       # Icon graphics
│   └── feature-icons.png   # Feature section icons
├── README.md              # This file
└── DEPLOYMENT.md          # Deployment docs
```

## 🎨 Brand Guidelines

### Colors
- **Primary:** `#FF6B35` (Wingman Orange)
- **Secondary:** `#0A0A0A` (Deep Black)
- **Backgrounds:** `#FFFFFF` (White), `#F5F5F5` (Light Gray)

### Typography
- **Display:** Space Grotesk (headings, labels, numbers)
- **Body:** Inter (paragraphs, descriptions)

### Voice
- Confident but not cocky
- Science-backed but accessible
- Direct without being cold
- Honest about limitations

## 🚀 Deployment

**Live URL:** https://landing-page-sigma-wheat.vercel.app

**Auto-deploy:** Enabled on push to `main` branch

```bash
# Make changes
git add .
git commit -m "Update landing page"
git push origin main

# Vercel automatically deploys
```

## 📊 Performance Targets

- **First Contentful Paint:** < 1.5s
- **Largest Contentful Paint:** < 2.5s
- **Cumulative Layout Shift:** < 0.1
- **Mobile PageSpeed:** 90+

## 🔄 Future Enhancements

- [ ] Add real customer photos/videos
- [ ] A/B test CTA variations
- [ ] Add analytics tracking
- [ ] Create Sleep version
- [ ] Add animation on scroll
- [ ] Generate unique QR codes per retail location
- [ ] Add "Find in Store" locator

## 📝 Content Strategy

### Primary Message
"Energy in 5 Minutes" - Fastest onset time is #1 differentiator

### Supporting Messages
1. **Science** - Oral-mucosal absorption bypasses digestion
2. **Clean** - Zero calories, zero sugar, pharmaceutical-grade
3. **Convenient** - TSA-approved, no water, pocket-sized
4. **Value** - $0.77/strip vs $2-5 for coffee

### Target Personas
1. **Busy Professional** - Values time efficiency
2. **Frequent Traveler** - Needs TSA-approved solution
3. **Fitness Enthusiast** - Wants zero-calorie pre-workout
4. **Biohacker** - Cares about bioavailability science

## ⚙️ Technical Details

### CSS Architecture
- Mobile-first media queries
- CSS custom properties for theming
- BEM-inspired naming (not strict)
- Logical property values
- Performant animations

### JavaScript
- Minimal, progressive enhancement
- No external dependencies
- CTA tracking (placeholder for analytics)
- Smooth scroll for anchor links
- Viewport height fix for mobile

### Images
- **Product hero:** Seedream-generated (856KB, optimized)
- **Icons:** Seedream-generated sets
- **Format:** JPG for photos, PNG for graphics
- **Loading:** Browser-native lazy loading

## 🔗 Links

- **Website:** https://thewingmanlabs.com
- **Instagram:** @thewingmanlabs
- **Email:** team@thewingmanlabs.com

## 📄 License

© 2026 Wingman Labs. All rights reserved.

---

**Created:** 2026-01-30  
**Optimized for:** iPhone 14 Pro, Google Pixel 7, Samsung Galaxy S22  
**Framework:** Vanilla HTML/CSS/JS (no dependencies)  
**Design System:** Wingman Labs brand guidelines  
**Quality:** Production-grade, no generic AI aesthetics
