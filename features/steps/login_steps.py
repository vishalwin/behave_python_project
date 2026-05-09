from behave import given, when, then
import time
from utils.json_reader import read_json
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
@given(u'user launches browser')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")


@when(u'user enter username and password')
def step_impl(context):
    data= read_json()
    username= data["username"]
    password = data["password"]
    context.driver.find_element("id","user-name").send_keys(username)
    context.driver.find_element("id","password").send_keys(password)
    
@when("clicks login button")
def step_impl(context):
    context.driver.find_element("id","login-button").click()
    
@then("user should navigate to home page")
def step_impl(context):
    try:
        product_locator=(By.XPATH,"//span[text()='Products']")
        product_element=context.driver.find_element(*product_locator)
        assert product_element.is_displayed(),"Product is not displayed"
    except NoSuchElementException:
        # self healing code
            assert False ,"product pae is not visisble"
  # adding exception handling mechanism in selenium web automation      

