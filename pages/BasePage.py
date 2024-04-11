from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, TimeoutException, NoSuchElementException, ElementNotInteractableException, InvalidElementStateException, InvalidSelectorException as EX
from selenium.webdriver.common.by import By

class BasePage:
    dasboard = (By.XPATH, "//body/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except EX as e:
            print("Cannot click on element")

    def input_element(self, locator, input):
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).send_keys(input)
        except EX as e:
            print("Unable to input text")

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, locator, attribute_name):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)
    
    def verify_element_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
        
    def goto_dashboard(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.dasboard)).click()
        except EX as E:
            print("Referesh the page")