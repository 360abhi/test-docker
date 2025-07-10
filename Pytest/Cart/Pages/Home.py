from Pytest.Project.utils.paths import Path_Utils
import ast
class Home_Page:

    # Xpaths
    add_cart_btn = f"//div[.='Sauce Labs Backpack']/../../following-sibling::div/div/following-sibling::button"
    cart_count = "//span[@class='fa-layers-counter shopping_cart_badge']"
    checkout_btn = "//a[@class='btn_action checkout_button']"
    first_name_field = "//input[@id='first-name']"
    last_name_field = "//input[@id='last-name']"
    zip_code_field = "//input[@id='postal-code']"
    continue_btn = "//input[@type='submit']"
    item_total_field = "//div[@class='summary_subtotal_label']"
    finish_btn = "//a[.='FINISH']"
    thanku_order_msg = "//h2"


    def __init__(self,driver,logger):
        self.driver = driver
        self.paths = Path_Utils(self.driver)
        self.logger = logger
    
    def log_action(self,action,success,error):
        if action:
            self.logger.info(success)
        else:
            self.logger.error(error)
            raise Exception

    def add_to_cart(self,items):
        items = ast.literal_eval(items)
        if len(items) < 1:
            print("Items cannot be less than 1")
            self.logger.error("Items cannot be less than 1")
            raise Exception
        for item in items:
            self.log_action(self.paths.click_xpath(f"//div[.='{item}']/../../following-sibling::div/div/following-sibling::button"),
                            f"{item} added to cart successfully",
                            f"{item} addition to cart exception")
            
    def get_cart_count(self):
        count = self.paths.get_element_text(self.cart_count)
        return str(count)
    
    def go_to_cart(self):
        self.log_action(self.paths.click_xpath(self.cart_count),
                        "Cart Page click success",
                        "Cart page click exception")

    def checkout(self):
        self.log_action(self.paths.click_xpath(self.checkout_btn),
                        "Checkout click success",
                        "Checkout click exception")
        
    def add_details(self,firstname,lastname,zip):
        self.log_action(self.paths.send_keys_xpath(self.first_name_field,keys=firstname),
                        f"{firstname} sent successfully",
                        f"{firstname} sending exception")
        
        self.log_action(self.paths.send_keys_xpath(self.last_name_field,keys=lastname),
                        f"{lastname} sent successfully",
                        f"{lastname} sent exception")
        
        self.log_action(self.paths.send_keys_xpath(self.zip_code_field,keys=zip),
                        f"{zip} sent successfully",
                        f"{zip} sending exception")
        
        self.log_action(self.paths.click_xpath(self.continue_btn),
                        "Continue button click success",
                        "Continue click exception")

    def get_total_item_price(self):
        price = self.paths.get_element_text(self.item_total_field)
        ele = price.find(":")
        last_string = price[ele+1:].strip()
        return str(last_string)
    
    def click_finish(self):
        self.log_action(self.paths.click_xpath(self.finish_btn),
                        "finish button click success",
                        "finish button click exception")
        
    def get_thankyou_text(self):
        text = self.paths.get_element_text(self.thanku_order_msg)
        return text

        
