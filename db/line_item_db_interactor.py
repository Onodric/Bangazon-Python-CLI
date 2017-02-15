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
        with sqlite3.connect(configuration.database_path) as db:
            cursor = db.cursor()

            cursor.execute("SELECT * FROM LineItem")
            line_items = cursor.fetchall()
            return line_items


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
