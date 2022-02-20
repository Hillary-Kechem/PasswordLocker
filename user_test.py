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
        
        def test_save_detail(self):
            """
            the test_save_detail checks if the detail is saved in the details
            """
            self.new_user.save_detail()
            self.assertEqual(len(User.user_detail),1)

        def test_save_multiple_detail(self):
            """
            method that checks if we can save multiple details
            """
            self.new_user.save_detail()
            test_user=User("Test","user","password","password")
            test_user.save_detail()
            self.assertEqual(len(User.user_detail),3)

        def test_display_all_details(self):
            """ this method returns a list of account details"""
            self.assertEqual(User.display_all_details(),User.user_detail)

        if __name__== '__main__':
            unittest.main()
