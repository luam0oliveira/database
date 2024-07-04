import os
from .file_adapter import FileAdapter
from .storage_item import StorageItem
from .modification_entry import ModificationEntry
from .google_sheets_api import GoogleSheetsApi

class CsvRepository:
	def __init__(self):
		self.fileAdapter = FileAdapter()
		self.backupApi = GoogleSheetsApi()
		self.path = "data"
		
		self.logsSheetId = "1eDaHmUgsEXwzhaj-1uAPsHv1-8pz6FNrXdLW0z1Gg9s"
		self.storageSheetId = "1aVDE_u-VzLTQzyPmHEFpqsJ0We692MNcBITWmBDMxCM"

	def save(self, listOfItems):
		csvText = "Id,Item,Quantidade,Preço\n"
		for item in listOfItems:
			if not isinstance(item, StorageItem): continue
			csvText += f"{str(item)}\n"

		self.backupApi.saveCSVtoSheets(csvText, self.storageSheetId)		
		self.fileAdapter.writeToFile(f"{self.path}/storage.csv", csvText)
	
	def saveLogs(self, listOfItems):
		csvText = "Id,Timestamp,Data,Tipo,Id item,Item,Quantidade,Preço\n"
  
		for item in  self.loadLogs()+listOfItems:
			if not isinstance(item, ModificationEntry): continue
			csvText += f"{str(item)}\n"

		self.backupApi.saveCSVtoSheets(csvText, self.logsSheetId)
		self.fileAdapter.writeToFile(f"{self.path}/logs.csv", csvText)

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

	def loadLogs(self):
		csvText = self.fileAdapter.readFile(f"{self.path}/logs.csv")
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