from model.storage_item import StorageItem
from model.csv_repository import CsvRepository
from model.modification_entry import ModificationEntry


print(str(StorageItem()))
print(str(ModificationEntry()))

print(str(StorageItem(name="Escudo", id="abc", price=100, amount=20)))
print(str(ModificationEntry(id="asldkfja", type="Modificação", item=StorageItem(name="Escudo", id="abc", price=100, amount=20))))

repo = CsvRepository()
storageItems = [
	StorageItem(name="Escudo", price=100, amount=20),
	StorageItem(name="Yogurte", price=3, amount=3),
	StorageItem(name="Vassoura", price=4, amount=6),
	StorageItem(name="Pedra", price=5, amount=2),
	StorageItem(name="Verdura", price=7, amount=1),
]
repo.save(storageItems)
storageItems2 = repo.load()
print("----------------")
for item in storageItems2:
	print(str(item))



modifications = [
	ModificationEntry(type="Criação", item=StorageItem(name="Escudo", price=100, amount=20)),
	ModificationEntry(type="Remoção", item=StorageItem(name="Escudo", price=100, amount=20)),
	ModificationEntry(type="Criação", item=StorageItem(name="Vassoura", price=4, amount=6)),
	ModificationEntry(type="Modificação", item=StorageItem(name="Vassoura", price=100, amount=20)),
]

repo.saveHistory(modifications)
modifications2 = repo.loadHistory()

print("----------------")
for item in modifications2:
	print(str(item))