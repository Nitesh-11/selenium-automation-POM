from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.LoginPage import LoginPage

# @given(u'Launch the browser')
# def launchBrowser(context):
#     service = Service(executable_path=r"D:\\Selenium\\Drivers\\chromedriver-win64\\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     context.driver = webdriver.Chrome(service=service, options=options)

# @when(u'open the website')
# def openWebsite(context):
#     context.loginPage = LoginPage(context.driver)
#     context.loginPage.openPage("http://localhost:3000/")

# @then(u'Login page opened')
# def navigateLogin(context):
#     context.loginPage.navigateLogin()


# @then(u'Provide the username "nitesharya37@gmail.com" and password "12345678"')
# def enterCredentials(context):
#     context.loginPage.enterCreds("nitesharya37@gmail.com", "12345678")


# @then(u'Click on the Login button')
# def clickLogin(context):
#     context.loginPage.clickLogin()

# @then(u'Validate Login')
# def validateLogin(context):
#     assert context.loginPage.validateLogin()

@then(u'Close the browser')
def step_impl(context):
    context.driver.close()