import sqlite3
from MVP.COGS.find_DataBase import FindDB


class TeacherCRUD:
	def __init__(self):
	
		self.db_path = FindDB().find_database_path()

		try:
			connect = sqlite3.connect(self.db_path)
			print('База данных успешно подключена. TeacherCRUD')
			connect.close()
		except:
			print('База данных не найдена!')

	def get_courses(self, teacher_id):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		cursor.execute("SELECT * FROM courses WHERE teacher_id = ?", (teacher_id,))

		result = cursor.fetchall()

		connect.close()

		return result

	def get_enrollments(self, teacher_id):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		result = cursor.execute(
    		"SELECT enrollments.id, students.name, courses.title, enrollments.grade "
    		"FROM enrollments "
    		"JOIN students ON enrollments.student_id = students.id "  # Corrected join condition
    		"JOIN courses ON enrollments.course_id = courses.id "  # Corrected join condition
    		"WHERE courses.teacher_id = ?", (teacher_id,)
		)
		result = cursor.fetchall()

		return result

		connect.close()

	def set_grade(self, enrollment_id, grade):
		connect = sqlite3.connect(self.db_path)
		cursor = connect.cursor()

		cursor.execute("UPDATE enrollments SET grade = ? WHERE id = ?", (grade, enrollment_id))

		connect.commit()
		connect.close()
