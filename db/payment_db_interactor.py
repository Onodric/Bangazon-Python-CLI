import sqlite3
from models.payment import Payment


class PaymentDatabaseInteractor():

    # def create_payment(self, payment):
    #     with sqlite3.connect("bangazon.db") as pago:
    #         cursor = pago.cursor()

    #         try:
    #             cursor.execute("SELECT * FROM Payment")
    #             payment = cursor.fetchall()
    #         except sqlite3.OperationalError:
    #             cursor.execute("""
    #             CREATE TABLE `Payment`
    #                 (
    #                     payment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #                     account_number INTEGER NOT NULL,
    #                     payment_type TEXT NOT NULL,
    #                     customer_id INTEGER NOT NULL FOREIGN KEY
    #                 )
    #             """)

    #             cursor.execute("""
    #             INSERT INTO Payment VALUES (null, ?, ?, null)
    #             """.format(
    #                         payment.get_payment_type(),
    #                         payment.get_account_number()))





# payment as argument should be instance of payment model

    def save_payment(self, payment):
        print(payment)
        with sqlite3.connect("/Users/daniadkins/workspace/group-projects/bangazon_cli/bangazon-cli/db/bangazon.db") as pago:
            cursor = pago.cursor()

        # try:
            cursor.execute("""
                INSERT INTO Payment VALUES (null, '{}', '{}', {})
            """.format(
                        payment.get_account_number(),
                        payment.get_payment_type(),
                        payment.get_customer_id()))
        # except sqlite3.OperationalError:
        #     return False


    def get_all_payments(self):
        with sqlite3.connect("/Users/daniadkins/workspace/group-projects/bangazon_cli/bangazon-cli/db/bangazon.db") as pago:
            cursor = pago.cursor()

        try:
            cursor.execute("""
                SELECT * FROM Payment
                """)
        except sqlite3.OperationalError:
            return False

        all_payments = cursor.fetchall()
        return all_payments








