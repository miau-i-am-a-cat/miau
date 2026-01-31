#!/usr/bin/env python3
"""
Wingman Labs Retail Acquisition Pipeline
Retailer Discovery Module

Scrapes convenience stores, liquor stores, vape shops, etc.
from Google Places API and other sources.
"""

import os
import json
import time
import uuid
import requests
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

# Load API key from environment
GOOGLE_API_KEY = os.environ.get('GOOGLE_PLACES_API_KEY')

@dataclass
class Retailer:
    """Represents a discovered retail location."""
    retailer_id: str
    business_name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone: Optional[str]
    website: Optional[str]
    business_type: str
    google_place_id: Optional[str]
    rating: Optional[float]
    review_count: Optional[int]
    latitude: float
    longitude: float
    source: str
    scraped_at: str

    def to_dict(self) -> Dict:
        return asdict(self)


class RetailerScraper:
    """Scrapes retailer data from multiple sources."""
    
    # Business types to search for
    BUSINESS_TYPES = [
        ("convenience_store", "c-store"),
        ("gas_station", "gas-station"),
        ("liquor_store", "liquor"),
        ("pharmacy", "pharmacy"),
        # Add more as needed
    ]
    
    # Custom search terms for types not in Google Places
    CUSTOM_SEARCHES = [
        ("vape shop", "vape"),
        ("smoke shop", "smoke-shop"),
        ("health food store", "health-food"),
        ("supplement store", "supplement"),
    ]
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://places.googleapis.com/v1/places:searchText"
        self.details_url = "https://places.googleapis.com/v1/places"
        
    def search_area(
        self,
        location: str,
        radius_miles: float = 10,
        business_types: Optional[List[str]] = None
    ) -> List[Retailer]:
        """
        Search for retailers in a given area.
        
        Args:
            location: City, zip code, or address to center search
            radius_miles: Search radius in miles
            business_types: Optional list of business types to search
        
        Returns:
            List of Retailer objects
        """
        retailers = []
        
        # Get coordinates for location
        coords = self._geocode(location)
        if not coords:
            print(f"Could not geocode location: {location}")
            return retailers
        
        lat, lng = coords
        radius_meters = int(radius_miles * 1609.34)
        
        # Search each business type
        types_to_search = business_types or [t[0] for t in self.BUSINESS_TYPES]
        
        for google_type, our_type in self.BUSINESS_TYPES:
            if google_type in types_to_search:
                print(f"Searching for {google_type} near {location}...")
                results = self._search_places(
                    query=google_type,
                    lat=lat,
                    lng=lng,
                    radius=radius_meters,
                    business_type=our_type
                )
                retailers.extend(results)
                time.sleep(0.5)  # Rate limiting
        
        # Custom text searches for specialized stores
        for search_term, our_type in self.CUSTOM_SEARCHES:
            print(f"Searching for '{search_term}' near {location}...")
            results = self._search_places(
                query=search_term,
                lat=lat,
                lng=lng,
                radius=radius_meters,
                business_type=our_type
            )
            retailers.extend(results)
            time.sleep(0.5)
        
        # Deduplicate by google_place_id
        seen = set()
        unique_retailers = []
        for r in retailers:
            if r.google_place_id and r.google_place_id not in seen:
                seen.add(r.google_place_id)
                unique_retailers.append(r)
            elif not r.google_place_id:
                unique_retailers.append(r)
        
        print(f"Found {len(unique_retailers)} unique retailers")
        return unique_retailers
    
    def _geocode(self, location: str) -> Optional[tuple]:
        """Convert location string to coordinates."""
        url = f"https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": location,
            "key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get("results"):
                loc = data["results"][0]["geometry"]["location"]
                return (loc["lat"], loc["lng"])
        except Exception as e:
            print(f"Geocoding error: {e}")
        
        return None
    
    def _search_places(
        self,
        query: str,
        lat: float,
        lng: float,
        radius: int,
        business_type: str
    ) -> List[Retailer]:
        """Search Google Places API for businesses."""
        retailers = []
        
        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
            "X-Goog-FieldMask": "places.id,places.displayName,places.formattedAddress,places.location,places.nationalPhoneNumber,places.websiteUri,places.rating,places.userRatingCount"
        }
        
        payload = {
            "textQuery": query,
            "locationBias": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": radius
                }
            },
            "maxResultCount": 20
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, json=payload)
            data = response.json()
            
            for place in data.get("places", []):
                retailer = self._parse_place(place, business_type)
                if retailer:
                    retailers.append(retailer)
                    
        except Exception as e:
            print(f"Search error: {e}")
        
        return retailers
    
    def _parse_place(self, place: Dict, business_type: str) -> Optional[Retailer]:
        """Parse Google Places result into Retailer object."""
        try:
            # Parse address components
            address = place.get("formattedAddress", "")
            address_parts = address.split(", ")
            
            # Extract city, state, zip (US format)
            city = ""
            state = ""
            zip_code = ""
            street_address = ""
            
            if len(address_parts) >= 3:
                street_address = address_parts[0]
                city = address_parts[-3] if len(address_parts) > 3 else address_parts[0]
                state_zip = address_parts[-2].split(" ")
                if len(state_zip) >= 2:
                    state = state_zip[0]
                    zip_code = state_zip[1] if len(state_zip) > 1 else ""
            
            location = place.get("location", {})
            
            return Retailer(
                retailer_id=str(uuid.uuid4()),
                business_name=place.get("displayName", {}).get("text", ""),
                address=street_address or address,
                city=city,
                state=state,
                zip_code=zip_code,
                phone=place.get("nationalPhoneNumber"),
                website=place.get("websiteUri"),
                business_type=business_type,
                google_place_id=place.get("id"),
                rating=place.get("rating"),
                review_count=place.get("userRatingCount"),
                latitude=location.get("latitude", 0),
                longitude=location.get("longitude", 0),
                source="google_places",
                scraped_at=datetime.utcnow().isoformat()
            )
        except Exception as e:
            print(f"Parse error: {e}")
            return None
    
    def save_to_json(self, retailers: List[Retailer], filename: str):
        """Save retailers to JSON file."""
        data = [r.to_dict() for r in retailers]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Saved {len(retailers)} retailers to {filename}")
    
    def load_from_json(self, filename: str) -> List[Retailer]:
        """Load retailers from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Retailer(**r) for r in data]


# LA Metro zip codes for phased rollout
LA_METRO_ZIPS = [
    # Downtown LA
    "90012", "90013", "90014", "90015", "90017",
    # Hollywood
    "90028", "90038", "90068",
    # West LA
    "90024", "90025", "90064",
    # Santa Monica
    "90401", "90402", "90403", "90404", "90405",
    # Venice/Marina
    "90291", "90292",
    # South LA
    "90001", "90002", "90003",
    # East LA
    "90022", "90023", "90033",
    # Valley
    "91601", "91602", "91604", "91605",
]


def main():
    """Example usage of the scraper."""
    if not GOOGLE_API_KEY:
        print("Error: Set GOOGLE_PLACES_API_KEY environment variable")
        print("\nDemo mode: Generating sample data...")
        
        # Generate sample data for testing
        sample_retailers = [
            Retailer(
                retailer_id=str(uuid.uuid4()),
                business_name="Quick Stop Convenience",
                address="123 Main St",
                city="Los Angeles",
                state="CA",
                zip_code="90012",
                phone="(213) 555-0101",
                website="https://quickstopla.com",
                business_type="c-store",
                google_place_id="ChIJ_sample1",
                rating=4.2,
                review_count=87,
                latitude=34.0522,
                longitude=-118.2437,
                source="demo",
                scraped_at=datetime.utcnow().isoformat()
            ),
            Retailer(
                retailer_id=str(uuid.uuid4()),
                business_name="Downtown Liquor & Wine",
                address="456 Spring St",
                city="Los Angeles",
                state="CA",
                zip_code="90013",
                phone="(213) 555-0202",
                website=None,
                business_type="liquor",
                google_place_id="ChIJ_sample2",
                rating=4.5,
                review_count=156,
                latitude=34.0505,
                longitude=-118.2456,
                source="demo",
                scraped_at=datetime.utcnow().isoformat()
            ),
            Retailer(
                retailer_id=str(uuid.uuid4()),
                business_name="Cloud 9 Vape Shop",
                address="789 Broadway",
                city="Los Angeles",
                state="CA",
                zip_code="90014",
                phone="(213) 555-0303",
                website="https://cloud9vape.la",
                business_type="vape",
                google_place_id="ChIJ_sample3",
                rating=4.8,
                review_count=234,
                latitude=34.0489,
                longitude=-118.2500,
                source="demo",
                scraped_at=datetime.utcnow().isoformat()
            ),
        ]
        
        # Save sample data
        output_file = "data/sample_retailers.json"
        os.makedirs("data", exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump([r.to_dict() for r in sample_retailers], f, indent=2)
        
        print(f"\nSaved {len(sample_retailers)} sample retailers to {output_file}")
        print("\nSample output:")
        print(json.dumps(sample_retailers[0].to_dict(), indent=2))
        return
    
    # Real scraping with API key
    scraper = RetailerScraper(GOOGLE_API_KEY)
    
    # Start with a few LA zip codes
    all_retailers = []
    for zip_code in LA_METRO_ZIPS[:3]:  # Start with 3 zip codes
        print(f"\n{'='*50}")
        print(f"Scraping zip code: {zip_code}")
        print('='*50)
        
        retailers = scraper.search_area(
            location=f"{zip_code}, California",
            radius_miles=2
        )
        all_retailers.extend(retailers)
        
        time.sleep(2)  # Be nice to the API
    
    # Save results
    os.makedirs("data", exist_ok=True)
    scraper.save_to_json(all_retailers, "data/la_retailers.json")
    
    print(f"\n{'='*50}")
    print(f"TOTAL: {len(all_retailers)} retailers found")
    print('='*50)


if __name__ == "__main__":
    main()
