# crie uma  função chamada calcular_media(nota_a, nota_b) 
# que recebe as duas notas, calcula a média ponderada e 
# retorna o resultado. A função princiapl leria as entradas e chamaria calcular_media

def calcular_media(nota_a, nota_b):
    media_ponderada = (nota_a * 2 + nota_b *3) /5 
    return print(f"A média é {media_ponderada}")

calcular_media(2, 3)

# **************************************************

def calcular_media_input():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    resultado_media_input = (n1 * 2 +n2 * 3)/5
    
    return f'A média do aluno é {resultado_media_input}'
print(calcular_media_input())