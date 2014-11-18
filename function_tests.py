from selenium import webdriver
from user_auth.models import MyUserManager
from selenium.webdriver.common.keys import Keys
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_page(self):
        self.browser.get('http://127.0.0.1:8000/user')
        assert 'email' in self.browser.page_source

    def test_login(self):
        self.browser.get('http://127.0.0.1:8000/user')
        email = self.browser.find_element_by_name('email')
        email.send_keys('test@test.com')
        password = self.browser.find_element_by_name('password')
        password.send_keys('test')
        button = self.browser.find_element_by_id('login_button')
        button.click()
        assert "Welcome to the profile page" in self.browser.page_source
