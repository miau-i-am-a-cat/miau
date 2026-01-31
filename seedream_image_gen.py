#!/usr/bin/env python3
"""
Seedream 4.5 Image Generation Script
Best for: Marketing materials with text, posters, branded visuals
ByteDance's model with superior typography and up to 4MP resolution
"""

import requests
import json
import time
import os
from pathlib import Path
from typing import Optional, Dict
import sys

# Load API key from credentials
def load_api_key():
    """Load Freepik API key from credentials file"""
    creds_path = Path(__file__).parent / ".credentials.json"
    if not creds_path.exists():
        raise FileNotFoundError("Credentials file not found.")
    
    with open(creds_path, 'r') as f:
        creds = json.load(f)
    
    return creds.get('freepik', {}).get('api_key')

BASE_URL = "https://api.freepik.com"

class SeedreamImageGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize Seedream 4.5 Image Generator"""
        self.api_key = api_key or load_api_key()
        self.headers = {
            "x-freepik-api-key": self.api_key,
            "Content-Type": "application/json"
        }
    
    def generate_image(
        self,
        prompt: str,
        aspect_ratio: str = "square_1_1",
        seed: Optional[int] = None,
        enable_safety_checker: bool = True,
        webhook_url: Optional[str] = None
    ) -> Dict:
        """
        Generate an image using Seedream 4.5
        
        Args:
            prompt: Text description of the image
            aspect_ratio: Image aspect ratio (square_1_1, widescreen_16_9, etc.)
            seed: Random seed for reproducibility (0-4294967295)
            enable_safety_checker: Filter unsafe content
            webhook_url: Optional webhook for async notifications
            
        Returns:
            dict: API response with task_id and status
        """
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "enable_safety_checker": enable_safety_checker
        }
        
        if seed is not None:
            payload["seed"] = seed
        
        if webhook_url:
            payload["webhook_url"] = webhook_url
        
        response = requests.post(
            f"{BASE_URL}/v1/ai/text-to-image/seedream-v4-5",
            headers=self.headers,
            json=payload
        )
        
        response.raise_for_status()
        return response.json()
    
    def check_task_status(self, task_id: str) -> Dict:
        """Check the status of a generation task"""
        response = requests.get(
            f"{BASE_URL}/v1/ai/text-to-image/seedream-v4-5/{task_id}",
            headers=self.headers
        )
        
        response.raise_for_status()
        return response.json()
    
    def wait_for_completion(
        self,
        task_id: str,
        poll_interval: int = 3,
        max_wait: int = 300,
        verbose: bool = True
    ) -> Dict:
        """Wait for image generation to complete"""
        start_time = time.time()
        
        while True:
            elapsed = time.time() - start_time
            
            if elapsed > max_wait:
                raise TimeoutError(f"Task did not complete within {max_wait} seconds")
            
            status_data = self.check_task_status(task_id)
            status = status_data.get('data', {}).get('status')
            
            if verbose:
                print(f"Status: {status} (elapsed: {int(elapsed)}s)")
            
            if status == "COMPLETED":
                return status_data
            elif status == "FAILED":
                raise RuntimeError(f"Task failed: {status_data}")
            
            time.sleep(poll_interval)
    
    def download_image(self, url: str, output_path: str) -> str:
        """Download generated image"""
        response = requests.get(url)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        with open(output_path, 'wb') as f:
            f.write(response.content)
        
        return output_path
    
    def generate_and_download(
        self,
        prompt: str,
        output_path: str,
        **kwargs
    ) -> str:
        """Generate image and automatically download when complete"""
        print(f"Generating image: {prompt[:80]}...")
        
        response = self.generate_image(prompt, **kwargs)
        task_id = response.get('data', {}).get('task_id')
        
        if not task_id:
            raise RuntimeError(f"No task_id in response: {response}")
        
        print(f"Task created: {task_id}")
        
        result = self.wait_for_completion(task_id)
        
        images = result.get('data', {}).get('generated', [])
        if not images:
            raise RuntimeError(f"No images generated: {result}")
        
        image_url = images[0]
        print(f"Image generated: {image_url}")
        
        print(f"Downloading to: {output_path}")
        self.download_image(image_url, output_path)
        
        print(f"✓ Image saved: {output_path}")
        return output_path


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate images using Seedream 4.5 (best for marketing materials with text)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Marketing poster
  python seedream_image_gen.py "Professional marketing poster for tech startup" -o poster.jpg
  
  # Product with text/branding
  python seedream_image_gen.py "Product photo with '50%% OFF' text overlay" -o promo.jpg --aspect widescreen_16_9
  
  # Social media ad
  python seedream_image_gen.py "Instagram ad for coffee shop grand opening" -o social_ad.jpg --aspect social_story_9_16
  
  # Reproducible generation
  python seedream_image_gen.py "Logo design" -o logo.jpg --seed 12345

Best for:
  - Marketing materials with text
  - Professional posters and banners  
  - Branded visual content
  - High-resolution images (up to 4MP)
        """
    )
    
    parser.add_argument('prompt', help='Text description of image to generate')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    parser.add_argument('--aspect', default='square_1_1',
                       choices=['square_1_1', 'widescreen_16_9', 'social_story_9_16',
                               'portrait_2_3', 'traditional_3_4', 'standard_3_2',
                               'classic_4_3', 'cinematic_21_9'],
                       help='Aspect ratio (default: square_1_1)')
    parser.add_argument('--seed', type=int, help='Random seed for reproducibility (0-4294967295)')
    parser.add_argument('--no-safety', action='store_true', help='Disable safety checker')
    
    args = parser.parse_args()
    
    try:
        generator = SeedreamImageGenerator()
        
        generator.generate_and_download(
            prompt=args.prompt,
            output_path=args.output,
            aspect_ratio=args.aspect,
            seed=args.seed,
            enable_safety_checker=not args.no_safety
        )
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
