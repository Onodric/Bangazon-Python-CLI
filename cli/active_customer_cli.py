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

		
		all_customers = Customer_db.get_all_customers()
		
		print("""\n\n\n\n\n\n""")
		print("Which customer will be active?")
		for index, customer in enumerate(all_customers):
			print("{}. {}".format(index + 1, customer[1]))
		selection_index = input(">")
		selected_customer_index = int(selection_index) - 1
		selected_customer = all_customers[selected_customer_index]

		if selected_customer_index >= 0:
			
			print("customer id = {}".format(selected_customer[0]))

