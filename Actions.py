from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Actions:

    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    def click_element(self, selector):
        current_url = self.__driver.current_url
        element = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.click()
        if current_url == self.__driver.current_url:
            is_radio = element.get_attribute('type')
            if is_radio != 'radio':
                self.click_element(selector)

    def input_text(self, selector, text):
        element = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.send_keys(text)
        keys = element.get_attribute('value')
        if len(keys) == 0:
            self.input_text(selector, text)
        else:
            self.send_keys(element, text)

    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)
