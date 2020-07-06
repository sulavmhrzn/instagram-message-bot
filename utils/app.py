from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep


class Bot:
    def __init__(self, username, password):
        self.driver = Chrome()
        self.username = username
        self.password = password

    def login(self):
        self.driver.get(
            'https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        uname = self.driver.find_element_by_name(
            'username').send_keys(self.username)
        password = self.driver.find_element_by_name(
            'password').send_keys(self.password)
        submit = self.driver.find_element_by_tag_name('form')
        submit.submit()
        sleep(3)

    def message_to(self, username):
        self.driver.get(f'https://www.instagram.com/{username}')
        sleep(3)
        message_button = self.driver.find_element_by_xpath(
            "//button[text()='Message']")
        message_button.click()
        sleep(3)
        not_now = self.driver.find_element_by_xpath(
            "//button[text()='Not Now']")
        not_now.click()
        text_area = self.driver.find_element_by_xpath("//textarea")
        with open('text.txt', 'r') as file:
            for word in file.readlines():
                text_area.send_keys(word)
                text_area.send_keys(Keys.RETURN)
                sleep(2)

    def close_browser(self):
        self.driver.close()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_browser()
