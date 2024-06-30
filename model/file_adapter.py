class FileAdapter:
	def readFile(self, name):
		try:
			file = open(name, "r")
			return file.read()
		except Exception as error:
			print(error)
			return ""

	def writeToFile(self, name, content):
		file = open(name, "w")
		file.write(content)
	
	def appendToFile(self, name, content):
		previousContent = self.readFile(name)

		file = open(name, "w")
		file.write(previousContent+"\n"+content)