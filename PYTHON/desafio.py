class Veiculo:
    def __init__(self,  marca, modelo, km, cor, rodas, precisa_cnh=True):
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.cor = cor
        self.precisa_cnh = precisa_cnh

    # def mostrar_dados(self):
    #     print(f"Tipo: {self.marca}")
    #     print(f"Modelo: {self.modelo}")
    #     print(f"Quilometragem: {self.km}")
    #     print(f"Cor: {self.cor}")
    #     print(f"Precisa de CNH: {"Sim" if self.precisa_cnh else "Não"}")

class Carro(Veiculo):
    def __init__(self, tipo, modelo, cor, precisa_cnh=True):
        super().__init__(self, modelo, cor, precisa_cnh=True)
        self.rodas
        self.portas

        def mostrar_dados(self):
            print(f"Tipo: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Quilometragem: {self.km}")
            print(f"Cor: {self.cor}")
            print(f"Precisa de CNH: {"Sim" if self.precisa_cnh else "Não"}")

class Moto(Veiculo):
    def __init__(self, tipo, modelo, cor, precisa_cnh=True):
        super().__init__(self, modelo, cor, precisa_cnh=True)
        self.rodas

minha_moto = Moto("FIAT", "TORO", "vermelho" )
meu_carro = Carro("FIAT", "TORO", "vermelho")

