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

class TestCredential(unittest.TestCase):
    def setup(self):
        '''
        setup method to run before each test case
        '''
        self.new_credential = Credential("Artjim","pinterest","pdrfg3")
    def __init__(self):
        '''
        test if the objects setup are propery initialized
        '''
        self.assertEqual(self.new_credential.user_name,"Artjim")
        self.assertEqual(self.new_credential.acount_name,"pinterest")
        self.assertEqual(self.new_credential.password, "pinterest")
    def test_save_credential(self):
        '''
        test if the credential data is saved into the contact list
        '''
        self.new_credential.save_credential()
        pinterest = Credential("Artjim", "pinterest", "pdrfg3")
        pinterest.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
if __name__ == '__main__':
    unittest.main()

