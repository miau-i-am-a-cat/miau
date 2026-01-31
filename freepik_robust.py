#!/usr/bin/env python3
"""
Robust Freepik automation with debugging
"""
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
import time
import os

def debug_screenshot(page, name):
    """Take a screenshot for debugging"""
    screenshots_dir = os.path.expanduser("~/Downloads/freepik_debug")
    os.makedirs(screenshots_dir, exist_ok=True)
    path = f"{screenshots_dir}/{name}.png"
    page.screenshot(path=path)
    print(f"  📸 Screenshot saved: {path}")

def wait_and_click(page, selectors, timeout=30000, name="element"):
    """Try multiple selectors until one works"""
    for selector in selectors:
        try:
            print(f"  Trying selector: {selector}")
            page.wait_for_selector(selector, timeout=5000, state="visible")
            page.click(selector, timeout=5000)
            print(f"  ✓ Clicked {name}")
            return True
        except PlaywrightTimeout:
            continue
        except Exception as e:
            print(f"  Error with {selector}: {e}")
            continue
    return False

def wait_and_fill(page, selectors, value, timeout=30000, name="input"):
    """Try multiple selectors for filling"""
    for selector in selectors:
        try:
            print(f"  Trying selector: {selector}")
            page.wait_for_selector(selector, timeout=5000, state="visible")
            page.fill(selector, value, timeout=5000)
            print(f"  ✓ Filled {name}")
            return True
        except PlaywrightTimeout:
            continue
        except Exception as e:
            print(f"  Error with {selector}: {e}")
            continue
    return False

def main():
    download_dir = os.path.expanduser("~/Downloads/freepik_sofas")
    os.makedirs(download_dir, exist_ok=True)
    
    with sync_playwright() as p:
        print("🚀 Launching browser...")
        browser = p.chromium.launch(
            headless=False,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        try:
            # Step 1: Navigate to Freepik
            print("\n📍 Step 1: Opening Freepik...")
            page.goto("https://www.freepik.com", wait_until="networkidle")
            time.sleep(3)
            debug_screenshot(page, "01_homepage")
            
            # Step 2: Find and click login
            print("\n🔐 Step 2: Looking for login button...")
            login_selectors = [
                'a[href*="login"]',
                'button:has-text("Log in")',
                'a:has-text("Log in")',
                'button:has-text("Sign in")',
                'a:has-text("Sign in")',
                '[data-cy="login"]',
                '.login-button',
                '#login-button'
            ]
            
            if not wait_and_click(page, login_selectors, name="login button"):
                print("  ❌ Could not find login button. Checking page content...")
                print(f"  Page title: {page.title()}")
                print(f"  Page URL: {page.url}")
                debug_screenshot(page, "02_login_not_found")
                
                # Try direct navigation to login page
                print("  🔄 Trying direct login URL...")
                page.goto("https://www.freepik.com/login", wait_until="networkidle")
                time.sleep(2)
            
            debug_screenshot(page, "03_login_page")
            time.sleep(2)
            
            # Step 3: Click "Continue with email" button
            print("\n✉️ Step 3: Clicking 'Continue with email'...")
            email_button_selectors = [
                'button:has-text("Continue with email")',
                'button:has-text("email")',
                '[class*="email"]',
                'button >> nth=2'  # Third button is email
            ]
            
            if not wait_and_click(page, email_button_selectors, name="continue with email"):
                print("  ❌ Could not find 'Continue with email' button")
                debug_screenshot(page, "03b_email_button_not_found")
                raise Exception("Continue with email button not found")
            
            debug_screenshot(page, "03c_after_email_button_click")
            time.sleep(3)  # Wait for email form to appear
            
            # Step 4: Fill email
            print("\n📧 Step 4: Entering email...")
            email_selectors = [
                'input[type="email"]',
                'input[name="email"]',
                'input[placeholder*="mail"]',
                'input[placeholder*="Email"]',
                '#email',
                '[data-cy="email"]'
            ]
            
            if not wait_and_fill(page, email_selectors, "menthamdc@gmail.com", name="email"):
                print("  ❌ Could not find email field")
                debug_screenshot(page, "04_email_not_found")
                raise Exception("Email field not found")
            
            debug_screenshot(page, "05_email_filled")
            time.sleep(1)
            
            # Step 5: Fill password
            print("\n🔑 Step 5: Entering password...")
            password_selectors = [
                'input[type="password"]',
                'input[name="password"]',
                '#password',
                '[data-cy="password"]'
            ]
            
            if not wait_and_fill(page, password_selectors, "HELLOBRO", name="password"):
                print("  ❌ Could not find password field")
                debug_screenshot(page, "06_password_not_found")
                raise Exception("Password field not found")
            
            debug_screenshot(page, "07_password_filled")
            time.sleep(1)
            
            # Step 6: Submit login
            print("\n✅ Step 6: Submitting login...")
            submit_selectors = [
                'button[type="submit"]',
                'button:has-text("Log in")',
                'button:has-text("Sign in")',
                'input[type="submit"]',
                '[data-cy="submit"]',
                'button:has-text("Continue")'
            ]
            
            if not wait_and_click(page, submit_selectors, name="submit button"):
                print("  ⚠️ Could not find submit button, trying Enter key...")
                page.keyboard.press("Enter")
            
            print("  ⏳ Waiting for login to complete and redirect...")
            time.sleep(8)  # Wait longer for login to fully complete
            debug_screenshot(page, "08_after_login")
            
            print("  Current URL:", page.url)
            
            # Step 7: Navigate to AI image generator AFTER login is complete
            print("\n🎨 Step 7: Navigating to AI Image Generator (after login)...")
            print("  Going to: https://www.freepik.com/pikaso/ai-image-generator")
            page.goto("https://www.freepik.com/pikaso/ai-image-generator", wait_until="domcontentloaded", timeout=30000)
            time.sleep(8)  # Wait for page to fully load
            debug_screenshot(page, "09_ai_generator_page")
            
            # Step 8: Close any modal/popup
            print("\n❌ Step 8: Closing any modal popups...")
            try:
                # Try to find and click close button on modal
                close_selectors = [
                    'button:has-text("×")',
                    '[aria-label="Close"]',
                    'button.close',
                    '[class*="close"]',
                    'button[aria-label*="close" i]'
                ]
                for selector in close_selectors:
                    try:
                        page.click(selector, timeout=2000)
                        print(f"  ✓ Closed modal with selector: {selector}")
                        time.sleep(2)
                        break
                    except:
                        continue
            except Exception as e:
                print(f"  No modal to close or already closed")
            
            debug_screenshot(page, "09b_after_closing_modals")
            
            # Step 9: Generate images
            print("\n🖼️ Step 9: Generating 10 red sofa images...")
            
            for i in range(10):
                print(f"\n  Image {i+1}/10:")
                
                # Find prompt input
                prompt_selectors = [
                    'textarea[placeholder="Describe your image"]',
                    '[placeholder="Describe your image"]',
                    'textarea',
                    '[contenteditable="true"]',
                    'input[type="text"]'
                ]
                
                prompt = f"red sofa, professional photography, clean background, high quality"
                if wait_and_fill(page, prompt_selectors, prompt, name="prompt"):
                    time.sleep(1)
                    
                    # Click generate
                    generate_selectors = [
                        'button:has-text("Generate")',
                        'button[type="submit"]',
                        'button:has-text("Create")',
                        '[data-cy="generate"]'
                    ]
                    
                    if wait_and_click(page, generate_selectors, name="generate button"):
                        print(f"    ⏳ Waiting for image to generate (30s)...")
                        time.sleep(30)
                        
                        # Try to download
                        download_selectors = [
                            'button:has-text("Download")',
                            'a:has-text("Download")',
                            '[data-cy="download"]',
                            'button:has-text("Save")'
                        ]
                        
                        if wait_and_click(page, download_selectors, name="download button"):
                            print(f"    ✓ Image {i+1} downloaded")
                        else:
                            print(f"    ⚠️ Could not download image {i+1}")
                        
                        debug_screenshot(page, f"10_image_{i+1}_done")
                        time.sleep(2)
                    else:
                        print(f"    ❌ Could not click generate for image {i+1}")
                else:
                    print(f"    ❌ Could not fill prompt for image {i+1}")
            
            print("\n✅ All done! Check ~/Downloads/freepik_sofas/")
            print("Keeping browser open for 30 seconds...")
            time.sleep(30)
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            debug_screenshot(page, "error_final")
            print("Check ~/Downloads/freepik_debug/ for screenshots")
            time.sleep(10)
        
        finally:
            browser.close()

if __name__ == "__main__":
    main()
