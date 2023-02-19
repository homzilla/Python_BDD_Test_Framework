from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_button = (By.ID, "logout")

    def is_logout_button_displayed(self):
        return self.driver.find_element(*self.logout_button).is_displayed()
