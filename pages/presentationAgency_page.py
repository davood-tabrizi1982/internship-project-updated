from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class PresentationAgency(BasePage):
    VERIFY_PRESENTATION_AGENCY_PAGE_URL = "presentation-for-the-agency"
    VIEW_PAGE_BUTTON = (By.XPATH, "//a [text() = 'View page template' ]")
    SEND_MY_CV = (By.XPATH, "//a[@class ='button-agency w-button' and text() = 'Send my CV']")

    def verify_presentation_agency_page(self):
        self.verify_partial_url(self.VERIFY_PRESENTATION_AGENCY_PAGE_URL)
    def click_view_page_button(self):
        sleep(5)
        self.wait_and_click(self.VIEW_PAGE_BUTTON)
        sleep(5)
