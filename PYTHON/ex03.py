n = int(input("Digite um numero: "))

soma = 0
#s = (n) / 2

for i in range(n):
    numero = float(input(f"Digite o {i+1} numero: "))
    soma += numero

media = soma / n

print(f"A média aritmética é {media} ")