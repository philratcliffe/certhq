from django.test import Client
from django.test import TestCase
from http import HTTPStatus

class TestErrorConditions(TestCase):

    def test_invalid_url(self):
        invalid_url = 'notvalidurl'
        client = Client()
        response = client.get(invalid_url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

