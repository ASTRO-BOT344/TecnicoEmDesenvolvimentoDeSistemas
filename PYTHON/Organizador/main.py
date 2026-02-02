import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

locais = {
    "imagens" : ["png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs" : [".pdf"],
    "csv" : [".cvs"],
    "docs" : [".docx"]
}

for arquivo in lista_arquivos:

    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(F"{caminho}/{pasta}")
            os.rename("caminho/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
