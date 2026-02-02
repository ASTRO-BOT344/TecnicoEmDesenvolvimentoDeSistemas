class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor} realizado.")
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizdo.")
        else:
            print("Saldo insuficiente ou valor inválido!")

    def ver_saldo(self):
        return f"Saldo atual: R$ {self._saldo}"
    
conta = ContaBancaria("João", 50000)

print(conta.ver_saldo())

conta.depositar(50)

print(conta.ver_saldo()) 

conta.sacar(200)

conta.sacar(70)

