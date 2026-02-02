class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("Um animal fazendo som")

class Cachorro(Animal):
   def __init__(self, nome, idade):
       super.__init__(nome, idade)


class Gato(Animal):
   def __init__(self, nome, idade):
       super.__init__(nome, idade)      

# cachorro1 = ("sem vergonha da silva", 1000)
# cachorro1.fazer_som()

gato1 = ("jabutinho", 800)
gato1.fazer_som(Animal)
print("O gato está miando")