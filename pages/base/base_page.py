from utils.common_imports import BaseElement, Logger, webdriver

class BasePage(BaseElement):
    logger = Logger.get_logger(__name__)
    
    def __init__(self, driver: webdriver):
        # BasePage.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__(driver)
        