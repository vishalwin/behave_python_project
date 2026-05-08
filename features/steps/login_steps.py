from behave import given, when, then
import time
from utils.json_reader import read_json
    
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
    time.sleep(10)
    assert "inventory" in context.driver.current_url
    

