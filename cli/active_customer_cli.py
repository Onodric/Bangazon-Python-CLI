import sys
sys.path.append("../")
from db.customer_db_interactor import Customer_db

class CustomerSelection():
    """Class to contain the Bangazon Customer Selection view. After running
     the file, the CustomerSelection.run() method is called. 

    Author: Sam Phillips
    """
    def run(self):
        """
        CustomerSelection.run() method prompts the user to select a customer 
        from a list of customers. This customer is then set as the active 
        customer by first making a call to the database to make sure that no 
        other customers are active. It then makes a call to the database to 
        set the selected customer as active.
        """

        # create an instance of the customer database interactor
        customer_db = Customer_db()

        # retrieve a list of customers
        all_customers = Customer_db.get_all_customers()
        
        # print the options to the command line and wait for the user to
        # select one
        print("""\n\n\n\n\n\n""")
        print("Which customer will be active?")
        for index, customer in enumerate(all_customers):
            print("{}. {}".format(index + 1, customer[1]))
        selection_index = input(">")

        # take the user selection and, if it's a valid option, update the 
        # database to reflect that customer as the active customer
        try:
            customer_index = int(selection_index) - 1
            if customer_index >= 0: 
                if customer_index < len(all_customers):
                    selected_customer = all_customers[customer_index]
                    selected_customer_id = selected_customer[0]
                    customer_db.update_active_false()
                    customer_db.update_active_true(selected_customer_id)

        except Exception as e:
            print("Invalid customer selection")