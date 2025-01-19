from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class MarketCompaniesPage(BasePage):

 MARKET_VERIFICATION_URL = "market-companies"
 ADD_COMPANY_BUTTON = (By.XPATH, "//div[text()='Add company']")

 def verify_market(self):
     self.verify_partial_url(self.MARKET_VERIFICATION_URL)
 def click_add_company(self):
     self.wait_and_click(*self.ADD_COMPANY_BUTTON)
