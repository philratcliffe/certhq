import unittest

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(NewVisitorTest, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(NewVisitorTest, cls).tearDownClass()

    def test_get_the_expected_root_home_page(self):
        # Terry has heard about a new online app certhq. She goes
        # to check out its homepage.
        self.selenium.get(self.live_server_url)

        # She notices that the page title and mention CertHQ
        self.assertTrue('CertHQ' in self.selenium.title)

        # She notices that she is invited to Sign In 
        self.assertTrue('Sign' in self.selenium.page_source)