import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QPushButton
from PyQt5.QtGui import QPixmap
import sqlite3


# Класс Welcome "welcome_menu.ui"
class Welcome(QDialog):
	def __init__(self):
		super(Welcome, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Menu/welcome_menu.ui", self)
		# Кнопка menubutton, функция enter
		self.menubutton.clicked.connect(self.enter)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Создание таблицы menu, если такой нет
		sql = db.execute("""CREATE TABLE IF NOT EXISTS menu (
		ID INTEGER,
		Dish TEXT,
		Price INTEGER
		)""")


		# Создание таблицы Gain, если такой нет
		sql = db.execute("""CREATE TABLE IF NOT EXISTS Gain (
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		Price INTEGER DEFAULT 0,
		Finall_price INTEGER DEFAULT 0
		)""")


		# Создание таблицы orders_menu, если такой нет
		sql = db.execute("""CREATE TABLE IF NOT EXISTS orders_menu (
		Dishes TEXT
		)""")


		# Создание таблицы orders_chef, если такой нет
		sql = db.execute("""CREATE TABLE IF NOT EXISTS orders_chef (
		Dishes TEXT
		)""")
		

		# Создание таблицы orders_waiter, если такой нет
		sql = db.execute("""CREATE TABLE IF NOT EXISTS orders_waiter (
		Dishes TEXT
		)""")

		db.commit()


	# Метод enter
	def enter(self):
		# Смена окна на то, которое описано в классе Menu
		menu = Menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Menu "menu.ui"
class Menu(QDialog):
	def __init__(self):
		super(Menu, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Menu/menu.ui", self)
		# Кнопки back, buy, pb_1 - pb_54, функции backfunction, buyfunction, orderfunction
		self.back.clicked.connect(self.backfunction)
		self.buy.clicked.connect(self.buyfunction)

		self.pb_1.clicked.connect(lambda: self.orderfunction(self.l_1.text()))
		self.pb_2.clicked.connect(lambda: self.orderfunction(self.l_2.text()))
		self.pb_3.clicked.connect(lambda: self.orderfunction(self.l_3.text()))
		self.pb_4.clicked.connect(lambda: self.orderfunction(self.l_4.text()))
		self.pb_5.clicked.connect(lambda: self.orderfunction(self.l_5.text()))
		self.pb_6.clicked.connect(lambda: self.orderfunction(self.l_6.text()))
		self.pb_7.clicked.connect(lambda: self.orderfunction(self.l_7.text()))
		self.pb_8.clicked.connect(lambda: self.orderfunction(self.l_8.text()))
		self.pb_9.clicked.connect(lambda: self.orderfunction(self.l_9.text()))
		self.pb_10.clicked.connect(lambda: self.orderfunction(self.l_10.text()))
		self.pb_11.clicked.connect(lambda: self.orderfunction(self.l_11.text()))
		self.pb_12.clicked.connect(lambda: self.orderfunction(self.l_12.text()))
		self.pb_13.clicked.connect(lambda: self.orderfunction(self.l_13.text()))
		self.pb_14.clicked.connect(lambda: self.orderfunction(self.l_14.text()))
		self.pb_15.clicked.connect(lambda: self.orderfunction(self.l_15.text()))
		self.pb_16.clicked.connect(lambda: self.orderfunction(self.l_16.text()))
		self.pb_17.clicked.connect(lambda: self.orderfunction(self.l_17.text()))
		self.pb_18.clicked.connect(lambda: self.orderfunction(self.l_18.text()))
		self.pb_19.clicked.connect(lambda: self.orderfunction(self.l_19.text()))
		self.pb_20.clicked.connect(lambda: self.orderfunction(self.l_20.text()))
		self.pb_21.clicked.connect(lambda: self.orderfunction(self.l_21.text()))
		self.pb_22.clicked.connect(lambda: self.orderfunction(self.l_22.text()))
		self.pb_23.clicked.connect(lambda: self.orderfunction(self.l_23.text()))
		self.pb_24.clicked.connect(lambda: self.orderfunction(self.l_24.text()))
		self.pb_25.clicked.connect(lambda: self.orderfunction(self.l_25.text()))
		self.pb_26.clicked.connect(lambda: self.orderfunction(self.l_26.text()))
		self.pb_27.clicked.connect(lambda: self.orderfunction(self.l_27.text()))
		self.pb_28.clicked.connect(lambda: self.orderfunction(self.l_28.text()))
		self.pb_29.clicked.connect(lambda: self.orderfunction(self.l_29.text()))
		self.pb_30.clicked.connect(lambda: self.orderfunction(self.l_30.text()))
		self.pb_31.clicked.connect(lambda: self.orderfunction(self.l_31.text()))
		self.pb_32.clicked.connect(lambda: self.orderfunction(self.l_32.text()))
		self.pb_33.clicked.connect(lambda: self.orderfunction(self.l_33.text()))
		self.pb_34.clicked.connect(lambda: self.orderfunction(self.l_34.text()))
		self.pb_35.clicked.connect(lambda: self.orderfunction(self.l_35.text()))
		self.pb_36.clicked.connect(lambda: self.orderfunction(self.l_36.text()))
		self.pb_37.clicked.connect(lambda: self.orderfunction(self.l_37.text()))
		self.pb_38.clicked.connect(lambda: self.orderfunction(self.l_38.text()))
		self.pb_39.clicked.connect(lambda: self.orderfunction(self.l_39.text()))
		self.pb_40.clicked.connect(lambda: self.orderfunction(self.l_40.text()))
		self.pb_41.clicked.connect(lambda: self.orderfunction(self.l_41.text()))
		self.pb_42.clicked.connect(lambda: self.orderfunction(self.l_42.text()))
		self.pb_43.clicked.connect(lambda: self.orderfunction(self.l_43.text()))
		self.pb_44.clicked.connect(lambda: self.orderfunction(self.l_44.text()))
		self.pb_45.clicked.connect(lambda: self.orderfunction(self.l_45.text()))
		self.pb_46.clicked.connect(lambda: self.orderfunction(self.l_46.text()))
		self.pb_47.clicked.connect(lambda: self.orderfunction(self.l_47.text()))
		self.pb_48.clicked.connect(lambda: self.orderfunction(self.l_48.text()))
		self.pb_49.clicked.connect(lambda: self.orderfunction(self.l_49.text()))
		self.pb_50.clicked.connect(lambda: self.orderfunction(self.l_50.text()))
		self.pb_51.clicked.connect(lambda: self.orderfunction(self.l_51.text()))
		self.pb_52.clicked.connect(lambda: self.orderfunction(self.l_52.text()))
		self.pb_53.clicked.connect(lambda: self.orderfunction(self.l_53.text()))
		self.pb_54.clicked.connect(lambda: self.orderfunction(self.l_54.text()))


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка Price из таблицы Gain, где ID = SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1
		sql.execute("SELECT Price FROM Gain WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
		sq = sql.fetchone()[0]


		# Блокировка кнопки Заказать, если клиент ничего не заказал
		if sq == 0:
			self.buy.setEnabled(False)

		db.commit()


	# Метод buyfunction
	def buyfunction(self):
		# Смена окна на то, которое описано в классе Menu
		pay = Payment()
		widget.addWidget(pay)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод orderfunction
	def orderfunction(self, label):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Удаление всех строк в таблице menu, где ID не равен NULL
		sql.execute("DELETE FROM menu WHERE ID IS NOT NULL")


		# Проверка, если label = 'Куриные крылья с овощами на гриле 380 ₽'
		if label == 'Куриные крылья с овощами на гриле 380 ₽':
			# Вписываем ID = 1 в таблицу menu
			sql.execute('INSERT INTO menu (ID) VALUES (1)')
		elif label == 'Хот-дог с куриной сосиской 380 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (2)')
		elif label == 'Куриные крылья барбекью 470 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (3)')
		elif label == 'Куриный бургер 470 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (4)')
		elif label == 'Куриные стрипсы 490 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (5)')
		elif label == 'Фиш-н-чипс 590 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (6)')
		elif label == 'Коул слоу белый 220 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (7)')
		elif label == 'Кобб салат 480 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (8)')
		elif label == 'Цезарь 480 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (9)')
		elif label == 'Салат с лососем 490 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (10)')
		elif label == 'Салат с розовыми креветками 690 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (11)')
		elif label == 'Салат из овощей 690 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (12)')
		elif label == 'Суп лапша с курицей 290 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (13)')
		elif label == 'Борщ 320 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (14)')
		elif label == 'Куриный бульон с яйцом и тостом 330 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (15)')
		elif label == 'Грибной крем-суп со сливками 340 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (16)')
		elif label == 'Том Ям 490 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (17)')
		elif label == 'Свиные уши с перцем чили 420 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (18)')
		elif label == 'Такос с говядиной и гуакамоле 490 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (19)')
		elif label == 'Начосы с рваной свининой 490 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (20)')
		elif label == 'Начосы с гуакамоле 540 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (21)')
		elif label == 'Креветки в кляре 540 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (22)')
		elif label == 'Морские гады и рыбки в кляре 560 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (23)')
		elif label == 'Запеченный камамбер 590 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (24)')
		elif label == 'Северные креветки жаренные 690 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (25)')
		elif label == 'Северные креветки вареные 690 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (26)')
		elif label == 'Тартар из говядины 690 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (27)')
		elif label == 'Тартар из лосося 790 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (28)')
		elif label == 'Круассан классический 90 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (29)')
		elif label == 'Мороженое карамель с морской солью 120 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (30)')
		elif label == 'Ванильное мороженое 120 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (31)')
		elif label == 'Маффин брусничный 150 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (32)')
		elif label == 'Маффин шоколадный 150 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (33)')
		elif label == 'Миндальный круассан 190 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (34)')
		elif label == 'Эклер фисташковый 210 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (35)')
		elif label == 'Штрудель 290 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (36)')
		elif label == 'Наполеон 290 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (37)')
		elif label == 'Тирамису 290 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (38)')
		elif label == 'Медовик 290 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (39)')
		elif label == 'Чизкейк 340 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (40)')
		elif label == 'Чипсы с солью 120 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (41)')
		elif label == 'Чипсы из говядины 190 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (42)')
		elif label == 'Чипсы из конины 190 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (43)')
		elif label == 'Арахис с васаби 190 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (44)')
		elif label == 'Чипсы из оленины 240 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (45)')
		elif label == 'Фисташки 260 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (46)')
		elif label == 'Капучино 0,2 л.  130 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (47)')
		elif label == 'Американо 0,3 л.  150 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (48)')
		elif label == 'Чай зеленый 0,3 л. 150 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (49)')
		elif label == 'Чай черный 0,3 л. 150 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (50)')
		elif label == 'Флэт уайт 0,2 л.  170 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (51)')
		elif label == 'Латте 0,3 л.  170 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (52)')
		elif label == 'Пиво светлое 0,5 л. 400 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (53)')
		elif label == 'Пиво темное 0,5 л. 400 ₽':
			sql.execute('INSERT INTO menu (ID) VALUES (54)')

		db.commit()


		# Смена окна на то, которое описано в классе Order
		order = Order()
		widget.addWidget(order)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Welcome
		welcome = Welcome()
		widget.addWidget(welcome)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Order "order.ui"
class Order(QDialog):
	def __init__(self):
		super(Order, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Menu/order.ui", self)
		# Кнопки back, add, функции backfunction, addfunction
		self.back.clicked.connect(self.backfunction)
		self.add.clicked.connect(self.addfunction)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка ID из таблицы menu отсортированного по убыванию значения ID
		sql.execute('SELECT ID FROM menu ORDER BY ID DESC LIMIT 1')
		sq = sql.fetchone()[0]

		db.commit()


		# Если sq = 1
		if sq == 1:
			# Выборка Dish из таблицы menu, где Dish = "Куриные крылья с овощами на гриле 380 ₽"
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Куриные крылья с овощами на гриле 380 ₽"')
			# Присвоение полю dish значение вышесформированной выборки
			self.dish.setText(sql.fetchone()[0])
			# Загрузка фотографии 1.jpg полю pixmap
			self.pixmap.setPixmap(QPixmap("jpg/Menu/1.jpg"))
		elif sq == 2:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Хот-дог с куриной сосиской 380 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/2.jpg"))
		elif sq == 3:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Куриные крылья барбекью 470 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/3.jpg"))
		elif sq == 4:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Куриный бургер 470 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/4.jpg"))
		elif sq == 5:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Куриные стрипсы 490 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/5.jpg"))
		elif sq == 6:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Фиш-н-чипс 590 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/6.jpg"))
		elif sq == 7:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Коул слоу белый 220 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/7.jpg"))
		elif sq == 8:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Кобб салат 480 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/8.jpg"))
		elif sq == 9:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Цезарь 480 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/9.jpg"))
		elif sq == 10:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Салат с лососем 490 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/10.jpg"))
		elif sq == 11:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Салат с розовыми креветками 690 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/11.jpg"))
		elif sq == 12:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Салат из овощей 690 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/12.jpg"))
		elif sq == 13:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Суп лапша с курицей 290 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/13.jpg"))
		elif sq == 14:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Борщ 320 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/14.jpg"))
		elif sq == 15:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Куриный бульон с яйцом и тостом 330 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/15.jpg"))
		elif sq == 16:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Грибной крем-суп со сливками 340 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/16.jpg"))
		elif sq == 17:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Том Ям 490 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/17.jpg"))
		elif sq == 18:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Свиные уши с перцем чили 420 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/18.jpg"))
		elif sq == 19:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Такос с говядиной и гуакамоле 490 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/19.jpg"))
		elif sq == 20:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Начосы с рваной свининой 490 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/20.jpg"))
		elif sq == 21:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Начосы с гуакамоле 540 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/21.jpg"))
		elif sq == 22:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Креветки в кляре 540 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/22.jpg"))
		elif sq == 23:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Морские гады и рыбки в кляре 560 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/23.jpg"))
		elif sq == 24:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Запеченный камамбер 590 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/24.jpg"))
		elif sq == 25:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Северные креветки жаренные 690 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/25.jpg"))
		elif sq == 26:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Северные креветки вареные 690 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/26.jpg"))
		elif sq == 27:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Тартар из говядины 690 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/27.jpg"))
		elif sq == 28:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Тартар из лосося 790 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/28.jpg"))
		elif sq == 29:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Круассан классический 90 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/29.jpg"))
		elif sq == 30:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Мороженое карамель с морской солью 120 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/30.jpg"))
		elif sq == 31:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Ванильное мороженое 120 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/31.jpg"))
		elif sq == 32:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Маффин брусничный 150 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/32.jpg"))
		elif sq == 33:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Маффин шоколадный 150 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/33.jpg"))
		elif sq == 34:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Миндальный круассан 190 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/34.jpg"))
		elif sq == 35:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Эклер фисташковый 210 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/35.jpg"))
		elif sq == 36:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Штрудель 290 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/36.jpg"))
		elif sq == 37:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Наполеон 290 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/37.jpg"))
		elif sq == 38:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Тирамису 290 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/38.jpg"))
		elif sq == 39:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Медовик 290 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/39.jpg"))
		elif sq == 40:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чизкейк 340 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/40.jpg"))
		elif sq == 41:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чипсы с солью 120 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/41.jpg"))
		elif sq == 42:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чипсы из говядины 190 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/42.jpg"))
		elif sq == 43:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чипсы из конины 190 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/43.jpg"))
		elif sq == 44:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Арахис с васаби 190 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/44.jpg"))
		elif sq == 45:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чипсы из оленины 240 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/45.jpg"))
		elif sq == 46:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Фисташки 260 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/46.jpg"))
		elif sq == 47:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Капучино 0,2 л.  130 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/47.jpg"))
		elif sq == 48:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Американо 0,3 л.  150 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/48.jpg"))
		elif sq == 49:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чай зеленый 0,3 л. 150 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/49.jpg"))
		elif sq == 50:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Чай черный 0,3 л. 150 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/50.jpg"))
		elif sq == 51:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Флэт уайт 0,2 л.  170 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/51.jpg"))
		elif sq == 52:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Латте 0,3 л.  170 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/52.jpg"))
		elif sq == 53:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Пиво светлое 0,5 л. 400 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/53.jpg"))
		elif sq == 54:
			sql.execute('SELECT Dish FROM menu WHERE Dish == "Пиво темное 0,5 л. 400 ₽"')
			self.dish.setText(sql.fetchone()[0])
			self.pixmap.setPixmap(QPixmap("jpg/Menu/54.jpg"))

		db.commit()


	# Метод addfunction
	def addfunction(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка ID из таблицы menu отсортированного по убыванию значения ID
		sql.execute('SELECT ID FROM menu ORDER BY ID DESC LIMIT 1')
		sq = sql.fetchone()[0]

		db.commit()


		# Если sq = 1
		if sq == 1:
			# Обновляем поле Price (присвоение ему +380) в таблице Gain, где ID = SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1
			sql.execute("UPDATE Gain SET Price = Price + 380 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			# Запись в таблицу orders_menu значения 'Куриные крылья с овощами на гриле 380 ₽'
			sql.execute("INSERT INTO orders_menu VALUES ('Куриные крылья с овощами на гриле 380 ₽')")
			# Обновляем поле col = col - 10 в таблице storage, где product = "Овощи" или product == "Мясо"
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Мясо"')
		elif sq == 2:
			sql.execute("UPDATE Gain SET Price = Price + 380 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Хот-дог с куриной сосиской 380 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 3:
			sql.execute("UPDATE Gain SET Price = Price + 470 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Куриные крылья барбекью 470 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 4:
			sql.execute("UPDATE Gain SET Price = Price + 470 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Куриный бургер 470 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 5:
			sql.execute("UPDATE Gain SET Price = Price + 490 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Куриные стрипсы 490 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 6:
			sql.execute("UPDATE Gain SET Price = Price + 590 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Фиш-н-чипс 590 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо" or product == "Овощи"')
		elif sq == 7:
			sql.execute("UPDATE Gain SET Price = Price + 220 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Коул слоу белый 220 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи"')
		elif sq == 8:
			sql.execute("UPDATE Gain SET Price = Price + 480 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Кобб салат 480 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Орехи"')
		elif sq == 9:
			sql.execute("UPDATE Gain SET Price = Price + 480 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Цезарь 480 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Мясо"')
		elif sq == 10:
			sql.execute("UPDATE Gain SET Price = Price + 490 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Салат с лососем 490 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Рыба"')
		elif sq == 11:
			sql.execute("UPDATE Gain SET Price = Price + 690 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Салат с розовыми креветками 690 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Морепродукты"')
		elif sq == 12:
			sql.execute("UPDATE Gain SET Price = Price + 690 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Салат из овощей 690 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи"')
		elif sq == 13:
			sql.execute("UPDATE Gain SET Price = Price + 290 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Суп лапша с курицей 290 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо" or product == "Овощи"')
		elif sq == 14:
			sql.execute("UPDATE Gain SET Price = Price + 320 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Борщ 320 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо" or product == "Овощи"')
		elif sq == 15:
			sql.execute("UPDATE Gain SET Price = Price + 330 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Куриный бульон с яйцом и тостом 330 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо" or product == "Овощи"')
		elif sq == 16:
			sql.execute("UPDATE Gain SET Price = Price + 340 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Грибной крем-суп со сливками 340 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Молоко"')
		elif sq == 17:
			sql.execute("UPDATE Gain SET Price = Price + 490 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Том Ям 490 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи" or product == "Мясо" or product == "Морепродукты"')
		elif sq == 18:
			sql.execute("UPDATE Gain SET Price = Price + 420 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Свиные уши с перцем чили 420 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 19:
			sql.execute("UPDATE Gain SET Price = Price + 490 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Такос с говядиной и гуакамоле 490 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 20:
			sql.execute("UPDATE Gain SET Price = Price + 490 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Начосы с рваной свининой 490 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 21:
			sql.execute("UPDATE Gain SET Price = Price + 540 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Начосы с гуакамоле 540 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 22:
			sql.execute("UPDATE Gain SET Price = Price + 540 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Креветки в кляре 540 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Морепродукты"')
		elif sq == 23:
			sql.execute("UPDATE Gain SET Price = Price + 560 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Морские гады и рыбки в кляре 560 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Рыба" or product == "Морепродукты"')
		elif sq == 24:
			sql.execute("UPDATE Gain SET Price = Price + 590 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Запеченный камамбер 590 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Молоко"')
		elif sq == 25:
			sql.execute("UPDATE Gain SET Price = Price + 690 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Северные креветки жаренные 690 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Морепродукты"')
		elif sq == 26:
			sql.execute("UPDATE Gain SET Price = Price + 690 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Северные креветки вареные 690 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Морепродукты"')
		elif sq == 27:
			sql.execute("UPDATE Gain SET Price = Price + 690 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Тартар из говядины 690 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 28:
			sql.execute("UPDATE Gain SET Price = Price + 790 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Тартар из лосося 790 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Рыба"')
		elif sq == 29:
			sql.execute("UPDATE Gain SET Price = Price + 90 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Круассан классический 90 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 30:
			sql.execute("UPDATE Gain SET Price = Price + 120 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Мороженое карамель с морской солью 120 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 31:
			sql.execute("UPDATE Gain SET Price = Price + 120 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Ванильное мороженое 120 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 32:
			sql.execute("UPDATE Gain SET Price = Price + 150 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Маффин брусничный 150 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Фрукты" or product == "Шоколад"')
		elif sq == 33:
			sql.execute("UPDATE Gain SET Price = Price + 150 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Маффин шоколадный 150 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 34:
			sql.execute("UPDATE Gain SET Price = Price + 190 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Миндальный круассан 190 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад" or product == "Орехи"')
		elif sq == 35:
			sql.execute("UPDATE Gain SET Price = Price + 210 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Эклер фисташковый 210 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад" or product == "Орехи"')
		elif sq == 36:
			sql.execute("UPDATE Gain SET Price = Price + 290 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Штрудель 290 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 37:
			sql.execute("UPDATE Gain SET Price = Price + 290 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Наполеон 290 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 38:
			sql.execute("UPDATE Gain SET Price = Price + 290 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Тирамису 290 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 39:
			sql.execute("UPDATE Gain SET Price = Price + 290 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Медовик 290 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 40:
			sql.execute("UPDATE Gain SET Price = Price + 340 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чизкейк 340 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Шоколад"')
		elif sq == 41:
			sql.execute("UPDATE Gain SET Price = Price + 120 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чипсы с солью 120 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Овощи"')
		elif sq == 42:
			sql.execute("UPDATE Gain SET Price = Price + 190 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чипсы из говядины 190 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 43:
			sql.execute("UPDATE Gain SET Price = Price + 190 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чипсы из конины 190 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 44:
			sql.execute("UPDATE Gain SET Price = Price + 190 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Арахис с васаби 190 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Орехи"')
		elif sq == 45:
			sql.execute("UPDATE Gain SET Price = Price + 240 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чипсы из оленины 240 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Мясо"')
		elif sq == 46:
			sql.execute("UPDATE Gain SET Price = Price + 260 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Фисташки 260 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Орехи"')
		elif sq == 47:
			sql.execute("UPDATE Gain SET Price = Price + 130 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Капучино 0,2 л.  130 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Кофе" or product == "Молоко"')
		elif sq == 48:
			sql.execute("UPDATE Gain SET Price = Price + 150 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Американо 0,3 л.  150 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Кофе"')
		elif sq == 49:
			sql.execute("UPDATE Gain SET Price = Price + 150 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чай зеленый 0,3 л. 150 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Чай"')
		elif sq == 50:
			sql.execute("UPDATE Gain SET Price = Price + 150 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Чай черный 0,3 л. 150 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Чай"')
		elif sq == 51:
			sql.execute("UPDATE Gain SET Price = Price + 170 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Флэт уайт 0,2 л.  170 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Кофе" or product == "Молоко"')
		elif sq == 52:
			sql.execute("UPDATE Gain SET Price = Price + 170 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Латте 0,3 л.  170 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Кофе" or product == "Молоко"')
		elif sq == 53:
			sql.execute("UPDATE Gain SET Price = Price + 400 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Пиво светлое 0,5 л. 400 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Пиво"')
		elif sq == 54:
			sql.execute("UPDATE Gain SET Price = Price + 400 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
			sql.execute("INSERT INTO orders_menu VALUES ('Пиво темное 0,5 л. 400 ₽')")
			sql.execute('UPDATE storage SET col = col - 10 WHERE product == "Пиво"')

		db.commit()


		# Смена окна на то, которое описано в классе Menu
		menu = Menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex() + 1)


	# Метод backfunction
	def backfunction(self):
		# Смена окна на то, которое описано в классе Menu
		menu = Menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex() + 1)


# Класс Payment "payment.ui"
class Payment(QDialog):
	def __init__(self):
		super(Payment, self).__init__()
		# Загрузка графического интерфейса
		loadUi("Designer/Menu/payment.ui", self)
		# Кнопки pay, back, del_order, функции payfunction, backfunction, delfunction
		self.pay.clicked.connect(self.payfunction)
		self.back.clicked.connect(self.backfunction)
		self.del_order.clicked.connect(self.delfunction)


		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Выборка Price из таблицы Gain, где ID = SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1
		sql.execute("SELECT Price FROM Gain WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)")
		sq = str(sql.fetchone()[0])
		# Присвоение полю total_sum значения из вышесформированной выборки
		self.total_sum.setText(sq + " ₽")

		db.commit()


		# Выборка Dishes из таблицы orders_menu
		sql.execute("SELECT Dishes FROM orders_menu")
		lab = str(sql.fetchall())
		# Присвоение полю menu_order значения из вышесформированной выборки
		self.menu_order.setText(lab)

		db.commit()


	# Метод delfunction
	def delfunction(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Удаление всего из таблицы orders_menu
		sql.execute('DELETE FROM orders_menu')


		# Обновление значения Price = 0 в таблице Gain, где ID = SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1
		sql.execute('UPDATE Gain SET Price = 0 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)')

		db.commit()


		# Обнуление полей menu_order и total_sum
		self.menu_order.setText("")
		self.total_sum.setText("")
		# Блокировка кнопки pay
		self.pay.setEnabled(False)


	# Метод payfunction
	def payfunction(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Запись в Price = 0 в таблице Gain
		sql.execute('INSERT INTO Gain (Price) VALUES (0)')


		# Запись в orders_chef все значения из orders_menu
		sql.execute('INSERT INTO orders_chef SELECT * FROM orders_menu')


		# Удаление всех значений из таблицы orders_menu
		sql.execute('DELETE FROM orders_menu')


		# Обновление значений Finall_price = SELECT sum(Price) FROM Gain в таблице Gain
		sql.execute("UPDATE Gain SET Finall_price = (SELECT sum(Price) FROM Gain)")

		db.commit()


		# Закрыть окно		
		widget.close()


	# Метод backfunction
	def backfunction(self):
		# Подключение БД server.db
		db = sqlite3.connect('SQL/server.db')
		sql = db.cursor()


		# Обновление Price = 0 в таблице Gain, где ID = SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1
		sql.execute('UPDATE Gain SET Price = 0 WHERE ID = (SELECT ID FROM Gain ORDER BY ID DESC LIMIT 1)')


		# Удаление всего из таблицы orders_menu
		sql.execute('DELETE FROM orders_menu')

		db.commit()


		# Смена окна на то, которое описано в классе Menu
		menu = Menu()
		widget.addWidget(menu)
		widget.setCurrentIndex(widget.currentIndex() + 1)


#main
app = QApplication(sys.argv)
welcome = Welcome()
widget = QStackedWidget()
widget.addWidget(welcome)
# Фиксированные размеры окон
widget.setFixedHeight(850)
widget.setFixedWidth(1200)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")