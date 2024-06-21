import re

arquivo_nome = "estomago.txt"

with open(arquivo_nome, "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()

print("Texto das primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

num_linhas = len(linhas)
print(f"\nNúmero total de linhas: {num_linhas}")

linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres ({len(linha_maior.strip())} caracteres):")
print(linha_maior.strip())

menções_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
menções_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))

print(f"\nNúmero de menções ao personagem 'Nonato': {menções_nonato}")
print(f"Número de menções ao personagem 'Íria': {menções_iria}")
