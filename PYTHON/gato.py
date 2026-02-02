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

gato1 = Gato("persa", "jabutinho", 30, 20)
gato2 = Gato("frajola", "endemoniadinho da silva", 1, 10000)

print(f"\n***gatitos cadastrados***\n")

gato1.mostrar_dados()
print("")
gato2.mostrar_dados()
print("")
# for Gato in gato1 and gato2:
#     gato1.mostrar_dados()
#     gato2.mostrar_dados()





    