from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:
    __DRIVER_PATH = ''
    __driver = None
    __options = Options()

    @classmethod
    def getChromeDriver(self, driver_path):
        self.__DRIVER_PATH = driver_path

        self.__options.add_argument('--disable-gpu')
        self.__options.add_argument('--disable-extensions')
        self.__options.add_argument('--proxy-server="direct://"')
        self.__options.add_argument('--proxy-bypass-list=*')
        self.__options.add_argument('--start-maximized')
        # self.__options.add_argument('--headless')

        print(self.__DRIVER_PATH)
        self.__driver = webdriver.Chrome(
            executable_path=self.__DRIVER_PATH, options=self.__options)

        return self.__driver
