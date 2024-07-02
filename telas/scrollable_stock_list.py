from functools import partial
import tkinter as Tk
from tkinter.font import BOLD, Font
from telas.scrollable_container import ScrollableContainer

class ScrollableStockList(ScrollableContainer):
	def __init__(self, parent, *args, **kw):
		super().__init__(parent, *args, **kw)

	def createList(self, list=[], callback = None):
		self.__clearElements()
		self.container.columnconfigure((0,1,2,3), weight=1)
		self.container.config(pady=1, background="black")
		self.__addHeader(self.container)
		for index, element in enumerate(list):
			self.__addElement(
				index,
				product=element,
				callback=callback
			)

	def __addHeader(self, master):
		font = Font(master, size=14, weight=BOLD)
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Id").grid(row=0, column = 0, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Name").grid(row=0, column = 1, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Quantidade").grid(row=0, column = 2, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Preço").grid(row=0, column = 3, sticky="NWSE")

	def __addElement(self, index, product=None, callback = None):
		row = index + 1 
		id = Tk.Entry(self.container)
		name = Tk.Entry(self.container,validate="focusout")
		amount = Tk.Entry(self.container,validate="focusout", validatecommand=partial(callback, index, "amount"))
		price = Tk.Entry(self.container,validate="focusout", validatecommand=partial(callback, index, "price"))
		
		
		name.configure(validatecommand=partial(callback, index, "name", name.get))
		amount.configure(validatecommand=partial(callback, index, "amount", amount.get))
		price.configure(validatecommand=partial(callback, index, "price", price.get))


		self.setTextEntry(id, product.id)
		self.setTextEntry(name, product.name)
		self.setTextEntry(amount, product.amount)
		self.setTextEntry(price, product.price)
		
		id.config(state="readonly")
		id.grid(row=row, column=0, sticky="WENS", padx=1, pady=1)
		name.grid(row=row, column=1, sticky="WENS", padx=1, pady=1)
		amount.grid(row=row, column=2, sticky="WENS", padx=1, pady=1)
		price.grid(row=row, column=3, sticky="WENS", padx=1, pady=1)

	def __clearElements(self):
		for child in self.container.winfo_children(): 
			child.destroy()
	

	def setTextEntry(self, entry:Tk.Entry, string: str):
		entry.delete(0)
		entry.insert(0, string)


