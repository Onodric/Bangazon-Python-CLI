class ShoppingCart():
    """
    Class defining a customer's shopping cart.
    
    Initially the cart is open (or "is_closed" is False), and will be
        closed (or "is_closed" is True) upon customer payment processing.

    Methods:
        get_all_products
        add_product
        get_cart_total
        accept_payment
        get_payment_method
        order_is_closed
    """

    def __init__(self, customer=tuple(), line_items=list(),
            payment_method=tuple()):
        """
        Method to initialize the class with empty default values

        Arguments:
            customer: A tuple containing all customer data
            line_items: A List of tuples, each containing
                product data
            payment_method: A tuple containing the payment
                method data
            is_closed: A boolean indicating that an order has
                been paid for and has been processed
        """
        self.__customer = customer
        self.__line_items = line_items
        self.__payment_method = payment_method
        self.__is_closed = False


    def get_all_products(self):
        """
        Method to return line items as a list of tuples

        Arguments: NONE
        """
        return self.__line_items


    def add_product(self, product):
        """
        Method to add one line item to the order

        Arguments:
            product: a tuple containing one product's data
        """
        self.__line_items.append(product)


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
        self.__is_closed = True


    def get_payment_method(self):
        """
        Method to return the cart's payment method as a tuple
        
        Arguments: NONE
        """
        return self.__payment_method


    def order_is_closed(self):
        """
        Method to return the cart's closed status as a boolean
        
        Arguments: NONE
        """

        return self.__is_closed