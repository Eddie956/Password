
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
