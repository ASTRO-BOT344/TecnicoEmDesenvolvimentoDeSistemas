# crie um progrma que inclua uma função chamada somaImposto. 
# Essa função deve receber dois parâmetros: taxaImposto, 
# que representa a porcentgem do imposto sobre vendas, e curso, 
# que é o valor do item antes da aplicação do imposto. 
# A função deve calcular o valor do imposto a partir da taxa fornecida 
# e adicionar esse valor ao custo inicial, retornando o novo custo 
# já com o imposto incluído.

def somaImposto():
    custo_inicial = float(input("qual o custo inicial?: "))
    taxa = float(input("Qual a taxa?: "))
    resultado = (taxa/100) * custo_inicial
    soma = resultado + custo_inicial 
    return print(f"O custo com o imposto incluído é R${resultado:.2f}")
somaImposto()