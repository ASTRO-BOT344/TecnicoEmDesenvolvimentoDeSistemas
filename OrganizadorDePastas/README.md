# PyOrganizer

### 📂 Organizado de Arquivos Python
Este é um script simples e eficiente em Python para automatizar a organização de pastas bagunçadas. 
Ele identifica a extensão dos arquivos e os move para subpastas categorizadas (Imagens, Planilhas, PDFs, etc.).

### 🚀 Como funciona?
O script utiliza uma interface gráfica simples para você selecionar a pasta que deseja organizar. 
Após a seleção, ele percorre todos os arquivos e os move seguindo esta lógica:

```
Pasta de Destino	  Extensões Suportadas
imagens	              .png, .jpg, .jpeg
planilhas	          .xlsx
pdfs	              .pdf
csv	                  .csv
docs	              .docx, .txt
```

### 🛠️ Pré-requisitos
O script utiliza bibliotecas que já vêm instaladas por padrão no Python (Standard Library), então você não precisa instalar nada via pip.

* **Python 3.x instalado.**

* **Tkinter:** Geralmente incluído no Python (usado para a janela de seleção de pasta).

### 💻 Como usar
Clone este repositório ou copie o código para um arquivo chamado organizador.py.

**Execute o script:**
```bash
python organizador.py
```
Uma janela do explorador de arquivos será aberta. Selecione a pasta que está bagunçada.

O script processará os arquivos e exibirá no terminal o que foi movido.

### 📝 Explicação Técnica do Código
* **O fluxo do script segue três etapas principais:**

**Entrada de Dados:** Usa o tkinter.filedialog.askdirectory para obter o caminho da pasta de forma visual.

**Mapeamento:** O dicionário locais define a regra de negócio (qual extensão vai para qual pasta).

**Processamento:**  
* **os.listdir:** Lista tudo que há na pasta.

* **os.path.splitext:** Separa o nome do arquivo da sua extensão.

* **os.path.exists e os.mkdir:** Verificam se a pasta de destino já existe e a criam, se necessário.

* **os.rename:** Realiza a movimentação física do arquivo no disco.

### ⚠️ Observações importantes
O script ignora pastas existentes para evitar mover uma categoria para dentro de outra.

As extensões são convertidas para minúsculas durante a verificação, garantindo que arquivos .JPG e .jpg sejam tratados da mesma forma.
