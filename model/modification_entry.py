import uuid
import datetime
from model.storage_item import StorageItem

class ModificationEntry:
	def __init__(self, id=str(uuid.uuid4()), timestamp=datetime.datetime.today().timestamp(), type="Criação", item=None):
		self.id = id
		self.timestamp = timestamp
		self.date = str(datetime.datetime.fromtimestamp(self.timestamp))
		self.type = type
		self.item = item
		
	def __str__(self):
		result = f"{self.id},{self.timestamp},{self.date},{self.type},"
		if isinstance(self.item, StorageItem):
			result += str(self.item)
		else:
			result += str(StorageItem())
		return result