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

        # This should create a dictionary of products containing the quantity sold and a set of unique orders its found on.
        for product in all_products:
            quantity = 0
            total = 0
            these_orders = set()
            customers = set()
            for item in all_line_items:
                if product[0] == item[1]:
                    quantity += 1
                    total += product[1]
                    these_orders.add(item[2])
            for sale_order in these_orders:
                for order in all_orders:
                    if sale_order == order[0]:
                        customers.add(order[-1])
            sales[product[2]] = dict(quantity = quantity, total = total, orders = these_orders, customers = customers)

        # print(sales.items())

        # # Now Sort!
        # sortable_list = list()
        # for product, value in sales.items():
        #     if len(sortable_list) < 1:
        #         sortable_list.append((product, value['quantity'], len(value['customers']), value['total']))
        #     else:
        #         for index, item in enumerate(sortable_list):
        #             if item[-1] < value['total']:
        #                 sortable_list.insert(index, (product, value['quantity'], len(value['customers']), value['total']))
        #                 return
        #         sortable_list.insert(-1, (product, value['quantity'], len(value['customers']), value['total']))

        # print('{}'.format(sortable_list[1]))

        print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        print ( BColor.stars+"{:*^55}".format("*")+ BColor.ENDC)
        # for key, product in sortable_list.items():
        #     print("{:<18}{:<11}{:<11}${:<15:.2f}".format(key[0:14], product['quantity'], len(product['customers']), product['total']))
        
        for key, product in sales.items():
            print("{:<18}{:<11}{:<11}${:<15.2f}".format(key[0:14], product['quantity'], len(product['customers']), product['total']))
        
        print ( BColor.stars+"{:*^55}".format("*")+ BColor.ENDC)
        # print("{:<18}{:<11}{:<11}{:<15}".format("Totals: ", sum(sum_orders), sum(sum_customers), sum(sum_revenue)))

        input("->Press any key to" + BColor.stars + " return" + BColor.ENDC + " to main menu" )
