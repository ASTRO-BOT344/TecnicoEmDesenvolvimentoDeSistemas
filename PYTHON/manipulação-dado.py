nome_completo = input("Digite nome e sobrenome: ")

# versão original
print(nome_completo)

# maiúsculas
print(nome_completo.upper())

# minúsculas
print(nome_completo.lower())

#Retirar espaços no início e no final
print(nome_completo.strip())

#vetor [] consegue atribuir varias variaveis 
# exemplo: comidas [frango, arroz]

#Primeiro nome, caio=0 felix=1 maia=5
nomes = nome_completo.split()
print(nomes[0])
print(len(nomes))

#Deixa a primeira letra da frase maiúscula
print(nome_completo.tittle())

#substituir um texto por outro
print(nome_completo.replace("Caio", "FIRJAN"))
