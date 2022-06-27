from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, url):
        service = Service(executable_path=ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=service)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @property
    def driver(self):
        return self._driver

    def get(self, url):
        return self.driver.get(url)

    def find_element(self, element):
        return self.driver.find_element(by=element[0], value=element[1])

    def find_elements(self, elements):
        return self.driver.find_elements(by=elements.by, value=elements.value)

    def close(self):
        self.driver.close()
        self.driver.quit()
