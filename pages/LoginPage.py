from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.BasePage import BasePage

class LoginPage(BasePage):
    login = (By.XPATH, "//button[contains(text(),'Login')]")
    username = (By.XPATH, "//input[@id='username']")
    pwd = (By.XPATH, "//input[@id='password']")
    login_auth = (By.XPATH, "//button[contains(text(),'Sign in')]")
    analytics = (By.XPATH, "//a[contains(text(),'Analytics')]")

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def openPage(self, url):
        self.driver.get(url)
    
    def navigateLogin(self):
        self.click_element(self.login)

    def enterCreds(self, username, pwd):
        self.input_element(self.username, username)
        self.input_element(self.pwd, pwd)

    def clickLogin(self):
        self.click_element(self.login_auth)

    # implementing validation by landing/analytics page
    def validateLogin(self):
        text = self.get_element_text(self.analytics)
        print(text)
        if(text == "Analytics"):
            return True
        else:
            return False