notas = [9.5, 7.5, 8.5, 5.5, 10.0, 6.0]
soma_das_notas = 0

for nota in notas:
    soma_das_notas += nota #Acumula o valo de cada nota

media = soma_das_notas / len(notas) #len() retorna o tamanho da lista

print(f"A média da turma é: {media:.2f}") # :.2f formata para 2 casas decimais