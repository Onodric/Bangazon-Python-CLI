import sqlite3

class LineItemDB():
    """
    """

    def get_all_line_items():
        pass

    def write_one_line_item(self, line_item):
        with sqlite3.connect("bangazon.db") as db:
            cursor = db.cursor()

            cursor.execute("""
                INSERT INTO LineItem VALUES ({}, '{}', '{}', '{}', '{}')
                """.format(None,
                            user.get_first_name(),
                            user.get_last_name(),
                            user.get_email(),
                            user.get_username()))