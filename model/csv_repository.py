from .file_adapter import FileAdapter
from .storage_item import StorageItem
from .modification_entry import ModificationEntry

class CsvRepository:
	def __init__(self):
		self.fileAdapter = FileAdapter()
		self.path = "data"

	def save(self, listOfItems):
		csvText = "Id,Item,Quantidade,Preço\n"
		for item in listOfItems:
			if not isinstance(item, StorageItem): continue
			csvText += f"{str(item)}\n"

		self.fileAdapter.writeToFile(f"{self.path}/storage.csv", csvText)
	
	def saveHistory(self, listOfItems):
		csvText = "Id,Timestamp,Data,Tipo,Id item,Item,Quantidade,Preço\n"
		for item in listOfItems:
			if not isinstance(item, ModificationEntry): continue
			csvText += f"{str(item)}\n"

		self.fileAdapter.writeToFile(f"{self.path}/history.csv", csvText)

	def load(self):
		csvText = self.fileAdapter.readFile(f"{self.path}/storage.csv")
		lines = csvText.split("\n")
		items = []

		if len(lines) <= 1:
			return []

		for item in lines[1:]:
			if len(item) > 0:
				fields = item.split(",")
				storageItem = StorageItem(id=fields[0], name=fields[1], price=float(fields[3]), amount=int(fields[2]))
				items.append(storageItem)
		return items

	def loadHistory(self):
		csvText = self.fileAdapter.readFile(f"{self.path}/history.csv")
		lines = csvText.split("\n")
		items = []

		if len(lines) <= 1:
			return []

		for item in lines[1:]:
			if len(item) > 0:
				fields = item.split(",")
				storageItem = StorageItem(id=fields[4], name=fields[5], price=float(fields[7]), amount=int(fields[6]))
				modificationEntry = ModificationEntry(id=fields[0], timestamp=float(fields[1]), type=fields[3], item=storageItem)
				items.append(modificationEntry)
		return items