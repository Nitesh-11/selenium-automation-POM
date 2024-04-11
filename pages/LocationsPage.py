from .BasePage import BasePage
from selenium.webdriver.common.by import By
class LocPage(BasePage):

    locTab = (By.XPATH, "//body/div[1]/div[1]/div[1]/div[1]/div[2]/a[4]")

    create = (By.XPATH, "//button[contains(text(),'Create')]")
    createLoc = (By.XPATH, "//button[contains(text(),'Create')]") ## realtive is same is it good to use same variable?

    # Location field
    loccode = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
    locdesc = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/input[1]")
    addressL1 = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/input[1]")
    addressL2 = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[2]/input[1]")
    town = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/input[1]")
    county = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/div[2]/input[1]")
    country = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[3]/div[1]/div[2]/input[1]")
    postcode = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[4]/div[1]/div[2]/input[1]")
    parent = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[2]/input[1]")
    site = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[2]/div[1]/div[2]/input[1]")
    company = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[3]/div[1]/div[2]/input[1]")


    def __init__(self, driver):
        super().__init__(driver)

    def navigateLocTab(self):
        self.goto_dashboard()
        self.click_element(self.locTab)

    def createLocation(self):
        self.click_element(self.create)

    # Location details
    def enterLoccode(self, value):
        self.input_element(self.loccode, value)

    def enterLocDesc(self, value):
        self.input_element(self.locdesc, value)

    def enterAddressL1(self, value):
        self.input_element(self.addressL1, value)

    def enterAddressL2(self, value):
        self.input_element(self.addressL2, value)

    def enterTown(self, value):
        self.input_element(self.town, value)

    def enterCountry(self, value):
        self.input_element(self.country, value)

    def enterCounty(self, value):
        self.input_element(self.county, value)

    def enterPostcode(self, value):
        self.input_element(self.postcode, value)

    def enterParent(self, value):
        self.input_element(self.parent, value)

    def enterSite(self, value):
        self.input_element(self.site, value)

    def enterCompany(self, value):
        self.input_element(self.company, value)

    # Create button after entering details
    def clickCreate(self):
        self.click_element(self.createLoc)    

