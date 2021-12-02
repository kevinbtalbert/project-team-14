import requests
from flaskr.tests.test_config import TestTestingConfig


class TestManagementRoute(TestTestingConfig):

    def test_management(self):
        """
        Test the "/management" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/management/")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_new_user(self):
        """
        Test the "/management/new" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/management/new")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_edit_user_by_id(self):
        """
        Test the "/management/lookup/<id>" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/management/lookup/1")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)