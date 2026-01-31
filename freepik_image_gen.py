#!/usr/bin/env python3
"""
Freepik Image Generation Script
Generates product photos and ad creatives using Freepik's Mystic AI model
Supports reference photos for structure and style, with text accuracy
"""

import requests
import json
import time
import base64
import os
from pathlib import Path
from typing import Optional, Dict, List, Union
import sys

# Load API key from credentials
def load_api_key():
    """Load Freepik API key from credentials file"""
    creds_path = Path(__file__).parent / ".credentials.json"
    if not creds_path.exists():
        raise FileNotFoundError(
            "Credentials file not found. Run this script with --setup to configure."
        )
    
    with open(creds_path, 'r') as f:
        creds = json.load(f)
    
    return creds.get('freepik', {}).get('api_key')

# Base configuration
API_KEY = None  # Will be loaded on demand
BASE_URL = "https://api.freepik.com"

class FreepikImageGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Freepik Image Generator
        
        Args:
            api_key: Freepik API key (optional, will load from credentials if not provided)
        """
        self.api_key = api_key or load_api_key()
        self.headers = {
            "x-freepik-api-key": self.api_key,
            "Content-Type": "application/json"
        }
    
    def encode_image(self, image_path: str) -> str:
        """
        Encode an image file to base64 string
        
        Args:
            image_path: Path to image file
            
        Returns:
            Base64 encoded image string
        """
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    
    def generate_image(
        self,
        prompt: str,
        resolution: str = "2k",
        aspect_ratio: str = "square_1_1",
        model: str = "realism",
        structure_reference: Optional[str] = None,
        structure_strength: int = 50,
        style_reference: Optional[str] = None,
        adherence: int = 50,
        hdr: int = 50,
        creative_detailing: int = 33,
        engine: str = "automatic",
        webhook_url: Optional[str] = None,
        characters: Optional[List[Dict]] = None,
        styles: Optional[List[Dict]] = None,
        colors: Optional[List[Dict]] = None,
        fixed_generation: bool = False
    ) -> Dict:
        """
        Generate an image using Freepik Mystic AI
        
        Args:
            prompt: Text description of the image to generate
            resolution: Image resolution (1k, 2k, 4k)
            aspect_ratio: Image aspect ratio (e.g., square_1_1, widescreen_16_9)
            model: AI model to use (realism, fluid, zen, flexible, super_real, editorial_portraits)
            structure_reference: Path to reference image for structure guidance
            structure_strength: Strength of structure reference (0-100)
            style_reference: Path to reference image for style guidance
            adherence: Prompt adherence when using style reference (0-100)
            hdr: HDR level when using style reference (0-100)
            creative_detailing: Detail level (0-100)
            engine: Processing engine (automatic, magnific_illusio, magnific_sharpy, magnific_sparkle)
            webhook_url: Optional webhook for async notifications
            characters: Optional list of character configurations
            styles: Optional list of style configurations
            colors: Optional list of color palette configurations
            fixed_generation: If True, same settings produce same image
            
        Returns:
            dict: API response with task_id and status
        """
        payload = {
            "prompt": prompt,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "model": model,
            "creative_detailing": creative_detailing,
            "engine": engine,
            "fixed_generation": fixed_generation
        }
        
        # Add structure reference if provided
        if structure_reference:
            if os.path.exists(structure_reference):
                payload["structure_reference"] = self.encode_image(structure_reference)
                payload["structure_strength"] = structure_strength
            else:
                print(f"Warning: Structure reference file not found: {structure_reference}")
        
        # Add style reference if provided
        if style_reference:
            if os.path.exists(style_reference):
                payload["style_reference"] = self.encode_image(style_reference)
                payload["adherence"] = adherence
                payload["hdr"] = hdr
            else:
                print(f"Warning: Style reference file not found: {style_reference}")
        
        # Add webhook if provided
        if webhook_url:
            payload["webhook_url"] = webhook_url
        
        # Add styling options if provided
        styling = {}
        if characters:
            styling["characters"] = characters
        if styles:
            styling["styles"] = styles
        if colors:
            styling["colors"] = colors
        
        if styling:
            payload["styling"] = styling
        
        # Make API request
        response = requests.post(
            f"{BASE_URL}/v1/ai/mystic",
            headers=self.headers,
            json=payload
        )
        
        response.raise_for_status()
        return response.json()
    
    def check_task_status(self, task_id: str) -> Dict:
        """
        Check the status of a generation task
        
        Args:
            task_id: Task ID returned from generate_image
            
        Returns:
            dict: Task status and generated image URLs (if completed)
        """
        response = requests.get(
            f"{BASE_URL}/v1/ai/mystic/{task_id}",
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
        """
        Wait for image generation to complete
        
        Args:
            task_id: Task ID to monitor
            poll_interval: Seconds between status checks
            max_wait: Maximum seconds to wait
            verbose: Print status updates
            
        Returns:
            dict: Final task status with generated image URLs
        """
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
        """
        Download generated image
        
        Args:
            url: Image URL from completed task
            output_path: Where to save the image
            
        Returns:
            str: Path to saved image
        """
        response = requests.get(url)
        response.raise_for_status()
        
        # Create output directory if it doesn't exist
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
        """
        Generate image and automatically download when complete
        
        Args:
            prompt: Text description of image
            output_path: Where to save the final image
            **kwargs: Additional arguments passed to generate_image
            
        Returns:
            str: Path to downloaded image
        """
        print(f"Generating image: {prompt[:80]}...")
        
        # Generate image
        response = self.generate_image(prompt, **kwargs)
        task_id = response.get('data', {}).get('task_id')
        
        if not task_id:
            raise RuntimeError(f"No task_id in response: {response}")
        
        print(f"Task created: {task_id}")
        
        # Wait for completion
        result = self.wait_for_completion(task_id)
        
        # Get image URL
        images = result.get('data', {}).get('generated', [])
        if not images:
            raise RuntimeError(f"No images generated: {result}")
        
        image_url = images[0]
        print(f"Image generated: {image_url}")
        
        # Download
        print(f"Downloading to: {output_path}")
        self.download_image(image_url, output_path)
        
        print(f"✓ Image saved: {output_path}")
        return output_path
    
    def list_available_loras(self) -> Dict:
        """
        List available LoRAs (styles and characters)
        
        Returns:
            dict: Available LoRAs with names and IDs
        """
        response = requests.get(
            f"{BASE_URL}/v1/ai/loras",
            headers=self.headers
        )
        
        response.raise_for_status()
        return response.json()


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate images using Freepik Mystic AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Simple generation
  python freepik_image_gen.py "a red sports car on a mountain road" -o car.jpg
  
  # Product photo with high detail
  python freepik_image_gen.py "professional product photo of wireless headphones on white background" \\
    -o headphones.jpg --resolution 4k --model super_real --detailing 50
  
  # Ad creative with reference style
  python freepik_image_gen.py "modern cafe interior with customers" \\
    -o cafe_ad.jpg --style-ref style_example.jpg --aspect widescreen_16_9
  
  # Use structure reference (sketch to photo)
  python freepik_image_gen.py "realistic portrait of a person" \\
    -o portrait.jpg --structure-ref sketch.jpg --structure-strength 70
  
  # List available styles
  python freepik_image_gen.py --list-loras
        """
    )
    
    parser.add_argument('prompt', nargs='?', help='Text description of image to generate')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('--resolution', default='2k', choices=['1k', '2k', '4k'],
                       help='Image resolution (default: 2k)')
    parser.add_argument('--aspect', default='square_1_1',
                       choices=['square_1_1', 'classic_4_3', 'traditional_3_4',
                               'widescreen_16_9', 'social_story_9_16', 
                               'smartphone_horizontal_20_9', 'smartphone_vertical_9_20',
                               'standard_3_2', 'portrait_2_3', 'horizontal_2_1',
                               'vertical_1_2', 'social_5_4', 'social_post_4_5'],
                       help='Aspect ratio (default: square_1_1)')
    parser.add_argument('--model', default='realism',
                       choices=['realism', 'fluid', 'zen', 'flexible', 'super_real', 'editorial_portraits'],
                       help='AI model (default: realism)')
    parser.add_argument('--engine', default='automatic',
                       choices=['automatic', 'magnific_illusio', 'magnific_sharpy', 'magnific_sparkle'],
                       help='Processing engine (default: automatic)')
    parser.add_argument('--structure-ref', help='Path to structure reference image')
    parser.add_argument('--structure-strength', type=int, default=50,
                       help='Structure reference strength 0-100 (default: 50)')
    parser.add_argument('--style-ref', help='Path to style reference image')
    parser.add_argument('--adherence', type=int, default=50,
                       help='Prompt adherence with style ref 0-100 (default: 50)')
    parser.add_argument('--hdr', type=int, default=50,
                       help='HDR level with style ref 0-100 (default: 50)')
    parser.add_argument('--detailing', type=int, default=33,
                       help='Creative detailing level 0-100 (default: 33)')
    parser.add_argument('--fixed', action='store_true',
                       help='Use fixed generation (same settings = same image)')
    parser.add_argument('--list-loras', action='store_true',
                       help='List available LoRAs (styles and characters)')
    
    args = parser.parse_args()
    
    try:
        generator = FreepikImageGenerator()
        
        # List LoRAs if requested
        if args.list_loras:
            print("Fetching available LoRAs...")
            loras = generator.list_available_loras()
            print(json.dumps(loras, indent=2))
            return
        
        # Validate required arguments for generation
        if not args.prompt:
            parser.error("prompt is required (unless using --list-loras)")
        if not args.output:
            parser.error("-o/--output is required")
        
        # Generate image
        generator.generate_and_download(
            prompt=args.prompt,
            output_path=args.output,
            resolution=args.resolution,
            aspect_ratio=args.aspect,
            model=args.model,
            engine=args.engine,
            structure_reference=args.structure_ref,
            structure_strength=args.structure_strength,
            style_reference=args.style_ref,
            adherence=args.adherence,
            hdr=args.hdr,
            creative_detailing=args.detailing,
            fixed_generation=args.fixed
        )
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
