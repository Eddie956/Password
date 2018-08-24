import unittest
from credential import User

class TestUser(unittest.TestCase1):
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

if __name__ == '__main__':
    unittest.main()

