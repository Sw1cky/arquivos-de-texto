import re 

original_arquivo = "frase.txt"
saida_arquivo = "palavras.txt"

with open(original_arquivo, "r") as arquivo: 
    conteudo = arquivo.read()
    textos = re.findall(r'\b\w+\b', conteudo)

with open(saida_arquivo, "w") as arquivo:
    for texto in textos:
        arquivo.write(texto + "\n")

with open(saida_arquivo, "r") as arquivo:
    saida_conteudo = arquivo.read()
    print(saida_conteudo)



