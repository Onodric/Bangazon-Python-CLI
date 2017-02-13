import sqlite3


class PaymentDatabaseInteractor():
    """
    This is a class for payment database interaction
    """

    def save_payment(self, payment):
        """
        This is a method to save payment data
        """
        with sqlite3.connect('../db/bangazon.db') as pago:
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
        """
        This is a method to return all payment data
        """
        with sqlite3.connect('../db/bangazon.db') as pago:
            cursor = pago.cursor()

        try:
            cursor.execute("""
                SELECT * FROM Payment
                """)
        except sqlite3.OperationalError:
            return False

        all_payments = cursor.fetchall()
        return all_payments








