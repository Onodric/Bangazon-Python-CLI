import sqlite3
import sys
sys.path.append("../")
import configuration

class Customer_db():
	"""
	Customer_db is a class module for  interacting with the Customer table in the bangazon.db file
	methods:
		save_new_customer
		get_all_customers
		update_active_true
		update_active_false
	"""

	def save_new_customer(self, Customer):
		"""
		excepts an instance of customer as an argument
		saves the new instance of customer to db
		"""
		with sqlite3.connect(configuration.database_path) as thingy:
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
		"""
		returns all customers in db
		"""
		with sqlite3.connect(configuration.database_path) as thingies:
			cursor = thingies.cursor()
			try:
				cursor.execute("SELECT * FROM Customer")
				customers = cursor.fetchall()
			except:
				pass
			return customers

	def update_active_true(self, thingy):
		"""
		accepts a customer's primary key as an argument
		changes that customers active status to true
		"""
		with sqlite3.connect(configuration.database_path) as thingies:
			cursor = thingies.cursor()
			try:
				cursor.execute('UPDATE Customer SET active = 1 WHERE customer_id = {}'.format(thingy))
			except:
				pass

	def update_active_false(self):
		"""
		when called, will filter through the Customer Table and change all customers who have active 
		as true to false
		"""
		with sqlite3.connect(configuration.database_path) as thingies:
			cursor = thingies.cursor()
			try:
				cursor.execute('UPDATE Customer SET active = 0 WHERE active = 1')
			except:
				pass



