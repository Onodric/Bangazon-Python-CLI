import sys
sys.path.append("../")
from db.order_db_interactor import *
from db.customer_db_interactor import *
from db.product_db_interactor import *

class ProductPopularity():
    """
        This class is to build the chart for product popularity.
        Methods:
        def get_total_revenue
        def get_total_num_of_customers
        def get_total_num_of_orders

        Author: Julia Kim-Chung
    """

    def __init__(self):

        """
        initialized get_all_orders() method from Orders from the order db file
        initialized get_all_products() method from Product from the product db file
        initialized get_all_line_items()method from Orders from the order db file
        initilaized get_all_customers()method from Orders from the customer db file
        """

        self.order_data = Orders.get_all_orders()
        self.product_data = Product.get_all_products()
        self.line_items = Line_items.get_all_line_items()
        self.customer_data = Customer.get_all_customers()


    def get_total_revenue(self):
        """
        This is a method to get total revenue of a specific product that's in the order_data
        """
        revenue = dict()
        for order in self.order_data:
            for item in self.line_items:
                if order[0] == item[1]:
                    for product in self.product_data:
                        if product[0] == item[2]:
                            revenue[product[1]] =list()
                            revenue[product[1]].append(product[2])
                            sum(revenue[product[1]])

        return revenue


    def get_total_num_of_customers(self):
        """
        This is a method to get total number of customers who have ordered the specific product that's in the order_data
        """
        customers = dict()
        for order in self.order_data:
            for item in self.line_items:
                if order[0] == item[1]:
                    for product in self.product_data:
                        for customer in self.customer_data:
                            if product[0] == item[2]:
                                if order[3] == customer[0]:
                                    customers[product[1]] =list()
                                    customers[product[1]].append(order[3])
                                    customers[product[1]] = len(customers[product[1]])
        return customers


    def get_total_num_of_orders(self):
        """
        This is a method to get total number of orders of a specific product that's in the order_data
        """
        orders = dict()
        for order in self.order_data:
          for item in self.line_items:
            if order[0] == line_item[1]:
                for product in self.product_data:
                    if product[0] == item[2]:
                        orders[product[1]] =list()
                        orders[product[1]].append(order[0])
                        orders[product[1]] = len(orders[product[1]])
        return orders


    def run(self):
        """
        ProductPopularity.run() method prompts to get total revenue, number of orders, number of customers on a product
        
        """

        total_revenue = self.get_total_revenue()

        total_customers = self.get_total_num_of_customers()
        total_orders = self.get_total_num_of_orders()

        print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        print ( "{:*^55}".format("*"))

        """
        This for loops will retrieve the total order number, total customer number, total revenue of a specific product 
        and print out the results in the command line
        """

        for key, value in total_orders.items():
            for prod, num in total_customers.items():
                if prod == key:
                    for name, revenue in total_revenue.items():
                        if name == key:
                            print("{:<18}{:<11}{:<11}{:<15}".format(key, value, num, revenue))




        input("->Press any key to return to main menu ")
       
        # print("{:<18}{:<11}{:<11}{:<15}".format(p_total_orders, total_customers[key], total_revenue[key] ))

        
        # print("{:<18}{:<11}{:<11}{:<15}".format("Baby Powder", 3, 2, "$96.00"))



    
       


