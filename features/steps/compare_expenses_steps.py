from behave import given, when, then
from time import sleep
from selenium import webdriver
from pages.login_page import LoginPage
from pages.expenses_page import ExpensesPage


@when("I am on the expenses page")
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    assert expenses_page.is_expenses_page_displayed()


@when('I click the "Compare Expenses" button')
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    expenses_page.click_compare_expenses_button()


@when('I select the "{year1}" and "{year2}" options')
def step_impl(context, year1, year2):
    expenses_page = ExpensesPage(context.driver)
    expenses_page.select_year_options(year1, year2)


@when('I click the "Show data" button')
def step_impl(context):
    expenses_page = ExpensesPage(context.driver)
    expenses_page.click_show_data_button()

# @then("I should see a chart comparing the expenses for the selected years")
# def step_impl(context):
#   expenses_page = ExpensesPage(context.driver)
#  assert expenses_page.is_chart_displayed()
