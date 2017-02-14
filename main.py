from cli.active_customer_cli import CustomerSelection
from cli.product_cli import ProductPopularity
from cli.customer_creation_cli import CustomerCreation


class MainMenu():
    """Class to contain the Bangazon CLI user input loop. After running the
     file, the MainMenu.run() method is called.

    Author: Sam Phillips
    """

    def run(self):
        """
        This method prompts the user to make selections which will navigate
         them to different interfaces to access the functionality of the
          Bangazon CLI. Users also have the option of exiting the program
           altogether.
        """
        running = True

        while running:
            print("""\n\n\n\n\n\n""")
            selected_option = input("""
*********************************************************
**  Welcome to Bangazon! Command Line Ordering System  **
*********************************************************
1. Create a customer account
2. Choose active customer
3. Create a payment option
4. Add product to shopping cart
5. Complete an order
6. See product popularity
7. Leave Bangazon!
>""")

            if selected_option == "1":
                customer_creation = CustomerCreation()
                customer_creation.run()
                print("Create a customer account")
            elif selected_option == "2":
                choose_customer = CustomerSelection()
                choose_customer.run()
            elif selected_option == "3":
                print("Create a payment option")
            elif selected_option == "4":
                print("Add product to shopping cart")
            elif selected_option == "5":
                print("complete an order")
            elif selected_option == "6":
                product_pop = ProductPopularity()
                product_pop.run()
            elif selected_option == "7":
                print("goodbye")
                running = False


bangazon_interface = MainMenu()
bangazon_interface.run()



