#!/usr/bin/env python3
"""Flux Pro 1.1 - Premium image generation"""
import requests, json, time, os, sys
from pathlib import Path

def load_api_key():
    with open(Path(__file__).parent / ".credentials.json") as f:
        return json.load(f)['freepik']['api_key']

BASE_URL = "https://api.freepik.com"

class FluxProGenerator:
    def __init__(self, api_key=None):
        self.api_key = api_key or load_api_key()
        self.headers = {"x-freepik-api-key": self.api_key, "Content-Type": "application/json"}
    
    def generate(self, prompt, aspect_ratio="widescreen_16_9", seed=None):
        payload = {"prompt": prompt, "aspect_ratio": aspect_ratio}
        if seed: payload["seed"] = seed
        response = requests.post(f"{BASE_URL}/v1/ai/text-to-image/flux-pro-v1-1", headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def check_status(self, task_id):
        response = requests.get(f"{BASE_URL}/v1/ai/text-to-image/flux-pro-v1-1/{task_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def wait_for_completion(self, task_id):
        start = time.time()
        while True:
            if time.time() - start > 300: raise TimeoutError()
            data = self.check_status(task_id)
            status = data.get('data', {}).get('status')
            print(f"Status: {status} ({int(time.time()-start)}s)")
            if status == "COMPLETED": return data
            elif status == "FAILED": raise RuntimeError(f"Failed: {data}")
            time.sleep(3)
    
    def download(self, url, output_path):
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(requests.get(url).content)
        return output_path
    
    def generate_and_download(self, prompt, output_path, **kwargs):
        print("Generating with Flux Pro 1.1...")
        result = self.generate(prompt, **kwargs)
        task_id = result.get('data', {}).get('task_id')
        if not task_id: raise RuntimeError(f"No task_id: {result}")
        print(f"Task: {task_id}")
        final = self.wait_for_completion(task_id)
        images = final.get('data', {}).get('generated', [])
        if not images: raise RuntimeError(f"No images: {final}")
        self.download(images[0], output_path)
        print(f"✓ Saved: {output_path}")
        return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt')
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('--aspect', default='widescreen_16_9')
    parser.add_argument('--seed', type=int)
    args = parser.parse_args()
    try:
        FluxProGenerator().generate_and_download(args.prompt, args.output, aspect_ratio=args.aspect, seed=args.seed)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
