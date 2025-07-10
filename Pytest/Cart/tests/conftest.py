import pytest
from pathlib import Path
import sys
root_path = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_path))
from Pytest.Project.driver import setup_webdriver
from Pytest.Cart.Pages.Home import Home_Page
from Pytest.Cart.Pages.Login import Login_Page
from BOT.Logging.logger import setup_logger



@pytest.fixture
def driver():
    webdriver = setup_webdriver()
    webdriver.get('https://www.saucedemo.com/v1/')
    yield webdriver
    webdriver.quit()

@pytest.fixture
def logger():
    log = setup_logger('sauce_demot')
    return log

@pytest.fixture
def login(driver,logger):
    setup_login = Login_Page(driver,logger)
    return setup_login

@pytest.fixture
def home(driver,logger):
    setup_home = Home_Page(driver,logger)
    return setup_home