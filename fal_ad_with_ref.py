import requests
import json
import base64
import time

# Get API key
with open('.credentials.json') as f:
    creds = json.load(f)
    api_key = creds['fal']['api_key']

headers = {
    "Authorization": f"Key {api_key}",
    "Content-Type": "application/json"
}

# Read and encode the reference image
ref_image_path = "businesses/wingman-labs/assets/creatives/product/energy/wingman-energy-strips-coffee-product-flatlay-hero.png"
with open(ref_image_path, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()
    img_data_url = f"data:image/png;base64,{img_base64}"

# Use imagen3 with image reference (edit mode)
url = "https://queue.fal.run/fal-ai/imagen3"

prompt = """Create a premium social media ad featuring this exact Wingman Labs Energy Strips product.
Keep the product packaging exactly as shown in the reference image.
Add bold headline text "SKIP THE CRASH" in large white letters.
Add subtext "Clean energy in seconds. No jitters."
Dark moody background with orange accent lighting.
Professional advertising photography style.
The Wingman Labs box and orange sachets must be clearly visible and accurate to the reference."""

payload = {
    "prompt": prompt,
    "image_url": img_data_url,
    "aspect_ratio": "1:1",
    "safety_tolerance": "5"
}

print("Submitting to fal.ai with reference image...")
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    request_id = result.get('request_id')
    print(f"Request ID: {request_id}")
    
    status_url = f"https://queue.fal.run/fal-ai/imagen3/requests/{request_id}/status"
    result_url = f"https://queue.fal.run/fal-ai/imagen3/requests/{request_id}"
    
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
                with open('wingman_ad_v2.png', 'wb') as f:
                    f.write(img_data)
                print("Saved to wingman_ad_v2.png")
            break
        elif status.get('status') == 'FAILED':
            print(f"Failed: {status}")
            break
        time.sleep(2)
else:
    print(f"Error {response.status_code}: {response.text}")
