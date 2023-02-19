from behave import given, when, then
from pages.login_page import LoginPage
from pages.expenses_page import ExpensesPage

@given('the user is logged in')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.login()

@when('the user clicks on the "Compare Expenses" button')
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    expenses_page.click_compare_expenses_button()

@when('the user clicks on the "Show data for next year" button')
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    expenses_page.click_show_data_next_year_button()

@when('the user clicks on the "Show expenses chart" button')
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    expenses_page.click_show_chart_button()

@then('the expenses chart should be displayed')
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    assert expenses_page.is_chart_displayed(), "Expenses chart is not displayed"
