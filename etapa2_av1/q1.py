#Aluno: João Paulo Costa Cordeiro
#Matrícula: 20141143000384

import random

print("Rolando os dados...")
print("Vamos rolar um dado de 6 lados com valores de 1 até 6!!!")
print("Tente acertar...")

print("Rolando o dado...")
r = (random.randrange(1,6))
print("Informe um número:")
n = (int(input()))

while n!=r:

	print("Tente outra vez...")
	print("Informe um número:")
	n = (int(input()))	
	

else:
	print("Parabéns!!! Você acertou!!!")



