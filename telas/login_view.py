import tkinter as Tk
# from controller.login_view_controller import LoginViewController

# Fazer
class LoginViewController:
	def __init__(self, view) -> None:
		pass

	def login(self):
		return True



class LoginView(Tk.Tk):
	def __init__(self):
		super().__init__()
		self.controller = LoginViewController(self)
		self.loggedIn = True
		self.initialize()
	
	def initialize(self):
		self.__clearElements()

		self.resizable(False, False)
		self.geometry("400x300")
		self.title("Login")	
		self.container = Tk.Frame(self)
		self.container.columnconfigure(0, weight=1)
		self.container.columnconfigure(1, weight=8, minsize=250)
		self.container.place(in_=self, anchor='center', relx=.5, rely=.5)

		self.__addNameInput(self.container)
		self.__addPassInput(self.container)
		self.__addLoginButton(self.container, self.controller.login)

	def getName(self):
		return self.nameInput.get()

	def getPassword(self):
		return self.passInput.get()

	def __addNameInput(self, container):
		self.nameLabel = Tk.Label(container, text="Nome: ", font=("Arial", 16, "bold"), justify="left").grid(sticky="W",column=0, row=0)
		self.nameInput = Tk.Entry(container, name="nome")
		self.nameInput.grid(column=1, row=0, sticky="ew")
	
	def __addPassInput(self, container):
		self.passLabel = Tk.Label(container, text="Senha: ", font=("Arial", 16, "bold"), justify="left").grid(sticky="W",column=0, row=1)
		self.passInput = Tk.Entry(container, name="password", show="*")
		self.passInput.grid(column=1, row=1, sticky="ew")

	def __addLoginButton(self, container, onclick):
		self.loginButton = Tk.Button(container, text="Login", font=("Arial", 14), command=onclick).grid(row=2, columnspan=2, pady=(10,0))

	def __clearElements(self):
		for child in self.winfo_children(): 
			child.destroy()