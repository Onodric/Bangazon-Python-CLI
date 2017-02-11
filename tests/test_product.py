import unittest
import os
import sqlite3
import sys
sys.path.append("../")
from models.Product import Product
from db.product_data import ProductData



class TestProduct(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.shampoo  = Product("Coconut Oil Shampoo", "7.99", "silky smoothe hair treatment shampoo")
        self.guitar   = Product('Electric Guitar', 3.50, 'Fun way to make music.')

    def test_product_has_all_the_attributes(self):
        self.assertIsNotNone(self.shampoo.price)
        self.assertIsNotNone(self.shampoo.name)
        self.assertIsNotNone(self.shampoo.description)

    def test_product_attributes_can_be_retrieved(self):
        self.assertEqual(self.shampoo.get_name(), "Coconut Oil Shampoo" )
        self.assertEqual(self.shampoo.get_price(), "7.99")
        self.assertEqual(self.shampoo.get_description(),"silky smoothe hair treatment shampoo" )

    def test_product_can_be_saved(self):
        productData = ProductData() 
        productData.save_product(self.shampoo)
        data = productData.get_product(1)
        self.assertIsInstance(data, list)
        for el in data:
        
            self.assertEqual(el, (1, "coconut oil shampoo", 7.99, "silky smoothe hair treatment shampoo"))

    
    def test_can_get_all_saved_product(self):
        prodData = ProductData()
        prodData.save_product(self.guitar)
        data = prodData.get_all_products()
        self.assertEqual(len(data), 62)
        self.assertIn((52, 3.50,'Electric Guitar'), data)
        

if __name__ =='__main__':
     unittest.main()