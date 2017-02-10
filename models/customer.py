class Customer():

	def __init__(self, name, address, city, state, postal, phone):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.postal = postal
		self.phone = phone
		self.active = False

	def get_current_customer(self):
		return[(self.name, self.address, self.city, self.state, self.postal, self.phone, self.active)]

