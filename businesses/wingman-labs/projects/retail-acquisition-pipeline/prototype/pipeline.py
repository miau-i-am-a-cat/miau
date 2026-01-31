#!/usr/bin/env python3
"""
Wingman Labs Retail Acquisition Pipeline
Main Orchestrator

Coordinates the full pipeline:
1. Scrape retailers
2. Enrich contacts
3. Generate personalized emails
4. Export for email automation
"""

import os
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass

from scraper import RetailerScraper, Retailer
from email_generator import EmailGenerator


@dataclass
class PipelineStats:
    """Track pipeline metrics."""
    retailers_scraped: int = 0
    contacts_enriched: int = 0
    emails_generated: int = 0
    ready_for_outreach: int = 0
    run_time_seconds: float = 0


class RetailAcquisitionPipeline:
    """
    Main pipeline orchestrator for retailer acquisition.
    
    Pipeline stages:
    1. DISCOVER: Scrape retailer data from multiple sources
    2. ENRICH: Find contact information (owner/manager email)
    3. PERSONALIZE: Generate AI-personalized emails
    4. EXPORT: Format for email automation tool (Instantly, Smartlead)
    """
    
    def __init__(
        self,
        google_api_key: Optional[str] = None,
        anthropic_api_key: Optional[str] = None,
        apollo_api_key: Optional[str] = None,
        data_dir: str = "data"
    ):
        self.google_api_key = google_api_key or os.environ.get('GOOGLE_PLACES_API_KEY')
        self.anthropic_api_key = anthropic_api_key or os.environ.get('ANTHROPIC_API_KEY')
        self.apollo_api_key = apollo_api_key or os.environ.get('APOLLO_API_KEY')
        
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
        self.stats = PipelineStats()
    
    def run_full_pipeline(
        self,
        locations: List[str],
        radius_miles: float = 5,
        max_retailers: Optional[int] = None
    ) -> Dict:
        """
        Run the complete pipeline for given locations.
        
        Args:
            locations: List of zip codes or city names
            radius_miles: Search radius per location
            max_retailers: Optional cap on total retailers
        
        Returns:
            Summary dict with results and stats
        """
        start_time = datetime.now()
        print("\n" + "="*60)
        print("WINGMAN LABS RETAIL ACQUISITION PIPELINE")
        print("="*60)
        
        # Stage 1: Discover
        print("\n📍 STAGE 1: DISCOVER RETAILERS")
        print("-"*40)
        retailers = self._stage_discover(locations, radius_miles)
        
        if max_retailers:
            retailers = retailers[:max_retailers]
        
        self.stats.retailers_scraped = len(retailers)
        print(f"✓ Found {len(retailers)} retailers")
        
        # Stage 2: Enrich
        print("\n📧 STAGE 2: ENRICH CONTACTS")
        print("-"*40)
        enriched = self._stage_enrich(retailers)
        self.stats.contacts_enriched = sum(1 for r in enriched if r.get('contact_email'))
        print(f"✓ Enriched {self.stats.contacts_enriched} contacts")
        
        # Stage 3: Personalize
        print("\n✍️ STAGE 3: GENERATE EMAILS")
        print("-"*40)
        with_emails = self._stage_personalize(enriched)
        self.stats.emails_generated = sum(1 for r in with_emails if r.get('email'))
        print(f"✓ Generated {self.stats.emails_generated} personalized emails")
        
        # Stage 4: Export
        print("\n📤 STAGE 4: EXPORT FOR OUTREACH")
        print("-"*40)
        export_file = self._stage_export(with_emails)
        self.stats.ready_for_outreach = len([r for r in with_emails if r.get('contact_email') and r.get('email')])
        print(f"✓ Exported {self.stats.ready_for_outreach} leads ready for outreach")
        
        # Calculate run time
        self.stats.run_time_seconds = (datetime.now() - start_time).total_seconds()
        
        # Summary
        print("\n" + "="*60)
        print("PIPELINE COMPLETE")
        print("="*60)
        print(f"""
📊 Results:
   Retailers scraped:    {self.stats.retailers_scraped}
   Contacts enriched:    {self.stats.contacts_enriched}
   Emails generated:     {self.stats.emails_generated}
   Ready for outreach:   {self.stats.ready_for_outreach}
   Run time:             {self.stats.run_time_seconds:.1f}s

📁 Output files:
   {self.data_dir}/retailers_raw.json
   {self.data_dir}/retailers_enriched.json
   {self.data_dir}/retailers_with_emails.json
   {export_file} (for Instantly.ai)
""")
        
        return {
            "stats": self.stats.__dict__,
            "export_file": export_file,
            "retailers": with_emails
        }
    
    def _stage_discover(self, locations: List[str], radius_miles: float) -> List[Dict]:
        """Stage 1: Discover retailers from multiple sources."""
        all_retailers = []
        
        if self.google_api_key:
            scraper = RetailerScraper(self.google_api_key)
            
            for location in locations:
                print(f"  Searching {location}...")
                retailers = scraper.search_area(location, radius_miles)
                all_retailers.extend([r.to_dict() for r in retailers])
        else:
            print("  [Demo mode - no Google API key]")
            all_retailers = self._load_sample_data()
        
        # Save raw data
        with open(f"{self.data_dir}/retailers_raw.json", 'w') as f:
            json.dump(all_retailers, f, indent=2)
        
        return all_retailers
    
    def _stage_enrich(self, retailers: List[Dict]) -> List[Dict]:
        """Stage 2: Enrich with contact information."""
        enriched = []
        
        for retailer in retailers:
            # Try to find contact info
            contact = self._find_contact(retailer)
            
            retailer.update({
                'contact_name': contact.get('name'),
                'contact_email': contact.get('email'),
                'contact_phone': contact.get('phone'),
                'contact_title': contact.get('title'),
                'enrichment_source': contact.get('source'),
                'enrichment_status': 'complete' if contact.get('email') else 'partial'
            })
            
            enriched.append(retailer)
        
        # Save enriched data
        with open(f"{self.data_dir}/retailers_enriched.json", 'w') as f:
            json.dump(enriched, f, indent=2)
        
        return enriched
    
    def _find_contact(self, retailer: Dict) -> Dict:
        """
        Find contact information for a retailer.
        
        In production, this would:
        1. Search Apollo.io
        2. Fall back to Hunter.io
        3. Try LinkedIn scraping
        4. Use AI research agent
        
        For demo, we generate placeholder data.
        """
        if self.apollo_api_key:
            # TODO: Implement Apollo.io lookup
            pass
        
        # Demo: Generate placeholder contact for some retailers
        business_name = retailer.get('business_name', '')
        
        # Simulate ~70% contact find rate
        if hash(business_name) % 10 < 7:
            # Generate plausible owner email
            domain = business_name.lower().replace(' ', '').replace("'", '')[:15]
            
            return {
                'name': f"Owner of {business_name}",
                'email': f"info@{domain}.com",
                'phone': retailer.get('phone'),
                'title': 'Owner',
                'source': 'demo_enrichment'
            }
        
        return {
            'name': None,
            'email': None,
            'phone': retailer.get('phone'),
            'title': None,
            'source': 'not_found'
        }
    
    def _stage_personalize(self, retailers: List[Dict]) -> List[Dict]:
        """Stage 3: Generate personalized emails."""
        generator = EmailGenerator(self.anthropic_api_key)
        
        for retailer in retailers:
            if retailer.get('contact_email'):
                email = generator.generate_email(retailer)
                retailer['email'] = {
                    'subject': email.subject,
                    'body': email.body,
                    'follow_up_1': email.follow_up_1,
                    'follow_up_2': email.follow_up_2
                }
                retailer['personalization_notes'] = email.personalization_notes
        
        # Save with emails
        with open(f"{self.data_dir}/retailers_with_emails.json", 'w') as f:
            json.dump(retailers, f, indent=2)
        
        return retailers
    
    def _stage_export(self, retailers: List[Dict]) -> str:
        """
        Stage 4: Export for email automation.
        
        Creates CSV in Instantly.ai format.
        """
        export_file = f"{self.data_dir}/instantly_import.csv"
        
        # Instantly.ai expects these columns
        fieldnames = [
            'email',
            'first_name',
            'last_name', 
            'company_name',
            'phone',
            'website',
            'custom_subject',
            'custom_body',
            'custom_follow_up_1',
            'custom_follow_up_2',
            # Custom fields
            'business_type',
            'city',
            'state',
            'retailer_id'
        ]
        
        with open(export_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for retailer in retailers:
                if not retailer.get('contact_email') or not retailer.get('email'):
                    continue
                
                # Parse name
                contact_name = retailer.get('contact_name', '')
                name_parts = contact_name.split(' ', 1) if contact_name else ['', '']
                first_name = name_parts[0]
                last_name = name_parts[1] if len(name_parts) > 1 else ''
                
                row = {
                    'email': retailer.get('contact_email'),
                    'first_name': first_name,
                    'last_name': last_name,
                    'company_name': retailer.get('business_name'),
                    'phone': retailer.get('phone', ''),
                    'website': retailer.get('website', ''),
                    'custom_subject': retailer['email']['subject'],
                    'custom_body': retailer['email']['body'],
                    'custom_follow_up_1': retailer['email'].get('follow_up_1', ''),
                    'custom_follow_up_2': retailer['email'].get('follow_up_2', ''),
                    'business_type': retailer.get('business_type'),
                    'city': retailer.get('city'),
                    'state': retailer.get('state'),
                    'retailer_id': retailer.get('retailer_id')
                }
                writer.writerow(row)
        
        return export_file
    
    def _load_sample_data(self) -> List[Dict]:
        """Load sample data for demo mode."""
        return [
            {
                "retailer_id": "demo-001",
                "business_name": "Quick Stop Convenience",
                "address": "123 Main St",
                "city": "Los Angeles",
                "state": "CA",
                "zip_code": "90012",
                "phone": "(213) 555-0101",
                "website": "https://quickstopla.com",
                "business_type": "c-store",
                "google_place_id": "ChIJ_sample1",
                "rating": 4.2,
                "review_count": 87,
                "latitude": 34.0522,
                "longitude": -118.2437,
                "source": "demo",
                "scraped_at": datetime.utcnow().isoformat()
            },
            {
                "retailer_id": "demo-002",
                "business_name": "Downtown Liquor & Wine",
                "address": "456 Spring St",
                "city": "Los Angeles",
                "state": "CA",
                "zip_code": "90013",
                "phone": "(213) 555-0202",
                "website": None,
                "business_type": "liquor",
                "google_place_id": "ChIJ_sample2",
                "rating": 4.5,
                "review_count": 156,
                "latitude": 34.0505,
                "longitude": -118.2456,
                "source": "demo",
                "scraped_at": datetime.utcnow().isoformat()
            },
            {
                "retailer_id": "demo-003",
                "business_name": "Cloud 9 Vape Shop",
                "address": "789 Broadway",
                "city": "Los Angeles",
                "state": "CA",
                "zip_code": "90014",
                "phone": "(213) 555-0303",
                "website": "https://cloud9vape.la",
                "business_type": "vape",
                "google_place_id": "ChIJ_sample3",
                "rating": 4.8,
                "review_count": 234,
                "latitude": 34.0489,
                "longitude": -118.2500,
                "source": "demo",
                "scraped_at": datetime.utcnow().isoformat()
            },
            {
                "retailer_id": "demo-004",
                "business_name": "Valley Health Foods",
                "address": "1234 Ventura Blvd",
                "city": "Sherman Oaks",
                "state": "CA",
                "zip_code": "91423",
                "phone": "(818) 555-0404",
                "website": "https://valleyhealthfoods.com",
                "business_type": "health-food",
                "google_place_id": "ChIJ_sample4",
                "rating": 4.6,
                "review_count": 312,
                "latitude": 34.1508,
                "longitude": -118.4512,
                "source": "demo",
                "scraped_at": datetime.utcnow().isoformat()
            },
            {
                "retailer_id": "demo-005",
                "business_name": "Sam's Gas & Mini Mart",
                "address": "5678 Sunset Blvd",
                "city": "Hollywood",
                "state": "CA",
                "zip_code": "90028",
                "phone": "(323) 555-0505",
                "website": None,
                "business_type": "gas-station",
                "google_place_id": "ChIJ_sample5",
                "rating": 3.9,
                "review_count": 45,
                "latitude": 34.0983,
                "longitude": -118.3267,
                "source": "demo",
                "scraped_at": datetime.utcnow().isoformat()
            }
        ]


def main():
    """Run the pipeline in demo mode."""
    print("\n🚀 WINGMAN LABS RETAIL ACQUISITION PIPELINE")
    print("   Demo Mode (no API keys required)")
    
    pipeline = RetailAcquisitionPipeline()
    
    # Run pipeline with sample LA zip codes
    results = pipeline.run_full_pipeline(
        locations=["90012", "90028", "91423"],
        radius_miles=3
    )
    
    # Show sample output
    print("\n" + "="*60)
    print("SAMPLE EMAIL OUTPUT")
    print("="*60)
    
    for retailer in results['retailers'][:2]:
        if retailer.get('email'):
            print(f"\n📧 To: {retailer.get('contact_email')}")
            print(f"   Company: {retailer.get('business_name')}")
            print(f"   Subject: {retailer['email']['subject']}")
            print(f"\n{retailer['email']['body']}")
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()
