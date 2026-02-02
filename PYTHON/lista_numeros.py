# implemente uma funcão que receba uma lista de números e 
# retorne o maior valor dessa lista
def maximo_valor(lista):
    maior = lista[0]
    for numero in lista[1:]:
        if numero > maior:
            maior = numero
    return maior

numeros = [19, 24, 52, 45, 23]
print(f"O maior valor é: {maximo_valor(numeros)}")

def maximo_valor(lista):
    maior = lista[0]
    for numero in lista[1:]:
        if numero > maior:
            maior = numero
    return maior

numeros = []
quantidade = int(input(f"Quantos numeros você deseja digitar?"))

for i in range(quantidade):
    numero = float(input(f"Digite o seu número {i+1}"))
    numeros.append(numero)

print(f"O maior valor é: {maximo_valor(numeros)}")