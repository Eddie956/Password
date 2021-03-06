import pyperclip
import string
import random
class User:

	users_list = []

	def __init__(self,f_name,l_name,password):
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
		for credential in  cls.credential_list:
			if credential.account_name == account_name:
				return credential
	@classmethod
	def account_exist(cls,account_name):
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

	@classmethod
	def checking_user(cls, f_name, password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if user.f_name == f_name and user.password == password:
				current_user = user.f_name
		return current_user

	def generate_password(self,size=8,char=string.ascii_uppercase+string.ascii_lowercase):
		'''
		function to generate a new pasword for the user
		'''
		generate_password ='' .join(random.choice(char) for _ in range(size))
		return generate_password
