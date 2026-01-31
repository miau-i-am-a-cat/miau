#!/usr/bin/env python3
"""
Simpler Freepik automation - assumes you're already logged in
Just opens a browser, you log in manually, then it automates the generation
"""
from playwright.sync_api import sync_playwright
import time
import os

def main():
    download_dir = os.path.expanduser("~/Downloads/freepik_sofas")
    os.makedirs(download_dir, exist_ok=True)
    
    with sync_playwright() as p:
        print("Opening browser...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Go to Freepik
        print("Opening Freepik...")
        page.goto("https://www.freepik.com")
        
        print("\n=== MANUAL STEP REQUIRED ===")
        print("1. Log in to Freepik in the browser window")
        print("2. Navigate to the AI Image Generator")
        print("3. Press ENTER here when you're ready...")
        input()
        
        print("\nStarting automation...")
        
        # Now try to find the text input and generate
        for i in range(10):
            print(f"\nGenerating image {i+1}/10...")
            
            try:
                # Wait for user to be on the right page
                time.sleep(2)
                
                # Try to find and fill the prompt
                page.fill('textarea, input[type="text"]', f"red sofa, professional photography, clean background", timeout=5000)
                
                # Click generate
                page.click('button:has-text("Generate"), button:has-text("Create")', timeout=5000)
                
                print(f"Waiting for image {i+1} to generate...")
                time.sleep(30)  # Wait for generation
                
                # Try to download
                try:
                    page.click('button:has-text("Download"), a:has-text("Download")', timeout=5000)
                    print(f"Image {i+1} download triggered")
                    time.sleep(3)
                except:
                    print(f"Couldn't find download button for image {i+1}, continuing...")
                
            except Exception as e:
                print(f"Error on image {i+1}: {e}")
                print("Continuing to next image...")
                continue
        
        print("\n\nAll done! Check your Downloads folder.")
        print("Keeping browser open for 30 seconds...")
        time.sleep(30)
        browser.close()

if __name__ == "__main__":
    main()
