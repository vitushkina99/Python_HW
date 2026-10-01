class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def prodname(self):
		return self.name 
	
	def get_price(self):
		return self.price
	
	def prod_info(self):
		return f"Product:{self.name}, Price:{self.price}"
