import unittest

from ZestMoneyAssignment.pages.FacebookPage import facebookpage
import pytest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class facebooktest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.fb = facebookpage(self.driver)

    @pytest.mark.run(order=1)
    def test_facebook_login(self):
        self.fb.launchFacebookPage()
        # User needs to pass the login and password as arguments
        self.fb.enter_credentials("xyz@gmail.com", "password")
        self.fb.click_login()

    @pytest.mark.run(order=3)
    def test_logout(self):
        self.fb.logout()
        self.fb.teardown()

    @pytest.mark.run(order=2)
    def test_post_flow(self):
        self.fb.click_home_button()
        self.fb.validate_create_post_text()
        self.fb.create_post()
        self.fb.validate_created_post()


