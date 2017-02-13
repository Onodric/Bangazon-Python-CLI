import sys
sys.path.append("../")
# from db.order_data import *
# from db.product_data import *

class ProductPopularity():
    """
        This class is to build the chart for product popularity.
        Methods:
        def get_total_revenue
        def get_total_num_of_customers
        def get_total_num_of_orders

        Author: Julia Kim-Chung
    """

    # def __init__(self):

    #     """
    #     """

    #     self.order_data = Orders.get_all_orders()
    #     self.product_data = Product.get_all_products()
    #     self.line_items = Line_items.get_all_line_items()
    #     self.customer_data = Customer.get_all_customers()


    # def get_total_revenue(self):
    #     revenue = dict()
    #     for order in order_data:
    #         for item in line_items:
    #             if order[0] == item[1]:
    #                 for product in product_data:
    #                     if product[0] == item[2]:
    #                         revenue[product[1]] =list()
    #                         revenue[product[1]].append(product[2])
    #                         sum(revenue[product[1]])

    #     return revenue


    # def get_total_num_of_customers(self):
    #     customers = dict()
    #     for order in order_data:
    #         for item in line_items:
    #             if order[0] == item[1]:
    #                 for product in product_data:
    #                     for customer in customer_data:
    #                         if product[0] == item[2]:
    #                             if order[3] == customer[0]:
    #                                 customers[product[1]] ==list()
    #                                 customers[product[1]].append(order[3])
    #                                 customers[product[1]] == len(cutomers[product[1]])
    #     return customers


    # def get_total_num_of_orders(self):
    #     orders = dict()
    #     for order in order_data:
    #       for item in line_items:
    #         if order[0] == line_item[1]:
    #             for product in product_data:
    #                 if product[0] == item[2]:
    #                     orders[product[1]] == list()
    #                     orders[product[1]].append(order[0])
    #                     orders[product[1]] == len(orders[product[1]])
    #     return orders


    def run(self):
        """
        ProductPopularity.run() method prompts to get total revenue, number of orders, number of customers on a product
        
        """

        # total_revenue = ProductPopularity.get_total_revenue()
        # total_customers = ProductPopularity.get_total_num_of_customers()
        # total_orders = ProductPopularity.get_total_num_of_orders()
        print("{}{:^15}{:^15}{:^15}{:^15}".format("Product", "Order", "Customers", "Revenue","") )
        print ( "{:*^55}".format("*"))
        
        print("{}{:^11}{:^15}{:^15}".format("Baby Powder", 3, 2, "$96.00"))


    if __name__ == '__main__':
        product_pop = ProductPopularity()
        product_pop.run()
        




