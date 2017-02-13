import unittest
import sys
sys.path.append("../")
from models.customer import Customer
from db.customer_db_interactor import Customer_db

class TestCustomer(unittest.TestCase):
	"""
	customer should have a:
	name, street address, city, state, zipcode, phone #, is active should default to false
	methods:
		test_customer_is_instance
		test_can_return_current_customer
		test_customer_has_attribute
		test_customer_can_be_saved_and_returned
		test_can_update_true
		test_can_update_false
	"""
	@classmethod
	def setUpClass(self):
		self.me = Customer("Me", "500 interstate blvd", "Nashville", "TN", "11111", "666-6666")

	def test_customer_is_instance(self):
		"""
		is this an instance of customer
		"""
		self.assertIsInstance(self.me, Customer)

	def test_can_return_current_customer(self):
		"""
		testing to see if you can return current customer with attributes
		"""
		current_customer = Customer.get_current_customer(self.me)
		self.assertEqual(self.me.name, current_customer[0][0])
		self.assertEqual(self.me.address, current_customer[0][1])
		self.assertEqual(self.me.city, current_customer[0][2])
		self.assertEqual(self.me.state, current_customer[0][3])
		self.assertEqual(self.me.postal, current_customer[0][4])
		self.assertEqual(self.me.phone, current_customer[0][5])
		self.assertEqual(self.me.active, current_customer[0][6])


	def test_customer_has_attribute(self):
		"""
		testing to see if customer has all necessary attributes
		"""
		self.assertEqual("Me", self.me.name)
		self.assertEqual("500 interstate blvd", self.me.address)
		self.assertEqual("Nashville", self.me.city)
		self.assertEqual('TN', self.me.state)
		self.assertEqual("11111", self.me.postal)
		self.assertEqual("666-6666", self.me.phone)
		self.assertEqual(0, self.me.active)

	def test_can_customer_be_saved_and_returned(self):
		"""
		testing to see if a customer can be saved to database and returned
		"""
		Customer_db().save_new_customer(self.me)
		data = Customer_db.get_all_customers()
		dataList = len(data)
		targetData = data[dataList -1]
		dummyTestData = (dataList, "Me", "500 interstate blvd", "Nashville", "TN", 11111, "666-6666", 0)
		self.assertTupleEqual(dummyTestData, targetData)

	def test_can_update_true(self):
		"""
		testing to see if you can update active status to true
		"""
		customers = Customer_db.get_all_customers()
		customer_id = customers[1][0]
		Customer_db().update_active_true(customer_id)
		new_customers = Customer_db.get_all_customers()
		active_status = new_customers[1][7]
		self.assertEqual(1, active_status)

	def test_can_update_false(self):
		"""
		testing to see if you can update active status to false
		"""
		Customer_db().update_active_false()
		new_customers_again = Customer_db.get_all_customers()
		for customer in new_customers_again:
			self.assertEqual(0, customer[7])




if __name__ == "__main__":
	unittest.main()