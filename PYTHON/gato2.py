class Gato:
    def __init__(self, raca, nome, peso , idade):
        self.raca = raca
        self.nome = nome
        self.peso = peso
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Raça: {self.raca}")
        print(f"Nome: {self.nome}")
        print(f"Peso: {self.peso} kg")
        print(f"Idade: {self.idade} anos")

raca = input("Digite a Raça: ")
nome = input("Digite um nome: ")
peso = float(input("Digite o peso: "))
idade = int(input("Digite a idade (em anos): "))

print(f"\nGato cadastrado\n")

gato = Gato(raca, nome, peso, idade)

gato.mostrar_dados()
