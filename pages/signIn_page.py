from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from pages.base_page import BasePage
from time import sleep

class SignIn(BasePage):

 EMAIL_PLACE_HOLDER = (By.CSS_SELECTOR, "input[data-name='Email 2']")
 PASSWORD_PLACE_HOLDER = (By.CSS_SELECTOR, "input[data-name='Password']")
 CONTINUE_BUTTON =(By.XPATH, "//a[text()='Continue']")

 def signin_username(self):
     sleep(2)
     self.input_text("davood_tabrizi@yahoo.com", *self.EMAIL_PLACE_HOLDER)
     sleep(2)

 def signin_password(self):
     sleep(2)
     self.input_text("Davood1234$", *self.PASSWORD_PLACE_HOLDER)

 def signin_button(self):
     self.wait_for_element_clickable(*self.CONTINUE_BUTTON).click()
     sleep(5)


