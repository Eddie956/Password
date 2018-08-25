
class User:

	users_list = []

	def __int__(self,f_name,l_name,password):
		'''
		methods that defines properties for each
		'''
		self.f_name = f_name
		self.l_name = l_name
		self.password = password
	def save_user(self):
		'''
		function to save new user
		'''
		User.users_list.append(self)

class Credential:

	credential_list = []

	def __init__(self,user_name,account_name,password):
		'''
		method that defines properties for each
		'''
		self.user_name = user_name
		self.account_name = account_name
		self.password = password
	def save_credential(self):

		'''
		save multiple credential objects in credential list
		'''
		Credential.credential_list.append(self)
	
	@classmethod
	def find_by_acount_name(cls, account_name):
		'''
		Method that takes an acount name that matches the credential details
		'''
		for credentialin cls.credential_list:
			if credential.account_name == account_name:
				return credential
	@classmethod
	def contact_exist(cls,account_name):
		'''
		method that checks if the account exists from the contact list.
		'''
		for credential in cls.credential_list:
			if credential.account_name == account_name:
				return True
		return False
	
	@classmethod
	def display_account_name(cls):
		'''
		method that returns the credential list
		'''
		return cls.credential_list
