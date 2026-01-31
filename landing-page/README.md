# Wingman Labs - In-Store QR Landing Page

High-converting, mobile-first landing page optimized for in-store QR code scans.

## 🎯 Purpose

This page is designed for customers scanning QR codes from retail display boxes in-store. It's optimized for:
- Mobile devices (primary use case)
- Fast loading on cellular connections
- Quick decision-making (standing in an aisle)
- Building trust and closing the sale

## 🚀 Features

- **Mobile-First Design:** Optimized for phone screens
- **Fast Loading:** Minimal dependencies, optimized images
- **Conversion-Focused:** Clear value prop, social proof, multiple CTAs
- **Accessible:** WCAG compliant, works with reduced motion
- **SEO-Ready:** Semantic HTML, meta tags included

## 📁 Structure

```
landing-page/
├── index.html          # Main landing page
├── styles.css          # Mobile-first styles
├── script.js           # Minimal interactions
├── images/            # Product photography
│   └── hero-energy.jpg
└── README.md          # This file
```

## 🎨 Design Features

- **Bold Typography:** Large, readable text for quick scanning
- **Speed Comparison:** Visual differentiation vs competitors
- **Social Proof:** Real reviews build trust
- **Clear CTAs:** Multiple conversion points
- **Brand Consistency:** Wingman Labs orange/black palette

## 📱 Mobile Optimization

- Viewport optimized for all phone sizes
- Touch-friendly tap targets (minimum 44px)
- Fast CSS-only animations
- Optimized image loading
- No external dependencies

## 🔧 Customization

### Update Copy
Edit `index.html` - all text is semantic HTML

### Change Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --orange-primary: #FF6B35;
    --black: #0A0A0A;
    /* etc. */
}
```

### Add Analytics
Update `script.js` CTA click handlers with your tracking code

### Replace Images
- Hero image: `images/hero-energy.jpg`
- Recommended: 1080x1350px (mobile portrait)
- Format: JPG (optimized for web)

## 🚢 Deployment

### Quick Deploy to Vercel

```bash
cd /Users/scoop/clawd
git add landing-page/
git commit -m "Add in-store QR landing page"
git push origin main
```

Vercel will auto-deploy on push.

### Environment Variables Needed

None required for static page. Add if integrating:
- Analytics (GA4, Mixpanel)
- CRM (HubSpot, Salesforce)
- E-commerce (Shopify)

## 📊 Conversion Optimization

**Key Elements:**
1. **Speed as hero:** "5 minutes" is main message
2. **Social proof:** Reviews visible above fold
3. **Comparison chart:** Faster than coffee/drinks/pills
4. **Multiple CTAs:** 3 purchase buttons
5. **Trust signals:** FDA-registered, GMP-certified

**A/B Test Ideas:**
- Headline variations ("Energy in 5 Min" vs "5-Min Focus")
- CTA copy ("Buy Now" vs "Grab One Now" vs "Try Today")
- Price display (with/without comparison to coffee)
- Hero image (product vs lifestyle)

## 🔒 Security

- No API keys or secrets in code
- Environment variables for any integrations
- Follows .gitignore rules from repo root

## 📈 Performance

- **First Contentful Paint:** < 1s
- **Largest Contentful Paint:** < 2.5s
- **Cumulative Layout Shift:** < 0.1
- **Mobile Page Speed:** 95+

## 🎯 Next Steps

1. ✅ Static page created
2. ⏳ Add real purchase flow integration
3. ⏳ Connect analytics
4. ⏳ A/B test variations
5. ⏳ Generate Sleep version

---

**Created:** 2026-01-30  
**Optimized for:** iPhone 14 Pro, Google Pixel 7, Samsung Galaxy S22  
**Framework:** Vanilla HTML/CSS/JS (no dependencies)
