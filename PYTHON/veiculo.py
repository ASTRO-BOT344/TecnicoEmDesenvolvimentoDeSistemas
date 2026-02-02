class Veiculo:
    def __init__(self, marca, modelo, velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self._velocidade_maxima = velocidade_maxima #protegido
        self.__codigo_interno = 'ABC123' #privado

    def _calcular_desempenho(self):
        #metodo protegido, complexidade oculta
        return f"O veículo pode atingir {self._velocidade_maxima} km/h"
    
    def mostrar_informacoes(self):
        #interface publica que abstrai os detalhes internos
        desempenho = self._calcular_desempenho()
        return f"Marca {self.marca}, Modelo: {self.modelo}, {desempenho}"
    
    def __metodo_privado(self):
        return "Esse método é privado" 
    
#LEITURA DOS DADOS PELO USUARIO

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
velocidade_maxima = float(input("Digite a velocidade maxima do veiculo (km/h): "))
veiculo = Veiculo(marca, modelo, velocidade_maxima)
print(veiculo.mostrar_informacoes())

# carro = Veiculo("Toyota", "Corolla", 180)
print(veiculo._calcular_desempenho())

# print(Veiculo.__metodo_privado) -ERRO NAO FUNCIONA

# metodo protegido (1_): método destinado ao uso interno da classe ou subclasse
# método privado (2__): dificulta o acesso acidental ou externo direto ao método