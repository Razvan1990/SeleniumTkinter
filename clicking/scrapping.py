import configparser
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import constants


class ScrapeWeb(object):

    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.file = os.path.join(os.getcwd(), "credentiuals.ini")
        self.service_driver = Service(r"G:\pycharm\pythonProject\DirectClickTkinter\chrome\chromedriver.exe")
        self.prefs = {"credentials_enable_service": False,
                      "profile.password_manager_enabled": False}
        self.counter_sessions = 0

    def create_driver(self):
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_argument("start-maximized")
        options_chrome.add_argument("disable-infobars")
        options_chrome.add_experimental_option("prefs", self.prefs)
        # options_chrome.add_experimental_option("debuggerAddress", "localhost:9222")
        options_chrome.add_experimental_option("excludeSwitches", ["enable-automation", "disable-popup-blocking"])
        options_chrome.add_experimental_option("detach", True)
        # create driver
        my_driver = webdriver.Chrome(service=self.service_driver, options=options_chrome)
        return my_driver

    def open_browser(self, url):
        driver = self.create_driver()
        # need to make now logic for every url and check how to connect
        self.parser.read(self.file)
        if url == constants.GIT:
            driver.get(constants.GIT)
            # click on sign in
            driver.implicitly_wait(2)
            sign_in_button = driver.find_element(by="css selector",
                                                 value="body > div.logged-out.env-production.page-responsive.header-overlay.header-overlay-fixed.js-header-overlay-fixed > div.position-relative.header-wrapper.js-header-wrapper > header > div > div.HeaderMenu.js-header-menu.height-fit.position-lg-relative.d-lg-flex.flex-column.flex-auto.top-0 > div > div > div > a")
            sign_in_button.click()
            # introduce the login information
            self.parser.read(self.file)
            driver.implicitly_wait(2)
            account_bar = driver.find_element(by="id", value="login_field")
            account_bar.clear()
            account_bar.send_keys(self.parser.get("GIT", "user"))
            password_bar = driver.find_element(by="id", value="password")
            password_bar.clear()
            password_bar.send_keys(self.parser.get("GIT", "password"))
            time.sleep(1)
            # click on login button
            login_button = driver.find_element(by="name", value="commit")
            login_button.click()
            self.counter_sessions += 1
        elif url == constants.LINKEDIN:
            driver.get(constants.LINKEDIN)
            # click on sign in
            driver.implicitly_wait(2)
            sign_in_button = driver.find_element(by="css selector",
                                                 value="body > nav > div > a.nav__button-secondary.btn-secondary-emphasis.btn-md")
            sign_in_button.click()
            # introduce login information
            email_info = driver.find_element(by="id", value="username")
            email_info.clear()
            email_info.send_keys(self.parser.get("LINKEDIN", "user"))
            password_bar = driver.find_element(by="id", value="password")
            password_bar.clear()
            password_bar.send_keys(self.parser.get("LINKEDIN", "password"))
            time.sleep(1)
            # press enter
            login_button = driver.find_element(by="css selector",
                                               value="#organic-div > form > div.login__form_action_container > button")
            login_button.send_keys(Keys.RETURN)
            self.counter_sessions += 1
        else:
            driver.get(constants.FILELIST)
            driver.implicitly_wait(2)
            # introduce credentials
            username = driver.find_element(by="id", value="username")
            username.clear()
            username.send_keys(self.parser.get("FILELIST", "user"))
            password = driver.find_element(by="id", value="password")
            password.clear()
            password.send_keys(self.parser.get("FILELIST", "password"))
            # press enter
            driver.implicitly_wait(2)
            login_button = driver.find_element(by="css selector",
                                               value="#loginContainer > div.login-options > div.login-btn > input")
            login_button.send_keys(Keys.RETURN)
            self.counter_sessions += 1
