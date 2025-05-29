from utils.common_imports import By, Config, BasePage, Logger, webdriver, ExpectedCondition, pytest
from pages.login.login_account_type import LoginAccountType

from pages.web.home_page import HomePage

class LoginPage(BasePage):
    logger = Logger.get_logger(__name__)
    
    __login_account_type_locator = (By.XPATH, "//div[@data-testid = 'login-account-type']")
    __account_id_locator = (By.XPATH, "//input[@data-testid = 'login-user-id']")
    __password_locator = (By.XPATH, "//input[@data-testid = 'login-password']")
    __login_button_locator = (By.XPATH, "//button[@data-testid = 'login-submit']")
    
    def __init__(self, driver: webdriver):
        LoginPage.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__(driver)
        
    @staticmethod
    def navigate_to(driver: webdriver):
        LoginPage.logger.debug("Navigating to Login page")
        driver.get(Config.BASE_URL)
        login_page = LoginPage(driver)
        if not login_page._wait_for_readiness:
            return None
        
        return login_page
        
    def enter_credential(self, account_id, password):
        LoginPage.logger.debug("Entering credentials")
        self._enter_text(LoginPage.__account_id_locator, account_id)
        self._enter_text(LoginPage.__password_locator, password)
        
    def login(self, account_id, password):
        LoginPage.logger.debug("Attempting to log in")
        self.enter_credential(account_id, password)
        self._click_element(LoginPage.__login_button_locator)
        return HomePage.get_page(self._driver)
    
    def _wait_for_readiness(self):
        LoginPage.logger.debug("Waiting for Login page is ready")
        result = False
        try:
            self._wait.until(ExpectedCondition.visibility_of_element_located(LoginPage.__account_id_locator) and 
                         ExpectedCondition.visibility_of_element_located(LoginPage.__password_locator) and
                         ExpectedCondition.visibility_of_element_located(LoginPage.__login_button_locator))
            result = True
        except Exception as e:
            LoginPage.logger.error(f"Error waiting for page readiness: {e}")
        
        return result
        
    def change_login_account_type(self, login_account_type: str):
        LoginPage.logger.debug(f"Changing login account type to {login_account_type}")
        login_account_type_element = self._find_element(LoginPage.__login_account_type_locator)
        login_account_type_section = LoginAccountType(self._driver, login_account_type_element)
        login_account_type_section.set_login_account_type(login_account_type)
        
        # self._wait_for_readiness()  # Wait for the page to be ready after changing account type
        