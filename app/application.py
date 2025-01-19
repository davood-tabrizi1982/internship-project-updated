
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.sideNavigation_page import SideNavigation
from pages.signIn_page import SignIn
from pages.marketCompanies_page import MarketCompaniesPage
from pages.presentationAgency_page import PresentationAgency
from pages.viewPageTemplate_page import  ViewPageTemplate

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.sideNavigation_page = SideNavigation(driver)
        self.signIn_page = SignIn(driver)
        self.marketCompanies_page = MarketCompaniesPage(driver)
        self.presentationAgency_page = PresentationAgency(driver)
        self.viewPageTemplate_page = ViewPageTemplate(driver)