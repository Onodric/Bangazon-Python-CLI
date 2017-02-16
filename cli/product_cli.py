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
   


    def run(self):
        """
        ProductPopularity.run() method prompts to get total revenue, number of orders, number of customers on a product
        
        """
        product_data = ProductData()
        total_rev = product_data.get_all_revenue()
        """
        This method total_rev is getting all data such as num of orders, customers, revenue of the specific product from product_db_interactor.py  
        """
        
        total_order = []
        total_customer = []
        total_revenue = []

        print("{:<18}{:<11}{:<11}{:<15}".format("Product", "Order", "Customers", "Revenue") )
        print ( BColor.stars+"{:*^55}".format("*")+ BColor.ENDC)
        for item in total_rev:
            print("{:<18}{:<11}{:<11}${:<15.2f}".format(item[0][:14], item[len(item)-3], item[len(item)-2], item[len(item)-1]))
            
            total_order.append(item[len(item)-3])
            total_customer.append(item[len(item)-2])
            total_revenue.append(item[len(item)-1])
        print ( BColor.stars+"{:*^55}".format("*")+ BColor.ENDC)
        print("{:<18}{:<11}{:<11}${:<15.2f}".format("Totals: ", sum(total_order), sum(total_customer), sum(total_revenue)))
        input("->Press any key to" + BColor.stars + " return" + BColor.ENDC + " to main menu" )
       
