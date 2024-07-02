import datetime
from functools import partial
from time import strftime, strptime
import tkinter as Tk
from tkinter.font import BOLD, Font
from telas.scrollable_container import ScrollableContainer

class ScrollableModificationList(ScrollableContainer):
	def __init__(self, parent, *args, **kw):
		super().__init__(parent, *args, **kw)
		self.line_colors = {"Criação": "green", "Modificação": "yellow", "Remoção": "red"}

	def createList(self, list=[]):
		self.__clearElements()
		self.container.columnconfigure((0,1,2,3,4,5,6), weight=1)
		self.container.config(pady=1, background="black")
		self.__addHeader(self.container)
		for index, element in enumerate(list):
			self.__addElement(
				index+1,
				modification=element
			)
	
	def __addHeader(self, master):
		font = Font(master, size=12, weight=BOLD)
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Id").grid(row=0, column = 0, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Data").grid(row=0, column = 1, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Tipo").grid(row=0, column = 2, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Id item").grid(row=0, column = 3, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Name").grid(row=0, column = 4, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Quant.").grid(row=0, column = 5, sticky="NWSE")
		Tk.Label(self.container,relief="groove", borderwidth=1, font=font, text="Preço").grid(row=0, column = 6, sticky="NWSE")
		

	def __addElement(self, index, modification=None):

		color = self.line_colors[modification.type]

		id = Tk.Label(self.container, text=modification.id, background=color)
		timestamp = Tk.Label(self.container, text=datetime.datetime.fromtimestamp(modification.timestamp), background=color)
		# date = Tk.Label(self.container, text= modification.date, background=color)
		type = Tk.Label(self.container, text=modification.type, background=color)
		itemId = Tk.Label(self.container, text=modification.item.id, background=color)
		itemName = Tk.Label(self.container, text=modification.item.name, background=color)
		itemAmount = Tk.Label(self.container, text=modification.item.amount, background=color)
		itemPrice = Tk.Label(self.container, text=modification.item.price, background=color)

		
		id.grid(row=index, column=0, sticky="WE", pady=1)
		timestamp.grid(row=index, column=1, sticky="WE", pady=1)
		# date.grid(row=index, column=2, sticky="WE", pady=1)
		type.grid(row=index, column=2, sticky="WE", pady=1)
		itemId.grid(row=index, column=3, sticky="WE", pady=1)
		itemName.grid(row=index, column=4, sticky="WE", pady=1)
		itemAmount.grid(row=index, column=5, sticky="WE", pady=1)
		itemPrice.grid(row=index, column=6, sticky="WE", pady=1)

	def __clearElements(self):
		for child in self.container.winfo_children(): 
			child.destroy()
	