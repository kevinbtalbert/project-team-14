import unittest
from main import hello

class TestMethods(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello World!")

if __name__ == '__main__':
    unittest.main()