class Calculadora:
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
           return "Erro: divisão por zero"
        return a / b
    
calculadora = Calculadora()
print("Soma: ", calculadora.somar(10, 5))
print("subtrair: ", calculadora.subtrair(10, 5))
print("Multiplicação ", calculadora.multiplicacao(10, 5))
print("Divisão: ", calculadora.divisao(10, 5))
print("Divisão: ", calculadora.divisao(10, 0))

# calculadora.somar()