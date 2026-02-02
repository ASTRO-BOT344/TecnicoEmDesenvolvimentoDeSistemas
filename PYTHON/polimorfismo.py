class Carro:
    def acelerar(self):
        print("O carro está acelerando de forma padrão.")

class CarroEsportivo(Carro):
    def acelerar(self):
        print("O carro esportivo acelera muito rápido!")

#Criando objetos
carro_comun = Carro()
carro_esportivo = CarroEsportivo()

#chamando método acelerar
carro_comun.acelerar()
carro_esportivo.acelerar()
