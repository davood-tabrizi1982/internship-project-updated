from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ViewPageTemplate(BasePage):
    EXPECTED_FOR_SEND_MY_CV_AVAILABILITY = 'Send my CV'
    SEND_MY_CV_TEXT = (By.XPATH, "//a[@class ='button-agency w-button' and text() = 'Send my CV']")

    def verify_send_my_cv_text(self):
        self.verify_text(self.EXPECTED_FOR_SEND_MY_CV_AVAILABILITY, *self.SEND_MY_CV_TEXT)
