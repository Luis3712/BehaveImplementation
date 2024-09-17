from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    account_success_heading_xpath = "//div[@id='content']/h1"

    def display_status_of_account_created_heading(self,  expected_text_message):
        return self.retrieved_element_text_equals("account_success_heading_xpath", self.account_success_heading_xpath, expected_text_message)
