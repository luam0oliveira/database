import uuid
class StorageItem:
	def __init__(self, name="", id="", price=0, amount=0):
		self.id = id or str(uuid.uuid4())
		self.name = name
		self.price = price
		self.amount = amount	

	def __str__(self):
		return f"{self.id},{self.name},{self.amount},{self.price}"