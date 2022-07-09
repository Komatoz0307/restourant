import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import sqlite3


# Класс Welcome "welcome_waiter.ui"
class Welcome(QDialog): 
	def __init__(self):
		super(Welcome, self).__init__()
		# Загрузка графичского интерфейса
		loadUi("Designer/Waiter/welcome_waiter.ui", self)
		# Кнопки login и newaccount обращаются к функциям gotologin и gotonewaccout соответственно
		self.login.clicked.connect(self.gotologin)
		self.newaccount.clicked.connect(self.gotonewaccount)


		# Подключение БД sever.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Удаление всех строк в таблице waiter, где значения Firstname и Lastname равны NULL
		sql.execute("DELETE FROM waiter WHERE Firstname IS NULL AND Lastname IS NULL")
		
		db.commit()
		

	# Метод gotologin
	def gotologin(self):
		# Смена окна на то, которое описано в классе Login
		login = Login()
		widget.addWidget(login)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод gotonewaccout
	def gotonewaccount(self):
		# Смена окна на то, которое описано в классе Signup
		newaccount = Signup()
		widget.addWidget(newaccount)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Signup "signup_waiter.ui"
class Signup(QDialog):
	def __init__(self):
		super(Signup, self).__init__()
		# Загрузка графичского интерфейса
		loadUi("Designer/Waiter/signup_waiter.ui", self)
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

			# Создание таблицы waiter, если такой нет
			sql = db.execute("""CREATE TABLE IF NOT EXISTS waiter (
			'user_id' INTEGER DEFAULT 0,
			'Username' TEXT,
			'Password' TEXT,
			'Firstname' TEXT,
			'Lastname' TEXT
			)""")
			
			db.commit()


			user_info = [user, password]


			# Выбираем из таблицы waiter Username, где Username = user
			sql.execute(f"SELECT Username FROM waiter WHERE Username = '{user}'")


			# Если такого Username нет, то записываем Username и Password в таблицу
			if sql.fetchone() is None:
				sql.execute('INSERT INTO waiter (Username, Password) VALUES (?, ?)', user_info)

				db.commit()


				# Смена окна на то, которое описано в классе Fillprofile
				fillprofile = Fillprofile()
				widget.addWidget(fillprofile)
				widget.setCurrentIndex(widget.currentIndex() + 1)


			# Если такой Username уже есть в таблице в error выводится ошибка (This username already exists)
			else:
				self.error.setText("This username already exists")


# Класс Login "login_waiter.ui"
class Login(QDialog):
	def __init__(self):
		super(Login, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Waiter/login_waiter.ui", self)
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


				# Выборка password из таблицы waiter, где Username = user
				query = 'SELECT Password FROM waiter WHERE Username = \'' + user + "\'"
				sql.execute(query)
				result_pass = sql.fetchone()[0]

				db.commit()


				# Проверка правильности пароля соответствующий данному username'у
				if result_pass == password:


					# Присвоение user_id единицу в таблице admin, где Username = user
					sql.execute('UPDATE waiter SET user_id = 1 WHERE Username = \'' + user + "\'")

					db.commit()
					

					# Смена окна на то, которое описано в классе Waiter
					waiter = Waiter()
					widget.addWidget(waiter)
					widget.setCurrentIndex(widget.currentIndex() + 1)


				# Пароль неверный - выводит ошибку в поле error (Invalid username or password)
				else:
					self.error.setText("Invalid username or password")
			# Ошибка в части try - выводит ошибку в поле error (Invalid username or password)
			except:
				self.error.setText("Invalid username or password")


# Класс Fillprofile "fillprofile_admin.ui"
class Fillprofile(QDialog):
	def __init__(self):
		super(Fillprofile, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Waiter/fillprofile_waiter.ui", self)
		# Кнопки back и continue_button, функции backfunction и continuefunction
		self.back.clicked.connect(self.backfunction)
		self.continue_button.clicked.connect(self.continuefunction)


		# Делаем поле ввода username_edit неактивным
		self.username_edit.setEnabled(False)


		# Подключение БД server.db
		db = sqlite3.connect("SQL/server.db")
		sql = db.cursor()


		# Выборка Usename из таблицы waiter отсортированного по rowid в порядке убывания
		sql.execute('SELECT Username FROM waiter ORDER BY rowid DESC LIMIT 1')


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


			# Присвоение полям Firstname и Lastname в  таблице waiter значения вписанные пользователем
			sql = db.execute("UPDATE waiter SET Firstname = ?, Lastname = ? WHERE Firstname IS NULL AND Lastname IS NULL", name)

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


# Класс Waiter "waiter.ui"
class Waiter(QDialog):
	def __init__(self):
		super(Waiter, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Waiter/waiter.ui", self)
		# Кнопки logoff, execute, функции logoffunction, execute_function
		self.logoff.clicked.connect(self.logoffunction)
		self.execute.clicked.connect(self.execute_function)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка Dishes из таблицы orders_waiter
		sql.execute("SELECT Dishes FROM orders_waiter")


		# Присвоение значения из выборки в поле waiter_order
		lab = str(sql.fetchall())
		self.waiter_order.setText(lab)

		db.commit()


		# Выборка Firstname из таблицы waiter , где user_id = 1
		sql.execute('SELECT Firstname FROM waiter WHERE user_id = 1')


		# Присвоение значения из выборки в поле first
		one = sql.fetchone()[0]
		self.first.setText(one)

		db.commit()


		# Выборка Lastname из таблицы waiter , где user_id = 1
		sql.execute('SELECT Lastname FROM waiter WHERE user_id = 1')


		# Присвоение значения из выборки в поле last
		two = sql.fetchone()[0]
		self.last.setText(two)

		db.commit()


		# Обновление всех полей в таблице waiter (Присвоение user_id значение 0)
		sql.execute('UPDATE waiter SET user_id = 0')

		db.commit()


	# Метод execute_function
	def execute_function(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Удаление всех полей из таблицы orders_waiter
		sql.execute('DELETE FROM orders_waiter')

		db.commit()


		# Присвоение полю waiter_order пустое значение
		self.waiter_order.setText("")

		
	# Метод logoffunction
	def logoffunction(self):
		# Смена окна на то, которое описано в классе Login
		login = Login()
		widget.addWidget(login)
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