import sys
sys.path.append("../")
from db.order_db_interactor import OrderDB
from db.line_item_db_interactor import LineItemDB
from db.customer_db_interactor import Customer_db
from db.product_db_interactor import ProductData

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

        Authors: Julia Kim-Chung, Sam Phillips
    """
    def __init__(self):
        self.order_db = OrderDB()
        self.line_item_db = LineItemDB()
        self.customer_db = Customer_db()
        self.product_db = ProductData()





    def run(self):
        """
        ProductPopularity.run() method prompts to get total revenue, number of orders, number of customers on a product
        
        """

        revenue = dict()
        orders = dict()
        customers = dict()

        # data processing
        self.products = self.product_db.get_all_products()
        for product in self.products:
            revenue[product[2]] = list()
            orders[product[2]] = set()
            customers[product[2]] = set()
            product_total_revenue = 0
            self.line_items= self.line_item_db.get_all_line_items()
            for item in self.line_items:
                # print(item)
                if item[2] == product[0]:

                    # add the product's price to a list holding each sale of that product
                    revenue[product[2]].append(product[1])

                    # add the order_id of the line_item to a set holding each order that contains that product
                    print("\nitem: " + str(item[1]))
                    pk = item[1]
                    orders[product[2]].update(str(item[1]))


                    # add the customer_id of the line_item's order to a set holding each customer that has ordered that product
                    all_orders = self.order_db.get_all_orders()
                    for single_order in all_orders:
                        if single_order[0] == item[2]:
                            # customers[product[2]].update("goodbye")
                            customers[product[2]].update(str(single_order[3]))


        print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        print ( "{:*^55}".format("*"))

        # condensing
        bangazon_total_revenue = 0
        for product in self.products:
            temp_revenue = 0
            temp_orders = 0
            temp_customers = 0

            for sale in revenue[product[2]]:
                temp_revenue += product[1]
                bangazon_total_revenue += product[1]
            temp_revenue = "{:.2f}".format(temp_revenue)
            revenue[product[2]] = temp_revenue
            # print(revenue[product[2]])


            for order in orders[product[2]]:
                temp_orders += 1
            orders[product[2]] = temp_orders
            # print(revenue[product[2]])


            for customer in customers[product[2]]:
                temp_customers += 1
            customers[product[2]] = temp_customers
            # print(revenue[product[2]])


            print("{:<18}{:<11}{:<11}{:<15}".format(product[2], str(orders[product[2]]), str(customers[product[2]]), "$" +str(revenue[product[2]])))



        print ( "{:*^55}".format("*"))
        print("{:<18}{:<11}{:<11}{:<15}".format("Totals: ", "nothing", "functional", "yet"))

        # Julia's
        # print("{:<18}{:<11}{:<11}{:<15}".format("Totals: ", sum(sum_orders), sum(sum_customers), "$" + total_bangazon_revenue))

        input("->Press any key to return to main menu ")


       


