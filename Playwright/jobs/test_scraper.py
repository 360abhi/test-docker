from playwright.sync_api import sync_playwright, expect

def test_scrape_quotes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")
        
        # Grab all quotes on the first page
        quotes = page.locator(".quote .text")
        count = quotes.count()

        assert count > 0, "No quotes found"
        
        print(f"✅ Found {count} quotes on the page.")

        browser.close()
