# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Document Formatting Requirements (MANDATORY)

### Document Format Standards
- **Always create documents as .docx, NEVER .md**
- Default format: DOCX (not PDF or MD)
- Professional formatting throughout

### Typography Standards
- **Headers:** Bold 14pt
- **Body text:** 11pt
- **Line spacing:** 1.15
- **Page numbers:** Required on all multi-page documents

### Table Formatting (CRITICAL)
- **Column width:** Minimum 1.5" per column, auto-fit to content
- **Landscape orientation:** Use for tables with 4+ columns
- **Portrait orientation:** Tables with 3 or fewer columns
- **Professional styling:** Clear headers, readable fonts
- **Bold headers:** Table column headers always bold
- **Adequate spacing:** Between rows/columns

### Document Delivery
- **Attribution:** Reports prepared by/for the business (e.g., "Wingman Labs", "Porcemall"), NOT "Clawd AI" or AI attribution
- Test that tables are readable before sending

## fal.ai - Image Generation (PRIMARY)

**Default model: Nano Banana Pro (Google)**
- Best for: Marketing materials, text/typography, branded content
- Google's state-of-the-art image generation model

### API Credentials
Stored in `.credentials.json` under `fal.api_key`

### Standard Workflow: Ads & Product Images

**Always use edit mode with reference image:**

```python
import fal_client

# 1. Upload reference image
ref_url = fal_client.upload_file("path/to/product.png")

# 2. Generate/edit with reference preserved
result = fal_client.subscribe(
    "fal-ai/nano-banana-pro/edit",
    arguments={
        "prompt": "Add bold headline 'YOUR TEXT' at top. Change X to Y. Keep product exactly as shown.",
        "image_urls": [ref_url],
    }
)

# 3. Download result
img_url = result['images'][0]['url']
```

**Key points:**
- **Endpoint:** `fal-ai/nano-banana-pro/edit` (or `nano-banana/edit`)
- **Param:** `image_urls` (list) — pass reference image
- **Prompt:** Describe changes; tell it what to keep unchanged
- Edit mode preserves original image, applies targeted changes
- Works for: adding text, color changes, background edits, etc.

### Environment Setup
```bash
export FAL_KEY=$(jq -r '.fal.api_key' .credentials.json)
```

---

## Freepik API - Image Generation (DEPRECATED)

> ⚠️ **DEPRECATED**: Use fal.ai with Nano Banana Pro instead

### API Credentials
Stored in `.credentials.json` (kept for legacy reference)

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
