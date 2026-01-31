import requests
import json
import base64
import time

with open('.credentials.json') as f:
    creds = json.load(f)
    api_key = creds['fal']['api_key']

headers = {
    "Authorization": f"Key {api_key}",
    "Content-Type": "application/json"
}

# Read and encode reference image
ref_path = "businesses/wingman-labs/assets/creatives/product/energy/wingman-energy-strips-coffee-product-flatlay-hero.png"
with open(ref_path, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()
    img_data_url = f"data:image/png;base64,{img_base64}"

# FLUX1.1 Pro Ultra with image conditioning
url = "https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra"

prompt = """Premium social media advertisement featuring Wingman Labs Energy Strips product.
The exact product packaging from the reference image must be shown prominently.
Dark moody background with dramatic orange accent lighting.
Bold white headline text: "SKIP THE CRASH"
Subtext: "Clean energy in seconds. No jitters."
Professional advertising photography, premium supplement brand aesthetic."""

payload = {
    "prompt": prompt,
    "image_url": img_data_url,
    "image_prompt_strength": 0.7,
    "aspect_ratio": "1:1",
    "output_format": "png",
    "safety_tolerance": 5
}

print("Submitting to FLUX1.1 Pro Ultra...")
response = requests.post(url, headers=headers, json=payload)
print(f"Response status: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    request_id = result.get('request_id')
    print(f"Request ID: {request_id}")
    
    # Wait and poll
    for i in range(60):
        time.sleep(3)
        try:
            result_url = f"https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra/requests/{request_id}"
            result_resp = requests.get(result_url, headers=headers)
            
            if result_resp.status_code == 200:
                try:
                    final = result_resp.json()
                    if 'images' in final and len(final['images']) > 0:
                        img_url = final['images'][0]['url']
                        print(f"Image URL: {img_url}")
                        img_data = requests.get(img_url).content
                        with open('wingman_ad_flux.png', 'wb') as f:
                            f.write(img_data)
                        print("Saved to wingman_ad_flux.png")
                        exit(0)
                except:
                    pass
            print(f"Waiting... ({i+1}/60)")
        except Exception as e:
            print(f"Error: {e}")
    print("Timeout")
else:
    print(f"Error: {response.text}")
