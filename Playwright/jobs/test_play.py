import sys
import os
from pathlib import Path
root_path  = Path(__file__).parent.parent.parent
sys.path.append(str(root_path))
import pytest
import datetime
from pymongo import MongoClient
from playwright.sync_api import sync_playwright, expect,Page

@pytest.fixture(scope='function')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

def log_to_mongo(data: dict):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["playwright_db"]
    collection = db["test_logs"]
    collection.insert_one(data)


def test_login(browser):
    try:
        browser.goto("https://www.saucedemo.com/")
        browser.fill("input[name='user-name']", "standard_user")
        browser.fill("input[name='password']", "secret_sauce")
        browser.click("input[type='submit']")

        expect(browser).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(browser.locator("#shopping_cart_container")).to_be_visible()

        log_to_mongo({
            "test": "test_login",
            "status": "passed",
            "timestamp": datetime.datetime.utcnow()
        })

    except Exception as e:
        log_to_mongo({
            "test": "test_login",
            "status": "failed",
            "error": str(e),
            "timestamp": datetime.datetime.utcnow()
        })
        raise

def test_login_fail(browser):
    try:
        browser.goto("https://www.saucedemo.com/")
        browser.fill("input[name='user-name']", "locked_out_user")
        browser.fill("input[name='password']", "secret_sauce")
        browser.click("input[type='submit']")

        expect(browser.locator("h3[data-test='error']")).to_contain_text("locked out")

        log_to_mongo({
            "test": "test_login_fail",
            "status": "passed",
            "timestamp": datetime.datetime.utcnow()
        })

    except Exception as e:
        log_to_mongo({
            "test": "test_login_fail",
            "status": "failed",
            "error": str(e),
            "timestamp": datetime.datetime.utcnow()
        })
        raise