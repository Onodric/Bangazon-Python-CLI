import unittest
import sys
sys.path.append("../")
from cli import product_cli
# from db.initializer.sql import *

class TestOrderData(unittest.TestCase):
	@classmethod
	def setUpClass(self):
		self.product_p = product_cli.ProductPopularity()

	

	def test_can_get_product_data(self):
		self.assertIsNotNone(self.product_p.line_items)
		self.assertIsNotNone(self.product_p.order_data)
		self.assertIsNotNone(self.product_p.product_data)

	def test_can_retrieve_total_revenue(self):
		total_price = self.product_p.get_total_revenue()
		self.assertIsInsatance(total_price, dict)


	def test_can_retrieve_num_of_customers(self):
		num = self.product_p.get_total_num_of_customers()
		self.assertIsEqual(num, 10)

	def test_can_retrieve_total_num_of_orders(self):
		num = self.product_p.get_total_num_of_orders()
		self.assertIsEqual(num, 7)







if __name__ =='__main__':
     unittest.main()






		

