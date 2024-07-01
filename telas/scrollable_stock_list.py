from functools import partial
import tkinter as Tk
from telas.scrollable_container import ScrollableContainer

class ScrollableStockList(ScrollableContainer):
	def __init__(self, parent, *args, **kw):
		super().__init__(parent, *args, **kw)

	def createList(self, list=[], callback = None):
		self.__clearElements()
		self.container.config(pady=10)
		for index, element in enumerate(list):
			self.__addElement(
				index,
				product=element,
				callback=callback
			)

	def __addElement(self, index, product=None, callback = None):
		self.container.columnconfigure((0,1,2,3), weight=1)

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
		id.grid(row=index, column=0, sticky="WE", padx=(10,0), pady=(0,10))
		name.grid(row=index, column=1, sticky="WE", padx=(10,0), pady=(0,10))
		amount.grid(row=index, column=2, sticky="WE", padx=(10,0), pady=(0,10))
		price.grid(row=index, column=3, sticky="WE", padx=(10,0), pady=(0,10))

	def __clearElements(self):
		for child in self.container.winfo_children(): 
			child.destroy()
	

	def setTextEntry(self, entry:Tk.Entry, string: str):
		entry.delete(0)
		entry.insert(0, string)


