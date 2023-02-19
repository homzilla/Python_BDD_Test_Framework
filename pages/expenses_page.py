from selenium.webdriver.common.by import By

class ExpensesPage:

    def __init__(self, driver):
        self.driver = driver
        self.compare_expenses_button = (By.ID, "showExpensesChart")
        self.year1_select = (By.ID, "addDataset")
        self.year2_select = (By.ID, "addDataset")
        self.show_data_button = (By.ID, "showData")
        self.chart = (By.ID, "canvas")

    def is_expenses_page_displayed(self):
        return "hackathonAppV2.html" in self.driver.current_url

    def click_compare_expenses_button(self):
        self.driver.find_element(*self.compare_expenses_button).click()

    def select_year_options(self, year1, year2):
        self.driver.find_element(*self.year1_select).send_keys(year1)
        self.driver.find_element(*self.year2_select).send_keys(year2)

    def click_show_data_button(self):
        self.driver.find_element(*self.show_data_button).click()

 #   def is_chart_displayed(self):
 #      return self.driver.find_element(*self.is_chart_displayed).is_displayed()
