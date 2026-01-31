# Wingman Labs Retail Acquisition Pipeline
## System Architecture & Design

**Version:** 1.0  
**Date:** 2026-01-30  
**Status:** Design Phase

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WINGMAN LABS RETAIL ACQUISITION PIPELINE                  │
│                         End-to-End Automation System                         │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   DISCOVER  │───▶│   ENRICH    │───▶│   ENGAGE    │───▶│   CONVERT   │
│  Retailers  │    │  Contacts   │    │  Outreach   │    │   Close     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
   Google            Apollo.io          Instantly.ai        HubSpot
   Places              Clay             Claude API           Quotes
   Yelp API          Hunter.io          Sequences           Orders
   State DBs         LinkedIn                               Delivery
```

---

## Complete System Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 1: DISCOVERY                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐                                                        │
│  │ Geographic      │                                                        │
│  │ Target Input    │  (Start: LA Metro, expand by zip code)                │
│  │ - Zip codes     │                                                        │
│  │ - Radius        │                                                        │
│  └────────┬────────┘                                                        │
│           │                                                                  │
│           ▼                                                                  │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    PARALLEL SCRAPING JOBS                          │    │
│  │                                                                    │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │    │
│  │  │ Google   │  │ Yelp     │  │ State    │  │ Industry │          │    │
│  │  │ Places   │  │ API      │  │ License  │  │ Lists    │          │    │
│  │  │          │  │          │  │ DBs      │  │          │          │    │
│  │  │ Types:   │  │ Types:   │  │          │  │ NACS     │          │    │
│  │  │ -c-store │  │ -gas     │  │ -ABC     │  │ members  │          │    │
│  │  │ -gas     │  │ -liquor  │  │ -Pharmacy│  │          │          │    │
│  │  │ -liquor  │  │ -vape    │  │ -Tobacco │  │          │          │    │
│  │  │ -pharmacy│  │ -health  │  │          │  │          │          │    │
│  │  │ -store   │  │          │  │          │  │          │          │    │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘          │    │
│  │       │             │             │             │                 │    │
│  │       └─────────────┴──────┬──────┴─────────────┘                 │    │
│  │                            │                                      │    │
│  └────────────────────────────┼──────────────────────────────────────┘    │
│                               ▼                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    DEDUPLICATION & NORMALIZATION                   │    │
│  │                                                                    │    │
│  │  - Match by address (fuzzy)                                       │    │
│  │  - Match by phone number                                          │    │
│  │  - Match by business name                                         │    │
│  │  - Merge records, keep richest data                              │    │
│  │  - Assign unique retailer_id                                      │    │
│  │                                                                    │    │
│  └────────────────────────────┬───────────────────────────────────────┘    │
│                               │                                            │
│                               ▼                                            │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                       RAW RETAILER DATABASE                        │    │
│  │                                                                    │    │
│  │  Fields:                                                          │    │
│  │  - retailer_id (UUID)                                             │    │
│  │  - business_name                                                   │    │
│  │  - address, city, state, zip                                      │    │
│  │  - phone                                                          │    │
│  │  - website                                                        │    │
│  │  - business_type (c-store, liquor, vape, etc.)                   │    │
│  │  - google_place_id                                                │    │
│  │  - yelp_id                                                        │    │
│  │  - rating, review_count                                           │    │
│  │  - hours                                                          │    │
│  │  - source                                                         │    │
│  │  - scraped_at                                                     │    │
│  │  - enrichment_status = 'pending'                                  │    │
│  │                                                                    │    │
│  └────────────────────────────┬───────────────────────────────────────┘    │
│                               │                                            │
└───────────────────────────────┼────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 2: ENRICHMENT                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    CONTACT DISCOVERY PIPELINE                      │    │
│  │                                                                    │    │
│  │  For each retailer where enrichment_status = 'pending':           │    │
│  │                                                                    │    │
│  │  ┌──────────────────────────────────────────────────────────────┐ │    │
│  │  │ Step 1: Apollo.io Lookup                                     │ │    │
│  │  │ - Search by company name + location                          │ │    │
│  │  │ - Find owner/manager contacts                                │ │    │
│  │  │ - Get email + phone if available                             │ │    │
│  │  └──────────────────┬───────────────────────────────────────────┘ │    │
│  │                     │                                             │    │
│  │                     ▼ (if no email found)                         │    │
│  │  ┌──────────────────────────────────────────────────────────────┐ │    │
│  │  │ Step 2: Hunter.io Domain Search                              │ │    │
│  │  │ - If website exists, search domain                           │ │    │
│  │  │ - Find email patterns                                        │ │    │
│  │  │ - Verify email                                               │ │    │
│  │  └──────────────────┬───────────────────────────────────────────┘ │    │
│  │                     │                                             │    │
│  │                     ▼ (if still no email)                         │    │
│  │  ┌──────────────────────────────────────────────────────────────┐ │    │
│  │  │ Step 3: LinkedIn Scrape (Phantombuster)                      │ │    │
│  │  │ - Search for business name + owner                           │ │    │
│  │  │ - Find decision maker profiles                               │ │    │
│  │  │ - Extract contact info if available                          │ │    │
│  │  └──────────────────┬───────────────────────────────────────────┘ │    │
│  │                     │                                             │    │
│  │                     ▼ (if still no email)                         │    │
│  │  ┌──────────────────────────────────────────────────────────────┐ │    │
│  │  │ Step 4: AI Research Agent (Claygent/Custom)                  │ │    │
│  │  │ - Search web for business + owner name                       │ │    │
│  │  │ - Check social media profiles                                │ │    │
│  │  │ - Find alternative contact methods                           │ │    │
│  │  └──────────────────┬───────────────────────────────────────────┘ │    │
│  │                     │                                             │    │
│  └─────────────────────┼─────────────────────────────────────────────┘    │
│                        ▼                                                   │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                      ENRICHED CONTACT DATABASE                     │    │
│  │                                                                    │    │
│  │  Additional fields:                                               │    │
│  │  - contact_name                                                   │    │
│  │  - contact_title (Owner, Manager, Buyer)                         │    │
│  │  - contact_email                                                  │    │
│  │  - contact_phone                                                  │    │
│  │  - linkedin_url                                                   │    │
│  │  - email_verified (boolean)                                       │    │
│  │  - enrichment_source                                              │    │
│  │  - enrichment_status = 'complete' | 'partial' | 'failed'         │    │
│  │  - ready_for_outreach (boolean)                                   │    │
│  │                                                                    │    │
│  └────────────────────────────┬───────────────────────────────────────┘    │
│                               │                                            │
└───────────────────────────────┼────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 3: OUTREACH                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    AI PERSONALIZATION ENGINE                       │    │
│  │                                                                    │    │
│  │  For each contact where ready_for_outreach = true:                │    │
│  │                                                                    │    │
│  │  ┌──────────────────────────────────────────────────────────────┐ │    │
│  │  │ Context Gathering:                                           │ │    │
│  │  │ - Business type (c-store, liquor, vape, etc.)               │ │    │
│  │  │ - Location (neighborhood/city context)                       │ │    │
│  │  │ - Reviews/rating (mention if high)                          │ │    │
│  │  │ - Any unique attributes                                      │ │    │
│  │  └──────────────────┬───────────────────────────────────────────┘ │    │
│  │                     │                                             │    │
│  │                     ▼                                             │    │
│  │  ┌──────────────────────────────────────────────────────────────┐ │    │
│  │  │ Claude API - Email Generation:                               │ │    │
│  │  │                                                              │ │    │
│  │  │ System Prompt:                                               │ │    │
│  │  │ "You are writing outreach emails for Wingman Labs,          │ │    │
│  │  │  a pharmaceutical-grade energy strip company. Write         │ │    │
│  │  │  direct, personal emails to store owners. Be specific       │ │    │
│  │  │  to their business type. No fluff. Reference their          │ │    │
│  │  │  specific store/location. Goal: get a brief call or         │ │    │
│  │  │  meeting to discuss carrying the product."                  │ │    │
│  │  │                                                              │ │    │
│  │  │ Variables:                                                   │ │    │
│  │  │ {{contact_name}}                                            │ │    │
│  │  │ {{business_name}}                                           │ │    │
│  │  │ {{business_type}}                                           │ │    │
│  │  │ {{city}}                                                    │ │    │
│  │  │ {{personalization_hook}}                                    │ │    │
│  │  │                                                              │ │    │
│  │  └──────────────────┬───────────────────────────────────────────┘ │    │
│  │                     │                                             │    │
│  └─────────────────────┼─────────────────────────────────────────────┘    │
│                        ▼                                                   │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    EMAIL SEQUENCE (Instantly.ai)                   │    │
│  │                                                                    │    │
│  │  ┌─────────────┐                                                  │    │
│  │  │  Email 1    │  Day 0: Initial outreach                        │    │
│  │  │  (Custom)   │  "Quick question about [Store Name]"            │    │
│  │  └──────┬──────┘                                                  │    │
│  │         │                                                         │    │
│  │         ▼ (Wait 3 days, if no reply)                             │    │
│  │  ┌─────────────┐                                                  │    │
│  │  │  Email 2    │  Day 3: Value add                               │    │
│  │  │  (Follow-up)│  "Thought you'd find this interesting..."       │    │
│  │  └──────┬──────┘                                                  │    │
│  │         │                                                         │    │
│  │         ▼ (Wait 4 days, if no reply)                             │    │
│  │  ┌─────────────┐                                                  │    │
│  │  │  Email 3    │  Day 7: Social proof                            │    │
│  │  │  (Follow-up)│  "Other [city] stores are seeing..."            │    │
│  │  └──────┬──────┘                                                  │    │
│  │         │                                                         │    │
│  │         ▼ (Wait 5 days, if no reply)                             │    │
│  │  ┌─────────────┐                                                  │    │
│  │  │  Email 4    │  Day 12: Direct ask                             │    │
│  │  │  (Follow-up)│  "15 minutes this week?"                        │    │
│  │  └──────┬──────┘                                                  │    │
│  │         │                                                         │    │
│  │         ▼ (Wait 7 days, if no reply)                             │    │
│  │  ┌─────────────┐                                                  │    │
│  │  │  Email 5    │  Day 19: Breakup                                │    │
│  │  │  (Final)    │  "Closing the loop"                             │    │
│  │  └──────┬──────┘                                                  │    │
│  │         │                                                         │    │
│  │         ▼                                                         │    │
│  │  ┌─────────────┐                                                  │    │
│  │  │  Move to    │  Mark as "sequence_complete"                    │    │
│  │  │  nurture    │  Add to monthly newsletter                      │    │
│  │  └─────────────┘                                                  │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PHASE 4: RESPONSE HANDLING                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    AI RESPONSE CLASSIFIER                          │    │
│  │                                                                    │    │
│  │  When reply received, classify into:                              │    │
│  │                                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ POSITIVE_INTERESTED                                         │  │    │
│  │  │ "Yes, I'd like to learn more"                              │  │    │
│  │  │ "Can you send pricing?"                                     │  │    │
│  │  │ "When can we talk?"                                        │  │    │
│  │  │ → Action: Route to CONVERT phase                           │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ QUESTION                                                    │  │    │
│  │  │ "What's the MOQ?"                                          │  │    │
│  │  │ "What's your margin?"                                       │  │    │
│  │  │ "Do you have samples?"                                      │  │    │
│  │  │ → Action: AI generates answer, human review optional        │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ OBJECTION                                                   │  │    │
│  │  │ "We already carry energy products"                         │  │    │
│  │  │ "Not interested in new vendors"                            │  │    │
│  │  │ "Too expensive"                                            │  │    │
│  │  │ → Action: AI generates objection handler, human review     │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ NOT_NOW                                                     │  │    │
│  │  │ "Contact me in 3 months"                                   │  │    │
│  │  │ "After the new year"                                       │  │    │
│  │  │ → Action: Schedule follow-up, add to nurture               │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ NEGATIVE                                                    │  │    │
│  │  │ "Not interested"                                           │  │    │
│  │  │ "Remove me from your list"                                 │  │    │
│  │  │ → Action: Unsubscribe, mark as DNC                        │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                    │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ NEEDS_HUMAN                                                 │  │    │
│  │  │ Complex questions, special requests                        │  │    │
│  │  │ → Action: Alert human, pause automation                    │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 5: CONVERT                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    QUOTE GENERATION SYSTEM                         │    │
│  │                                                                    │    │
│  │  When contact shows interest:                                      │    │
│  │                                                                    │    │
│  │  1. Auto-generate custom quote based on:                          │    │
│  │     - Store type (c-store vs liquor vs specialty)                 │    │
│  │     - Estimated volume (based on reviews/rating)                  │    │
│  │     - Location (delivery logistics)                               │    │
│  │                                                                    │    │
│  │  2. Include:                                                       │    │
│  │     - Product catalog (Energy, Sleep, Bundle)                     │    │
│  │     - Wholesale pricing tiers                                      │    │
│  │     - Suggested MOQ (starter pack option)                         │    │
│  │     - Payment terms                                                │    │
│  │     - Delivery info                                                │    │
│  │                                                                    │    │
│  │  3. Send via:                                                      │    │
│  │     - Email with PDF attached                                      │    │
│  │     - Optional: Docusign-style acceptance                         │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    MEETING SCHEDULING                              │    │
│  │                                                                    │    │
│  │  If call/meeting requested:                                        │    │
│  │  - Send Calendly/Cal.com link                                      │    │
│  │  - Pre-populate with context                                       │    │
│  │  - Auto-send reminder                                              │    │
│  │  - Auto-send follow-up after meeting                              │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                    ORDER PROCESSING                                │    │
│  │                                                                    │    │
│  │  When order confirmed:                                             │    │
│  │  - Generate invoice                                                │    │
│  │  - Update CRM status                                               │    │
│  │  - Trigger fulfillment                                             │    │
│  │  - Schedule follow-up check-in (2 weeks)                          │    │
│  │  - Add to reorder automation                                       │    │
│  │                                                                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Human Touchpoints (Where Automation Pauses)

### Required Human Review

1. **Complex negotiations** - Custom pricing, special terms
2. **Large orders** - Orders over $1,000 initial
3. **Complaints/issues** - Negative responses that escalate
4. **Legal/compliance** - Any questions about FDA, claims, etc.
5. **Partnership requests** - Distribution, exclusive deals

### Optional Human Review

1. **First email send** - Review AI-generated personalization initially
2. **Objection responses** - AI drafts, human can approve
3. **Quote approval** - For custom pricing scenarios

### Notification System

- **Slack alerts** for human-needed situations
- **Daily digest** of pipeline status
- **Weekly report** of metrics

---

## Tech Stack Summary

| Component | Primary Tool | Backup/Alternative |
|-----------|-------------|-------------------|
| Retailer Discovery | Google Places API | Yelp API |
| Data Storage | PostgreSQL | Airtable |
| Contact Enrichment | Apollo.io | Hunter.io, Clay |
| Email Personalization | Claude API | GPT-4 |
| Email Automation | Instantly.ai | Smartlead |
| Response Classification | Claude API | GPT-4 |
| CRM | HubSpot | Pipedrive |
| Quote Generation | Custom (Python) | PandaDoc |
| Scheduling | Calendly | Cal.com |
| Notifications | Slack | Email |
| Orchestration | Python + Celery | n8n, Zapier |

---

## Database Schema

```sql
-- Core retailers table
CREATE TABLE retailers (
    retailer_id UUID PRIMARY KEY,
    business_name VARCHAR(255) NOT NULL,
    address VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(2),
    zip VARCHAR(10),
    phone VARCHAR(20),
    website VARCHAR(255),
    business_type VARCHAR(50), -- c-store, liquor, vape, pharmacy, etc.
    google_place_id VARCHAR(100),
    yelp_id VARCHAR(100),
    rating DECIMAL(2,1),
    review_count INTEGER,
    hours JSONB,
    source VARCHAR(50),
    scraped_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Contacts table
CREATE TABLE contacts (
    contact_id UUID PRIMARY KEY,
    retailer_id UUID REFERENCES retailers(retailer_id),
    contact_name VARCHAR(255),
    contact_title VARCHAR(100),
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    linkedin_url VARCHAR(255),
    email_verified BOOLEAN DEFAULT FALSE,
    enrichment_source VARCHAR(50),
    enrichment_status VARCHAR(20), -- pending, complete, partial, failed
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Outreach tracking
CREATE TABLE outreach (
    outreach_id UUID PRIMARY KEY,
    contact_id UUID REFERENCES contacts(contact_id),
    sequence_name VARCHAR(100),
    email_number INTEGER,
    email_subject VARCHAR(255),
    email_body TEXT,
    sent_at TIMESTAMP,
    opened_at TIMESTAMP,
    clicked_at TIMESTAMP,
    replied_at TIMESTAMP,
    reply_classification VARCHAR(50),
    status VARCHAR(50) -- pending, sent, opened, replied, converted, unsubscribed
);

-- Pipeline/deals
CREATE TABLE deals (
    deal_id UUID PRIMARY KEY,
    retailer_id UUID REFERENCES retailers(retailer_id),
    contact_id UUID REFERENCES contacts(contact_id),
    stage VARCHAR(50), -- lead, contacted, interested, quoted, negotiating, won, lost
    quote_amount DECIMAL(10,2),
    products JSONB,
    notes TEXT,
    won_at TIMESTAMP,
    lost_reason VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Response templates
CREATE TABLE response_templates (
    template_id UUID PRIMARY KEY,
    response_type VARCHAR(50), -- question, objection, interest
    trigger_keywords TEXT[],
    response_template TEXT,
    requires_human_review BOOLEAN DEFAULT FALSE
);
```

---

## API Integrations Required

### 1. Google Places API
- Text Search (find retailers by type)
- Place Details (get contact info)
- Nearby Search (radius-based)

### 2. Apollo.io API
- People Search (find contacts)
- Email Verification
- Company Enrichment

### 3. Instantly.ai API
- Campaign creation
- Lead upload
- Email sending
- Analytics retrieval

### 4. Claude API
- Email generation
- Response classification
- Objection handling

### 5. Slack API (optional)
- Notifications
- Human review requests

### 6. Calendly API (optional)
- Meeting scheduling
- Availability sync

---

## Security Considerations

1. **API Keys** - Store in environment variables, rotate regularly
2. **PII Handling** - Encrypt contact emails/phones at rest
3. **Unsubscribe Handling** - Immediate processing, maintain DNC list
4. **Rate Limiting** - Respect all API limits, implement backoff
5. **Data Retention** - Delete failed enrichment data after 30 days

---

## Monitoring & Alerting

### Key Metrics Dashboard

- Retailers scraped (daily/total)
- Enrichment success rate
- Emails sent/delivered/opened/replied
- Response rate by segment
- Pipeline value
- Conversion rate

### Alerts

- Email deliverability drops below 90%
- Response rate drops below 3%
- API errors/failures
- Human review queue > 10 items

---

*Design document v1.0 - 2026-01-30*
