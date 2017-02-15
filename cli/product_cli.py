import sys
sys.path.append("../")
from db.order_db_interactor import OrderDB
from db.line_item_db_interactor import LineItemDB
from db.customer_db_interactor import Customer_db
from db.product_db_interactor import ProductData

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
                print(item)
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



        # report printing
        # print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        # print ( "{:*^55}".format("*"))
        # for product in self.products:
        #     print("{:<18}{:<11}{:<11}{:<15}".format(product[2], str(orders[product[2]]), str(customers[product[2]]), "$" +str(revenue[product[2]])))


        print ( "{:*^55}".format("*"))
        input("->Press any key to return to main menu ")




            # print("{:<18}{:<11}{:<11}{:<15}".format(product[2], "\norders" + str(orders[product[2]]), '\ncustomers' + str(customers[product[2]]), "\n$" +str(revenue[product[2]])))



            # print("{:<18}{:<11}{:<11}{:<15}".format(product[2], str(value), str(num), "$" +product_total_revenue))

        





        # total_customers = self.get_total_num_of_customers()
        # total_orders = self.get_total_num_of_orders()

        
        """
        This for loops will retrieve the total order number, total customer number, total revenue of a specific product 
        and print out the results in the command line
        """
        # sum_revenue = []
        # sum_customers = []
        # sum_orders = []


        # total_bangazon_revenue = 0

        # print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        # print ( "{:*^55}".format("*"))
        # for key, value in total_orders.items():
        #     for prod, num in total_customers.items():
        #         if prod == key:
        #             for name, revenue in total_revenue.items():
        #                 if name == key:
        #                     # print(name)
        #                     print(name, revenue)
        #                     sum_orders.append(value)
        #                     sum_customers.append(num)
        #                     sum_revenue.append(revenue)
        #                     product_total_revenue = 0
        #                     for sale in revenue:
        #                         product_total_revenue += sale
        #                         total_bangazon_revenue += sale
        #                     product_total_revenue = "{:.2f}".format(product_total_revenue)    
        #                     print("{:<18}{:<11}{:<11}{:<15}".format(key[0:14], str(value), str(num), "$" +product_total_revenue))
        # print ( "{:*^55}".format("*"))



        # total_bangazon_revenue = "{:.2f}".format(total_bangazon_revenue)

        # print("{:<18}{:<11}{:<11}{:<15}".format("Totals: ", sum(sum_orders), sum(sum_customers), "$" + total_bangazon_revenue))
        # input("->Press any key to return to main menu ")




















       


    # def __init__(self):

    #     """
    #     initialized get_all_orders() method from Orders from the order db file
    #     initialized get_all_products() method from Product from the product db file
    #     initialized get_all_line_items()method from Orders from the order db file
    #     initilaized get_all_customers()method from Orders from the customer db file
    #     """

    #     self.order_data = OrderDB.get_all_orders(self)
    #     self.product_data = ProductData.get_all_products(self)
    #     self.line_items = LineItemDB.get_all_line_items(self)
    #     self.customer_data = Customer_db.get_all_customers()


    # def get_total_revenue(self):
    #     """
    #     This is a method to get total revenue of a specific product that's in the order_data
    #     """
    #     self.order_data = OrderDB.get_all_orders(self)
    #     self.product_data = ProductData.get_all_products(self)
    #     self.line_items = LineItemDB.get_all_line_items(self)
    #     self.customer_data = Customer_db.get_all_customers()


    #     revenue = dict()
    #     for order in self.order_data:
    #         print(order)
    #         for product in self.product_data:
    #             revenue[product[2]] = list()
    #             for item in self.line_items:
    #                 # if the line_item belongs to the order
    #                 if order[0] == item[1]:
    #                     if order[1] == order[1]:
    #                         if product[0] == item[2]:
    #                             revenue[product[2]].append(product[1])
    #     return revenue



    # def get_total_num_of_customers(self):
    #     """
    #     This is a method to get total number of customers who have ordered the specific product that's in the order_data
    #     """

    #     self.order_data = OrderDB.get_all_orders(self)
    #     self.product_data = ProductData.get_all_products(self)
    #     self.line_items = LineItemDB.get_all_line_items(self)
    #     self.customer_data = Customer_db.get_all_customers()


    #     customers = dict()
    #     for order in self.order_data:
    #         for item in self.line_items:
    #             if order[0] == item[1]:
    #                 for product in self.product_data:
    #                     for customer in self.customer_data:
    #                         if product[0] == item[2]:
    #                             if order[3] == customer[0]:
    #                                 customers[product[2]] =list()
    #                                 customers[product[2]].append(order[3])
    #                                 customers[product[2]] = len(customers[product[2]])

    #     return customers


    # def get_total_num_of_orders(self):
    #     """
    #     This is a method to get total number of orders of a specific product that's in the order_data
    #     """

    #     self.order_data = OrderDB.get_all_orders(self)
    #     self.product_data = ProductData.get_all_products(self)
    #     self.line_items = LineItemDB.get_all_line_items(self)
    #     self.customer_data = Customer_db.get_all_customers()


    #     orders = dict()
    #     for order in self.order_data:
    #       for item in self.line_items:
    #         if order[0] == item[1]:
    #             for product in self.product_data:
    #                 if product[0] == item[2]:
    #                     orders[product[2]] =list()
    #                     orders[product[2]].append(order[0])
    #                     orders[product[2]] = len(orders[product[2]])
    #     return orders


    # def run(self):
    #     """
    #     ProductPopularity.run() method prompts to get total revenue, number of orders, number of customers on a product
        
    #     """

    #     total_revenue = self.get_total_revenue()

    #     total_customers = self.get_total_num_of_customers()
    #     total_orders = self.get_total_num_of_orders()

        
    #     """
    #     This for loops will retrieve the total order number, total customer number, total revenue of a specific product 
    #     and print out the results in the command line
    #     """
    #     sum_revenue = []
    #     sum_customers = []
    #     sum_orders = []


    #     total_bangazon_revenue = 0

    #     print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
    #     print ( "{:*^55}".format("*"))
    #     for key, value in total_orders.items():
    #         for prod, num in total_customers.items():
    #             if prod == key:
    #                 for name, revenue in total_revenue.items():
    #                     if name == key:
    #                         # print(name)
    #                         print(name, revenue)
    #                         sum_orders.append(value)
    #                         sum_customers.append(num)
    #                         sum_revenue.append(revenue)
    #                         product_total_revenue = 0
    #                         for sale in revenue:
    #                             product_total_revenue += sale
    #                             total_bangazon_revenue += sale
    #                         product_total_revenue = "{:.2f}".format(product_total_revenue)    
    #                         print("{:<18}{:<11}{:<11}{:<15}".format(key[0:14], str(value), str(num), "$" +product_total_revenue))
    #     print ( "{:*^55}".format("*"))



    #     total_bangazon_revenue = "{:.2f}".format(total_bangazon_revenue)

    #     print("{:<18}{:<11}{:<11}{:<15}".format("Totals: ", sum(sum_orders), sum(sum_customers), "$" + total_bangazon_revenue))
    #     input("->Press any key to return to main menu ")
       

        



    
       


