import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
import sqlite3

# hello world
# Класс Welcome "welcome_admin.ui"
class Welcome(QDialog): 
	def __init__(self):
		super(Welcome, self).__init__()
		# Загрузка графичского интерфейса
		loadUi("Designer/Admin/welcome_admin.ui", self)
		# Кнопки login и newaccount обращаются к функциям gotologin и gotonewaccout соответственно
		self.login.clicked.connect(self.gotologin)
		self.newaccount.clicked.connect(self.gotonewaccount)


		# Подключение БД server.db
		db = sqlite3.connect("SQL/server.db")
		sql = db.cursor()


		# Перезапись всех значений user_id в таблице admin на 0
		sql.execute('UPDATE admin SET user_id = 0')

		db.commit()


		# Создание таблицы storage
		sql = db.execute("""CREATE TABLE IF NOT EXISTS storage (
			product TEXT,
			col INTEGER
			)""")

		db.commit()


	# Метод gotologin
	def gotologin(self):
		# Смена окна на то, которое описано в классе Login
		login = Login()
		widget.addWidget(login)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод gotonewaccout
	def gotonewaccount(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Удаление всех строк в таблице admin, где значения Firstname и Lastname равны NULL
		sql.execute("DELETE FROM admin WHERE Firstname IS NULL AND Lastname IS NULL")

		db.commit()


		# Смена окна на то, которое описано в классе Signup
		newaccount = Signup()
		widget.addWidget(newaccount)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Signup "signup_admin.ui"
class Signup(QDialog):
	def __init__(self):
		super(Signup, self).__init__()
		# Загрузка графичского интерфейса
		loadUi("Designer/Admin/signup_admin.ui", self)
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


			# Создание таблицы admin, если такой нет
			sql = db.execute("""CREATE TABLE IF NOT EXISTS admin (
			'user_id' INTEGER DEFAULT 0,
			'Username' TEXT,
			'Password' TEXT,
			'Firstname' TEXT,
			'Lastname' TEXT
			)""")
			
			db.commit()


			user_info = [user, password]


			# Выбираем из таблицы admin Username, где Username = user
			sql.execute(f"SELECT Username FROM admin WHERE Username = '{user}'")


			# Если такого Username нет, то записываем Username и Password в таблицу
			if sql.fetchone() is None:
				sql.execute('INSERT INTO admin (Username, Password) VALUES (?, ?)', user_info)

				db.commit()


				# Смена окна на то, которое описано в классе Fillprofile
				fillprofile = Fillprofile()
				widget.addWidget(fillprofile)
				widget.setCurrentIndex(widget.currentIndex() + 1)


			# Если такой Username уже есть в таблице в error выводится ошибка (This username already exists)
			else:
				self.error.setText("This username already exists")


# Класс Login "login_admin.ui"
class Login(QDialog):
	def __init__(self):
		super(Login, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Admin/login_admin.ui", self)
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


				# Выборка password из таблицы admin, где Username = user
				query = 'SELECT Password FROM admin WHERE Username = \'' + user + "\'"
				sql.execute(query)
				result_pass = sql.fetchone()[0]

				db.commit()


				# Проверка правильности пароля соответствующий данному username'у
				if result_pass == password:

					
					# Присвоение user_id единицу в таблице admin, где Username = user
					sql.execute('UPDATE admin SET user_id = 1 WHERE Username = \'' + user + "\'")

					db.commit()
					

					# Смена окна на то, которое описано в классе Admin
					admin = Admin()
					widget.addWidget(admin)
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
		loadUi("Designer/Admin/fillprofile_admin.ui", self)
		# Кнопки back и continue_button, функции backfunction и continuefunction
		self.back.clicked.connect(self.backfunction)
		self.continue_button.clicked.connect(self.continuefunction)


		# Делаем поле ввода username_edit неактивным
		self.username_edit.setEnabled(False)


		# Подключение БД server.db
		db = sqlite3.connect("SQL/server.db")
		sql = db.cursor()


		# Выборка Usename из таблицы admin отсортированного по rowid в порядке убывания
		sql.execute('SELECT Username FROM admin ORDER BY rowid DESC LIMIT 1')


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


			# Присвоение полям Firstname и Lastname в  таблице admin значения вписанные пользователем
			sql = db.execute("UPDATE admin SET Firstname = ?, Lastname = ? WHERE Firstname IS NULL AND Lastname IS NULL", name)

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


# Класс Admin "admin.ui"
class Admin(QDialog):
	def __init__(self):
		super(Admin, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Admin/admin.ui", self)
		# Кнопки logoff, storage и menu_on_day, функции logoffunction, storagefunction и menu_on_day_function
		self.logoff.clicked.connect(self.logoffunction)
		self.storage.clicked.connect(self.storagefunction)
		self.menu_on_day.clicked.connect(self.menu_on_day_function)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка Firstname из таблицы admin, где user_id = 1
		sql.execute('SELECT Firstname FROM admin WHERE user_id = 1')


		# Присвоение значения из выборки в поле first
		one = sql.fetchone()[0]
		self.first.setText(one)

		db.commit()


		# Выборка Lastname из таблицы admin, где user_id = 1
		sql.execute('SELECT Lastname FROM admin WHERE user_id = 1')


		# Присвоение значения из выборки в поле last
		two = sql.fetchone()[0]
		self.last.setText(two)

		db.commit()


		# Выборка Finall_price из таблицы Gain отсортированного в порядке убывания			
		sql.execute("SELECT Finall_price FROM Gain ORDER BY ID ASC LIMIT 1")


		# Присвоение значения из выборки в поле finallprice
		sq = str(sql.fetchone()[0])
		self.finallprice.setText(sq + " ₽")
		
		db.commit()

		
	# Метод menu_on_day_function
	def menu_on_day_function(self):
		# Смена окна на то, которое описано в классе Add
		add = Add()
		widget.addWidget(add)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод storagefunction
	def storagefunction(self):
		# Смена окна на то, которое описано в классе Storage
		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)

		
	# Метод logoffunction
	def logoffunction(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Обновление всех полей в таблице admin (Присвоение user_id значение 0)
		sql.execute('UPDATE admin SET user_id = 0')

		db.commit()


		# Смена окна на то, которое описано в классе Login
		login = Login()
		widget.addWidget(login)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Storage "storage.ui"
class Storage(QDialog):
	def __init__(self):
		super(Storage, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Admin/storage.ui", self)
		# Кнопка back, add_1 - add_11, функции backfunction, add_1_function - add_11_function
		self.back.clicked.connect(self.backfunction)
		self.add_1.clicked.connect(self.add_1_function)
		self.add_2.clicked.connect(self.add_2_function)
		self.add_3.clicked.connect(self.add_3_function)
		self.add_4.clicked.connect(self.add_4_function)
		self.add_5.clicked.connect(self.add_5_function)
		self.add_6.clicked.connect(self.add_6_function)
		self.add_7.clicked.connect(self.add_7_function)
		self.add_8.clicked.connect(self.add_8_function)
		self.add_9.clicked.connect(self.add_9_function)
		self.add_10.clicked.connect(self.add_10_function)
		self.add_11.clicked.connect(self.add_11_function)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка col в таблице storage, где product = "Овощи"	
		sql.execute('SELECT col FROM storage WHERE product = "Овощи"')
		vegetables = str(sql.fetchone()[0])
		# Присвоение значени из выборки полю l_1
		self.l_1.setText(vegetables)


		sql.execute('SELECT col FROM storage WHERE product = "Фрукты"')
		fruits = str(sql.fetchone()[0])
		self.l_2.setText(fruits)


		sql.execute('SELECT col FROM storage WHERE product = "Мясо"')
		meat = str(sql.fetchone()[0])
		self.l_3.setText(meat)


		sql.execute('SELECT col FROM storage WHERE product = "Рыба"')
		fish = str(sql.fetchone()[0])
		self.l_4.setText(fish)


		sql.execute('SELECT col FROM storage WHERE product = "Морепродукты"')
		seafood = str(sql.fetchone()[0])
		self.l_5.setText(seafood)


		sql.execute('SELECT col FROM storage WHERE product = "Пиво"')
		beer = str(sql.fetchone()[0])
		self.l_6.setText(beer)


		sql.execute('SELECT col FROM storage WHERE product = "Чай"')
		tea = str(sql.fetchone()[0])
		self.l_7.setText(tea)


		sql.execute('SELECT col FROM storage WHERE product = "Кофе"')
		coffee = str(sql.fetchone()[0])
		self.l_8.setText(coffee)


		sql.execute('SELECT col FROM storage WHERE product = "Орехи"')
		nuts = str(sql.fetchone()[0])
		self.l_9.setText(nuts)


		sql.execute('SELECT col FROM storage WHERE product = "Шоколад"')
		chocolate = str(sql.fetchone()[0])
		self.l_10.setText(chocolate)


		sql.execute('SELECT col FROM storage WHERE product = "Молоко"')
		milk = str(sql.fetchone()[0])
		self.l_11.setText(milk)
		
		db.commit()


	# Метод add_1_function
	def add_1_function(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		# Обновление поля col в таблице storage, где product = "Овощи", присвоение ему + 100
		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Овощи"')
		
		db.commit()


		# Обновление окна
		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_2_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Фрукты"')
		
		db.commit()
		

		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_3_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
		

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Мясо"')
		
		db.commit()
		

		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_4_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Рыба"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_5_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Морепродукты"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_6_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Пиво"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_7_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Чай"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_8_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Кофе"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_9_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Орехи"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_10_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()

			
		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Шоколад"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	def add_11_function(self):
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()
			

		sql.execute('UPDATE storage SET col = col + 100 WHERE product == "Молоко"')
		
		db.commit()


		storage = Storage()
		widget.addWidget(storage)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Admin
		admin = Admin()
		widget.addWidget(admin)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Add "add.ui"
class Add(QDialog):
	def __init__(self):
		super(Add, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Admin/add.ui", self)
		# Кнопка back, функция backfunction
		self.back.clicked.connect(self.backfunction)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Admin
		admin = Admin()
		widget.addWidget(admin)
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