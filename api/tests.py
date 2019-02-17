# Create your tests here.
from django.test import Client
from django.test import TestCase

from api.apps import ApiConfig


class ExempleTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_app_name(self):
        """The ApiConfig name shoud be api"""
        self.assertEqual(ApiConfig.name, "api")

    def test_healthcheck(self):
        response = self.client.get("/healthcheck/")

        self.assertEqual(response.status_code, 200)
