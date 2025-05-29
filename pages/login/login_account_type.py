from utils.common_imports import By, BaseObject, Logger, webdriver, WebElement, ExpectedCondition

class LoginAccountType(BaseObject):
    logger = Logger.get_logger(__name__)
    
    __live_account_type_locator = (By.XPATH, "./div[@data-testid = 'tab-login-account-type-live']")
    __demo_account_type_locator = (By.XPATH, "./div[@data-testid = 'tab-login-account-type-demo']")
    
    def __init__(self, driver: webdriver, element: WebElement):
        LoginAccountType.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__(driver, element)
        self._wait_for_readiness()
        
    def set_login_account_type(self, account_type: str):
        LoginAccountType.logger.debug(f"Setting login account type to {account_type}")
        match account_type:
            case "Live Account":
                self._click_element(LoginAccountType.__live_account_type_locator)
            case "Demo Account":
                self._click_element(LoginAccountType.__demo_account_type_locator)
            case _:
                raise ValueError(f"Invalid account type: {account_type}. Expected 'live' or 'demo'.")
        
    def _wait_for_readiness(self):
        LoginAccountType.logger.debug("Waiting for Login Account Type section is ready")
        try:
            self._find_nested_element(LoginAccountType.__live_account_type_locator)
            self._find_nested_element(LoginAccountType.__demo_account_type_locator)
        except Exception as e:
            LoginAccountType.logger.error(f"Error waiting for account type readiness: {e}")
            raise RuntimeError("Login account type section is not ready") from e