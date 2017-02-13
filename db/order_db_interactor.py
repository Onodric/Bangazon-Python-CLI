import sqlite3
import sys
sys.path.append('../')
import configuration

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

        with sqlite3.connect(configuration.database_path) as db:
            cursor = db.cursor()

            try:
                cursor.execute("SELECT * FROM Orders")
                orders = cursor.fetchall()
                return orders
            except sqlite3.OperationalError:
                pass
                # return "There was an error reading from the Orders table"


    def write_one_order(self, input_order):
        """
        Method to write one order to the Orders table
        """

        with sqlite3.connect(configuration.database_path) as db:
            cursor = db.cursor()

            # try:
            cursor.execute("""
                INSERT INTO Orders VALUES (null, {}, {}, {})
                """
                .format(0, 'null', input_order[2]))
            # except sqlite3.OperationalError:
                # pass
                # return "There was an error writing to the Orders table"


    def close_one_order(self, input_order, payment_method):
        """
        Method to return all orders in the Order table
        """

        with sqlite3.connect(configuration.database_path) as db:
            cursor = db.cursor()

            try:
                cursor.execute("""
                    UPDATE Orders SET is_closed=1,
                        payment_id=payment_method[0],
                        customer_id=input_order[3]
                    WHERE orders_id=input_order[0]""")
            except sqlite3.OperationalError:
                pass
                # return "There was an error writing to the Orders table"

