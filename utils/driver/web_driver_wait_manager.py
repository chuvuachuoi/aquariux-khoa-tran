from selenium.webdriver.support.ui import WebDriverWait

from config.config import Config

class WebDriverWaitManager:
    @staticmethod
    def get_web_driver_wait(driver):
        if (driver is None):
            return None
        
        return WebDriverWait(driver=driver, timeout=Config.TIMEOUT, poll_frequency=0.5, ignored_exceptions=None)