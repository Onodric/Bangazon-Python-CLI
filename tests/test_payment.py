import unittest
import sys
sys.path.append("../")
from models.payment import *
from db.payment_db_interactor import *

class TestPayment(unittest.TestCase):
    """
    A class for testing all payment methods and database interactions
    Author, Dani Adkins
    """

    @classmethod
    def setUpClass(self):
        self.juan_payment = Payment("Visa", "12345678", 1)
        self.taylor_payment = Payment("Mastercard", "87654321", 2)

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

    def test_payment_can_be_saved(self):
        """
        A test method that tests that a payment can be saved to the database
        Author, Dani Adkins
        """
        saved_payment = PaymentDatabaseInteractor()
        saved_payment.save_payment(self.juan_payment)
        self.assertIn((4, "12345678", "Visa", 1), saved_payment.get_all_payments())



if __name__ == "__main__":
    unittest.main()

