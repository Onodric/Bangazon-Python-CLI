import sqlite3



class ProductData():
    """
        This is a class for product data 
    """

    def save_product(self, product):
        """
        This is a method to save product data
        """
        with sqlite3.connect('bangazon.db') as proc:
            cursor = proc.cursor()

            try: 
                cursor.execute("SELECT * FROM Product")
                users = cursor.fetchall()
            except sqlite3.OperationalError:
                cursor.execute("""
                CREATE TABLE `Product`
                (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price NUMBER NOT NULL,
                    description TEXT NOT NULL
                )
                """)
            cursor.execute("""
            INSERT INTO Product VALUES (null, '{}', '{}', '{}')
            """.format(
                "coconut oil shampoo", 7.99, "silky smoothe hair treatment shampoo"
                )
            )
            proc.commit()


    def get_product(self, product_id):
        """
        This is a method to get product data
        """

        with sqlite3.connect('bangazon.db') as proc:
            cursor = proc.cursor()

            cursor.execute("""SELECT * FROM Product p
                WHERE p.id = {}
                """.format(product_id))
            products = cursor.fetchall()
            products = list()


        return products


