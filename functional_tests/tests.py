from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.home_page_url = 'http://localhost:8000'

    def tearDown(self):
        self.browser.quit()

    def test_get_the_expected_root_home_page(self):
        # Terry has heard about a new online app certhq. She goes
        # to check out its homepage.
        self.browser.get(self.home_page_url)

        # She notices that the page title and mention CertHQ
        self.assertIn('CertHQ', self.browser.title)

        # She notices that she is invited to Sign In 
        self.assertIn('Sign', self.browser.page_source)


if __name__ == '__main__':
    unittest.main()
