import requests
from flaskr.tests.test_config import TestTestingConfig


class TestProductsRoute(TestTestingConfig):

    def test_products(self):
        """
        Test the "/products" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/products/")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_new_product(self):
        """
        Test the "/products/new" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/products/new")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_lookup_product(self):
        """
        Test the "/products/lookup" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/products/lookup")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_product_by_id(self):
        """
        Test the "/products/lookup/<id>" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/products/lookup/1")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_edit_product_by_id(self):
        """
        Test the "/products/lookup/<id>/edit_product" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/products/lookup/1/edit_profile")
        print(response)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)

    def test_delete_product_by_id(self):
        """
        Test the "/products/lookup/<id>/delete_product" route
        - Test successful GET request to the route
        - Test status code of GET request is 200 (OK)
        """
        response = self.client.get("/products/lookup/1/delete_product")
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
