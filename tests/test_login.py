from pages.login.login_page import LoginPage 
from utils.common_imports import Logger

logger = Logger.get_logger("Test Login")

def test_login_with_demo_account(driver):
    logger.info("Starting test_login_with_demo_account")
    login_page = LoginPage.navigate_to(driver)
    login_page.change_login_account_type("Demo Account")
    home_page = login_page.login("2092008680", "Ar7O#77y!mcZ")
    assert home_page is not None, "Login with demo account should have succeeded"
    
def test_login_with_live_account(driver):
    logger.info("Starting test_login_with_live_account")
    login_page = LoginPage.navigate_to(driver)
    home_page = login_page.login("2092008680", "Ar7O#77y!mcZ")
    assert home_page is None, "Login with live account should have failed"