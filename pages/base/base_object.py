from utils.common_imports import BaseElement, Logger, webdriver, WebElement, By

class BaseObject(BaseElement):
    logger = Logger.get_logger(__name__)
    
    def __init__(self, driver: webdriver, element: WebElement):
        # BaseObject.logger.debug(f"Initializing {self.__class__.__name__} with element: {element}")
        super().__init__(driver)
        self._element = element
    
    def _find_nested_element(self, locator: By):
        BaseObject.logger.debug(f"Finding nested element with locator: {locator} in parent element: {self._element}")
        
        class nested_element_to_be_visible(object):
            def __init__(self, parent_element: WebElement, locator: By):
                self.__parent_element = parent_element
                self.__locator = locator
            
            def __call__(self, driver):
                try:
                    element = self.__parent_element.find_element(*self.__locator)
                    return element.is_displayed()
                except:
                    return False
        
        element = None
        try:
            self._wait.until(nested_element_to_be_visible(self._element, locator))
            element = self._element.find_element(*locator)
        except Exception as e:
            BaseObject.logger.error(f"Error finding nested element: {e}")
            raise RuntimeError(f"Nested element with locator {locator} not found in parent element") from e
            
        return element
    
    def _click_element(self, locator: By):
        BaseObject.logger.debug(f"Clicking nested element with locator: {locator} in parent element: {self._element}")
        element = self._find_nested_element(locator)
        element.click()