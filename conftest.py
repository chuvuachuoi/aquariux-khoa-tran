from utils.common_imports import Config, ChromeDriver, pytest

@pytest.fixture
def driver():
    if Config.BROWSER == "chrome":
        driver = ChromeDriver()
    else:
        raise Exception(f"Browser {Config.BROWSER} is not supported yet")
    
    yield driver.get_driver()
    
    driver.quit()