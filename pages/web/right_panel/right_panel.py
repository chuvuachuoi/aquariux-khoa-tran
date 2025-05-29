from utils.common_imports import By, BaseObject, Logger, webdriver, WebElement, By

class RightPanel(BaseObject):
    logger = Logger.get_logger(__name__)
    
    __buy_button_locator = (By.XPATH, ".//div[@data-testid = 'trade-button-order-buy']")
    __sell_button_locator = (By.XPATH, ".//div[@data-testid = 'trade-button-order-sell']")
    __order_type_dropdown_locator = (By.XPATH, ".//div[@data-testid = 'trade-dropdown-order-type']")
    
    def __init__(self, driver: webdriver, element: WebElement):
        RightPanel.logger.debug(f"Initializing {self.__class__.__name__}")
        super().__init__(driver, element)
    
    def get_current_order_type(self):
        RightPanel.logger.debug("Retrieving current Order Type value")
        order_type_dropdown_element = super()._find_nested_element(RightPanel.__order_type_dropdown_locator)
        return order_type_dropdown_element.text if order_type_dropdown_element else None
    
    