import sqlite3

class OrderDB():
    """
    Class to interact with the Order table of the database

    format of order:
        (pk_order (autoIncrement!), is_closed_int, fk_payment, fk_customer)
    format of payment_method:
        (pk_order (autoIncrement!), name (string), account_number (string), fk_customer)

    Methods:
        get_all_orders
        write_one_order
            arguments: order (as a tuple, see above)
        close_one_order
            arguments:
                order (as a tuple, see above)
                payment_method (as a tuple, see above)
    
    Author: Ben Marks, Ludicrous Ducks
    """

    def get_all_orders(self):
        """
        Method to return all orders in the Order table
        """

        with sqlite3.connect("../db/bangazon.db") as db:
            cursor = db.cursor()

            try:
                cursor.execute("SELECT * FROM Order")
                orders = cursor.fetchall()
                return orders
            except sqlite3.OperationalError:
                return "There was an error reading from the Orders table"


    def write_one_order(self, order):
        """
        Method to write one order to the Order table
        """

        with sqlite3.connect("../db/bangazon.db") as db:
            cursor = db.cursor()

            try:
                cursor.execute("""
                    INSERT INTO Order VALUES ({}, {}, {}, {})
                    """.format(order[0], order[1], order[2], order[3]))
                return orders
            except sqlite3.OperationalError:
                return "There was an error reading from the Orders table"


    def close_one_order(self, order, payment_method):
        """
        Method to return all orders in the Order table
        """
        pass