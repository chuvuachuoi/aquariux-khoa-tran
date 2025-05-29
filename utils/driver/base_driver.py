from utils.common_imports import Logger
from config.config import Config

class BaseDriver:
    logger = Logger.get_logger(__name__)
    
    def __init__(self):
        self._driver = None
        self._options = None
    
    def _configure_driver(self):
        BaseDriver.logger.debug("Configuring the driver")
        self._driver.implicit_wait = Config.TIMEOUT
        self._driver.set_page_load_timeout(Config.TIMEOUT)
        self._driver.set_script_timeout(Config.TIMEOUT)
        self._driver.maximize_window()
        
    def quit(self):
        if self._driver:
            BaseDriver.logger.debug("Quitting the driver")
            self._driver.quit()
            self._driver = None
        else:
            BaseDriver.logger.error("Driver is not initialized or already quit.")
            raise Exception("Driver is not initialized or already quit.")
        
    def get_driver(self):
        return self._driver