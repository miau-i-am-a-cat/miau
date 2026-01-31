import requests
import json
import time

with open('.credentials.json') as f:
    creds = json.load(f)
    api_key = creds['fal']['api_key']

headers = {
    "Authorization": f"Key {api_key}",
}

# First upload the image to fal storage
ref_path = "businesses/wingman-labs/assets/creatives/product/energy/wingman-energy-strips-coffee-product-flatlay-hero.png"

print("Uploading reference image to fal storage...")
with open(ref_path, "rb") as f:
    upload_resp = requests.post(
        "https://fal.run/fal-ai/storage/upload",
        headers=headers,
        files={"file": ("reference.png", f, "image/png")}
    )

if upload_resp.status_code != 200:
    print(f"Upload failed: {upload_resp.status_code} - {upload_resp.text}")
    exit(1)

upload_result = upload_resp.json()
ref_url = upload_result.get("url")
print(f"Uploaded to: {ref_url}")

# Now generate with reference
headers["Content-Type"] = "application/json"
url = "https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra"

prompt = """Premium social media ad for Wingman Labs Energy Strips.
Show the exact product from the reference: white box with orange accents, "ENERGY STRIPS" text, mouth/tongue illustration, and orange sachets.
Dark dramatic background with orange lighting accents.
Add bold text overlay: "SKIP THE CRASH" 
Subtext: "Clean energy in seconds"
Professional advertising photography style."""

payload = {
    "prompt": prompt,
    "image_url": ref_url,
    "image_prompt_strength": 0.75,
    "aspect_ratio": "1:1",
    "output_format": "png",
    "safety_tolerance": 5
}

print("Generating ad with FLUX Pro Ultra...")
response = requests.post(url, headers=headers, json=payload)
print(f"Status: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    request_id = result.get('request_id')
    print(f"Request ID: {request_id}")
    
    for i in range(40):
        time.sleep(3)
        result_url = f"https://queue.fal.run/fal-ai/flux-pro/v1.1-ultra/requests/{request_id}"
        result_resp = requests.get(result_url, headers={"Authorization": f"Key {api_key}"})
        
        if result_resp.status_code == 200:
            try:
                final = result_resp.json()
                if 'images' in final and len(final['images']) > 0:
                    img_url = final['images'][0]['url']
                    print(f"Done! Image: {img_url}")
                    img_data = requests.get(img_url).content
                    with open('wingman_ad_flux.png', 'wb') as f:
                        f.write(img_data)
                    print("Saved to wingman_ad_flux.png")
                    exit(0)
            except:
                pass
        print(f"Waiting... {i+1}/40")
else:
    print(f"Error: {response.text}")
