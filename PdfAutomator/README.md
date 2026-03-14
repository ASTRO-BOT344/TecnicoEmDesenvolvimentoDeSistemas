# PDF Merger Automator 📄🚀

Este script Python automatiza a tarefa de mesclar múltiplos arquivos PDF localizados em uma pasta específica em um único arquivo final. Ideal para organizar documentos, relatórios ou materiais de estudo rapidamente.

### 🛠️ Tecnologias
* **Python 3.x**
* **PyPDF2**: Biblioteca para manipulação de arquivos PDF.

### 📋 Pré-requisitos
Antes de executar o script, você precisará instalar a biblioteca `PyPDF2`. **Você pode fazer isso via terminal com o comando:**

```bash
pip install PyPDF2
```
### 🚀 Como usar
Crie uma pasta chamada arquivos no mesmo diretório onde o script está salvo.

Coloque todos os arquivos PDF que deseja juntar dentro dessa pasta.

**Execute o script:**

```Bash
python nome_do_seu_script.py
```
O arquivo final será gerado na raiz do projeto com o nome PDF_mesclado.pdf.

### 📌 Observações
O script organiza os arquivos por ordem alfabética. Se precisar de uma ordem específica, renomeie os arquivos com números no início (ex: 01_capa.pdf, 02_conteudo.pdf).

Apenas arquivos com a extensão .pdf serão processados.
