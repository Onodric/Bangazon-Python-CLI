import sqlite3

class Product():
    """
        This is a class to define a Product 
    """
    def __init__(self, name, price, description):
        """
            product has name, price, description as attributes
        """
        self.name = name
        self.price = price
        self.description = description

    def get_name(self):
        """
        Method to return the product name
        """
        return self.name

    def get_price(self):
        """
        Method to return the product price
        """
        return self.price

    def get_description(self):
        """
        Method to return the product description
        """
        return self.description


    

