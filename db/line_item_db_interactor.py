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

    def get_all_line_items():
        """
        Method to return all lineitems in the LineItem table
        """
        with sqlite3.connect("bangazon.db") as db:
            cursor = db.cursor()

            try:
                cursor.execute("SELECT * FROM LineItem")
                line_items = cursor.fetchall()
                return line_items
            except sqlite3.OperationalError:
                return False


    def write_one_line_item(self, line_item):
        """
        Method to write one line item to the LineItem table
        """

        with sqlite3.connect("bangazon.db") as db:
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO LineItem VALUES ('{}', '{}', '{}')
                """.format(None,
                            line_item[]
                            line_item.get_last_name(),
                            line_item.get_email(),
                            user.get_username()))