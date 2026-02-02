#faça uma função que recebe um número inteiro 
# e retorna TRUE se for par e FALSE  se for ímpar
# pares = 0
def numero_par():
    n = int(input("Digite um numero inteiro: "))
    
    if n %2 == 0:
        # pares += 1
        return True
    
    else:
        return False

print (numero_par())
