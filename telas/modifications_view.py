import tkinter as Tk

from telas.scrollable_modification_list import ScrollableModificationList

class ModificationsView(Tk.Toplevel):
	def __init__(self, history, master: Tk.Misc | None = None):
		super().__init__(master)
		self.title("Deletar item")
		self.history = history
		self.initialize()
	
	def initialize(self):
		self.container = Tk.Frame(self)
		self.container.rowconfigure(0, weight=1)
		self.container.columnconfigure(0, weight=1)
		self.__createTable(self.container)
		self.container.pack(fill="both")


	def __createTable(self, master):
		self.table = ScrollableModificationList(master)
		self.table.createList(self.history)
		self.table.grid(row=0, column=0, sticky="NSWE")