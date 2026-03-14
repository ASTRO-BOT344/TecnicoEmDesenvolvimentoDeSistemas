import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
if not caminho:
    print("Nenhuma pasta selecionada.")
    exit()

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
    "docs": [".docx", ".txt"]
}

for arquivo in lista_arquivos:

    if os.path.isfile(os.path.join(caminho, arquivo)):
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower() 
        
        for pasta in locais:
            if extensao in locais[pasta]:
                pasta_destino = os.path.join(caminho, pasta)
        
                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)

                origem = os.path.join(caminho, arquivo)
                destino = os.path.join(pasta_destino, arquivo)
                os.rename(origem, destino)
                print(f"Movido: {arquivo} -> {pasta}/")

print("Organização concluída!")
