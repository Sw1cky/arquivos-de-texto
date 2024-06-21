import os

frase = input("Digite uma frase: ")
nome_do_arquivo = "frase.txt"

with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write(frase)
    
caminho = os.path.abspath(nome_do_arquivo)

print(f"Frase salva em {caminho}")
