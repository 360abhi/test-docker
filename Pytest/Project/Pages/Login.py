from Pytest.Project.utils.paths import Path_Utils

class Login_Page:

    # Xpaths
    username_field = "//input[@id='user-name']"
    password_field = "//input[@id='password']"
    login_btn = "//input[@type='submit']"
    error_element = "//h3[@data-test='error']"

    def __init__(self,driver):
        self.driver = driver
        self.paths = Path_Utils(self.driver)

    def log_action(self,action,success,error):
        if action:
            print(success)
        else:
            print(error)

    def enter_username(self,username):
        self.log_action(self.paths.send_keys_xpath(self.username_field,keys=str(username)),
                        "username sent successfully",
                        "username sent exception")

    def enter_password(self,password):
        self.log_action(self.paths.send_keys_xpath(self.password_field,keys=str(password)),
                        "password sent successfully",
                        "password sending failed")

    def click_login(self):
        self.log_action(self.paths.click_xpath(self.login_btn),
                        "login click success",
                        "login click exception")
        
    def get_error_text(self):
        element_text = self.paths.get_element_text(self.error_element)
        return element_text
