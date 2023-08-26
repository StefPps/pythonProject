from driver import Driver


class BasePage(Driver):

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def is_displayed(self, locator):
        self.driver.find_element(*locator).is_displayed()
