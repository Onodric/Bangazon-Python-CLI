import sys
sys.path.append("../")
from db.order_db_interactor import OrderDB
from db.line_item_db_interactor import LineItemDB

class ShoppingCart():
    """
    Class defining a customer's shopping cart.

    Initially the cart is open (or "is_closed" is False), and will be
        closed (or "is_closed" is True) upon customer payment processing.

    format of payment_method:
        (pk_order (autoIncrement!), name (string), account_number (string), fk_customer)

    format of product:
        (pk_order (autoIncrement!), name (string), price (number), description (string))


    Author: Ben Marks, Ludicrous Ducks

    Methods:
        get_customer
        get_line_items
        get_payment_method
        get_is_closed
        add_product
        get_cart_total
        accept_payment
    """

    def __init__(self, customer=tuple(), line_items=list(),
            payment_method=None, current_order=tuple()):
        """
        Method to initialize the class with empty default values

        Arguments:
            customer: A tuple containing all customer data
            line_items: A List of tuples, each containing
                product data
            payment_method: A tuple containing the payment
                method data
            is_closed: An integer indicating that an order has
                been paid for (1) or is still open (0)
        """
        self.__customer = customer
        self.__line_items = line_items
        self.__payment_method = payment_method
        self.__is_closed = 0
        self.__current_order = current_order
        self.__line_item_db = LineItemDB()
        self.__order_db = OrderDB()


    def get_customer(self):
        """
        Method to return the customer as a tuple

        Arguments: NONE
        """
        return self.__customer


    def get_line_items(self):
        """
        Method to return line items as a list of tuples

        Arguments: NONE
        """
        return self.__line_items


    def get_payment_method(self):
        """
        Method to return payment method as a tuple

        format of payment_method:
            (pk_order (autoIncrement!), name (string), account_number (string), fk_customer)

        Arguments: NONE
        """
        return self.__payment_method


    def get_is_closed(self):
        """
        Method to return order closed status as an integer:
            open (0) or closed (1)

        Arguments: NONE
        """
        return self.__is_closed


    def add_product(self, product):
        """
        Method to add one line item to the order

        format of productl:
            (pk_order (autoIncrement!), name (string), price (number), description (string))

        Arguments:
            product: a tuple containing one product's data
        """
        self.__line_items.append(product)
        self.__line_item_db.write_one_line_item(self.__current_order, product)


    def get_cart_total(self):
        """
        Method to return the total price of line items in the cart
        
        Arguments: NONE
        """

        total_price = 0

        for item in self.__line_items:
            total_price += item[2]

        return total_price


    def accept_payment(self, payment_method):
        """
        Method to add a payment method to the order

        Arguments:
        payment_method: a tuple containing one payment method's data
        """

        self.__payment_method = payment_method
        self.__is_closed = 1
        self.__order_db.close_one_order(self.__current_order, payment_method)
