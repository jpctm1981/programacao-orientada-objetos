#Aluno: João Paulo Costa Cordeiro
#Matrícula: 20141143000384

import random #biblioteca para a geração de valores aletórios

#início da aplicação e instruções ao usuário
print("Rolando os dados...")
print("Vamos rolar um dado de 6 lados com valores de 1 até 6!!!")
print("Tente acertar...")

#primeira execução
print("Rolando o dado...")
r = (random.randrange(1,6)) #declaração dos valores que podem ser obtidos e que serão armazenados na variável "r"
print("Informe um número:") #aqui o usuário informa um valor
n = (int(input())) #a string de entrada é convertida em um valor do tipo inteiro e é armazenado na variável "n"

while n!=r: #teste comparativo entre os valores de n e r
	
	#bloco de código com uma nova instrução ao usuário e que permite ao usuário uma nova tentativa. 
	print("Tente outra vez...")
	print("Informe um número:") #um novo valor para n é informado, possibilitando uma nova comparação.
	n = (int(input()))	
	

else:
	print("Parabéns!!! Você acertou!!!")#mensagem informando que o usuário acertou o valor do dado.