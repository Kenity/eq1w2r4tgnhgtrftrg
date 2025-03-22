from MVP.MODEL.teacher_crud import TeacherCRUD 


class TeacherPRESENTER:
	def __init__(self):

		self.teacher_crud = TeacherCRUD()

	def get_courses(self, teacher_id):
		result = self.teacher_crud.get_courses(teacher_id)
		return result

	def get_enrollments(self, teacher_id):
		result = self.teacher_crud.get_enrollments(teacher_id)
		return result

	def set_grade(self, enrollment_id, grade):
		self.teacher_crud.set_grade(enrollment_id, grade)