import csv
from functools import partial
import tkinter as TK

from model.csv_repository import CsvRepository
from telas.create_product_view import CreateProductView
from telas.delete_product_view import DeleteProductView
from telas.scrollable_stock_list import  ScrollableStockList


class Home(TK.Tk):
	def __init__(self):
		super().__init__()
		self.container = TK.Frame(self.master)
		self.container.rowconfigure((0), weight=1)
		self.container.rowconfigure((1), weight=9)
		self.container.columnconfigure((0), weight=1)
		self.csvRepository = CsvRepository()
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
		if entryValue != storageValue:
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
		button.pack(side="left")
	
	def __add_button_remove(self, master):
		button = TK.Button(master, text="Remover produto", command=self.__call_delete_product)
		button.pack(side="left")
		
	def __add_button_salvar(self, master):
		button = TK.Button(master, text="Salvar", command=self.__call_save)
		button.pack(side="right")

	def __call_create_product(self):
		createProductView = CreateProductView(self.create_product, self)
		createProductView.mainloop()

	def __call_save(self):
		self.csvRepository.save(self.storage)
	
	def __call_delete_product(self):
		deleteProductView = DeleteProductView(self.delete_product, self)
		deleteProductView.mainloop()
	
	def create_product(self, product):
		self.storage.append(product)
		self.__recreate_table()
	
	def delete_product(self, id):
		index = -1
		for i, item in enumerate(self.storage):
			if item.id == id:
				index = i
				break
		if (index != -1):
			del self.storage[i]
			self.__recreate_table()		