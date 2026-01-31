#!/usr/bin/env python3
"""
Automate Freepik image generation
"""
from playwright.sync_api import sync_playwright
import time
import os

def main():
    download_dir = os.path.expanduser("~/Downloads/freepik_sofas")
    os.makedirs(download_dir, exist_ok=True)
    
    with sync_playwright() as p:
        # Launch browser with visible window (headless=False)
        browser = p.chromium.launch(
            headless=False,
            downloads_path=download_dir
        )
        
        # Create context and page
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            accept_downloads=True
        )
        page = context.new_page()
        
        try:
            print("Opening Freepik...")
            page.goto("https://www.freepik.com", timeout=60000)
            time.sleep(3)
            
            print("Looking for login button...")
            # Click login/sign in
            page.click('a[href*="login"], button:has-text("Log in"), a:has-text("Log in")', timeout=10000)
            time.sleep(2)
            
            print("Entering credentials...")
            # Fill email and password
            page.fill('input[type="email"], input[name="email"]', "menthamdc@gmail.com")
            page.fill('input[type="password"], input[name="password"]', "HELLOBRO")
            
            print("Clicking login...")
            # Click login button
            page.click('button[type="submit"], button:has-text("Log in")', timeout=10000)
            time.sleep(5)
            
            print("Navigating to AI image generator...")
            # Navigate to AI image generator
            # Look for "Pikaso" or "AI Image Generator" link
            page.goto("https://www.freepik.com/ai/image-generator", timeout=60000)
            time.sleep(5)
            
            print("Generating red sofa images...")
            # Generate 10 images
            for i in range(10):
                print(f"Generating image {i+1}/10...")
                
                # Find the prompt input
                prompt_input = page.locator('textarea, input[placeholder*="prompt"], input[placeholder*="describe"]').first
                prompt_input.click()
                prompt_input.fill(f"red sofa, high quality, professional photography, clean background")
                
                # Click generate button
                page.click('button:has-text("Generate"), button:has-text("Create")', timeout=10000)
                
                # Wait for generation (this might take 10-30 seconds)
                time.sleep(30)
                
                # Download the image
                print(f"Downloading image {i+1}...")
                # Look for download button
                with page.expect_download(timeout=60000) as download_info:
                    page.click('button:has-text("Download"), a:has-text("Download")', timeout=10000)
                download = download_info.value
                download.save_as(f"{download_dir}/red_sofa_{i+1}.png")
                
                print(f"Image {i+1} saved!")
                time.sleep(2)
            
            print(f"\nAll 10 images generated and saved to {download_dir}")
            
        except Exception as e:
            print(f"Error: {e}")
            print("Taking screenshot for debugging...")
            page.screenshot(path=f"{download_dir}/error_screenshot.png")
            raise
        
        finally:
            # Keep browser open for 10 seconds so user can see
            print("\nKeeping browser open for 10 seconds...")
            time.sleep(10)
            browser.close()

if __name__ == "__main__":
    main()
