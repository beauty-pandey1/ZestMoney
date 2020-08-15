import time

from selenium.webdriver.common.by import By

import ZestMoneyAssignment.utilities.customLogger as c_log
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class facebookpage:
    log = c_log.customLogger()

    _email = 'email' # id
    _pwd = 'pass' # name
    _url = "https://www.facebook.com/"
    _title = 'Facebook – log in or sign up'
    _login = 'login' # name

    def __init__(self, driver):
        self.driver = driver

    def launchFacebookPage(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self._url)
            self.driver.implicitly_wait(2)
            assert self._title in self.driver.title
            self.log.info("Facebook page launched successfully with URL {}".format(self._url))
        except:
            self.log.error("Unable to launch the Facebook page with URL {}".format(self._url))

    def enter_credentials(self, email_id, password):
        try:
            global wait
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     NoSuchElementException])
            login_id_field = wait.until(ec.presence_of_element_located((By.ID, self._email)))
            login_id_field.send_keys(email_id)
            password_field = wait.until(ec.presence_of_element_located((By.NAME, self._pwd)))
            password_field.send_keys(password)
            self.log.info("Successfully entered the credentials")
        except:
            self.log.error("Unable to enter the credentials")

    def click_login(self):
        try:
            wait.until(ec.presence_of_element_located((By.NAME, 'login'))).click()
            self.log.info("Login button clicked successfully")
        except:
            self.log.error("Could not click Login button")

    def click_home_button(self):
        try:
            home_button = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@class="_3qcu _cy7"]')))
            home_button.click()
            self.log.info("Clicked on Home button successfully")
        except:
            self.log.error("Unable to click on the Home button")

    def validate_create_post_text(self):
        try:
            wait.until(ec.presence_of_element_located((By.XPATH, '//*[@class="_5qtp"]/../../../following-sibling::*[@method="post"]')))
            self.log.info("Create post is visible")
        except:
            self.log.error("Create post is not visible")

    def create_post(self):
        try:
            post_field = wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(@title,'Writ"
                                                                         "e something here...' )]")))
            post_field.send_keys("Hello World")
            self.driver.implicitly_wait(5)
            post_button = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@class="_1mf7 '
                                                                          '_4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft" and @type="submit"]//child::*[text()="Post"]')))
            post_button.click()
            self.log.info("Created post successfully")
        except:
            self.log.error("Unable to create post")

    def validate_created_post(self):
        try:
            post = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@class="_5pbx userContent _3ds9 _3576"]/div[1]')))
            assert post.text == "Hello World"
            self.log.info("Created post is visible")
            pass
        except:
            self.log.info("Unable to see the created post")

    def logout(self):
        try:
            logout_btn = wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='logoutMenu']")))
            logout_btn.click()
            time.sleep(2)
            logout_option = wait.until(ec.presence_of_element_located((By.XPATH, "//*[@class='_54ni navSubmenu _6398 _64kz __MenuItem']")))
            print("Element identified successfully")
            logout_option.click()
            self.log.info("Logged out successfully")
        except:
            self.log.error("Unable to log out successfully")

    def teardown(self):
        self.driver.close()
        self.driver.quit()








