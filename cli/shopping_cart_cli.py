import sys
sys.path.append("../")
from db.order_db_interactor import *
from db.line_item_db_interactor import *
from db.customer_db_interactor import *
from db.product_db_interactor import *
from db.payment_db_interactor import *

class ShoppingCartCLI():
    """
    Class defining the interaction with a customer's shopping cart.

    format of order:
        (pk_order (autoIncrement!), is_closed (integer),
        fk_payment (null or integer), fk_customer (integer))

    format of line_item:
        (pk_line_item (autoIncrement!), fk_product (integer), fk_customer (integer))

    format of customer:
        (pk_customer (autoIncrement!), name (string),
        address (string), city (string), state (string),
        zip code (string), phone (string))

    format of payment_method:
        (pk_order (autoIncrement!), name (string),
        account_number (string), fk_customer)

    format of product:
        (pk_product (autoIncrement!), name (string), price (number),
        description (string))

    Author: Ben Marks, Ludicrous Ducks

    Methods:
        get_current_customer
        add_line_item
        pay_for_cart
        run
    """
    def __init__(self):
        """
        Method to initialize the class with default values
        """
        self.customer = Customer_db()
        self.order = OrderDB()
        self.line_item = LineItemDB()
        self.payment = PaymentDatabaseInteractor()
        self.products = ProductData()
        self.all_products = self.products.get_all_products()
        self.all_line_items = self.line_item.get_all_line_items()

        self.current_customer = self.customer.get_active()
        self.active_order = get_active_order()
        self.existing_line_items = get_line_items()
        self.shopping_cart = ShoppingCart(customer=self.current_customer, line_items=self.existing_line_items, order=self.active_order)


    def get_active_order(self):

        all_orders = self.order.get_all_orders()
        for item in all_orders:
            if item[-1] == self.current_customer_id and item[1] == 0:
                return item
        new_order = (0, None, self.current_customer_id)
        self.order.write_one_order(new_order)
        return ((len(all_orders)+1), 0, None, self.current_customer_id)


    def get_line_items(self, order):

        cart_contents = []
        for item in self.all_line_items:
            if item[1] == order[0]:
                cart_contents.append(item)
        return cart_contents


    def add_line_item(self):
        """
        CLI Method for option 4 of the main menu
        """
        choice = None
        while choice != 0:
            for item in self.all_products:
                print("{}. {}".format(item[0], item[1]))
            print("0. Return to Main Menu")
            choice = input("Please press the number of the product you wish to add to your order:")
            if choice == 0:
                return
            else:
                for item in self.all_products:
                    if choice == item[0]:
                        self.shopping_cart.add_product(item)


    def pay_for_cart(self):
        """
        CLI Method for option 5 of the main menu
        """
        print(self.current_customer)

if __name__ == '__main__':
    ShoppingCartCLI()