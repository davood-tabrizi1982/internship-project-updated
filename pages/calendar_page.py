from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class Calendar(BasePage):

 COMPANIES_BUTTON = (By.XPATH, "//a[text() = 'Companies']")
 def click_companies_button(self):
        self.wait_and_click(self.COMPANIES_BUTTON)