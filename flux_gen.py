#!/usr/bin/env python3
"""Flux Dev image generation with proper ad creation"""
import requests, json, time, base64, os, sys
from pathlib import Path

def load_api_key():
    with open(Path(__file__).parent / ".credentials.json") as f:
        return json.load(f)['freepik']['api_key']

class FluxGenerator:
    def __init__(self):
        self.api_key = load_api_key()
        self.headers = {"x-freepik-api-key": self.api_key, "Content-Type": "application/json"}
        self.base_url = "https://api.freepik.com/v1/ai/text-to-image/flux-dev"
    
    def encode_image(self, path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    
    def generate(self, prompt, size="portrait_4_5", guidance=3.5, seed=None):
        payload = {
            "prompt": prompt,
            "guidance_scale": guidance,
            "num_images": 1,
            "image": {"size": size}
        }
        if seed:
            payload["seed"] = seed
        
        r = requests.post(self.base_url, headers=self.headers, json=payload)
        r.raise_for_status()
        return r.json()
    
    def check_status(self, task_id):
        r = requests.get(f"{self.base_url}/{task_id}", headers=self.headers)
        r.raise_for_status()
        return r.json()
    
    def wait_for_result(self, task_id, timeout=120):
        start = time.time()
        while time.time() - start < timeout:
            data = self.check_status(task_id)
            status = data.get('data', {}).get('status')
            print(f"  Status: {status} ({int(time.time()-start)}s)")
            if status == "COMPLETED":
                return data
            elif status == "FAILED":
                raise RuntimeError(f"Generation failed: {data}")
            time.sleep(3)
        raise TimeoutError("Generation timed out")
    
    def download(self, url, output_path):
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        r = requests.get(url)
        with open(output_path, 'wb') as f:
            f.write(r.content)
        return output_path
    
    def generate_and_save(self, prompt, output_path, **kwargs):
        print(f"Generating: {prompt[:60]}...")
        result = self.generate(prompt, **kwargs)
        task_id = result.get('data', {}).get('task_id')
        if not task_id:
            raise RuntimeError(f"No task_id: {result}")
        print(f"  Task: {task_id}")
        
        final = self.wait_for_result(task_id)
        images = final.get('data', {}).get('generated', [])
        if not images:
            raise RuntimeError(f"No images generated: {final}")
        
        self.download(images[0], output_path)
        print(f"  ✓ Saved: {output_path}")
        return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--size", default="portrait_4_5")
    parser.add_argument("--guidance", type=float, default=3.5)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    
    gen = FluxGenerator()
    gen.generate_and_save(args.prompt, args.output, size=args.size, guidance=args.guidance, seed=args.seed)
