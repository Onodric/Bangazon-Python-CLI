# from db.order_data import OrderDB
# from db.product_data import *

class ProductPopularity():

	def __init__(self):
	 	self.order_data = Orders.get_all_orders()
		self.product_data = Product.get_all_products()
		self.line_items = Line_items.get_all()

	def get_total_revenue(self):
		revenue = dict()
		for order in order_data:
			for item in line_items:
				if order[0] == item[1]:
					for product in product_data:
						if product[0] == item[2]:
							revenue[product[0]] =list()
							revenue[product[0]].append(product[2])
							sum(revenue[product[0]])

		return revenue


	def get_total_customers(self):
		customers = list()
		for order in order_data:
			for item in line_item:
				if order[0] == item[1]:
					for product in product_data:
						if product[0] == item[2]:
							if order[3] == item[1][3]:
								customers.append(order[3])
								sum(customers)


		

    




