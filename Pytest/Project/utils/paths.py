from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

class Path_Utils:

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.timeout = timeout

    def click_xpath(self,xpath):
        for _ in range(3):
            try:
                element = WebDriverWait(self.driver,timeout=self.timeout).until(
                    EC.element_to_be_clickable((By.XPATH,xpath))
                )
                element.click()
                return True
            except Exception as e:
                print(str(e))
                print(f"Retrying... failed to click {xpath}")
        
        return False
    
    def send_keys_xpath(self,xpath,keys):
        for _ in range(3):
            try:
                element = WebDriverWait(self.driver,self.timeout).until(
                    EC.visibility_of_element_located((By.XPATH,xpath))
                )
                element.send_keys(keys)
                return True
            except Exception as e:
                print(str(e))

        return False
    
    def get_element_text(self,xpath):
        for _  in range(3):
            try:
                element = WebDriverWait(self.driver,self.timeout).until(
                    EC.visibility_of_element_located((By.XPATH,xpath))
                )
                return str(element.text)
            except Exception as e:
                print("element not found")    

        return "Element not found"
            