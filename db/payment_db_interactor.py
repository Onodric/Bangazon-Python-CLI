import sqlite3
from .filepath import *
from models.payment import Payment


class PaymentDatabaseInteractor():


    def save_payment(self, payment):
        with sqlite3.connect(filepath) as pago:
            cursor = pago.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Payment VALUES (null, '{}', '{}', {})
                """.format(
                            payment.get_account_number(),
                            payment.get_payment_type(),
                            payment.get_customer_id()))

            except sqlite3.OperationalError:
                return False

    def get_all_payments(self):
        with sqlite3.connect(filepath) as pago:
            cursor = pago.cursor()

        try:
            cursor.execute("""
                SELECT * FROM Payment
                """)
        except sqlite3.OperationalError:
            return False

        all_payments = cursor.fetchall()
        return all_payments








