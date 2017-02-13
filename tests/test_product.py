import unittest
import os
import sqlite3
import sys
sys.path.append("../")
from models.Product import Product
from db.product_db_interactor.py import ProductData




class TestProduct(unittest.TestCase):
    """
    Tests for class Product in model file
    Tests for class ProductData in db to save product,  get the saved product and get all saved products


    Methods:
    test_product_has_all_the_attributes
    test_product_attributes_can_be_retrieved
    test_product_can_be_saved
    test_can_get_all_saved_product

    Author: Julia Kim-Chung
    """
    @classmethod
    def setUpClass(self):
        """
        Method to setup global values needed for all tests

        """
        self.guitar   = Product('Electric Guitar', 3.50, 'Fun way to make music.')
        self.shampoo  = Product("Coconut Oil Shampoo", 7.99, "silky smoothe hair treatment shampoo")

    def test_product_has_all_the_attributes(self):
        """
        Method to test if the product has price, name, description as attributes

        """
        self.assertIsNotNone(self.shampoo.price)
        self.assertIsNotNone(self.shampoo.name)
        self.assertIsNotNone(self.shampoo.description)

    def test_product_attributes_can_be_retrieved(self):
        """
        Method to test if each get_name, get_price, get_desciption method can retrieve each attributes
        """
        self.assertEqual(self.shampoo.get_name(), "Coconut Oil Shampoo" )
        self.assertEqual(self.shampoo.get_price(), 7.99)
        self.assertEqual(self.shampoo.get_description(),"silky smoothe hair treatment shampoo" )

    def test_product_can_be_saved(self):
        """
        Method to test if the product can be saved in db as tuple

        """
        productData = ProductData() 
        productData.save_product(self.shampoo)
        data = productData.get_all_products()
        test_product = data[len(data)-1]
        self.assertIsInstance(data, list)
        test_index = len(data)
        self.assertEqual(test_product, (test_index,7.99, "Coconut Oil Shampoo"))
    
    def test_can_get_all_saved_product(self):
        """
        Method to test if all saved product can be retrieved with the attibutes of id, price, name

        """
        prodData = ProductData()
        prodData.save_product(self.guitar)
        data = prodData.get_all_products()

        data_index_1 = len(data)
        self.Electric   = Product('Electric Guitar', 5.50, 'Fun way to make music.')
        prodData.save_product(self.Electric)
        data = prodData.get_all_products()

        data_index_2 = len(data)

        self.assertEqual(data_index_2, data_index_1+1 )
        self.assertIn((data_index_2, 5.50,'Electric Guitar'), data)
        

if __name__ =='__main__':
     unittest.main()