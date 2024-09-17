from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_information_option_link_test = "Edit your account information"

    def display_status_of_edit_your_account_information(self):
        return self.display_status("edit_your_account_information_option_link_test", self.edit_your_account_information_option_link_test)

