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

# Read reference image as base64
ref_path = "businesses/wingman-labs/assets/creatives/product/energy/wingman-energy-strips-coffee-product-flatlay-hero.png"
with open(ref_path, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()
    img_data_url = f"data:image/png;base64,{img_base64}"

# Try flux dev img2img
url = "https://queue.fal.run/fal-ai/flux/dev/image-to-image"

prompt = """Premium advertising photo of this energy supplement product.
Keep the exact Wingman Labs packaging visible.
Dark moody studio background with dramatic orange rim lighting.
Professional product photography for social media ad.
Add subtle motion blur and energy effects around the product."""

payload = {
    "prompt": prompt,
    "image_url": img_data_url,
    "strength": 0.55,
    "num_inference_steps": 28,
    "guidance_scale": 3.5
}

print("Submitting to FLUX dev image-to-image...")
response = requests.post(url, headers=headers, json=payload)
print(f"Status: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    request_id = result.get('request_id')
    print(f"Request ID: {request_id}")
    
    for i in range(30):
        time.sleep(2)
        result_url = f"https://queue.fal.run/fal-ai/flux/dev/image-to-image/requests/{request_id}"
        result_resp = requests.get(result_url, headers={"Authorization": f"Key {api_key}"})
        
        if result_resp.status_code == 200:
            try:
                final = result_resp.json()
                if 'images' in final and len(final['images']) > 0:
                    img_url = final['images'][0]['url']
                    print(f"Done! {img_url}")
                    img_data = requests.get(img_url).content
                    with open('wingman_ad_flux.png', 'wb') as f:
                        f.write(img_data)
                    print("Saved!")
                    exit(0)
            except:
                pass
        print(f"Waiting... {i+1}")
else:
    print(f"Error: {response.text}")
