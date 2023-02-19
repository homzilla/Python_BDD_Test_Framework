from behave import given, when, then
from pages.expenses_page import ExpensesPage

@given("I am on the expenses page")
def step_impl(context):
    context.expenses_page = ExpensesPage(context.driver)
    context.expenses_page.load()

@when("I refresh the page")
def step_impl(context):
    context.expenses_page.refresh()

@then("I should see different dynamic ads on the page")
def step_impl(context):
    ad1 = context.expenses_page.get_dynamic_ad_1_text()
    ad2 = context.expenses_page.get_dynamic_ad_2_text()
    assert ad1 != ad2, "Dynamic ads are not different"
