from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')\
            .click()
        # the code I written since here could be used all instagram bots in login process.

        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()

my_bot = InstaBot('user_name', 'password')




