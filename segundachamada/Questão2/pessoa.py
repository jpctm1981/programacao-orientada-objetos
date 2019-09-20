class Pessoa:

	def __init__(self, nome, idade, peso, altura, imc):

		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura
		self.imc = imc

	def imc(self):
		self.imc = (self.peso/(self.altura*self.altura))	

	def envelhecer(self):
		pass

	def engordar(self):
		if(self.imc < 18.5):
			print("Seu imc é ", self.imc,"você precisa comer mais...")

	def emagrecer(self):
		pass

	def crescer(self):
		if(self.idade <= 21):
			self.altura = ((self.idade*0.05)+0.5)
			print("Altura = ", self.altura)

		else:
			print("Altura =", self.altura)