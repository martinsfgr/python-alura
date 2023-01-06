import random

def jogar():
	imprimir_mensagem_abertura()
	
	palavra_secreta = carregar_palavra_secreta()
	letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
	print(letras_acertadas)

	enforcou = False
	acertou = False
	erros = 0
	
	while not enforcou and not acertou:
		chute = chutar_letra()

		if chute in palavra_secreta:
			verificar_chute(chute, letras_acertadas, palavra_secreta)
		else:
			erros += 1
			print(f"Você errou. Você ainda tem {6-erros} chance(s)")

		enforcou = erros == 6
		acertou = "_" not in letras_acertadas
		print(letras_acertadas)
	
	if acertou:
		imprimir_mensagem_vitoria(erros)
	else:
		imprimir_mensagem_derrota(palavra_secreta)

def imprimir_mensagem_abertura():
	print("---------------------------")
	print("Bem vindo ao jogo da forca!")
	print("---------------------------")

def carregar_palavra_secreta():
	palavras = []

	with open("palavras.txt") as arquivo:
		for linha in arquivo:
			linha = linha.strip()
			palavras.append(linha)
	
	numero = random.randrange(0, len(palavras))
	palavra_secreta = palavras[numero].upper()

	return palavra_secreta

def inicializar_letras_acertadas(palavra):
	return ["_" for letra in palavra]

def chutar_letra():
	chute = input("Digite uma letra: ")
	return chute.strip().upper()

def verificar_chute(chute, letras_acertadas, palavra_secreta):
	index = 0
	for letra in palavra_secreta:
		if chute == letra:
			print(f"Letra {letra} na posição {index}")
			letras_acertadas[index] = letra
		index += 1

def imprimir_mensagem_vitoria(erros):
	print(f"Parabéns! Você ganhou a partida com {erros} erros")

def imprimir_mensagem_derrota(palavra_secreta):
	print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogar()
