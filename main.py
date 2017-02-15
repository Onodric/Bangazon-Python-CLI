from cli.active_customer_cli import CustomerSelection
from cli.shopping_cart_cli import ShoppingCartCLI
from cli.product_cli import ProductPopularity
from cli.customer_creation_cli import CustomerCreation
from cli.payment_cli import PaymentSelection
from db.customer_db_interactor import Customer_db

class BColor:
    stars = '\033[91m'
    ENDC = '\033[0m'

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

        # Set all customers as inactive to start the program
        customer_db = Customer_db()
        customer_db.update_active_false()

        # while running == True, MainMenu loop will run repeatedly.
        # To leave Bangazon, running is set to False
        running = True

        # starts the main loop, which handles all CLI functionality and acts
        # as the control hub for the other modules
        while running:
            print("""\n\n\n\n\n\n""")
            print(BColor.stars+"{:*^54}".format("*")+ BColor.ENDC)
            print(BColor.stars+ "**" + BColor.ENDC + "Welcome to Bangazon! Command Line Ordering System" + BColor.stars + "**" + BColor.ENDC)
            print(BColor.stars+"{:*^54}".format("*")+ BColor.ENDC)
            selected_option = input("""
1. Create a customer account
2. Choose active customer
3. Create a payment option
4. Add product to shopping cart
5. Complete an order
6. See product popularity
7. Leave Bangazon!
>""")
                    

            if selected_option == "1":
                create_customer = CustomerCreation()
                create_customer.run()
            elif selected_option == "2":
                choose_customer = CustomerSelection()
                choose_customer.run()
            elif selected_option == "3":
                payment_create = PaymentSelection()
                payment_create.run()
            elif selected_option == "4":
                add_item = ShoppingCartCLI()
                add_item.add_line_item()
            elif selected_option == "5":
                add_item = ShoppingCartCLI()
                add_item.pay_for_cart()
            elif selected_option == "6":
                product_pop = ProductPopularity()
                product_pop.run()
            elif selected_option == "7":
                print("goodbye")
                customer_db.update_active_false()
                running = False


bangazon_interface = MainMenu()
bangazon_interface.run()



