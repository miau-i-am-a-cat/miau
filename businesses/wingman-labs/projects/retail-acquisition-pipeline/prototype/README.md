# Wingman Labs Retail Acquisition Pipeline
## Prototype v1.0

Automated system to discover, enrich, and reach out to retail partners.

## Quick Start

### 1. Setup

```bash
cd prototype
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

### 2. Environment Variables (optional)

Create a `.env` file:

```bash
GOOGLE_PLACES_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
APOLLO_API_KEY=your_key_here
```

Without API keys, the pipeline runs in **demo mode** with sample data.

### 3. Run the Pipeline

```bash
# Full pipeline (demo mode)
python pipeline.py

# Just scraper (demo mode)
python scraper.py

# Just email generator (demo mode)
python email_generator.py
```

## Pipeline Stages

### Stage 1: Discover
Scrapes retailers from:
- Google Places API (convenience stores, liquor stores, gas stations, etc.)
- Yelp API (coming soon)
- State licensing databases (coming soon)

### Stage 2: Enrich
Finds contact information:
- Apollo.io lookup
- Hunter.io domain search
- LinkedIn scraping
- AI research agent

### Stage 3: Personalize
Generates AI-personalized emails:
- Uses Claude API for natural, specific emails
- Falls back to smart templates without API key
- Different messaging for each business type

### Stage 4: Export
Creates import-ready CSV for email automation:
- Instantly.ai format
- Smartlead format
- HubSpot format

## Output Files

After running, check the `data/` directory:

```
data/
├── retailers_raw.json        # Raw scraped data
├── retailers_enriched.json   # With contact info
├── retailers_with_emails.json # With personalized emails
└── instantly_import.csv      # Ready for Instantly.ai
```

## Configuration

Edit business types and email templates in `email_generator.py`:

```python
EMAIL_TEMPLATES = {
    "c-store": {
        "hook": "energy drinks are your #1 packaged beverage category",
        "benefit": "grab-and-go format that sits right at checkout",
        "social_proof": "convenience stores across LA"
    },
    # Add more...
}
```

## Costs (Production)

| Service | Cost |
|---------|------|
| Google Places API | ~$17 per 1,000 searches |
| Apollo.io | $99-149/month |
| Claude API | ~$0.01 per email |
| Instantly.ai | $37-97/month |

**Estimated cost per 1,000 retailers:** ~$50-75

## Next Steps

1. **Add API keys** - Enable real data scraping
2. **Set up Instantly.ai** - Import the CSV and configure sequences
3. **Monitor responses** - Build response classification
4. **Iterate** - Improve targeting and messaging based on results

## Files

```
prototype/
├── pipeline.py         # Main orchestrator
├── scraper.py          # Retailer discovery
├── email_generator.py  # AI email personalization
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Support

Questions? Check the `/research` and `/system-design` directories for detailed documentation.
