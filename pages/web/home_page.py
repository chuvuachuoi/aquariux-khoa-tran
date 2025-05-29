from utils.common_imports import ExpectedCondition, By, BasePage, Logger, webdriver

class HomePage(BasePage):
    logger = Logger.get_logger(__name__)
    
    __right_panel_locator = (By.XPATH, "//div[@data-testid = 'trade-button-order-buy']/../../..")
    __one_click_trading_section_locator = (By.XPATH, "//div[div[string() = 'One-Click Trading'] and div[@data-testid = 'toggle-oct']]")
    
    def __init__(self, driver: webdriver):
        HomePage.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__(driver)
        
    @staticmethod
    def get_page(driver: webdriver):
        HomePage.logger.debug("Get Home page")
        home_page = HomePage(driver)
        if not home_page._wait_for_readiness():
            return None
        
        return home_page
    
    def _wait_for_readiness(self):
        HomePage.logger.debug("Waiting for Home page is ready")
        result = False
        try:
            self._wait.until(ExpectedCondition.url_contains("/web"))
            self._wait.until(ExpectedCondition.visibility_of_element_located(self.__right_panel_locator) and 
                          ExpectedCondition.visibility_of_element_located(self.__one_click_trading_section_locator))
            result = True
        except Exception as e:
            HomePage.logger.error(f"Error waiting for page readiness: {e}")
            
        return result