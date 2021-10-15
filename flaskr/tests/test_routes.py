import requests
from flaskr.tests.test_config import TestTestingConfig


class TestIndexRoute(TestTestingConfig):

    def test_index(self):
        """
        Test the "/" (index) route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

class TestUtilRoutes(TestTestingConfig):

    def test_404(self):
        """
        Test the 404 (Error: Page not found) route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/404")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
