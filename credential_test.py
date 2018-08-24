import unittest
from credential import User

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each test case
        '''
        self.new_user = User("Eddie","Mutugi","pdrfg")

    def test_init(self):
        '''
        test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.f_name,"Eddie")
        self.assertEqual(self.new_user.l_name,"Mutugi")
        self.assertEqual(self.new_user.password,"pdrfg")
    def test_save_user(self):
        '''
        test that saves the new user object
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()

