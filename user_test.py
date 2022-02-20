import unittest
from user import User
class TestUser(unittest.TestCase):
    """
    test class for creating test cases
    """

    def setUp(self):
        """
        this method carries instructions of what is to be done"""

    def tearDown(self):
        """ this is used to reset the test cases"""    

        self.new_user=User("twitter", "beliot","password","password")

        def test_init(self):
            """this is used to test the initialization"""

            self.assertEqual(self.new_user.account_name,"twitter")
            self.assertEqual(self.new_user.username,"beliot")
            self.assertEqual(self.new_user.password,"password")
            self.assertEqual(self.new_user.confirm_password,"password")
