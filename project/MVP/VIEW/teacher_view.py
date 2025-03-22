import customtkinter as ctk
from MVP.PRESENTER.teacher_presenter import TeacherPRESENTER
from tkinter import ttk



class TeacherVIEW(ctk.CTk):
	def __init__(self, teacher_id):
		super().__init__()

		self.geometry('800x600')

		self.teacher_presenter = TeacherPRESENTER()

		self.navigate_frame = ctk.CTkFrame(self)
		self.navigate_frame.pack(side = 'left', fill = 'y')

		self.course_button = ctk.CTkButton(self.navigate_frame, text = 'Курсы', command = self.open_courses)
		self.course_button.pack(pady = 5)

		self.journal_button = ctk.CTkButton(self.navigate_frame, text = 'Ведомость', command = self.open_enrollments)
		self.journal_button.pack(pady = 5)

		self.main_frame = ctk.CTkFrame(self)
		self.main_frame.pack(fill = 'both', expand = True)

		self.this_tree = None
		self.teacher_id = teacher_id

	def open_courses(self):
		if self.this_tree != None:
			for widget in self.main_frame.winfo_children():
				widget.pack_forget()

		courses = self.teacher_presenter.get_courses(self.teacher_id)

		tree = ttk.Treeview(self.main_frame, columns = ('id', 'title', 'description'), show = 'headings')
		tree.heading('id', text = 'ID')
		tree.heading('title', text = 'Титул')
		tree.heading('description', text = 'Описание')
		tree.column('id', width = 50, anchor = 'center')
		tree.column('title', width = 50, anchor = 'center')
		tree.column('description', width = 50, anchor = 'center')

		tree.delete(*tree.get_children())
		for row in courses:
			tree.insert("", "end", values = row)

		self.this_tree = tree 
		tree.pack(side = 'left', fill = 'both', expand = True)

	def open_enrollments(self):
		if self.this_tree != None:
			for widget in self.main_frame.winfo_children():
				widget.pack_forget()

		enrollments = self.teacher_presenter.get_enrollments(self.teacher_id)
		
		tree = ttk.Treeview(self.main_frame, columns = ('id', 'student_name', 'course_title', 'grade'), show = 'headings')
		tree.heading('id', text = 'ID')
		tree.heading('student_name', text = 'Студент')
		tree.heading('course_title', text = 'Курс')
		tree.heading('grade', text = 'Оценка')
		tree.column('id', width = 50, anchor = 'center')
		tree.column('student_name', width = 50, anchor = 'center')
		tree.column('course_title', width = 50, anchor = 'center')
		tree.column('grade', width = 50, anchor = 'center')

		tree.delete(*tree.get_children())
		for row in enrollments:
			tree.insert("", "end", values = row)

		tree.bind("<Double-1>", self.open_set_grade_window)
		self.this_tree = tree 
		tree.pack(side = 'left', fill = 'both', expand = True)

	def open_set_grade_window(self, event):
		selected_item = self.this_tree.selection()
		if selected_item:
			data = self.this_tree.item(selected_item, 'values')

			enrollment_id = int(data[0])

			window = ctk.CTkToplevel()
			window.geometry('200x300')

			grade_label = ctk.CTkLabel(window, text = 'Оценка')
			grade_label.pack()

			grade_entry = ctk.CTkEntry(window)
			grade_entry.pack()

			save_button = ctk.CTkButton(window, text = 'Сохранить', command = lambda: self.set_grade(enrollment_id,grade_entry.get()))
			save_button.pack(side = 'bottom', pady = 15)

	def set_grade(self, enrollment_id, grade):
		self.teacher_presenter.set_grade(enrollment_id, grade)
		self.open_enrollments()
