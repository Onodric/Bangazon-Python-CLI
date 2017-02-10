import unittest
import sys
sys.path.append("../")
from models.shopping_cart import ShoppingCart
from db.order_db_interactor import OrderDB


class TestShoppingCart(unittest.TestCase):
    """
    A test suite for the Shopping cart Feature of Bangazon CLI

    Author: Ben Marks, Ludicrous Ducks

    Methods:
    Model_Class
        test_current_cart_should_be_ShoppingCart_object

        test_get_customer_should_return_attached_customer
        test_get_line_items_should_return_all_line_items
        test_get_payment_method_should_return_payment_method
        test_get_is_closed_should_return_is_closed_flag
        
        test_ShoppingCart_should_add_product
        test_ShoppingCart_should_return_cart_total_price
        test_ShoppingCart_should_be_able_to_be_closed
    DB_Interactors
        test_OrderDB_should_return_all_orders
        test_OrderDB_should_write_new_order
        test_OrderDB_should_update_order_status
        test_LineItemDB_should_return_all_line_items
        test_LineItemDB_should_write_new_line_item
    """
    
    @classmethod
    def setUpClass(self):
        """
        Method to setup global values needed for all tests
        """
        print('Set up class')
        # Create an instance of the ShoppingCart that can be used in all
        #   tests
        self.current_customer = (1, "Me", "500 Interstate Blvd", "Nashville",
            "TN", "11111", "(615) 123-4567", 1)
        # Create an instance of a product that can be used in all tests
        # Product tuple will need alteration
        self.product1 = (1, "Widget", 5, "Widget")
        self.product2 = (2, "FooBar", 10, "foobar widget")
        self.payment_method = (1, "Visa", "1234567812345678", 1)
        self.current_cart = ShoppingCart(customer=self.current_customer)


    def test_current_cart_should_be_ShoppingCart_object(self):
        """
        Method to test whether the ShoppingCart object is created correctly
        """
        self.assertIsInstance(self.current_cart, ShoppingCart)
        

    def test_get_customer_should_return_attached_customer(self):
        """
        Method to test whether the ShoppingCart object can return the active
            customer
        """
        self.assertEqual(self.current_cart.get_customer(),
            self.current_customer)


    def test_get_payment_method_should_return_payment_method(self):
        """
        Method to test whether the ShoppingCart object return the payment
            method
        """
        self.assertEqual(self.current_cart.get_payment_method(), ())


    def test_get_is_closed_should_return_is_closed_flag(self):
        """
        Method to test whether the ShoppingCart object can return the
            is_closed flag
        """
        self.assertFalse(self.current_cart.get_is_closed())


    def test_ShoppingCart_should_add_product(self):
        """
        Method to test whether the ShoppingCart object can add a product
        """
        self.current_cart = ShoppingCart()
        self.assertEqual(self.current_cart.get_line_items(), [])
        self.current_cart.add_product(self.product1)
        self.assertEqual(self.current_cart.get_line_items(), [self.product1])
        self.assertEqual(self.current_cart.get_line_items(), [self.product1, self.product2])


    def test_get_line_items_should_return_all_line_items(self):
        """
        Method to test whether the ShoppingCart object can return all line
            items
        """
        self.current_cart.add_product(self.product2)
        self.assertEqual(self.current_cart.get_line_items,
            [self.product1, self.product2])


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
        self.assertEqual(self.current_cart.get_payment_method(), [(1, "Visa", "1234567812345678", 1)])
        self.assertTrue(self.current_cart.order_is_closed())


    def test_OrderDB_should_return_all_orders(self):
        """
        Method to test whether the Order DB Interactor can return all orders
        """


    def test_OrderDB_should_write_new_order(self):
        """
        Method to test whether the Order DB Interactor can create a new order
        """


    def test_OrderDB_should_update_order_status(self):
        """
        Method to test whether the Order DB Interactor can update an order
        """


    def test_LineItemDB_should_write_new_line_item(self):
        """
        Method to test whether the LineItem DB Interactor can write a new line item
        """


    def test_LineItemDB_should_return_all_line_items(self):
        """
        Method to test whether the LineItem DB Interactor can return all line items
        """


if __name__ == '__main__':
    unittest.main()
