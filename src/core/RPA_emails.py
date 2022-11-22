import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class RPA_Emails:
    def __init__(self, driver):
        self.driver = driver
        #driver = webdriver.Chrome()
    def get_emails(self):

        elements_mails = self.driver.find_elements(By.CSS_SELECTOR, '.hcptT')

        limitDate = datetime(2022,11,7,6,0,0)

        mails = [{}]
        hCMDB = [{}]

        cont = 0