import tkinter as Tk

from model.storage_item import StorageItem


class CreateProductView(Tk.Toplevel):
	def __init__(self, create_product, master: Tk.Misc | None = None):
		super().__init__(master)
		self.title("Criar item")
		self.create_product = create_product
		self.initialize()
	
	def initialize(self):
		self.container = Tk.Frame(self)
		self.container.rowconfigure((0,1,2,3), weight=1)
		self.container.columnconfigure(0, weight=1)
		self.container.columnconfigure(1, weight=3, minsize=250)
		self.name = Tk.StringVar(self)
		self.amount = Tk.IntVar(self)
		self.price = Tk.DoubleVar(self)
		self.__create_entry_name()
		self.__create_entry_amount()
		self.__create_entry_price()
		self.__create_button_create()
		self.container.pack()

	def __create_entry_name(self):
		label = Tk.Label(self.container, text="Nome: ")
		label.grid(row=0, column=0, pady=(20,10))

		entry = Tk.Entry(self.container, textvariable=self.name)
		entry.grid(row=0, column=1, pady=(20,10))

	def __create_entry_price(self):
		label = Tk.Label(self.container, text="Preço: ")
		label.grid(row=1, column=0, pady=(0,10))
		
		entry = Tk.Entry(self.container, textvariable=self.price)
		entry.grid(row=1, column=1, pady=(0,10))
	
	def __create_entry_amount(self):
		label = Tk.Label(self.container, text="Quantidade: ")
		label.grid(row=2, column=0, pady=(0,20))
		
		entry = Tk.Entry(self.container, textvariable=self.amount)
		entry.grid(row=2, column=1, pady=(0,20))

	def __create_product(self):
		storage_item = StorageItem(name = self.name.get(), price = self.price.get(), amount=self.amount.get())
		self.create_product(storage_item)

	def __create_button_create(self):
		button = Tk.Button(self.container, text="Criar produto", command= self.__create_product)
		button.grid(row = 3, column=0, columnspan=2)
		