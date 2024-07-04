import csv
from functools import partial
import tkinter as TK

from model.csv_repository import CsvRepository
from model.modification_entry import ModificationEntry
from telas.create_product_view import CreateProductView
from telas.delete_product_view import DeleteProductView
from telas.modifications_view import ModificationsView
from telas.scrollable_stock_list import  ScrollableStockList


class Home(TK.Tk):
	def __init__(self):
		super().__init__()
		self.container = TK.Frame(self.master)
		self.geometry("1000x600")
		self.container.rowconfigure((0), weight=1, minsize=50)
		self.container.rowconfigure((1), weight=9)
		self.container.columnconfigure((0), weight=1)
		self.csvRepository = CsvRepository()
		self.geometry("1000x600")
		self.modifications = []
		self.storage = self.csvRepository.load()
		self.inicializar()

	def inicializar(self):
		self.__add_header(self.container)
		self.__add_table()
		self.container.pack(expand=True, fill="both")

	def __recreate_table(self):
		self.table.destroy()
		self.__add_table()
	
	def callback(self, index, field, getValueFromEntry):
		entryValue = getValueFromEntry()
		storageValue = getattr(self.storage[index], field)
		if entryValue != str(storageValue):
			modification = ModificationEntry(type="update", item = self.storage[index])
			self.modifications.append(modification)
			setattr(self.storage[index], field, entryValue)

	def __add_table(self):
		self.table = ScrollableStockList(self.container)
		self.table.createList(self.storage, self.callback)
		self.table.grid(row=1, column=0, sticky="NSEW")
		
	def __add_header(self, master):
		header = TK.Frame(master, background="blue")
		header.rowconfigure(0, weight=0)
		self.__add_button_adicionar_produto(header)
		self.__add_button_remove(header)
		self.__add_button_salvar(header)
		header.grid(column=0, row=0, sticky="NWSE")

	def __add_button_adicionar_produto(self, master):
		button = TK.Button(master, text="Adicionar produto", command=self.__call_create_product)
		button.pack(side="left", padx=10)
	
	def __add_button_remove(self, master):
		button = TK.Button(master, text="Remover produto", command=self.__call_delete_product)
		button.pack(side="left")
		
	def __add_button_salvar(self, master):
		self.buttonSave = TK.Button(master, text="Salvar", command=self.__call_save)
		self.buttonSave.pack(side="right", padx=10)

	def __call_create_product(self):
		createProductView = CreateProductView(self.create_product, self)
		createProductView.mainloop()

	def __call_save(self):
		# modificationsView = ModificationsView(self.modifications, self)
		# modificationsView.mainloop()
		columns = ['id', 'name', 'amount', 'price']
		campo = self.focus_get()
		if isinstance(campo, TK.Entry):
			info = campo.grid_info()
			self.callback(info['row']-1, columns[info['column']], campo.get)

		self.buttonSave.focus()
		self.csvRepository.save(self.storage)
		if len(self.modifications):
			self.csvRepository.saveLogs(self.modifications)
			self.modifications.clear()
	
	def __call_delete_product(self):
		deleteProductView = DeleteProductView(self.delete_product, self)
		deleteProductView.mainloop()
	
	def create_product(self, product):
		self.storage.append(product)
		modification = ModificationEntry(item = product)
		self.modifications.append(modification)
		self.__recreate_table()
	
	def delete_product(self, id):
		index = -1
		for i, item in enumerate(self.storage):
			if item.id == id:
				index = i
				break
		if (index != -1):
			modification = ModificationEntry(item = self.storage[i], type="remove")
			self.modifications.append(modification)
			del self.storage[i]
			self.__recreate_table()		
