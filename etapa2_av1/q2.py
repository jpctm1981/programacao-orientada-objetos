#Aluno: João Paulo Costa Cordeiro
#Matrícula: 20141143000384


import random

print("Escolha o nivel de 1 a 3:")
nivel = int(input())

if(int(nivel) == 1):
	tentativas = 9

elif(int(nivel) == 2):
	tentativas = 6

else:
	tentativas = 3

numero_secreto = int(random.random()*100)
rodada = 1 

for total_tentativas in range (1, tentativas+1):
	
	print("Seu chute é:")
	chute = int(input())
	print("Rodada {} de {}".format(rodada, tentativas))
	rodada = rodada+1	

	if(int(chute) < 1 or int(chute) > 100):
		print("Digite um valor entre 1 e 100")
		continue

	acertou = numero_secreto == chute
	maior = numero_secreto < chute
	menor = numero_secreto > chute

	if(acertou):
		print("Você acertou")
		break

	else:
		if(maior):
			print("Você digitou um número maior...tente outra vez")
			
		elif(menor):
			print("Você digitou um número menor...tente ontra vez")
			
print("Fim de Jogo.")