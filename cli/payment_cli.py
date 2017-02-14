import sys
sys.path.append("../")
from db.payment_db_interactor import *
from models.payment import *
from db.customer_db_interactor import Customer_db


class PaymentSelection():
    """Class to contain the Bangazon Payment Selection view. After running this file the PaymentSelection run method is called.
    Author: Dani Adkins
    """

    def run(self):
        """
        PaymentSelection.run() method prompts the user to enter their payment type and account number information. The payment information is then saved to the database.
        """
        print("""\n\n\n\n\n\n""")

        try:
            customer_on_payment = Customer_db.get_active()[0]
            customer_id = customer_on_payment[0]

            print("Enter payment type (Visa, Mastercard, etc.):")
            payment_type = input(">")
            print("You entered", payment_type)

            print("Enter account number:")
            account_number = input(">")
            print("You entered", account_number)

            pay = Payment(payment_type, account_number, customer_id)
            PaymentDatabaseInteractor().save_payment(pay)
        except:
            print("Please choose an active customer")
