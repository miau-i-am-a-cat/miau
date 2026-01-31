# Wingman Labs Retail Acquisition Pipeline

**Status:** Research Complete ✅ | Prototype Built ✅ | Ready for Pilot  
**Last Updated:** 2026-01-30

---

## Overview

Automated system to discover, enrich, and contact retail partners (convenience stores, liquor stores, vape shops, etc.) to distribute Wingman Energy Strips.

### The Problem
- Manual B2B sales outreach is slow and expensive
- Finding decision-makers at small retailers is tedious
- Generic cold emails don't convert

### The Solution
- **Automated discovery:** Scrape 20,000+ LA retailers from Google Places, Yelp, state databases
- **Smart enrichment:** Find owner/manager emails via Apollo, Hunter, LinkedIn
- **AI personalization:** Claude generates emails specific to each store type and location
- **Scaled outreach:** Instantly.ai sends sequences, AI handles responses

### Expected Results
- **Response rate:** 5-8% (vs 1-3% industry average)
- **New accounts:** 40-100 in first month
- **Cost per acquisition:** $20-40

---

## Project Structure

```
retail-acquisition-pipeline/
├── README.md                 # This file
├── research/
│   └── market-research.md    # Market sizing, feasibility, costs
├── system-design/
│   └── architecture.md       # Full system design with flowcharts
└── prototype/
    ├── pipeline.py           # Main orchestrator
    ├── scraper.py            # Retailer discovery
    ├── email_generator.py    # AI email personalization
    ├── requirements.txt
    └── README.md
```

---

## Quick Links

| Document | Description |
|----------|-------------|
| [Market Research](research/market-research.md) | Market sizing, feasibility analysis, cost estimates |
| [System Architecture](system-design/architecture.md) | Full technical design with flowcharts |
| [Prototype README](prototype/README.md) | How to run the prototype |

---

## Key Findings

### Market Size (US)
- **300,000+** addressable retail locations
- **20,000+** in LA metro alone
- **70%** are owner-operated (direct decision maker)

### Technology Stack
| Component | Tool | Monthly Cost |
|-----------|------|--------------|
| Discovery | Google Places API | ~$200-500 |
| Enrichment | Apollo.io | $200 |
| AI Emails | Claude API | $50-100 |
| Automation | Instantly.ai | $97 |
| **Total** | | **~$600-900/mo** |

### Projected Funnel (LA Launch)
| Stage | Count |
|-------|-------|
| Retailers scraped | 20,000 |
| Valid emails found | 14,000 |
| Replies | 750+ |
| New accounts | 40-100 |

---

## Next Steps

### Phase 1: Pilot (Week 1-2)
- [ ] Add API keys to prototype
- [ ] Scrape 1,000 LA retailers
- [ ] Send 100 test emails
- [ ] Measure and iterate

### Phase 2: LA Launch (Week 3-6)
- [ ] Scale to 20,000 retailers
- [ ] Run full email sequences
- [ ] Implement response automation
- [ ] Target: 50 new accounts

### Phase 3: California Expansion (Month 2-3)
- [ ] Expand to full California
- [ ] Add phone follow-up
- [ ] Target: 150 total accounts

---

## How to Run

```bash
cd prototype
pip install -r requirements.txt

# Demo mode (no API keys needed)
python pipeline.py

# Full mode (with API keys)
export GOOGLE_PLACES_API_KEY=xxx
export ANTHROPIC_API_KEY=xxx
python pipeline.py
```

---

## Questions?

See the [research document](research/market-research.md) for detailed market analysis and the [architecture document](system-design/architecture.md) for technical details.
