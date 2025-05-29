from utils.common_imports import webdriver, Logger
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.driver.base_driver import BaseDriver
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config

class ChromeDriver(BaseDriver):
    logger = Logger.get_logger(__name__)
    
    def __init__(self):
        ChromeDriver.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__()
        self._options = self._configure_options()
        self._driver = webdriver.Chrome(options=self._options, service=ChromeService(ChromeDriverManager().install()))
        self._configure_driver()
        
    def _configure_options(self):
        ChromeDriver.logger.debug("Configuring Chrome options")
        options = webdriver.ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless")
        return options