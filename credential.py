
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
	
