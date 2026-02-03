import fal_client
import requests
import os

os.environ["FAL_KEY"] = "2140b03a-2f9a-4750-b7f8-a5d9751d6487:6a41b7f755df2099cec1d15872a61cb2"

# Upload the source image
print("Uploading source image...")
ref_url = fal_client.upload_file("/Users/scoop/clawd/kalina-brand/source/glock-bag.jpg")
print(f"Uploaded: {ref_url}")

# Generate angle shot
print("\nGenerating angle shot...")
result1 = fal_client.subscribe("fal-ai/nano-banana-pro/edit", arguments={
    "prompt": "Same cognac brown leather handbag with sculpted Glock pistol relief, shot from a 3/4 angle showing the side profile and depth of the bag, warm studio lighting, cream beige background, luxury product photography, shot on 85mm f/1.8, shallow depth of field, warm color grade matching cognac leather tones",
    "image_urls": [ref_url],
    "image_size": "square"
})
img1_url = result1['images'][0]['url']
print(f"Generated: {img1_url}")

r = requests.get(img1_url)
with open("/Users/scoop/clawd/kalina-glock/product-angle.png", "wb") as f:
    f.write(r.content)
print("Saved: product-angle.png")

# Generate detail shot
print("\nGenerating detail shot...")
result2 = fal_client.subscribe("fal-ai/nano-banana-pro/edit", arguments={
    "prompt": "Extreme close-up detail shot of the sculpted Glock pistol relief on cognac brown leather, showing the incredible hand-crafted texture and depth of the embossed weapon design, warm side lighting emphasizing shadows and contours, macro photography style, shot on 100mm macro lens, luxury leather craftsmanship detail, warm cognac tones",
    "image_urls": [ref_url],
    "image_size": "square"
})
img2_url = result2['images'][0]['url']
print(f"Generated: {img2_url}")

r = requests.get(img2_url)
with open("/Users/scoop/clawd/kalina-glock/product-detail.png", "wb") as f:
    f.write(r.content)
print("Saved: product-detail.png")

# Generate lifestyle shot
print("\nGenerating lifestyle shot...")
result3 = fal_client.subscribe("fal-ai/nano-banana-pro/edit", arguments={
    "prompt": "Fashion model carrying this cognac brown leather Glock handbag, wearing cream and earth tone outfit, walking on sunlit terracotta street in warm Mediterranean setting, editorial fashion photography, shot on 50mm f/1.4, golden hour natural light, warm color grade, model's face not visible, focus on the bag",
    "image_urls": [ref_url],
    "image_size": "portrait_4_3"
})
img3_url = result3['images'][0]['url']
print(f"Generated: {img3_url}")

r = requests.get(img3_url)
with open("/Users/scoop/clawd/kalina-glock/lifestyle.png", "wb") as f:
    f.write(r.content)
print("Saved: lifestyle.png")

print("\nAll images generated!")
