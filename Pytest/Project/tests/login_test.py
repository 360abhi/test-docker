import pytest
import os
from pathlib import Path
import sys

root_path = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_path))

from Pytest.Project.Pages.Login import Login_Page
from Pytest.Project.driver import setup_webdriver


@pytest.fixture(scope="function")
def setup_driver():
    driver = setup_webdriver()
    driver.get('https://www.saucedemo.com/v1/')
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_loginpage(setup_driver):
    login = Login_Page(setup_driver)
    return login

@pytest.mark.parametrize("username,password,error_msg",[
    ("standard_user","secret_sauce","Element not found"),
    ("abhishek","password","Epic sadface: Username and password do not match any user in this service"),
    ("","pass","Epic sadface: Username is required")
],ids=["Positive Case","Negative Case","Empty Case"])
def test_login(setup_loginpage,username,password,error_msg):
    setup_loginpage.enter_username(username=username)
    setup_loginpage.enter_password(password=password)
    setup_loginpage.click_login()
    text = setup_loginpage.get_error_text()
    assert text == error_msg

