import sqlite3
# import sys
# sys.path.append("../")
import configuration

class PaymentDatabaseInteractor():
    """
    This is a class for payment database interaction
    Author: Dani Adkins
    """



    def save_payment(self, payment):
        """
        This is a method to save payment data
        Author: Dani Adkins

        """
        with sqlite3.connect(configuration.database_path) as pago:
            cursor = pago.cursor()

            try:
                cursor.execute("SELECT * FROM Payment")
                payments = cursor.fetchall()
            except sqlite3.OperationalError:
                cursor.execute("""
                CREATE TABLE `Payment`
                (
                    payment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    account_number TEXT NOT NULL,
                    payment_type TEXT NOT NULL,
                    customer_id INTEGER NOT NULL,
                    FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`customer_id`)
                )
                """)
            cursor.execute("""
                INSERT INTO Payment VALUES (null, '{}', '{}', {})
                """.format(
                        payment.get_account_number(),
                        payment.get_payment_type(),
                        payment.get_customer_id()))

            pago.commit()

    def get_all_payments(self):
        """
        This is a method to return all payment data
        Author: Dani Adkins
        """
        with sqlite3.connect(configuration.database_path) as pago:
            cursor = pago.cursor()

        try:
            cursor.execute("""
                SELECT * FROM Payment
                """)
        except sqlite3.OperationalError:
            return False

        all_payments = cursor.fetchall()
        return all_payments








