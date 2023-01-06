import random

def jogar():
	print("Bem vindo ao jogo da forca!")

	palavras = []
	with open("palavras.txt") as arquivo:
		for linha in arquivo:
			linha = linha.strip()
			palavras.append(linha)
	
	numero = random.randrange(0, len(palavras))
	palavra_secreta = palavras[numero].upper()

	letras_acertadas = ["_" for letra in palavra_secreta]
	print(letras_acertadas)

	enforcou = False
	acertou = False
	erros = 0
	
	while not enforcou and not acertou:
		chute = input("Digite uma letra: ")
		chute = chute.strip().upper()

		if chute in palavra_secreta:
			index = 0
			for letra in palavra_secreta:
				if chute == letra:
					print(f"Letra {letra} na posição {index}")
					letras_acertadas[index] = letra
				index += 1
		else:
			erros += 1
			print(f"Você errou. Você ainda tem {6-erros} chance(s)")

		enforcou = erros == 6
		acertou = "_" not in letras_acertadas
		print(letras_acertadas)
	
	if acertou:
		print("Você ganhou!")
	else:
		print("Você perdeu!")

	print("Fim do jogo.")

if __name__ == "__main__":
    jogar()
