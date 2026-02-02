class Pet:
    def __init__(self, nome, especie, idade):
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Especie: {self.__especie}")
        print(f"Idade: {self.__idade} anos")

    def atualizar_idades(self, nova_idade):
        if nova_idade >= self.__idade:
            self.__idade = nova_idade
            print(f"Idade atualizada para {self.__idade}")
        else:
            print(f"Idade não pode ser menor que a idade antiga ")

    def fazer_som(self):
        if self.__especie.lower() == "cachorro":
            print("Au au")
        elif self.__especie.lowr() == "gato":
            print("Miauuuuuuuuu")
        else:
            print("Som não definido para a espécie.")

pet1 = Pet("coitadinho", "cachorro", 3)
pet1.mostrar_dados()
pet1.fazer_som()
pet1.atualizar_idades(4)





    