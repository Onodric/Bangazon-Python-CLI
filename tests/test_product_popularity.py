import unittest
import sys
sys.path.append("../")
from cli import product_cli
# from db.initializer.sql import *
from db.order_db_interactor import OrderDB
from db.customer_db_interactor import Customer_db
from db.product_db_interactor import ProductData
from db.line_item_db_interactor import LineItemDB

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
		self.orders_all = OrderDB.get_all_orders(self)
		self.customer_all = Customer_db.get_all_customers()
		self.prod_all = ProductData.get_all_products(self)
		self.line_item_all = LineItemDB.get_all_line_items(self)

	

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
		price_t = dict()
		order_num = self.orders_all
		line_items = self.line_item_all
		prod_id = self.prod_all
		for orders in order_num:
			for line_item in line_items:
				if orders[0] == line_item[1]:
					for prod in prod_id:
						if orders[2] == prod[0]:
							price_t[prod[0]] = list()
							price_t[prod[0]].append(prod[1])
							self.assertIn(prod[1], price_t[prod[0]])
							self.assertEqual(orders[2], prod[0])
							self.assertIsInstance(total_price, dict)

							for key, val in total_price.items():
								self.assertEqual(type(total_price[key]), int)



	def test_can_retrieve_num_of_customers(self):
		"""
		Method to test if get_total_num_of_customers method brings back numbers in a dict()
		and an integer value
		"""
		num = self.product_p.get_total_num_of_customers()
		customer_n = dict()
		customer_id = self.customer_all
		order_num = self.orders_all
		line_items = self.line_item_all
		for orders in order_num:
			for customer in customer_id:
				if orders[3] == customer[0]:
					customer_n[customer[0]] = list()
					customer_n[customer[0]].append(customer[0])
					self.assertIn(customer[0], customer_n[customer[0]])
					self.assertEqual(orders[3], customer[0])

					for key, val in num.items():
						self.assertEqual(type(num[key]), int)
						self.assertIsNotNone(num[key])

	def test_can_retrieve_total_num_of_orders(self):
		"""
		Method to test if get_total_num_of_orders method brings back numbers in a dict()
		and an integer value
		"""
		num = self.product_p.get_total_num_of_orders()
		order_n = dict()
		order_num = self.orders_all
		line_items = self.line_item_all
		prod_id = self.prod_all
		for orders in order_num:
			for line_item in line_items:
				if orders[0] == line_item[1]:
					for prod in prod_id:
						if orders[2] == prod[0]:
							order_n[orders[0]] = list()
							order_n[orders[0]].append(orders[0])
							self.assertIn(orders[0], order_n[orders[0]])
							self.assertEqual(orders[2], prod[0])

							for key, val in num.items():
								self.assertEqual(type(num[key]),int)
								self.assertIsNotNone(num[key])








if __name__ =='__main__':
     unittest.main()






		

