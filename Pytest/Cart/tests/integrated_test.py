import pytest
import allure
from pathlib import Path
import sys
root_path = Path(__file__).parent.parent.parent.parent
sys.path.append(str(root_path))
from Pytest.Cart.Data.get_data import get_initiate_data

@allure.step("checkout Cart Count is {expected}")
def checkout_cart(actual,expected):
    assert actual == expected

@allure.step("price check")
def price_checkout(act,exp):
    assert act == exp

@pytest.mark.parametrize("username,password,items,firstname,lastname,zip,expected_price,exp_message",get_initiate_data())
def test_flow(login,home,username,password,items,firstname,lastname,zip,expected_price,exp_message,subtests):
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    home.add_to_cart(items)
    cart_count = home.get_cart_count()
    checkout_cart(cart_count,str(2))
    home.go_to_cart()
    home.checkout()
    home.add_details(firstname,lastname,zip)
    price = home.get_total_item_price()
    price_checkout(price,expected_price)
    home.click_finish()
    message = home.get_thankyou_text()
    with subtests.test("Thank you message"):
        assert exp_message.lower() in message.lower(),"Message mismatch"



