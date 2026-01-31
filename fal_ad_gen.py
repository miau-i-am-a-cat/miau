import requests
import json
import base64
import sys
import os

# Get API key
with open('.credentials.json') as f:
    creds = json.load(f)
    api_key = creds['fal']['api_key']

# fal.ai endpoint for Nano Banana Pro (imagen3)
url = "https://queue.fal.run/fal-ai/imagen3"

headers = {
    "Authorization": f"Key {api_key}",
    "Content-Type": "application/json"
}

prompt = """Premium advertising graphic for energy supplement product. 
Clean modern design with bold typography on dark background.
Text says "SKIP THE CRASH" as main headline in large white bold letters.
Subtext: "Clean energy in seconds. No jitters. No crash."
Professional product photography style, dramatic lighting, 
modern minimalist aesthetic suitable for social media ad.
Orange and white color accents on dark gray/black background.
High-end supplement brand vibes, premium feel."""

payload = {
    "prompt": prompt,
    "aspect_ratio": "1:1",
    "safety_tolerance": "5"
}

print("Submitting to fal.ai...")
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    print(f"Request ID: {result.get('request_id')}")
    
    # Poll for result
    request_id = result.get('request_id')
    status_url = f"https://queue.fal.run/fal-ai/imagen3/requests/{request_id}/status"
    result_url = f"https://queue.fal.run/fal-ai/imagen3/requests/{request_id}"
    
    import time
    while True:
        status_resp = requests.get(status_url, headers=headers)
        status = status_resp.json()
        print(f"Status: {status.get('status')}")
        if status.get('status') == 'COMPLETED':
            # Get result
            result_resp = requests.get(result_url, headers=headers)
            final = result_resp.json()
            if 'images' in final:
                img_url = final['images'][0]['url']
                print(f"Image URL: {img_url}")
                # Download image
                img_data = requests.get(img_url).content
                with open('wingman_ad_fal.png', 'wb') as f:
                    f.write(img_data)
                print("Saved to wingman_ad_fal.png")
            break
        elif status.get('status') == 'FAILED':
            print(f"Failed: {status}")
            break
        time.sleep(2)
else:
    print(f"Error {response.status_code}: {response.text}")
