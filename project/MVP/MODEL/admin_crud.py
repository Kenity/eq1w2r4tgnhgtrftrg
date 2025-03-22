import sqlite3
from MVP.COGS.find_DataBase import FindDB


class AdminCRUD:
	def __init__(self):
		self.db_path = FindDB().find_database_path()

		try:
			connect = sqlite3.connect(self.db_path)
			print('База данных успешно подключена. AdminCRUD')
			connect.close()
		except:
			print('База данных не найдена!')

	def get_users(self):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		cursor.execute("SELECT * FROM users")

		result = cursor.fetchall()

		connect.close()

		return result

	def get_students(self):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		cursor.execute("SELECT * FROM students")

		result = cursor.fetchall()

		connect.close()

		return result

	def add_user(self, username, password, role):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))

		connect.commit()
		connect.close()

	def add_student(self, id, name, age, phone):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		cursor.execute("INSERT INTO students (id, name, age, phone) VALUES (?, ?, ?, ?)", (id, name, age, phone))

		connect.commit()
		connect.close()



