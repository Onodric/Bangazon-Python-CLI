import unittest
import sys
sys.path.append("../")
from models.payment import *

class TestPayment(unittest.TestCase):
    """
    A class for testing all payment methods and database interactions
    Author, Dani Adkins
    """

    @classmethod
    def setUpClass(self):
        self.juan_payment = Payment(1, "Visa", "12345678", 1)
        self.taylor_payment = Payment(2, "Mastercard", "87654321", 2)

    def test_user_payment_is_a_user_payment(self):
        """
        A test method which tests that user payment is an instance of user payment
        Author, Dani Adkins
        """
        self.assertIsInstance(self.juan_payment, Payment)
        self.assertIsInstance(self.taylor_payment, Payment)

     def test_payment_has_all_fields_filled_in(self):
        """
        A test method which tests that all fields Payment are entered by the user
        Author, Dani Adkins
        """
        self.assertIsNotNone(self.juan_payment.get_payment_type())
        self.assertIsNotNone(self.juan_payment.get_account_number())

    def test_user_has_entered_payment_credentials(self):
        """
        A test method which tests that user has entered payment credentials
        Author, Dani Adkins
        """
        self.assertEqual(self.juan_payment.get_payment_type(), "Visa")
        self.assertEqual(self.juan_payment.get_account_number(), "12345678")

    def test_can_get_full_payment_info_current_account_and_current_user(self):
        """
        A test method which tests that the full payment for current account matches that which is returned
        Author, Dani Adkins
        """
        self.assertIn((1, "Visa", "12345678"), self.juan_payment.get_full_payment_info_current_account_current_user())

    ##test that you're getting a tuple with the expected information

     # def test_can_get_payment_info_as_tuple(self):
     #    """
     #    A method that tests that payment information is returned as the expected tuple
     #    Author, Dani Adkins
     #    """
     #    # payment_method = get_payment()
     #    payment_method = [(1, "Visa", "12345678", 1)]
     #    self.assertIs(type(payment_method), tuple)
     #    self.assertIs(type(payment_method[0]), int)
     #    self.assertIs(type(payment_method[1]), str)
     #    self.assertIs(type(payment_method[2]), str)
     #    self.assertIs(type(payment_method[3]), int)



    def test_payment_can_be_saved(self):
        """
        A test method that tests that a payment can be saved to the database
        Author, Dani Adkins
        """
        saved_payment = PaymentDatabaseInteractor()
        saved_payment.save_payment(self.juan_payment)
        self.assertIsIn((1, "Visa", "12345678", 1), saved_payment.get_all_payments())







if __name__ == "__main__":
    unittest.main()









  # def test_product_has_all_the_attributes(self):
  #       self.assertIsNotNone(self.shampoo.price)
  #       self.assertIsNotNone(self.shampoo.name)
  #       self.assertIsNotNone(self.shampoo.description)

  #   def test_product_attributes_can_be_retrieved(self):
  #       self.assertEqual(self.shampoo.get_name(), "Coconut Oil Shampoo" )
  #       self.assertEqual(self.shampoo.get_price(), "7.99")
  #       self.assertEqual(self.shampoo.get_description(),"silky smoothe hair treatment shampoo" )

  #   def test_product_can_be_saved(self):
  #       productData = ProductData()
  #       productData.save_product(self.shampoo)
  #       data = productData.get_product(1)
  #       for el in data:

  #           self.assertIsInstance(data, tuple)
  #           self.assertEqual(el, (1, "coconut oil Shampoo", 7.99, "silky smoothe hair treatment shampoo"),)

