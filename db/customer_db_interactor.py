import sqlite3

class Customer_db():

	def save_new_customer(self, Customer):
		with sqlite3.connect('bangazon.db') as thingy:
			cursor = thingy.cursor()
			try:
				cursor.execute("SELECT * FROM Customer")
				cursor.fetchall()
			except sqlite3.OperationalError:
				cursor.execute("""
					CREATE TABLE `Customer` (
						customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
						name TEXT NOT NULL,
						address TEXT NOT NULL,
						city TEXT NOT NULL,
						state TEXT NOT NULL,
						postal INTEGER NOT NULL,
						phone TEXT NOT NULL,
						active INTEGER NOT NULL
					)
					""")
			cursor.execute("""
				INSERT INTO Customer VALUES (null, '{}', '{}', '{}', '{}', '{}', '{}', '{}')
				""".format(
					Customer.name,
					Customer.address,
					Customer.city,
					Customer.state,
					Customer.postal,
					Customer.phone,
					Customer.active
					)) 

	def get_all_customers():
		with sqlite3.connect('bangazon.db') as thingies:
			cursor = thingies.cursor()
			try:
				cursor.execute("SELECT * FROM Customer")
				customers = cursor.fetchall()
			except:
				pass
			return customers
