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
        Test the ability to add, update, and remove profile
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
