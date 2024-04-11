from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.LocationsPage import LocPage
from pages.LoginPage import LoginPage

# Background Steps - need to organise in different file

@given(u'Launch the browser')
def launchBrowser(context):
    service = Service(executable_path=r"D:\\Selenium\\Drivers\\chromedriver-win64\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)

@when(u'open the website')
def openWebsite(context):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.openPage("http://localhost:3000/")

@then(u'Login page opened')
def navigateLogin(context):
    context.loginPage.navigateLogin()


@then(u'Provide the username "nitesharya37@gmail.com" and password "12345678"')
def enterCredentials(context):
    context.loginPage.enterCreds("nitesharya37@gmail.com", "12345678")


@then(u'Click on the Login button')
def clickLogin(context):
    context.loginPage.clickLogin()

@then(u'Validate Login')
def validateLogin(context):
    assert context.loginPage.validateLogin()


# Locations scenerios

@then(u'Navigate to Location tab')
def step_impl(context):
    context.locPage = LocPage(context.driver)
    context.locPage.navigateLocTab()

@then(u'Click on Create button')
def step_impl(context):
    context.locPage.createLocation()
    
@then(u'Enter the details for creating Location')
def step_impl(context):
    context.locPage.enterLoccode("124563")
    context.locPage.enterLocDesc("Description for 1")
    context.locPage.enterAddressL1("Line1 for loc1")
    context.locPage.enterAddressL2("Line2 for loc1")
    context.locPage.enterAddressL2("Line2 for loc1")
    context.locPage.enterTown("Town1")
    context.locPage.enterCountry("Country1")
    context.locPage.enterCounty("County1")
    context.locPage.enterPostcode("456321")
    # context.locPage.enterParent("Parent1")
    context.locPage.enterSite("s1")
    context.locPage.enterCompany("Company1")

@then(u'Click on Create')
def step_impl(context):
    context.locPage.clickCreate()

# @then(u'Go back to Location')
# def step_impl(context):
#     context.locPage.navigateLocTab()