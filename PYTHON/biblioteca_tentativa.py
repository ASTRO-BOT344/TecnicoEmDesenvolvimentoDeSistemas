class Livro:
    def __init__(self, titulo, autor, solicitante):
        self.titulo = titulo
        self.autor = autor
    #escolher os livros
    def escolher_livro(self, escolher):
        # self.livro = input("digite o livro que você deseja: ")
        # while escolher != "Cancelar":print("aperte 1 para escolher")
        for livro in meus_livros():
            print([0,1,2,3,4])
            if livro == 1:
                print(f"O livro escolhido foi Doutor sono")
            elif livro == 2:
                print(f"O livro escolhido foi O iluminado")
            elif livro == 3:
                print(f"O livro escolhido foi IT")
            elif livro == 4:
                print(f"O livro escolhido foi Harry Potter")
            elif livro == 5:
                print(f"O livro escolhido foi Mitologia nórdica")
                # deixar assim por enquanto pq estou com preguiça
            else:
                break

print("***Livros disponíveis***")
print("Digite o numero correspondente ao livro 1-doutor sono,", "2-O iluminado,", "3-IT,", "4-harry potter,", "5-mitologia nordica")    
nome = input("Digite o solicitante: ")
livro = int(input("Digite o livro que você deseja: "))

meus_livros = ["doutor sono", "O iluminado", "IT", "harry potter", "mitologia nordica"]
meus_livros.escolher_livro()
nome.cadastro_pessoas()