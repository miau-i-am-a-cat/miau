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
Professional advertising photography, premium supplement brand aesthetic.
Keep the product box and orange sachets exactly as shown in reference."""

payload = {
    "prompt": prompt,
    "image_url": img_data_url,
    "image_prompt_strength": 0.7,
    "aspect_ratio": "1:1",
    "output_format": "png",
    "safety_tolerance": 5
}

print("Submitting to FLUX1.1 Pro Ultra with reference image...")
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    request_id = result.get('request_id')
    print(f"Request ID: {request_id}")
    
    status_url = f"https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra/requests/{request_id}/status"
    result_url = f"https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra/requests/{request_id}"
    
    while True:
        status_resp = requests.get(status_url, headers=headers)
        status = status_resp.json()
        print(f"Status: {status.get('status')}")
        if status.get('status') == 'COMPLETED':
            result_resp = requests.get(result_url, headers=headers)
            final = result_resp.json()
            if 'images' in final:
                img_url = final['images'][0]['url']
                print(f"Image URL: {img_url}")
                img_data = requests.get(img_url).content
                with open('wingman_ad_flux.png', 'wb') as f:
                    f.write(img_data)
                print("Saved to wingman_ad_flux.png")
            break
        elif status.get('status') == 'FAILED':
            print(f"Failed: {status}")
            break
        time.sleep(2)
else:
    print(f"Error {response.status_code}: {response.text}")
