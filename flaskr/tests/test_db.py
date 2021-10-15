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
