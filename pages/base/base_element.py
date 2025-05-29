from abc import abstractmethod
from utils.common_imports import Config, ExpectedCondition, WebDriverWaitManager, Logger, webdriver, By, WebElement

class BaseElement:
    logger = Logger.get_logger(__name__)
    
    def __init__(self, driver: webdriver):
        self._driver = driver
        self._timeout = Config.TIMEOUT
        self._wait = WebDriverWaitManager.get_web_driver_wait(self._driver)
        
    def _find_element(self, locator: By):
        BaseElement.logger.debug(f"Finding element with locator: {locator}")
        element = None
        try:
            element = self._wait.until(ExpectedCondition.visibility_of_element_located(locator))
        except Exception as e:
            BaseElement.logger.error(f"Error finding element with locator {locator}: {e}")
            raise RuntimeError(f"Element with locator {locator} not found") from e
        
        return element
        
    def _click_element(self, locator: By):
        BaseElement.logger.debug(f"Clicking element with locator: {locator}")
        element = self._find_element(locator)
        element.click()
        
    def _enter_text(self, locator: By, text_value):
        BaseElement.logger.debug(f"Entering text '{text_value}' into element with locator: {locator}")
        element = self._find_element(locator)
        element.clear() # Clear the field before entering text
        element.send_keys(text_value)
        
    def _get_text(self, locator: By):
        BaseElement.logger.debug(f"Getting text from element with locator: {locator}")
        element = self._find_element(locator)
        return element.text
    
    @abstractmethod
    def _wait_for_readiness(self):
        pass