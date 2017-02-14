import sqlite3
import sys
sys.path.append('../')
import configuration

class LineItemDB():
    """
    Class for writing to the LineItem table in bangazon.db

    format of order:
        (pk_order (autoIncrement!), is_closed_int, fk_payment, fk_customer)
    format of product:
        (pk_order (autoIncrement!), name (string), price (number), description (string))


    Author: Ben Marks, Ludicrous Ducks
    
    Methods:
        get_all_line_items
        write_one_line_item
            Argument: line_item, a tuple of line item data
    """

    def get_all_line_items(self):
        """
        Method to return all lineitems in the LineItem table
        """
        print(configuration.database_path)
        with sqlite3.connect(configuration.database_path) as db:
            cursor = db.cursor()

            try:
                cursor.execute("SELECT * FROM LineItem")
                line_items = cursor.fetchall()
                return line_items
            except sqlite3.OperationalError:
                pass
                # return "There was an Error reading from the Line Items Table"

    def write_one_line_item(self, order, product):
        """
        Method to write one line item to the LineItem table
        """
        
        with sqlite3.connect(configuration.database_path) as db:
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO LineItem VALUES (null, {}, {})
                """
                .format(order[0], product[0]))
