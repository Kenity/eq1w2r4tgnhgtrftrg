import customtkinter as ctk
from tkinter import ttk
from MVP.PRESENTER.admin_presenter import AdminPRESENTER


class AdminVIEW(ctk.CTk):
	def __init__(self):
		super().__init__()

		self.geometry('800x600')

		self.admin_presenter = AdminPRESENTER()

		self.navigate_frame = ctk.CTkFrame(self)
		self.navigate_frame.pack(side = 'left', fill = 'y')

		self.student_button = ctk.CTkButton(self.navigate_frame, text = 'Студенты', command = self.open_student)
		self.student_button.pack(pady = 5)

		self.teachers_button = ctk.CTkButton(self.navigate_frame, text = 'Преподаватели')
		self.teachers_button.pack(pady = 5)

		self.user_button = ctk.CTkButton(self.navigate_frame, text = 'Пользователи', command = self.open_user)
		self.user_button.pack(pady = 5)

		self.course_button = ctk.CTkButton(self.navigate_frame, text = 'Курсы')
		self.course_button.pack(pady = 5)

		self.record_button = ctk.CTkButton(self.navigate_frame, text = 'Записи')
		self.record_button.pack(pady = 5)

		self.report_button = ctk.CTkButton(self.navigate_frame, text = 'Отчеты')
		self.report_button.pack(pady = 5)


		self.main_frame = ctk.CTkFrame(self)
		self.main_frame.pack(fill = 'both', expand = True)

		self.this_tree = None

	def open_student(self):
		if self.this_tree != None:
			for widget in self.main_frame.winfo_children():
				widget.pack_forget()

		students = self.admin_presenter.get_students()

		tree = ttk.Treeview(self.main_frame, columns = ('id', 'name', 'age', 'phone'), show = 'headings')
		tree.heading('id', text = 'ID')
		tree.heading('name', text = 'Имя')
		tree.heading('age', text = 'Возраст')
		tree.heading('phone', text = 'Телефон')
		tree.column('id', width = 50, anchor = 'center')
		tree.column('name', width = 50, anchor = 'center')
		tree.column('age', width = 50, anchor = 'center')
		tree.column('phone', width = 50, anchor = 'center')
		
		tree.delete(*tree.get_children())
		for row in students:
			tree.insert("", "end", values = row)

		self.this_tree = tree
		tree.pack(side = 'left', fill = 'both', expand = True)

		add_button = ctk.CTkButton(self.main_frame, text = 'Добавить студента', command = self.open_add_student_window)
		add_button.pack(side = 'bottom', expand = True)

	def open_add_student_window(self):
		window = ctk.CTkToplevel()
		window.geometry('200x400')

		id_label = ctk.CTkLabel(window, text = 'id')
		id_label.pack()

		id_entry = ctk.CTkEntry(window)
		id_entry.pack()

		name_label = ctk.CTkLabel(window, text = 'Имя')
		name_label.pack()

		name_entry = ctk.CTkEntry(window)
		name_entry.pack()

		age_label = ctk.CTkLabel(window, text = 'Возраст')
		age_label.pack()

		age_entry = ctk.CTkEntry(window)
		age_entry.pack()

		phone_label = ctk.CTkLabel(window, text = 'Телефон')
		phone_label.pack()

		phone_entry = ctk.CTkEntry(window)
		phone_entry.pack()

		add_button = ctk.CTkButton(window, text = 'Добавить', command = lambda: self.add_student(id_entry.get(), name_entry.get(), age_entry.get(), phone_entry.get()))
		add_button.pack(pady = 10)

	def add_student(self, id, name, age, phone):
		self.admin_presenter.add_student(id, name, age, phone)
		self.open_student()

	def open_user(self):
		if self.this_tree != None:
			for widget in self.main_frame.winfo_children():
				widget.pack_forget()

		users = self.admin_presenter.get_users()

		tree = ttk.Treeview(self.main_frame, columns = ('id', 'username', 'password', 'role'), show = 'headings')
		tree.heading('id', text = 'ID')
		tree.heading('username', text = 'USERNAME')
		tree.heading('password', text = 'Пароль')
		tree.heading('role', text = 'Роль')
		tree.column('id', width = 50, anchor = 'center')
		tree.column('username', width = 50, anchor = 'center')
		tree.column('password', width = 50, anchor = 'center')
		tree.column('role', width = 50, anchor = 'center')

		tree.delete(*tree.get_children())
		for row in users:
			tree.insert("", "end", values = row)


		self.this_tree = tree
		tree.pack(side = 'left', fill = 'both', expand = True)

		add_button = ctk.CTkButton(self.main_frame, text = 'Добавить пользователя', command = self.open_add_user_window)
		add_button.pack(side = 'bottom', expand = True)

	def open_add_user_window(self):
		window = ctk.CTkToplevel()
		window.geometry('200x400')

		username_label = ctk.CTkLabel(window, text = 'username')
		username_label.pack()

		username_entry = ctk.CTkEntry(window)
		username_entry.pack()

		password_label = ctk.CTkLabel(window, text = 'Пароль')
		password_label.pack()

		password_entry = ctk.CTkEntry(window)
		password_entry.pack()

		role_label = ctk.CTkLabel(window, text = 'Роль')
		role_label.pack()

		role_entry = ctk.CTkEntry(window)
		role_entry.pack()

		add_button = ctk.CTkButton(window, text = 'Добавить', command = lambda: self.add_user(username_entry.get(), password_entry.get(), role_entry.get()))
		add_button.pack(pady = 10)

	def add_user(self, username, password, role):
		self.admin_presenter.add_user(username, password, role)
		self.open_user()

		