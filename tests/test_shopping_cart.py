import unittest
import sys
sys.path.append("../")
from models.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    """
    A test suite for the Shopping cart Feature of Bangazon CLI

    Methods:
    test_current_cart_should_be_ShoppingCart_object
    test_ShoppingCart_should_add_product
    test_ShoppingCart_should_return_cart_total_price
    test_ShoppingCart_should_be_able_to_be_closed
    """
    
    @classmethod
    def setUpClass(self):
        """
        Method to setup global values needed for all tests
        """
        print('Set up class')
        # Create an instance of the ShoppingCart that can be used in all tests
        self.current_cart = ShoppingCart()
        # Create an instance of a product that can be used in all tests
        # Product tuple will need alteration
        self.product1 = (1, "Widget", 5)
        self.product2 = (2, "FooBar", 10)
        self.payment_method = (1, "Visa", "1234567812345678")


    def test_current_cart_should_be_ShoppingCart_object(self):
        """
        Method to test whether the ShoppingCart object id created correctly
        """
        self.assertIsInstance(self.current_cart, ShoppingCart)
        

    def test_ShoppingCart_should_add_product(self):
        """
        Method to test whether the ShoppingCart object can add a product
        """
        current_cart = ShoppingCart()
        self.assertEqual(current_cart.get_all_products(), [])
        current_cart.add_product(self.product1)
        self.assertEqual(current_cart.get_all_products(), [self.product1])
        current_cart.add_product(self.product2)
        self.assertEqual(current_cart.get_all_products(), [self.product1, self.product2])


    def test_ShoppingCart_should_return_cart_total_price(self):
        """
        Method to test whether the shopping cart can return the total
        """
        total = self.current_cart.get_cart_total()
        self.assertEqual(total, 15)

    def test_ShoppingCart_should_accept_payment_method(self):
        """
        Method to test whether the shopping cart can be closed
        """
        self.current_cart.accept_payment(self.payment_method)
        self.assertEqual(self.current_cart.get_payment_method(), (1, "Visa", "1234567812345678"))
        self.assertTrue(self.current_cart.order_is_closed())


if __name__ == '__main__':
    unittest.main()
