import sys
sys.path.append("../")
from db.order_db_interactor import *
from db.line_item_db_interactor import *
from db.customer_db_interactor import *
from db.product_db_interactor import *
from db.payment_db_interactor import *

class ShoppingCartCLI():
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
        run
    """

    pass