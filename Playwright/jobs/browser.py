from playwright.sync_api import sync_playwright

def setup_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        return page,browser