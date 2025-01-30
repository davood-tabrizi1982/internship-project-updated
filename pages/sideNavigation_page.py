from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from pages.base_page import BasePage
from time import sleep

class SideNavigation(BasePage):
 MARKET_BUTTON = (By.XPATH, "//div[text()='Market']")

 def click_market(self):
     sleep(5)
     self.wait_and_click(self.MARKET_BUTTON)