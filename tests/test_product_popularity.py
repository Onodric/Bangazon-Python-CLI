# import unittest
# import sys
# sys.path.append("../")
# from cli import product_cli
# # from db.initializer.sql import *

# class TestOrderData(unittest.TestCase):
# 	"""
#     Tests for class ProductPopularity in cli file


#     Methods:
#     test_can_get_product_data
#     test_can_retrieve_total_revenue
#     test_can_retrieve_num_of_customers
#     test_can_retrieve_total_num_of_orders

#     Author: Julia Kim-Chung
#     """

# 	@classmethod
# 	def setUpClass(self):
# 		"""
# 		 Create an instance of the product_p that can be used in all tests
# 		"""
# 		self.product_p = product_cli.ProductPopularity()

	

# 	def test_can_get_product_data(self):
# 		"""
# 		Method to test if data from db can be retrieved

# 		"""
# 		self.assertIsNotNone(self.product_p.line_items)
# 		self.assertIsNotNone(self.product_p.order_data)
# 		self.assertIsNotNone(self.product_p.product_data)

# 	def test_can_retrieve_total_revenue(self):
# 		"""
# 		Method to test if get_total_revenue method brings back a dict()
# 		"""
# 		total_price = self.product_p.get_total_revenue()
# 		self.assertIsInsatance(total_price, dict)


# 	def test_can_retrieve_num_of_customers(self):
# 		"""
# 		Method to test if get_total_num_of_customers method brings back numbers in a dict()

# 		"""
# 		num = self.product_p.get_total_num_of_customers()
# 		self.assertIsEqual(num[key], 10)

# 	def test_can_retrieve_total_num_of_orders(self):
# 		"""
# 		Method to test if get_total_num_of_orders method brings back numbers in a dict()

# 		"""
# 		num = self.product_p.get_total_num_of_orders()
# 		self.assertIsEqual(num[key], 7)







# if __name__ =='__main__':
#      unittest.main()






		

