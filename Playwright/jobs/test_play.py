import sys
import os
from pathlib import Path
root_path  = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))
import pytest
from playwright.sync_api import sync_playwright, expect,Page

@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_login(browser):
    browser.goto("https://www.saucedemo.com/")
    browser.fill("input[name='user-name']", "standard_user")
    browser.fill("input[name='password']", "secret_sauce")
    browser.click("input[type='submit']")

    expect(browser).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(browser.locator("#shopping_cart_container")).to_be_visible()

def test_login_fail(browser):
    browser.goto("https://www.saucedemo.com/")
    browser.fill("input[name='user-name']", "locked_out_user")
    browser.fill("input[name='password']", "secret_sauce")
    browser.click("input[type='submit']")

    expect(browser.locator("h3[data-test='error']")).to_contain_text("locked out")