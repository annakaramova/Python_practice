from selenium.webdriver.common.by import By
from Browser import Browser


class MainPage(object):
    REMARKS = (By.XPATH, '/html/body/main/section/div/h1')

    def __init__(self):
        self.browser = Browser("https://automation-remarks.com/")

    def close(self):
        self.browser.close()

    def get_remarks(self):
        return self.browser.find_element(self.REMARKS)
