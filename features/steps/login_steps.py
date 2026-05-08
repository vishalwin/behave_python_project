from behave import given, when, then
import time
    
@given(u'user launches browser')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")


@when(u'user enter username and password')
def step_impl(context):
    context.driver.find_element("id","user-name").send_keys("standard_user")
    context.driver.find_element("id","password").send_keys("secret_sauce")
    
@when("clicks login button")
def step_impl(context):
    context.driver.find_element("id","login-button").click()
    
@then("user should navigate to home page")
def step_impl(context):
    time.sleep(10)
    assert "inventory" in context.driver.current_url
    

