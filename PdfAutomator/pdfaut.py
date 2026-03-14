import PyPDF2
import os

def mesclar_pdfs(diretorio_entrada, nome_saida):
    merger = PyPDF2.PdfMerger()

    if not os.path.exists(diretorio_entrada):
        print(f"Erro: A pasta '{diretorio_entrada}' não foi encontrada.")
        return

    lista_arquivos = os.listdir(diretorio_entrada)
    lista_arquivos.sort()

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(".pdf"):
            caminho_completo = os.path.join(diretorio_entrada, arquivo)
            print(f"Adicionando: {arquivo}")
            merger.append(caminho_completo)

    merger.write(nome_saida)
    merger.close()
    print(f"\nSucesso! Arquivo '{nome_saida}' gerado com êxito.")

if __name__ == "__main__":
    mesclar_pdfs("arquivos", "PDF_mesclado.pdf")
