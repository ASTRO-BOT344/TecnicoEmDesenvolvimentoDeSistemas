class Pessoa:
    def __init__ (self):
        # construtor: inicalizar atributos ao criar o objeto
        self.nome = input("Digite o seu nome: ")
        self.idade = int(input("Digite a sua idade: "))

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e a minha idade é {self.idade}")

#Criando objetos(instância) da classe pessoa
pessoa1 = Pessoa()
pessoa2 = Pessoa()

#Usando os objetos
pessoa1.apresentar()
pessoa2.apresentar()