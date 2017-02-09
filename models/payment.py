# import sqlite3

class Payment():

    def __init__(self, customer_id, payment_type, account_number):
        self.__customer_id = customer_id
        self.__payment_type = payment_type
        self.__account_number = account_number
        self.__full_payment_info_current_account_current_user = [(1 ,"Visa", "12345678"), (2, "MC", "34534")]

    def get_payment_type(self):
        return self.__payment_type

    def get_account_number(self):
        return self.__account_number

    def get_full_payment_info_current_account_current_user(self):
        return self.__full_payment_info_current_account_current_user






