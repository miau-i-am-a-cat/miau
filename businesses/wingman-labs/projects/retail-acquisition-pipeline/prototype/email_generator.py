#!/usr/bin/env python3
"""
Wingman Labs Retail Acquisition Pipeline
AI Email Personalization Module

Generates personalized outreach emails for each retailer
using Claude API.
"""

import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    anthropic = None


# Email templates for different business types
EMAIL_TEMPLATES = {
    "c-store": {
        "hook": "energy drinks are your #1 packaged beverage category",
        "benefit": "grab-and-go format that sits right at checkout",
        "social_proof": "convenience stores across LA"
    },
    "liquor": {
        "hook": "customers looking for something beyond Red Bull",
        "benefit": "premium positioning with better margins than energy drinks",
        "social_proof": "liquor stores in the LA area"
    },
    "vape": {
        "hook": "your customers already understand bioavailability",
        "benefit": "strip format they'll instantly recognize",
        "social_proof": "vape shops who've added our strips"
    },
    "gas-station": {
        "hook": "impulse buys at the counter drive your margin",
        "benefit": "pocket-sized format perfect for checkout display",
        "social_proof": "gas station convenience stores"
    },
    "pharmacy": {
        "hook": "customers asking for cleaner energy alternatives",
        "benefit": "pharmaceutical-grade ingredients they can trust",
        "social_proof": "independent pharmacies"
    },
    "health-food": {
        "hook": "clean, functional products are what your customers want",
        "benefit": "no sugar, no artificial ingredients, real bioavailability",
        "social_proof": "health food stores"
    },
    "supplement": {
        "hook": "your customers understand supplement quality",
        "benefit": "bioavailable delivery that actually works",
        "social_proof": "supplement retailers"
    },
    "smoke-shop": {
        "hook": "your customers appreciate innovative formats",
        "benefit": "discreet, portable, instantly dissolving strips",
        "social_proof": "smoke shops across California"
    }
}

@dataclass
class EmailOutput:
    """Generated email content."""
    subject: str
    body: str
    personalization_notes: str
    follow_up_1: Optional[str] = None
    follow_up_2: Optional[str] = None


class EmailGenerator:
    """Generates personalized outreach emails using Claude."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if self.api_key and HAS_ANTHROPIC:
            self.client = anthropic.Anthropic(api_key=self.api_key)
        else:
            self.client = None
    
    def generate_email(
        self,
        retailer: Dict,
        sender_name: str = "Alex",
        sender_title: str = "Partnerships",
        company: str = "Wingman Labs"
    ) -> EmailOutput:
        """
        Generate a personalized outreach email for a retailer.
        
        Args:
            retailer: Dict with retailer info (business_name, business_type, city, etc.)
            sender_name: Name of the person sending
            sender_title: Title of sender
            company: Company name
        
        Returns:
            EmailOutput with subject, body, and notes
        """
        business_type = retailer.get('business_type', 'c-store')
        template = EMAIL_TEMPLATES.get(business_type, EMAIL_TEMPLATES['c-store'])
        
        # Build context for AI
        context = {
            "business_name": retailer.get('business_name', 'your store'),
            "business_type": business_type,
            "city": retailer.get('city', 'your area'),
            "rating": retailer.get('rating'),
            "review_count": retailer.get('review_count'),
            "contact_name": retailer.get('contact_name'),
            "template": template
        }
        
        if self.client:
            return self._generate_with_ai(context, sender_name, sender_title, company)
        else:
            return self._generate_template(context, sender_name, sender_title, company)
    
    def _generate_with_ai(
        self,
        context: Dict,
        sender_name: str,
        sender_title: str,
        company: str
    ) -> EmailOutput:
        """Generate email using Claude API."""
        
        system_prompt = """You are writing cold outreach emails for Wingman Labs, 
a company that makes pharmaceutical-grade dissolving energy and sleep strips.

Product: Wingman Energy Strips
- Dissolves on tongue in 30 seconds
- 100mg caffeine + B-vitamins + adaptogens
- Pharmaceutical-grade bioavailability (better absorption than drinks)
- Compact format, perfect for checkout display
- Good margins for retailers

Your job: Write short, direct, personalized emails to store owners.

Rules:
1. SHORT. 3-5 sentences max for the main pitch.
2. SPECIFIC. Reference their actual store name and city.
3. NO FLUFF. No "I hope this email finds you well."
4. DIRECT ASK. Ask for a 10-minute call or quick chat.
5. AUTHENTIC. Sound like a real human, not a sales robot.

The goal is to get a brief conversation started, not close a deal in one email."""

        user_prompt = f"""Write an outreach email for this retailer:

Business Name: {context['business_name']}
Business Type: {context['business_type']}
City: {context['city']}
Rating: {context.get('rating', 'N/A')} ({context.get('review_count', 'N/A')} reviews)
Contact Name: {context.get('contact_name', 'Not available')}

Key hook for this business type: {context['template']['hook']}
Key benefit: {context['template']['benefit']}

Sender: {sender_name}, {sender_title} at {company}

Return the email in this exact format:
SUBJECT: [subject line]
BODY:
[email body]
PERSONALIZATION_NOTES:
[brief notes on why this approach was chosen]"""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=800,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}]
        )
        
        return self._parse_ai_response(response.content[0].text)
    
    def _generate_template(
        self,
        context: Dict,
        sender_name: str,
        sender_title: str,
        company: str
    ) -> EmailOutput:
        """Generate email using templates (no API needed)."""
        
        template = context['template']
        business_name = context['business_name']
        city = context['city']
        contact_name = context.get('contact_name')
        
        # Personalized greeting
        if contact_name:
            greeting = f"Hi {contact_name.split()[0]},"
        else:
            greeting = f"Hi there,"
        
        # Build subject line
        subjects = [
            f"Quick question about {business_name}",
            f"Spotted {business_name} - had an idea",
            f"For {business_name}: new product for your checkout counter",
            f"{city} stores are asking about this"
        ]
        subject = subjects[hash(business_name) % len(subjects)]
        
        # Build body
        body = f"""{greeting}

I run partnerships at {company}. We make energy strips — think breath strips, but with 100mg caffeine, B-vitamins, and adaptogens that actually absorb properly.

Given {template['hook']}, thought this might be a good fit for {business_name}. It's a {template['benefit']} that customers grab on impulse.

A few {template['social_proof']} have started carrying us. Happy to send samples or hop on a 10-minute call if you're curious.

— {sender_name}
{sender_title}, {company}"""

        personalization_notes = f"""
- Matched business type: {context['business_type']}
- Used type-specific hook about {template['hook']}
- Referenced city: {city}
- Subject line variant based on store name hash"""

        # Follow-up templates
        follow_up_1 = f"""{greeting}

Following up on my note about energy strips for {business_name}.

Quick stat: energy drinks are the #1 packaged beverage in convenience retail. Our strips are a premium alternative that sits at checkout — small footprint, high impulse buy rate.

Worth 10 minutes to see if it makes sense?

— {sender_name}"""

        follow_up_2 = f"""{greeting}

Last try — I'll keep it brief.

{company} makes energy strips that a handful of {template['social_proof']} are now carrying. We're based in LA, so can personally drop off samples if helpful.

Either way, no hard feelings. Just thought it'd be a fit.

— {sender_name}"""

        return EmailOutput(
            subject=subject,
            body=body,
            personalization_notes=personalization_notes,
            follow_up_1=follow_up_1,
            follow_up_2=follow_up_2
        )
    
    def _parse_ai_response(self, response_text: str) -> EmailOutput:
        """Parse AI response into EmailOutput."""
        subject = ""
        body = ""
        notes = ""
        
        lines = response_text.split('\n')
        current_section = None
        
        for line in lines:
            if line.startswith('SUBJECT:'):
                subject = line.replace('SUBJECT:', '').strip()
                current_section = 'subject'
            elif line.startswith('BODY:'):
                current_section = 'body'
            elif line.startswith('PERSONALIZATION_NOTES:'):
                current_section = 'notes'
            elif current_section == 'body':
                body += line + '\n'
            elif current_section == 'notes':
                notes += line + '\n'
        
        return EmailOutput(
            subject=subject,
            body=body.strip(),
            personalization_notes=notes.strip()
        )
    
    def generate_batch(
        self,
        retailers: List[Dict],
        output_file: Optional[str] = None
    ) -> List[Dict]:
        """Generate emails for a batch of retailers."""
        results = []
        
        for i, retailer in enumerate(retailers):
            print(f"Generating email {i+1}/{len(retailers)}: {retailer.get('business_name')}")
            
            email = self.generate_email(retailer)
            
            result = {
                "retailer_id": retailer.get('retailer_id'),
                "business_name": retailer.get('business_name'),
                "business_type": retailer.get('business_type'),
                "email": {
                    "subject": email.subject,
                    "body": email.body,
                    "follow_up_1": email.follow_up_1,
                    "follow_up_2": email.follow_up_2
                },
                "personalization_notes": email.personalization_notes
            }
            results.append(result)
        
        if output_file:
            os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nSaved {len(results)} emails to {output_file}")
        
        return results


def main():
    """Demo the email generator."""
    print("Wingman Labs Email Generator")
    print("="*50)
    
    # Sample retailers for demo
    sample_retailers = [
        {
            "retailer_id": "demo-001",
            "business_name": "Quick Stop Convenience",
            "business_type": "c-store",
            "city": "Los Angeles",
            "state": "CA",
            "rating": 4.2,
            "review_count": 87
        },
        {
            "retailer_id": "demo-002",
            "business_name": "Downtown Liquor & Wine",
            "business_type": "liquor",
            "city": "Los Angeles",
            "state": "CA",
            "rating": 4.5,
            "review_count": 156
        },
        {
            "retailer_id": "demo-003",
            "business_name": "Cloud 9 Vape Shop",
            "business_type": "vape",
            "city": "Los Angeles",
            "state": "CA",
            "rating": 4.8,
            "review_count": 234
        }
    ]
    
    generator = EmailGenerator()
    
    for retailer in sample_retailers:
        print(f"\n{'='*50}")
        print(f"Store: {retailer['business_name']} ({retailer['business_type']})")
        print('='*50)
        
        email = generator.generate_email(retailer)
        
        print(f"\nSUBJECT: {email.subject}")
        print(f"\n{email.body}")
        print(f"\n--- Follow-up 1 ---")
        print(email.follow_up_1)
    
    # Save batch output
    print("\n" + "="*50)
    print("Generating batch output...")
    generator.generate_batch(
        sample_retailers,
        output_file="data/generated_emails.json"
    )


if __name__ == "__main__":
    main()
