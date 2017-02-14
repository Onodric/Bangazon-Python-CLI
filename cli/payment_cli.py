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

        try:
            customer_on_payment = Customer_db.get_active()[0]
            customer_id = customer_on_payment[0]

            payment_type = input("Enter payment type (Visa, Mastercard, etc.):")
            print("You entered", payment_type)

            account_number = input("Enter account number:")
            print("You entered", account_number)

            pay = Payment(payment_type, account_number, customer_id[0])
            PaymentDatabaseInteractor().save_payment(pay)
        except:
            print("Please choose an active customer")


# if __name__ == '__main__':
#     payment_create = PaymentSelection()
#     payment_create.run()