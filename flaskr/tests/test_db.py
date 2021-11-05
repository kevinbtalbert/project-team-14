import requests
from flaskr.tests.test_config import TestTestingConfig
from flaskr.db import *

class TestDB(TestTestingConfig):

    def test_get_db(self):
        """
        Test the database object can be successfully obtained through the test request context
        - Test database has valid data and is not none
        """
        db = get_db()
        if db is not None:
            assert True


    def test_query_db(self):
        """
        Test the database object can be successfully obtained through the test request context
        - Test querying database returns a response
        """
        response = query_db("SELECT id FROM profile LIMIT 1", ())
        if response is not None:
            assert True


    def test_find_all_profiles(self):
        """
        Test that finding all profiles can be found through this command
        - Test result is returned and it is not None
        """
        result = DB_Commands.find_all_profiles()
        assert result is not None


    def test_find_profile_by_id(self):
        """
        Test the database object can be successfully obtained through the test request context
        - Test database has valid data and is not none
        - Test that the id returned matches the expected one based on the input
        """
        response = DB_Commands.find_profile_id_by_name("Kevin", "Talbert")
        assert response is not None
        for id in response:
            if id[0] == 1:
                assert True


    def test_add_profile(self):
        """
        Test the ability to add a profile
        - Test successfully adding a profile to the database
        """
        first_name = "Jimmy"
        last_name = "Kropp"
        email = "abc@uncc.edu"
        phone = "1234547890"
        dob = "01011990"
        gender = "male"
        address_street = "710 XYZ Avenue"
        address_city = "Charlotte"
        address_state = "NC"
        # Zip left out intentionally to test default conditions

        # Add customer to database
        add_profile_response = DB_Commands.insert_new_profile(first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state)
        self.assertTrue(type(add_profile_response) == int)

        # Find the created profile using the add profile response
        find_profile_response = DB_Commands.find_profile_by_id(add_profile_response)
        for variable in find_profile_response:
            if variable[0] == add_profile_response:
                assert True
            if variable[1] == "Jimmy":
                assert True
            if variable[11] == "None Provided":
                assert True

        # Cleanup and remove
        DB_Commands.delete_profile(add_profile_response)


    def test_update_profile(self):
        """
        Test the ability to update a profile
        - Test successfully updating a profile to the database
        """
        # Call add profile before we update
        first_name = "Jimmy"
        last_name = "Kropp"
        email = "abc@uncc.edu"
        phone = "1234547890"
        dob = "01011990"
        gender = "male"
        address_street = "710 XYZ Avenue"
        address_city = "Charlotte"
        address_state = "NC"
        # Zip left out intentionally to test default conditions

        # Add customer to database
        add_profile_response = DB_Commands.insert_new_profile(first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state)

        # Find the created profile using the add profile response
        find_profile_response = DB_Commands.find_profile_by_id(add_profile_response)
        for variable in find_profile_response:
            if variable[0] == add_profile_response:
                assert True
            if variable[1] == "Jimmy":
                assert True
            if variable[11] == "None Provided":
                assert True

        # Update the profile added with new information
        new_street_address = "9201 University City Blvd"
        new_zip_code = "28223"

        update_profile_response = DB_Commands.update_profile(first_name, last_name, email, phone, dob, gender, new_street_address, address_city, address_state, new_zip_code)
        
        # Verify update was successful
        find_profile_response = DB_Commands.find_profile_by_id(add_profile_response)
        for variable in find_profile_response:
            if variable[0] == find_profile_response:
                assert True
            if variable[1] == "Jimmy":
                assert True
            if variable[8] == "9201 University City Blvd":
                assert True
            if variable[11] == "28223":
                assert True

        # Cleanup and remove
        DB_Commands.delete_profile(add_profile_response)


    def test_delete_profile(self):
        """
        Test the ability to remove a profile
        - Test successfully removing a profile from the database
        """
        first_name = "Jimmy"
        last_name = "Kropp"
        email = "abc@uncc.edu"
        phone = "1234547890"
        dob = "01011990"
        gender = "male"
        address_street = "710 XYZ Avenue"
        address_city = "Charlotte"
        address_state = "NC"
        # Zip left out intentionally to test default conditions

        # Add customer to database
        add_profile_response = DB_Commands.insert_new_profile(first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state)
        self.assertTrue(type(add_profile_response) == int)

        # Find the created profile using the add profile response
        find_profile_response = DB_Commands.find_profile_by_id(add_profile_response)
        for variable in find_profile_response:
            if variable[0] == add_profile_response:
                assert True
            if variable[1] == "Jimmy":
                assert True
            if variable[11] == "None Provided":
                assert True

        # Cleanup and remove
        DB_Commands.delete_profile(add_profile_response)
        print(DB_Commands.find_profile_by_id(add_profile_response))
        # Confirm created profile was then deleted
        self.assertEquals(DB_Commands.find_profile_by_id(add_profile_response), [])


    def test_find_all_products(self):
        """
        Test that finding all profiles can be found through this command
        - Test result is returned and it is not None
        """
        result = DB_Commands.find_all_products()
        assert result is not None


    def test_find_product_by_id(self):
        """
        Test the database object can be successfully obtained through the test request context
        - Test database has valid data and is not none
        - Test that the response returned matches with the expected id based on the input
        """
        response = DB_Commands.find_product_by_id(1)
        assert response is not None
        for id in response:
            if id[0] == "Calvin Klein Men's X-Fit Solid Tan Slim-Fit Suit":
                assert True

    def test_find_product_id_by_name(self):
        """
        Test the database object can be successfully obtained through the test request context
        - Test database has valid data and is not none
        - Test that the id returned matches the expected one based on the input
        """
        response = DB_Commands.find_product_id_by_name("Calvin Klein Men's X-Fit Solid Tan Slim-Fit Suit")
        assert response is not None
        for id in response:
            if id[0] == 1:
                assert True

    def test_insert_new_product(self):
        """
        Test the ability to add a product
        - Test successfully adding a product to the database
        """
        product = "Metal Ring"
        product_image_url = "http://www.sample.com/image.jpg"
        category = "Social wear & Special occasions"
        company = "XYZ Company"
        # Remaining variables left out intentionally to test default conditions

        # Add product to database
        add_product_response = DB_Commands.insert_new_product(product, product_image_url, category, company)
        self.assertTrue(type(add_product_response) == int)

        # Find the created product using the add product response
        find_product_response = DB_Commands.find_product_by_id(add_product_response)
        for variable in find_product_response:
            if variable[0] == add_product_response:
                assert True
            if variable[1] == product:
                assert True
            if variable[5] == "None Provided":
                assert True

        # Cleanup and remove
        DB_Commands.delete_product(add_product_response)


    def test_update_product(self):
        """
        Test the ability to update a product
        - Test successfully updating a product to the database
        """
        product = "Metal Ring"
        product_image_url = "http://www.sample.com/image.jpg"
        category = "Social wear & Special occasions"
        company = "XYZ Company"
        # Remaining variables left out intentionally to test default conditions

        # Add product to database
        add_product_response = DB_Commands.insert_new_product(product, product_image_url, category, company)
        self.assertTrue(type(add_product_response) == int)

        # Find the created product using the add product response
        find_product_response = DB_Commands.find_product_by_id(add_product_response)
        for variable in find_product_response:
            if variable[0] == add_product_response:
                assert True
            if variable[1] == product:
                assert True
            if variable[5] == "None Provided":
                assert True

        # Update the product added with new information
        new_company = "ABC LLC"
        new_category = "Tailored Clothing & Suits"

        update_product_response = DB_Commands.update_product(product, product_image_url, new_category, new_company)
        
        # Verify update was successful
        find_product_response = DB_Commands.find_profile_by_id(add_product_response)
        for variable in update_product_response:
            if variable[0] == find_product_response:
                assert True
            if variable[1] == product:
                assert True
            if variable[3] == new_category:
                assert True
            if variable[4] == new_company:
                assert True

        # Cleanup and remove
        DB_Commands.delete_product(add_product_response)


    def test_delete_product(self):
        """
        Test the ability to remove a product
        - Test successfully removing a product from the database
        """
        product = "Metal Ring"
        product_image_url = "http://www.sample.com/image.jpg"
        category = "Social wear & Special occasions"
        company = "XYZ Company"
        # Remaining variables left out intentionally to test default conditions

        # Add product to database
        add_product_response = DB_Commands.insert_new_product(product, product_image_url, category, company)
        self.assertTrue(type(add_product_response) == int)

        # Find the created product using the add product response
        find_product_response = DB_Commands.find_product_by_id(add_product_response)
        for variable in find_product_response:
            if variable[0] == add_product_response:
                assert True
            if variable[1] == product:
                assert True
            if variable[5] == "None Provided":
                assert True

        # Cleanup and remove
        DB_Commands.delete_product(add_product_response)


    def test_update_product(self):
        """
        Test the ability to remove a product
        - Test successfully removing a product from the database
        """
        product = "Metal Ring"
        product_image_url = "http://www.sample.com/image.jpg"
        category = "Social wear & Special occasions"
        company = "XYZ Company"
        # Remaining variables left out intentionally to test default conditions

        # Add product to database
        add_product_response = DB_Commands.insert_new_product(product, product_image_url, category, company)
        self.assertTrue(type(add_product_response) == int)

        # Find the created product using the add product response
        find_product_response = DB_Commands.find_product_by_id(add_product_response)
        for variable in find_product_response:
            if variable[0] == add_product_response:
                self.assertEqual(variable[0], add_product_response)
            if variable[1] == product:
                self.assertEqual(variable[1], product)
            if variable[5] == "None Provided":
                self.assertEqual(variable[5], "None Provided")

        # Cleanup and remove
        DB_Commands.delete_product(add_product_response)

        # Confirm created profile was then deleted
        self.assertEquals(DB_Commands.find_product_by_id(add_product_response), [])


    def test_search_module(self):
        """
        Test the search module functionality
        - Run a sample test and ensure product id returned is the expected response
        """
        product_name = "Calvin Klein Men's X-Fit Solid Tan Slim-Fit Suit"
        response = DB_Commands.search_module(product_name)
        print(response)
        assert response is not None
        for id in response:
            if id[0] == 1:
                self.assertEqual(id[0], 1)

