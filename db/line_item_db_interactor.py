import sqlite3

class LineItemDB():
    """
    Class for writing to the LineItem table in bangazon.db

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
        pass

        # with sqlite3.connect("../db/bangazon.db") as db:
        #     cursor = db.cursor()

        #     try:
        #         cursor.execute("SELECT * FROM LineItem")
        #         line_items = cursor.fetchall()
        #         return line_items
        #     except sqlite3.OperationalError:
        #         return False


    def write_one_line_item(self, order, product):
        """
        Method to write one line item to the LineItem table
        """
        pass
        
        # with sqlite3.connect("../db/bangazon.db") as db:
        #     cursor = db.cursor()

        #     cursor.execute("""
        #         INSERT INTO LineItem VALUES ('{}', '{}', '{}')
        #         """.format(None, line_item[0], line_item[1], line_item[2])