# função recursiva é uma fução que chama a si mesma dentro
# de sau definição

def fatorial(n):
    #calcular o fatorial de n recursivamente
    if n <= 1:
        return 1
    return n* fatorial(n - 1)
print(fatorial(5))