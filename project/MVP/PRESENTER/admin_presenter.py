from MVP.MODEL.admin_crud import AdminCRUD


class AdminPRESENTER:
	def __init__(self):
		self.admin_crud = AdminCRUD()

	def get_users(self):
		users = self.admin_crud.get_users()
		return users

	def get_students(self):
		students = self.admin_crud.get_students()
		return students

	def add_user(self, username, password, role):
		self.admin_crud.add_user(username, password, role)

	def add_student(self, id, name, age, phone):
		self.admin_crud.add_student(id, name, age, phone)

