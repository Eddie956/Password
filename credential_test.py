import unittest
import pyperclip

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
    def tearDown(self):
        '''
        it cleans up after the testcase 
        '''
        User.user_list = []
        Credential.credential_list = []
    def test_save_multiple_credential(self):
        '''
        test if multiple credential data is saved into the contact list
        '''
        self.new_credential.save_credential()
        pinterest = Credential("Artjim", "pinterest", "pdrfg3")
        pinterest.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
    def test_display_credential(self):
        '''
        test to check if al credential are displayed 
        '''
        self.new_credential.save_credential()
        pinterest = Credential("Artjim", "pinterest", "pdrfg3")
        pinterest.save_credential()
        self.assertEqual(len(Credential.display_credential(pinterest.user_name)),2)
    def test_find_by_account_name(self):
        '''
        test to check if we can find an account  and display information
        '''
        self.new_credential.save_credentials()
        pinterest = Credential("Artjim", "pinterest", "pdrfg3")
        pinterest.save_credential()
        found_account = Credential.find_by_account_name("pinterest")
        self.assertEqual(found_account,pinterest)
    def test_credential_exists(self):
        '''
        test to check if we can return a Bolean if we canot find the credential
        '''
        self.new_credential.save_credential()
        pinterest = Credential("Artjim", "pinterest", "pdrfg3")
        pinterest.save_credential()

        credential_exists = Credential.account_name_exists("pinterest")

        self.assertTrue(account_name_exists)
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.asertEqual(Credential.display_credential(),Credential.credential_list)
    def test_copy_credential(self):
        '''
        Test to check if the copied the correct credential
        '''
        self.new_credential.save_credential()
        pinterest = Credential("Artjim", "pinterest", "pdrfg3")
        pinterest.save_credential()
        find_credential = None
        for credential in Credential.user_credential_list:
            find_credential = Credential.find_by_account_name(credential.account_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.account_name)
        self.assertEqual('pdrfg3'pyperclip.paste())
        print(pyperclip.paste())
        
if __name__ == '__main__':
    unittest.main()

