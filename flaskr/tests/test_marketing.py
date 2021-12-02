import requests
from flaskr.tests.test_config import TestTestingConfig


class TestMarketingRoute(TestTestingConfig):

    def test_marketing(self):
        """
        Test the "/marketing" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/marketing/")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
