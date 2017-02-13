import sys
sys.path.append("../")
from db.payment_db_interactor import *
from models.payment import *

class PaymentSelection():
    """Class to contain the Bangazon Payment Selection view. After running this file the PaymentSelection run method is called.
    Author: Dani Adkins
    """

    def run(self, customer_id):
        """
        PaymentSelection.run() method prompts the user to enter their payment type and account number information. The payment information is then saved to the database.
        """
        payment_type = input("Enter payment type (Visa, Mastercard, etc.):")
        print("You entered", payment_type)

        account_number = input("Enter account number:")
        # correct_account_number = input("Is this correct?")
        print("You entered", account_number)

        pay = Payment(payment_type, account_number, customer_id)
        PaymentDatabaseInteractor().save_payment(pay)


##STRETCH GOAL: need an if statement that says in human terms: if for customer id there is a card entered with payment type and account number the same then spit out an error that says "You already entered that payment type!"

if __name__ == '__main__':
    enter_payment = PaymentSelection()
    enter_payment.run(1)