#!/usr/bin/env python3
"""
Flux 2 Pro Image Generation
Best for: Marketing materials, advertisements, professional photography
Supports image-to-image with up to 4 reference images
"""

import requests
import json
import time
import base64
import os
from pathlib import Path
from typing import Optional
import sys

def load_api_key():
    creds_path = Path(__file__).parent / ".credentials.json"
    with open(creds_path, 'r') as f:
        return json.load(f).get('freepik', {}).get('api_key')

BASE_URL = "https://api.freepik.com"

class Flux2ProGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or load_api_key()
        self.headers = {
            "x-freepik-api-key": self.api_key,
            "Content-Type": "application/json"
        }
    
    def encode_image(self, image_path: str) -> str:
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    
    def generate(
        self,
        prompt: str,
        width: int = 1440,
        height: int = 768,
        seed: Optional[int] = None,
        prompt_upsampling: bool = False,
        input_image: Optional[str] = None,
        input_image_2: Optional[str] = None,
        input_image_3: Optional[str] = None,
        input_image_4: Optional[str] = None
    ):
        payload = {
            "prompt": prompt,
            "width": width,
            "height": height,
            "prompt_upsampling": prompt_upsampling
        }
        
        if seed is not None:
            payload["seed"] = seed
        
        # Add input images if provided
        for idx, img_path in enumerate([input_image, input_image_2, input_image_3, input_image_4], 1):
            if img_path and os.path.exists(img_path):
                key = "input_image" if idx == 1 else f"input_image_{idx}"
                payload[key] = self.encode_image(img_path)
        
        response = requests.post(
            f"{BASE_URL}/v1/ai/text-to-image/flux-2-pro",
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def check_status(self, task_id: str):
        response = requests.get(
            f"{BASE_URL}/v1/ai/text-to-image/flux-2-pro/{task_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
    
    def wait_for_completion(self, task_id: str, verbose: bool = True):
        start = time.time()
        while True:
            elapsed = int(time.time() - start)
            if elapsed > 300:
                raise TimeoutError("Generation timeout")
            
            data = self.check_status(task_id)
            status = data.get('data', {}).get('status')
            
            if verbose:
                print(f"Status: {status} ({elapsed}s)")
            
            if status == "COMPLETED":
                return data
            elif status == "FAILED":
                raise RuntimeError(f"Failed: {data}")
            
            time.sleep(3)
    
    def download(self, url: str, output_path: str):
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return output_path
    
    def generate_and_download(self, prompt: str, output_path: str, **kwargs):
        print(f"Generating with Flux 2 Pro...")
        result = self.generate(prompt, **kwargs)
        task_id = result.get('data', {}).get('task_id')
        
        if not task_id:
            raise RuntimeError(f"No task_id: {result}")
        
        print(f"Task: {task_id}")
        final = self.wait_for_completion(task_id)
        
        images = final.get('data', {}).get('generated', [])
        if not images:
            raise RuntimeError(f"No images: {final}")
        
        print(f"Downloading...")
        self.download(images[0], output_path)
        print(f"✓ Saved: {output_path}")
        return output_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Flux 2 Pro - Marketing & Ad Generation')
    parser.add_argument('prompt', help='Image description')
    parser.add_argument('-o', '--output', required=True, help='Output path')
    parser.add_argument('--width', type=int, default=1440, help='Width (256-1440)')
    parser.add_argument('--height', type=int, default=768, help='Height (256-1440)')
    parser.add_argument('--seed', type=int, help='Seed for reproducibility')
    parser.add_argument('--enhance-prompt', action='store_true', help='Auto-enhance prompt')
    parser.add_argument('--input', help='Input image for image-to-image')
    parser.add_argument('--input2', help='Second input image')
    parser.add_argument('--input3', help='Third input image')
    parser.add_argument('--input4', help='Fourth input image')
    
    args = parser.parse_args()
    
    try:
        gen = Flux2ProGenerator()
        gen.generate_and_download(
            prompt=args.prompt,
            output_path=args.output,
            width=args.width,
            height=args.height,
            seed=args.seed,
            prompt_upsampling=args.enhance_prompt,
            input_image=args.input,
            input_image_2=args.input2,
            input_image_3=args.input3,
            input_image_4=args.input4
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
