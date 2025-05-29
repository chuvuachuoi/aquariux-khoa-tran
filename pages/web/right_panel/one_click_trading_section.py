from utils.common_imports import By, BaseObject, Logger, webdriver, WebElement


class OneClickTradingSection(BaseObject):
    logger = Logger.get_logger(__name__)
    
    __toggle_button_locator = (By.XPATH, "./div[@data-testid = 'toggle-oct']")
    
    def __init__(self, driver: webdriver, element: WebElement):
        OneClickTradingSection.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__(driver, element)
        self.__get_toggle_button()
        
    def __get_toggle_button(self):
        OneClickTradingSection.logger.debug("Locating toggle button for One-Click Trading")
        return self._find_nested_element(OneClickTradingSection.__toggle_button_locator)