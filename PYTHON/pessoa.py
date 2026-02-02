class Pessoa:
    def __init__(self, nome, idade):
        # construtor: inicalizar atributos ao criar o objeto
        self.nome= nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e a minha idade é {self.idade}")

#Criando objetos(instância) da classe pessoa
pessoa1 = Pessoa("Ana, 25")
pessoa2 = Pessoa("The weekend", 19)

#Usando os objetos
pessoa1.apresentar()
pessoa2.apresentar()