#!/usr/bin/env python3
"""
Quick test script for Freepik API setup
"""

from freepik_image_gen import FreepikImageGenerator
import sys

def test_api_connection():
    """Test API key and connection"""
    print("Testing Freepik API connection...")
    
    try:
        generator = FreepikImageGenerator()
        print("✓ API key loaded successfully")
        
        # Try to list LoRAs as a connection test
        print("Testing API connection...")
        loras = generator.list_available_loras()
        print(f"✓ API connection successful")
        print(f"✓ Found {len(loras.get('data', []))} available LoRAs")
        
        return True
        
    except FileNotFoundError as e:
        print(f"✗ Error: {e}")
        print("Run script with your API key to set up credentials")
        return False
    except Exception as e:
        print(f"✗ API connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_api_connection()
    sys.exit(0 if success else 1)
