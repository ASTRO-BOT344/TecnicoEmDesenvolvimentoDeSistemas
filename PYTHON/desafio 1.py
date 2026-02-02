# imprima números pares de 1 a 30 que 
# são divisíveis por 3
# n = 0
# if n %2 == 0:
def divisor():
    for n in range(2,31,2):
        if n %2 == 0 and n %3 == 0:
            print(n)

divisor()

