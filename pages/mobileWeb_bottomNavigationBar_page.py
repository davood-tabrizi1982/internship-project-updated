from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class BottomNavigationBar(BasePage):

 EVENTS_BUTTON = (By.XPATH, "//div[text() = 'Events']")
 def click_events_button(self):
        self.wait_and_click(self.EVENTS_BUTTON)




