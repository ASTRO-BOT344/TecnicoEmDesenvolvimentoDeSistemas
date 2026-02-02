class Livros:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
def main():
    livros = [
       
        Livros("guia de mochileiro", "Douglas Adams"),
        Livros("Quem é você, Alaska?", "João Verde"),
        Livros("")

    ]
nome = input("Digite o seu nome: ")
print("\n Livros disponíveis para empréstimo: ")
for i, livro in enumerate(Livros, start=1):
    print(f"{i}. {livro.titulo} - {livro.autor}")

while True:
    escolha = int(input("\n Digite o número do livro que deseja pegar emprestado"))

    if 1 <= escolha <= len(Livros):
        livro_selecionado = Livros[escolha - 1]
        break
    else:
        # print(f"Por favor, digite um número entre 1 e {len(livros)}.")

        print("\n Empréstimo confirmado!")
        # print(f"{nome} pegou emprestado o livro '{livro_selecionado.titulo}' de {livro_selecionado.autor}")

main()
