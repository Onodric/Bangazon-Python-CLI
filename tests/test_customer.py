import unittest
import sys
sys.path.append("../")
from models.customer import Customer

class TestCustomer(unittest.TestCase):
	"""
	customer should have a:
	name
	street address, city, state, zipcode
	phone #
	"""
	@classmethod
	def setUpClass(self):
		self.me = Customer("Me", "500 interstate blvd", "Nashville", "TN", "11111", "666-6666")

	def test_customer_is_instance(self):
		self.assertIsInstance(self.me, Customer)

	def test_can_return_current_customer(self):
		current_customer = Customer.get_current_customer(self.me)
		self.assertEqual(self.me.name, current_customer[0][0])
		self.assertEqual(self.me.address, current_customer[0][1])
		self.assertEqual(self.me.city, current_customer[0][2])
		self.assertEqual(self.me.state, current_customer[0][3])
		self.assertEqual(self.me.postal, current_customer[0][4])
		self.assertEqual(self.me.phone, current_customer[0][5])
		self.assertEqual(self.me.active, current_customer[0][6])


	def test_customer_has_attribute(self):
		self.assertEqual("Me", self.me.name)
		self.assertEqual("500 interstate blvd", self.me.address)
		self.assertEqual("Nashville", self.me.city)
		self.assertEqual('TN', self.me.state)
		self.assertEqual("11111", self.me.postal)
		self.assertEqual("666-6666", self.me.phone)
		self.assertEqual(False, self.me.active)



if __name__ == "__main__":
	unittest.main()