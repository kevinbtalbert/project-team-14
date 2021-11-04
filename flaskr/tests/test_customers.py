import requests
from flaskr.tests.test_config import TestTestingConfig


class TestCustomersRoute(TestTestingConfig):

    def test_customers(self):
        """
        Test the "/customers" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_new_customers(self):
        """
        Test the "/customers/new" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/new")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_lookup_customer(self):
        """
        Test the "/customers/lookup" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/lookup")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_customer_profile_by_id(self):
        """
        Test the "/customers/lookup/<id>" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/lookup/1")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_edit_customer_profile_by_id(self):
        """
        Test the "/customers/lookup/<id>/edit_profile" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/lookup/1/edit_profile")
        print(response)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_edit_customer_sizing_by_id(self):
        """
        Test the "/customers/lookup/<id>/edit_sizing" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/lookup/1/edit_sizing")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_delete_customer_by_id(self):
        """
        Test the "/customers/lookup/<id>/delete_profile" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/customers/lookup/1/delete_profile")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
