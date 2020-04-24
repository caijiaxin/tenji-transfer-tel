from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Actions:

    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    def clickElement(self, selector):
        current_url = self.__driver.current_url
        element = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.click()
        if current_url == self.__driver.current_url:
            isRadio = element.get_attribute('type')
            print('is radio :' + isRadio)
            if isRadio != 'radio':
                self.clickElement(selector)
        else:
            print(self.__driver.current_url)

    def inputText(self, selector, text):
        element = WebDriverWait(self.__driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.send_keys(text)
        keys = element.get_attribute('value')
        if len(keys) == 0:
            self.inputText(selector, text)
        else:
            self.sendKeys(element, text)
            print('key is :' + keys)

    def sendKeys(self, element, text):
        element.clear()
        element.send_keys(text)
