import sqlite3

class Payment:
    """
    A class for payment that has the following methods on it:
        get_payment_type
        get_account_number
        get_customer_id
        get_full_payment_info
        get_full_payment_info_current_account_current_user
        set_payment_info
    Author, Dani Adkins
    """

    def __init__(self, payment_type, account_number, customer_id):
        self.__payment_type = payment_type
        self.__account_number = account_number
        self.__customer_id = customer_id
        self.__full_payment_info_current_account_current_user = [(1 ,"Visa", "12345678"), (2, "MC", "34534")]

    def get_payment_type(self):
        """
        A method that will return the payment type of an instance of payment
        Author, Dani Adkins
        """
        return self.__payment_type

    def get_account_number(self):
        """
        A method that will return the account number of an instance of payment
        Author, Dani Adkins
        """
        return self.__account_number

    def get_customer_id(self):
        """
        A method that will return the customer id of an instance of payment
        Author, Dani Adkins
        """
        return self.__customer_id

    def get_full_payment_info(self):
        """
        A method that will return a string with full payment information for an instance of payment
        Author, Dani Adkins
        """
        return "{} {}".format(self.__payment_type, self.__account_number)

    def set_payment_info(self):
        """
        A metho that will set the payment type and account number information for an instance of payment
        Author, Dani Adkins
        """
        self.__payment_type
        self.__account_number

    def get_full_payment_info_current_account_current_user(self):
        """
        A method that will return a string with full payment info for the current accound and current user for an instance of payment
        Author, Dani Adkins
        """
        return self.__full_payment_info_current_account_current_user






