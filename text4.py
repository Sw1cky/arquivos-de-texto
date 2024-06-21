import random

def escolher_palavra():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()

def mostrar_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Começando o jogo da forca!")
    print("Adivinhe a palavra.")
    mostrar_forca(palavra_secreta, letras_corretas)

    while tentativas > 0:
        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_corretas:
            print("Você já tentou esta letra. Tente novamente!")
            continue

        if palpite in palavra_secreta:
            letras_corretas.append(palpite)
            print("Acertou!")
        else:
            print("Errou!")
            tentativas -= 1

        mostrar_forca(palavra_secreta, letras_corretas)

        if all(letra in letras_corretas for letra in palavra_secreta):
            print("Parabéns! Você ganhou!")
            break

    else:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

if __name__ == "__main__":
    jogar_forca()