import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QPlainTextEdit
import sqlite3


# Класс Welcome "welcome_chef.ui"
class Welcome(QDialog): 
	def __init__(self):
		super(Welcome, self).__init__()
		# Загрузка графичского интерфейса
		loadUi("Designer/Chef/welcome_chef.ui", self)
		# Кнопки login и newaccount обращаются к функциям gotologin и gotonewaccout соответственно
		self.login.clicked.connect(self.gotologin)
		self.newaccount.clicked.connect(self.gotonewaccount)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()

		# Обновление столбца user_id в аблице chef (изменение значения на 0)
		sql.execute('UPDATE chef SET user_id = 0')

		db.commit()
		
	# Метод gotologin
	def gotologin(self):
		# Смена окна на то, которое описано в классе Login
		login = Login()
		widget.addWidget(login)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод gotonewaccount
	def gotonewaccount(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()

		# Удаление всех строк в таблице chef, где значения Firstname и Lastname равны NULL
		sql.execute("DELETE FROM chef WHERE Firstname IS NULL AND Lastname IS NULL")

		db.commit()


		# Смена окна на то, которое описано в классе Signup
		newaccount = Signup()
		widget.addWidget(newaccount)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Signup "signup_chef.ui"
class Signup(QDialog):
	def __init__(self):
		super(Signup, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Chef/signup_chef.ui", self)
		# Кнопки signup, back, функции signupfunction и backfunction
		self.signup.clicked.connect(self.signupfunction)
		self.back.clicked.connect(self.backfunction)


		# Поля ввода пароля password_edit и confirm_password_edit делаем точками
		self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
		self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Welcome
		b = Welcome()
		widget.addWidget(b)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод signupfunction
	def signupfunction(self):
		user = self.username_edit.text()
		password = self.password_edit.text()
		confirmpassword = self.confirm_password_edit.text()


		# Проверка заполнения логина, пароля или подтверждения пароля
		if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
			# Вывод в error ошибку (Please fill in all fields)
			self.error.setText("Please fill in all fields")


		# Проверка соответствия пароля и подтверждения пароля
		elif password != confirmpassword:
			# Вывод в error ошибку (Passwords don't match)
			self.error.setText("Passwords don't match")


		# Минимальное количество знаков в пароле - 5
		elif len(password) <= 4:
			# Вывод в error ошибку (Password must be more than 4 symbols)
			self.error.setText("Password must be more than 4 symbols")


		else:
			# Подключение БД server.db
			db = sqlite3.connect('SQL/server.db')
			sql = db.cursor()


			# Создание таблицы chef, если такой нет
			sql = db.execute("""CREATE TABLE IF NOT EXISTS chef (
			'user_id' INTEGER DEFAULT 0,
			'Username' TEXT,
			'Password' TEXT,
			'Firstname' TEXT,
			'Lastname' TEXT
			)""")
			
			db.commit()


			user_info = [user, password]


			# Выбираем из таблицы chef Username, где Username = user
			sql.execute(f"SELECT Username FROM chef WHERE Username = '{user}'")


			# Если такого Username нет, то записываем Username и Password в таблицу
			if sql.fetchone() is None:
				sql.execute('INSERT INTO chef (Username, Password) VALUES (?, ?)', user_info)

				db.commit()


				# Смена окна на то, которое описано в классе Fillprofile
				fillprofile = Fillprofile()
				widget.addWidget(fillprofile)
				widget.setCurrentIndex(widget.currentIndex() + 1)


			# Если такой Username уже есть в таблице в error выводится ошибка (This username already exists)
			else:
				self.error.setText("This username already exists")


# Класс Login "login_chef.ui"
class Login(QDialog):
	def __init__(self):
		super(Login, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Chef/login_chef.ui", self)
		# Кнопки login и back, функции loginfunction и backfunction
		self.login.clicked.connect(self.loginfunction)
		self.back.clicked.connect(self.backfunction)


		# Поля ввода пароля password_edit делаем точками
		self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Welcome
		b = Welcome()
		widget.addWidget(b)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод loginfunction
	def loginfunction(self):
		user = self.username_edit.text()
		password = self.password_edit.text()


		# Проверка заполнения обоих полей (username, password)
		if len(user) == 0 or len(password) == 0:
			# Вывод ошибки в error (Please input all fields)
			self.error.setText("Please input all fields")

			
		else:
			

			# Проверка на ошибку в программе
			try:
				# Подключение БД server.db
				db = sqlite3.connect("SQL/server.db")
				sql = db.cursor()


				# Выборка password из таблицы chef, где Username = user
				query = 'SELECT Password FROM chef WHERE Username = \'' + user + "\'"
				sql.execute(query)
				result_pass = sql.fetchone()[0]

				db.commit()


				# Проверка правильности пароля соответствующий данному username'у
				if result_pass == password:


					# Присвоение user_id единицу в таблице chef, где Username = user
					sql.execute('UPDATE chef SET user_id = 1 WHERE Username = \'' + user + "\'")

					db.commit()


					# Смена окна на то, которое описано в классе Chef
					chef = Chef()
					widget.addWidget(chef)
					widget.setCurrentIndex(widget.currentIndex() + 1)


				# Пароль неверный - выводит ошибку в поле error (Invalid username or password)
				else:
					self.error.setText("Invalid username or password")
			# Ошибка в части try - выводит ошибку в поле error (Invalid username or password)
			except:
				self.error.setText("Invalid username or password")


# Класс Fillprofile "fillprofile_chef.ui"
class Fillprofile(QDialog):
	def __init__(self):
		super(Fillprofile, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Chef/fillprofile_chef.ui", self)
		# Кнопки back и continue_button, функции backfunction и continuefunction
		self.back.clicked.connect(self.backfunction)
		self.continue_button.clicked.connect(self.continuefunction)


		# Делаем поле ввода username_edit неактивным
		self.username_edit.setEnabled(False)


		# Подключение БД server.db
		db = sqlite3.connect("SQL/server.db")
		sql = db.cursor()


		# Выборка Usename из таблицы chef отсортированного по rowid в порядке убывания
		sql.execute('SELECT Username FROM chef ORDER BY rowid DESC LIMIT 1')


		# Присвоение полю username_edit значение из вышесформированной выборки
		self.username_edit.setText(sql.fetchone()[0])

		db.commit()


	# Метод continuefunction
	def continuefunction(self):
		firstname = self.firstname_edit.text()
		lastname = self.lastname_edit.text()


		# Проверка на заполнение полей firstname_edit и lastname_edit
		if len(firstname) == 0 or len(lastname) == 0:
			# Ошибка (Please fill in all fields)
			self.error.setText("Please fill in all fields")


		else:
			name = [firstname, lastname]


			# Подключение БД server.db
			db = sqlite3.connect('SQL/server.db')
			sql = db.cursor()


			# Присвоение полям Firstname и Lastname в  таблице chef значения вписанные пользователем
			sql = db.execute("UPDATE chef SET Firstname = ?, Lastname = ? WHERE Firstname IS NULL AND Lastname IS NULL", name)

			db.commit()


			# Смена окна на то, которое описано в классе Login
			log = Login()
			widget.addWidget(log)
			widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Signup
		b = Signup()
		widget.addWidget(b)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Chef "chef.ui"
class Chef(QDialog):
	def __init__(self):
		super(Chef, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Chef/chef.ui", self)
		# Кнопки logoff, execute и menu, функции logoffunction, execute_function и menufunction
		self.logoff.clicked.connect(self.logoffunction)
		self.execute.clicked.connect(self.execute_function)
		self.menu.clicked.connect(self.menufunction)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка Dishes из таблицы orders_chef
		sql.execute("SELECT Dishes FROM orders_chef")


		# Запись значений из выборки в chef_order
		lab = str(sql.fetchall())
		self.chef_order.setText(lab)

		db.commit()
		

		# Выборка Firstname из таблицы chef, где user_id = 1
		sql.execute('SELECT Firstname FROM chef WHERE user_id = 1')


		# Присвоение значения из выборки в поле first
		one = sql.fetchone()[0]
		self.first.setText(one)

		db.commit()


		# Выборка Lastname из таблицы chef, где user_id = 1
		sql.execute('SELECT Lastname FROM chef WHERE user_id = 1')


		# Присвоение значения из выборки в поле last
		two = sql.fetchone()[0]
		self.last.setText(two)

		db.commit()
		

	# Метод execute_function
	def execute_function(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Запись в таблицу orders_waiter все значения из таблицы orders_chef
		sql.execute('INSERT INTO orders_waiter SELECT * FROM orders_chef')


		# Удаление всех значений в таблице orders_chef
		sql.execute('DELETE FROM orders_chef')

		db.commit()


		# Удаление всего текста в поле chef_order
		self.chef_order.setText("")


	# Метод menufunction
	def menufunction(self):
		# Смена окна на то, которое описано в классе Menu
		menu = Menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод logoffunction
	def logoffunction(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Перезапись всех user_id в таблице chef, присвоение значения 0
		sql.execute('UPDATE chef SET user_id = 0')

		db.commit()


		# Смена окна на то, которое описано в классе Login
		login = Login()
		widget.addWidget(login)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Menu "menu.ui"
class Menu(QDialog):
	def __init__(self):
		super(Menu, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Chef/chef_menu.ui", self)
		# Кнопка back, функция backfunction
		self.back.clicked.connect(self.backfunction)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Chef
		chef = Chef()
		widget.addWidget(chef)
		widget.setCurrentIndex(widget.currentIndex() + 1)


#main
app = QApplication(sys.argv)
welcome = Welcome()
widget = QStackedWidget()
widget.addWidget(welcome)
# Фиксированные размеры окон
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")