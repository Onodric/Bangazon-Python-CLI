import sys
sys.path.append("../")
# from db.data_man import DataMan

class CustomerSelection():
	"""Class to contain the Bangazon Customer Selection view. After running the file, the CustomerSelection.run() method is called. 

	Author: Sam Phillips
	"""
	def run(self):
		"""
		CustomerSelection.run() method prompts the user to select a customer from a list of customers. This customer is then set as the active customer by first making a call to the database to make sure that no other customers are active. It then makes a call to the database to set the selected customer as active.
		"""

		# data_man = DataMan()
		# all_customers = data_man.get_all_customers()

		all_customers = [(0, "Jon Con", "address", "city", "state", 37174, "(615) 867-5309", 0), (1, "Sam", "sam's address", "sam's city", "sam's state", 37174, "(615) 555-5555", 0),]

		print("Which customer will be active?")
		for index, customer in enumerate(all_customers):
			print("{}. {}".format(index + 1, customer[1]))
		selection_index = input(">")
		selected_customer_id = int(selection_index) - 1

		if selected_customer_id >= 0:
			# data_man.deactivate_customers()
			# data_man.activate_customer(selected_customer_id)
			print("customer id = {}".format(selected_customer_id))

choose_customer = CustomerSelection()
choose_customer.run()