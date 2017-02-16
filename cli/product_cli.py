import sys
sys.path.append("../")
from db.order_db_interactor import *
from db.line_item_db_interactor import *
from db.customer_db_interactor import *
from db.product_db_interactor import *

class BColor:
    stars = '\033[91m'
    ENDC = '\033[0m'

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

        self.order_data = OrderDB()
        self.product_data = ProductData()
        self.line_item_data = LineItemDB()
        self.customer_data = Customer_db()


    def run(self):
        """
        ProductPopularity.run() method prompts to get total revenue, number of orders, number of customers on a product
        
        """

        all_orders = self.order_data.get_all_orders()
        all_products = self.product_data.get_all_products()
        all_line_items = self.line_item_data.get_all_line_items()
        sales = dict()
        unique_customers = set()
        closed_orders = list()
        closed_line_items = list()

        for order in all_orders:
            if order[1] == 1:
                closed_orders.append(order)

        for order in closed_orders:
            for item in all_line_items:
                if item[1] == order[0]:
                    closed_line_items.append(item)

        # This should create a dictionary of products containing the quantity sold and a set of unique orders its found on.
        for product in all_products:
            quantity = 0
            total = 0
            these_orders = set()
            customers = set()
            for item in closed_line_items:
                if product[0] == item[2]:
                    quantity += 1
                    total += product[1]
                    these_orders.add(item[1])
            for sale_order in these_orders:
                for order in all_orders:
                    if sale_order == order[0]:
                        customers.add(order[-1])
            sales[product[2]] = dict(quantity = quantity, total = total, orders = these_orders, customers = customers)

        # Now Sort!
        sortable_list = list()
        for product in sales.keys():
            sortable_list.append([product, sales[product]['quantity'], len(sales[product]['customers']), sales[product]['total']])

        totals = [0, 0, 0]
        sortable_list.sort(key=lambda x: x[3], reverse=True)
        sorted_list = sortable_list
        for item in sortable_list:
            print("Sorting List: {}".format(item))
            totals[0] += item[1]
            totals[1] += item[2]
            totals[2] += item[3]

        print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        print ( BColor.stars+"{:*^55}".format("*")+ BColor.ENDC)
        for product in sorted_list:
            print("{:<18}{:<11}{:<11}${:<15.2f}".format(product[0], product[1], product[2], product[3]))
        
        print ( BColor.stars+"{:*^55}".format("*")+ BColor.ENDC)
        print("{:<18}{:<11}{:<11}${:<15.2f}".format("Totals: ", totals[0], totals[1], totals[2]))

        input("->Press any key to" + BColor.stars + " return" + BColor.ENDC + " to main menu" )
