# class Funcionario: 
#     def __init__(self, salario_bruto, descontos): 
#         self.salario_bruto = salario_bruto 
#         self.descontos = descontos 

#     def calcular_salario(self): 
#         salario_liquido = self.salario_bruto - self.descontos 
#         print(salario_liquido)

# opcoes = int(input("digite oque precisa fazer: "))
saldo_inicial = [0]
deposito = 0
class ContaBancaria():
    def __init__(self, nome_titular, saldo_inicial):
         self.__nome_titular = nome_titular
         self.saldo_inicial = saldo_inicial

    def obter_nome_titular(self):
        return self.__nome

    def depositar(self, valor): 
        if valor >0:
            saldo_inicial + deposito
            self.__saldo += valor 
            print(f"Depósito de R${valor} realizado com sucesso")
        else:
            print("Erro: valor deve ser positivo")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")

        elif valor > self.__saldo:
            print("Erro: saldo insuficiente para saque")
            saldo_inicial -= valor
        else:
            self.__saldo -= valor
            print(f"Saque de {valor:.2f} realizado com suceso")

    def consultar_saldo(self):
        print(f"Saldo atual: {self:.2f}")
        return self.__saldo

conta = ContaBancaria("João Silva")

print(f"Titular da conta: {conta.obter_nome_titular()}")

conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()

print(conta.__saldo)
# tentar fazer depois, 

# def lista_n():
#      numeros = [6,3,5,4]
#      print(f"Essa é a lista original: {numeros}")
#      numeros.sort()
#      print(f"A lista organizada é essa:")
#      print(numeros)
# lista_n()

# a = [5,6,3,2]
# a.sort()
# print(a)

# class Pet:
#     def __init__(self, nome, especie, idade):
#          self._nome = nome
#          self._especie = especie
#          self._idade = idade
    
#     def mostrar_dados(self, nome, especie, idade):
#          print(nome, especie, idade)


#     def fazer_som(self, latir):
#          print("O cachorro está fazendo um barulho!!!")
    
    
#     def fazer_som(self, miar):
#         self.miar = miar
#         print("O gato está fazendo barulho!!!")


# cachorro1 = ("ronaldinho pitola", "LULU da Palmirinha", 5)
# gato1 = ("coitadnho da silva", "Laranjinha caramelo" 4)
# print(cachorro1)
# print(gato1)
# cachorro1.fazer_som()
# gato1.fazer_som()

#como diria o filosofo chico moedas; EU TENTEIIIIII