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


    def get_active_order(self):
        """
        Method to return the current active order, or to create one if none are open

        Arguments: None 
        """

        current_customer = Customer_db.get_active()[0]
        all_orders = self.order.get_all_orders()
        active_order = ()
        if len(all_orders) < 1:
            new_order = (0, None, current_customer[0])
            self.order.write_one_order(new_order)
            all_orders = self.order.get_all_orders()
        for item in all_orders:
            if item[-1] == current_customer[0] and item[1] == 0:
                active_order = item
        if active_order == ():
            new_order = (0, None, current_customer[0])
            self.order.write_one_order(new_order)
            all_orders = self.order.get_all_orders()
            for item in all_orders:
                if item[-1] == self.current_customer[0] and item[1] == 0:
                    active_order = item
                    return active_order
        return active_order


    def get_current_line_items(self, order):
        """
        Method to return the current active order, or to create one if none are open
        
        Arguments: the current order as a tuple 
        """

        existing_line_items = []
        if len(self.all_line_items) > 0:
            for item in self.all_line_items:
                if item[1] == order[0]:
                    self.existing_line_items.append(item)
        return existing_line_items


    def get_payment_methods(self):
        """
        Method to return the active user's payment methods
        """

        current_customer = Customer_db.get_active()[0]
        customers_payments = []
        all_payments = self.payment.get_all_payments()
        for item in all_payments:
            if item[-1] == current_customer[0]:
                self.customers_payments.append(item)


    def add_line_item(self):
        """
        CLI Method for option 4 of the main menu
        """

        current_customer = Customer_db.get_active()[0]
        if type(current_customer) != tuple
            input("Please choose an active customer")
            break

        active_order = get_active_order()
        all_products = self.products.get_all_products()
        shopping_cart = ShoppingCart(customer=current_customer, line_items=get_current_line_items(active_order), current_order=active_order)
        
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
                        shopping_cart.add_product(active_order, item)


    def pay_for_cart(self):
        """
        CLI Method for option 5 of the main menu
        """

        current_customer = Customer_db.get_active()[0]
        if type(current_customer) != tuple
            input("Please choose an active customer")
            break

        active_order = get_active_order()
        payment_methods = get_payment_methods()
        shopping_cart = ShoppingCart(customer=current_customer, line_items=get_current_line_items(active_order), current_order=active_order)
        line_items = shopping_cart.get_line_items()
        
        if line_items == []:
            input("Please add some products to your order first. Press any key to return to main menu.")
        else:
            total = 0
            for product in self.all_products:
                for item in line_items:
                    if product[0] == item[-1]:
                        total += product[1]
            print("Your order total is ${:.2f}. Ready to purchase?\n(Y/N) ".format(total))
            choice = input(">")
            if choice == "Y" or choice == "y":
                if payment_methods == []:
                    input("Please add a payment method to your account first. Press any key to return to main menu.")
                else:
                    print("Choose a payment option:")
                    for item in payment_methods:
                        print("{}. {}".format(item[0], item[2]))
                    pay_choice = input(">")
                    paid = False
                    for item in payment_methods:
                        if pay_choice == str(item[0]):
                            shopping_cart.accept_payment(item, active_order)
                            paid = True
                            input("Your order is complete! Press any key to return to main menu.")
                    if paid == False:
                        input("Not a valid payment choice, payment cancelled.")
            else:
                return
