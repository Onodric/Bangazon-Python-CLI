import sys
sys.path.append("../")
from db.order_db_interactor import *
from db.line_item_db_interactor import *
from db.customer_db_interactor import *
from db.product_db_interactor import *
from db.payment_db_interactor import *
from models.shopping_cart import *

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
        self.current_customer = Customer_db.get_active()

        # retrieve the first open order that a customer has, or make a new one        
        all_orders = self.order.get_all_orders()
        self.active_order = ()
        if len(all_orders) < 1:
            new_order = (0, None, self.current_customer[0][0])
            self.order.write_one_order(new_order)
            all_orders = self.order.get_all_orders()
        for item in all_orders:
            if item[-1] == self.current_customer[0][0] and item[1] == 0:
                self.active_order = item
        if self.active_order == ():
            new_order = (0, None, self.current_customer[0][0])
            self.order.write_one_order(new_order)
        

        # get all attached line items of an order
        self.existing_line_items = []
        print(self.all_line_items)
        if len(self.all_line_items) > 0:
            for item in self.all_line_items:
                if item[1] == self.active_order[0]:
                    self.existing_line_items.append(item)

        # retrieve the customer payment types        
        self.customers_payments = []
        all_payments = self.payment.get_all_payments()
        for item in all_payments:
            if item[-1] == self.current_customer[0][0]:
                self.customers_payments.append(item)

        self.shopping_cart = ShoppingCart(customer=self.current_customer, line_items=self.existing_line_items, current_order=self.active_order)


    def add_line_item(self):
        """
        CLI Method for option 4 of the main menu
        """
        choice = None
        while choice != 0:
            print('\n\n\nAvailable Products\n')
            for item in self.all_products:
                print("{}. {}".format(item[0], item[-1]))
            print("\n0. Return to Main Menu")
            choice = input("\nPlease press the number of the product you wish to add to your order:")
            if choice == '0':
                break
            else:
                for item in self.all_products:
                    if choice == str(item[0]):
                        print("added {}".format(item[-1]))
                        self.shopping_cart.add_product(self.active_order, item)
                        self.existing_line_items.append(item)


    def pay_for_cart(self):
        """
        CLI Method for option 5 of the main menu
        """

        self.all_line_items = self.line_item.get_all_line_items()
        self.existing_line_items = []
        for item in self.all_line_items:
            if item[1] == self.active_order[0]:
                self.existing_line_items.append(item)
        
        if self.existing_line_items == []:
            input("Please add some products to your order first. Press any key to return to main menu.")
        else:
            total = 0
            line_items = self.shopping_cart.get_cart_total(self.active_order)
            for product in self.all_products:
                for item in line_items:
                    if product[0] == item[-1]:
                        total += product[1]
            print("Your order total is ${:.2f}. Ready to purchase?\n(Y/N) ".format(total))
            choice = input(">")
            if choice == "Y" or choice == "y":
                if self.customers_payments == []:
                    input("Please add a payment method to your account first. Press any key to return to main menu.")
                else:
                    print("Choose a payment option:")
                    for item in self.customers_payments:
                        print("{}. {}".format(item[0], item[2]))
                    pay_choice = input(">")
                    for item in self.customers_payments:
                        if pay_choice == str(item[0]):
                            self.shopping_cart.accept_payment(item, self.active_order)
                            input("Your order is complete! Press any key to return to main menu.")
                        else:
                            input("Not a valid payment choice, payment cancelled.")
            else:
                return
