from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class ViewPageTemplate(BasePage):
    EXPECTED_FOR_SEND_MY_CV_AVAILABILITY = 'Send my CV'
    SEND_MY_CV_TEXT = (By.XPATH, "//a[@class ='button-agency w-button' and text() = 'Send my CV']")

    def verify_send_my_cv_text(self):
        sleep(7)
        #self.verify_text(self.EXPECTED_FOR_SEND_MY_CV_AVAILABILITY, *self.SEND_MY_CV_TEXT)
        #self.wait_and_click(self.SEND_MY_CV_TEXT)
        element = self.wait.until(EC.presence_of_element_located(self.SEND_MY_CV_TEXT))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.element_to_be_clickable(self.SEND_MY_CV_TEXT)).click()
