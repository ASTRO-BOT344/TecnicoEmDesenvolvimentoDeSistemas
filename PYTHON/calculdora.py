# opcao = ""
lista = ""
def soma():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))
    if b == 0:
        return "ERRO: numero inválido"
    
    return print(a + b)

def subtração():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))
    if b == 0:
        return "ERRO: numero inválido"   

    return print(a - b)

def multiplicação():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))
    if b == 0:
        return "ERRO: numero inválido"

    return print(a * b)

def divisão():
    a = float(input("Digite um numero: "))
    b = float(input("Digite um numero: "))
    if b == 0:
        return "ERRO: numero inválido"

    return print(a / b)

while lista != "sair":
    print("***Escolha qual operação quer usar***")
    print("1 - soma")
    print("2 - diminuição")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - sair ")
    lista = input("Digite uma opção: ")

    if lista == "1":
        print(f"---A opção escolhida foi soma---")
        soma()
    elif lista == "2":
        print(f"---A opção escolhida foi subtração---")
        subtração()
    elif lista == "3":
        print(f"---A opção escolhida foi multiplicação---")
        multiplicação()
    elif lista == "4":
        print(f"---A opção escolhida foi divisão---")
        divisão()
    else:
        print("O usuário saiu")
        break