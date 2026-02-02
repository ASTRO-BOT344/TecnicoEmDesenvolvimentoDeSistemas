pares = 0
for i in range(0,6):
    numero = int(input(f"Digite o {i+1} numero: "))

    if numero %2 == 0:
        pares += 1
    print(f"A quantidade de numeros pares digitados: {pares}")




