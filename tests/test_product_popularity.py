import unittest
import sys
sys.path.append("../")
from cli import product_cli
# from db.initializer.sql import *

class TestOrderData(unittest.TestCase):
	"""
    Tests for class ProductPopularity in cli file


    Methods:
    test_can_get_product_data
    test_can_retrieve_total_revenue
    test_can_retrieve_num_of_customers
    test_can_retrieve_total_num_of_orders

    Author: Julia Kim-Chung
    """

	@classmethod
	def setUpClass(self):
		"""
		 Create an instance of the product_p that can be used in all tests
		"""
		self.product_p = product_cli.ProductPopularity()

	

	def test_can_get_data_from_each_method(self):
		"""
		Method to test if data from db can be retrieved

		"""
		self.assertIsNotNone(self.product_p.line_items)
		self.assertIsNotNone(self.product_p.order_data)
		self.assertIsNotNone(self.product_p.product_data)

	def test_can_retrieve_total_revenue(self):
		"""
		Method to test if get_total_revenue method brings back a dict()
		and an integer value
		"""
		total_price = self.product_p.get_total_revenue()
		self.assertIsInstance(total_price, dict)
		for key, val in total_price.items():
			self.assertEqual(type(total_price[key]), int)



	def test_can_retrieve_num_of_customers(self):
		"""
		Method to test if get_total_num_of_customers method brings back numbers in a dict()
		and an integer value
		"""
		num = self.product_p.get_total_num_of_customers()
		for key, val in num.items():
			self.assertEqual(type(num[key]), int)
			self.assertIsNotNone(num[key])

	def test_can_retrieve_total_num_of_orders(self):
		"""
		Method to test if get_total_num_of_orders method brings back numbers in a dict()
		and an integer value
		"""
		num = self.product_p.get_total_num_of_orders()
		for key, val in num.items():
			self.assertEqual(type(num[key]), int)
			self.assertIsNotNone(num[key])







if __name__ =='__main__':
     unittest.main()






		

