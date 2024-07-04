import tkinter as Tk

class DeleteProductView(Tk.Toplevel):
	def __init__(self, delete_product, master: Tk.Misc | None = None):
		super().__init__(master)
		self.title("Deletar item")
		self.delete_product = delete_product
		self.initialize()
	
	def initialize(self):
		self.container = Tk.Frame(self)
		self.container.rowconfigure((0,1), weight=1)
		self.container.columnconfigure(0, weight=1)
		self.container.columnconfigure(1, weight=3, minsize=250)
		self.id = Tk.StringVar(self)
		self.__create_entry_id()
		self.__create_button_delete()
		self.container.pack(padx=10, pady=10)

	def __create_entry_id(self):
		label = Tk.Label(self.container, text="Id: ")
		label.grid(row=0, column=0, pady=(20,10))

		entry = Tk.Entry(self.container, textvariable=self.id)
		entry.grid(row=0, column=1, pady=(20,10))

	def __delete_product(self):
		id = self.id.get()
		self.delete_product(id)

	def __create_button_delete(self):
		button = Tk.Button(self.container, text="Deletar produto", command= self.__delete_product)
		button.grid(row = 1, column=0, columnspan=2)
		