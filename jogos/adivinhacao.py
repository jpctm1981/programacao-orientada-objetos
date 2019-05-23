print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
print("xxxxxx","Bem Vindo", end= "!!!" " xxxxxx\n")
print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Vamos tentar adivinhar o número secreto...")

numero_secreto = 5

tentativa = input("Tente adivinhar o número secreto...\n")
tentativa_int = int(tentativa)

print("Você digitou :", tentativa_int)

if(tentativa_int == numero_secreto):
	print("Parabéns!!! Você acertou!!!")

elif tentativa_int > numero_secreto:
	print("O valor está alto... Jogue outra vez!")

else:
	print("O valor está baixo... Jogue outra vez!")