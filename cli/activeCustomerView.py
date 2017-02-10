import sys
sys.path.append("../")
# from db.data_man import DataMan

class CustomerSelection():
	def run(self):
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