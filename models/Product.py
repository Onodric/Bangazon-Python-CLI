import sqlite3

class Product():
    """
        This is a class for Product
    """
    def __init__(self, name, price, description):
        """
            product has name, price, description as attributes
        """
        self.name = name
        self.price = price
        self.description = description

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description


    

