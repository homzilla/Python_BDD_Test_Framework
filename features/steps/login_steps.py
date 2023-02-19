from behave import given, when, then
from time import sleep
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage

@given("I am on the login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.applitools.com/hackathon.html")
    context.login_page = LoginPage(context.driver)

@when("I enter valid credentials")
def step_impl(context):
    context.login_page.enter_username("test@example.com")
    context.login_page.enter_password("test1234")

@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()

@then("I should be redirected to the main page")
def step_impl(context):
    main_page = MainPage(context.driver)
    sleep(2)
    assert "ACME" in context.driver.current_url
