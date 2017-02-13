import sys
sys.path.append("../")
from models.customer import Customer
from db.customer_db_interactor import Customer_db

class CustomerCreation():
    """
    Class to contain the Bangazon Customer Creation view. The view itself, 
    as well as the ability to create a customer, may be accessed by running 
    the CustomerCreation.run() method.

    Methods:
        run
        save_customer

    Author: Sam Phillips 
    """

    def run(self):
        """
        CustomerCreation.run() method prompts the user to input all of the 
        information needed to create a new instance of the Customer class. 
        Once the information has been provided by the user, it is used to 
        create a new instance of the Customer classs which is then passed 
        to the save_new_customer() method found in an instance of the 
        Customer_db class.

        Author: Sam Phillips
        """
        database_interactor = Customer_db()

        print("""\n\n\n\n\n\n""")
        print("Enter customer name")
        name = input(">")
        print("Enter street address")
        street_address = input(">")
        print("Enter city")
        city = input(">")
        print("Enter state")
        state = input(">")
        print("Enter postal code")
        postal_code = int(input(">"))
        print("Enter phone number")
        phone_number = input(">")

        new_customer = Customer(name, street_address, city, state, 
            postal_code, phone_number)
        database_interactor.save_new_customer(new_customer)

    